from sqlalchemy.orm import Session
from database import db
from models.product_model import Product

def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'], price=product_data['price'])
            session.add(new_product)
            session.commit()
        session.refresh(new_product)
        return new_product

def find_all(page=1, per_page=10, search_term=None):
    query = db.select(Product)
    if search_term:
        query = query.where(Product.name.ilike(f"%{search_term}%"))
    query = query.limit(per_page).offset((page-1)*per_page)
    return db.session.execute(query).scalars().all()