from sqlalchemy.orm import Session
import models, schemas

# Config
def get_configs(db: Session):
    return db.query(models.SiteConfig).all()

def update_config(db: Session, config: schemas.ConfigUpdate):
    db_config = db.query(models.SiteConfig).filter(models.SiteConfig.key == config.key).first()
    if db_config:
        db_config.value = config.value
    else:
        db_config = models.SiteConfig(key=config.key, value=config.value)
        db.add(db_config)
    db.commit()
    return db_config

# Categories
def get_categories(db: Session):
    return db.query(models.ItemCategory).all()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_cat = models.ItemCategory(name=category.name)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def delete_category(db: Session, category_id: int):
    db_cat = db.query(models.ItemCategory).filter(models.ItemCategory.id == category_id).first()
    if db_cat:
        db.delete(db_cat)
        db.commit()
    return db_cat

# Items
def get_item(db: Session, item_id: int):
    return db.query(models.JewelryItem).filter(models.JewelryItem.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.JewelryItem).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    item_data = item.model_dump(exclude={"gallery_images"})
    db_item = models.JewelryItem(**item_data)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    # Add gallery images
    if item.gallery_images:
        for img_url in item.gallery_images:
            db_img = models.ItemImage(url=img_url, item_id=db_item.id)
            db.add(db_img)
        db.commit()
        db.refresh(db_item)
        
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = db.query(models.JewelryItem).filter(models.JewelryItem.id == item_id).first()
    if db_item:
        item_data = item.model_dump(exclude={"gallery_images"}, exclude_unset=True)
        for key, value in item_data.items():
            setattr(db_item, key, value)
        
        # Handle gallery images (replace old ones for simplicity)
        if hasattr(item, 'gallery_images') and item.gallery_images is not None:
            # Clear old
            db.query(models.ItemImage).filter(models.ItemImage.item_id == item_id).delete()
            # Add new
            for img_url in item.gallery_images:
                db_img = models.ItemImage(url=img_url, item_id=item_id)
                db.add(db_img)
        
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.JewelryItem).filter(models.JewelryItem.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
