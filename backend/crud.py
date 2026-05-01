from sqlalchemy.orm import Session
import models, schemas
import datetime

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

# Tracking
def log_event(db: Session, event: schemas.EventCreate):
    now = datetime.datetime.utcnow()
    db_event = models.EventLog(
        **event.model_dump(),
        timestamp=now,
        date=now.date(),
        hour=now.hour
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

# Analytics Aggregations
from sqlalchemy import func

def get_analytics_dashboard(db: Session):
    # 1. Daily Sales (Purchases)
    daily = db.query(
        models.EventLog.date, 
        func.count(models.EventLog.id)
    ).filter(models.EventLog.event_type == 'purchase').group_by(models.EventLog.date).all()
    
    # 2. Hourly Activity (All events)
    hourly = db.query(
        models.EventLog.hour,
        func.count(models.EventLog.id)
    ).group_by(models.EventLog.hour).order_by(models.EventLog.hour).all()

    # 3. Top Products (Views)
    top_viewed = db.query(
        models.JewelryItem.name, 
        func.count(models.EventLog.id)
    ).join(models.EventLog).filter(models.EventLog.event_type == 'view').group_by(models.JewelryItem.name).order_by(func.count(models.EventLog.id).desc()).limit(10).all()

    # 4. Top Products (Add to cart)
    top_cart = db.query(
        models.JewelryItem.name,
        func.count(models.EventLog.id)
    ).join(models.EventLog).filter(models.EventLog.event_type == 'add_to_cart').group_by(models.JewelryItem.name).order_by(func.count(models.EventLog.id).desc()).limit(10).all()

    # 5. Funnel
    views_count = db.query(func.count(models.EventLog.id)).filter(models.EventLog.event_type == 'view').scalar() or 0
    cart_count = db.query(func.count(models.EventLog.id)).filter(models.EventLog.event_type == 'add_to_cart').scalar() or 0
    purchase_count = db.query(func.count(models.EventLog.id)).filter(models.EventLog.event_type == 'purchase').scalar() or 0
    
    # 6. Cart Abandonment Estimation
    # (Sessions with add_to_cart but NO purchase)
    sessions_with_cart = db.query(models.EventLog.session_id).filter(models.EventLog.event_type == 'add_to_cart').distinct().all()
    sessions_with_cart = [s[0] for s in sessions_with_cart]
    
    sessions_with_purchase = db.query(models.EventLog.session_id).filter(models.EventLog.event_type == 'purchase').distinct().all()
    sessions_with_purchase = [s[0] for s in sessions_with_purchase]
    
    abandoned_count = len(set(sessions_with_cart) - set(sessions_with_purchase))
    total_cart_sessions = len(set(sessions_with_cart))
    abandonment_rate = (abandoned_count / total_cart_sessions * 100) if total_cart_sessions > 0 else 0

    return {
        "daily_sales": [{"date": str(d[0]), "count": d[1]} for d in daily],
        "hourly_activity": [{"hour": h[0], "count": h[1]} for h in hourly],
        "top_viewed": [{"product_name": p[0], "count": p[1]} for p in top_viewed],
        "top_cart": [{"product_name": p[0], "count": p[1]} for p in top_cart],
        "conversion_funnel": {
            "views": views_count,
            "add_to_cart": cart_count,
            "purchase": purchase_count
        },
        "cart_abandonment_rate": round(abandonment_rate, 2)
    }

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
