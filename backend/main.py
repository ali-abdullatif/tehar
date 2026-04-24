import os
import uuid
from pathlib import Path

from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List

import models, schemas, crud
from database import engine, get_db
from auth import router as auth_router, verify_admin

# Create database tables on startup
models.Base.metadata.create_all(bind=engine)

# Ensure uploads directory exists
UPLOAD_DIR = Path("/app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="Jewelry API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve uploaded images as static files at /static/uploads/...
app.mount("/static", StaticFiles(directory="/app"), name="static")

# Include auth routes
app.include_router(auth_router)


# --- Public Endpoints ---

@app.get("/items", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)


@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.get("/categories", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


# --- Protected Endpoints (require JWT) ---

@app.post("/categories", response_model=schemas.Category, dependencies=[Depends(verify_admin)])
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@app.delete("/categories/{category_id}", dependencies=[Depends(verify_admin)])
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_cat = crud.delete_category(db, category_id=category_id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted"}


@app.post("/upload", dependencies=[Depends(verify_admin)])
async def upload_image(file: UploadFile = File(...)):
    """Upload an image file and return its public URL."""
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")

    # Generate a unique filename to avoid collisions
    suffix = Path(file.filename).suffix
    unique_filename = f"{uuid.uuid4()}{suffix}"
    dest = UPLOAD_DIR / unique_filename

    # Write file to disk
    contents = await file.read()
    with open(dest, "wb") as f:
        f.write(contents)

    # Return a URL the frontend can use to display the image
    backend_host = os.getenv("BACKEND_PUBLIC_HOST", "http://localhost:8000")
    return {"url": f"{backend_host}/static/uploads/{unique_filename}"}


@app.post("/items", response_model=schemas.Item, dependencies=[Depends(verify_admin)])
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.put("/items/{item_id}", response_model=schemas.Item, dependencies=[Depends(verify_admin)])
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.delete("/items/{item_id}", dependencies=[Depends(verify_admin)])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
