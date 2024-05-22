from sqlalchemy.orm import Session
from database import db
from models.order_model import Order

def save(order_data):
        
    with Session(db.engine) as session:
        with session.begin():
            new_order = Order(customer_id=order_data['customer_id'], product_id=order_data['product_id'], quantityd=order_data['quantity'], total_price=order_data['total_price'])
            session.add(new_order)
            session.commit()
        session.refresh(new_order)
        return new_order

def find_all(page=1, per_page=10, search_term=None):
    query = db.select(Order)
    if search_term:
        query = query.where(Order.name.ilike(f"%{search_term}%"))
    query = query.limit(per_page).offset((page-1)*per_page)
    return db.session.execute(query).scalars().all()