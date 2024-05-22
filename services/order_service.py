from sqlalchemy.orm import Session
from database import db
from models.order import Order
from circuitbreaker import circuit

def fallback_func():
    print('The fallback function is being executed')
    return None

@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_func)
def save(order_data):
    try:
        if order_data['name'] == 'Failure':
            raise Exception("Failure condition triggered") 
        
        with Session(db.engine) as session:
            with session.begin():
                new_order = Order(customer_id=order_data['customer_id'], product_id=order_data['product_id'], quantityd=order_data['quantity'], total_price=order_data['total_price'])
                session.add(new_order)
                session.commit()
            session.refresh(new_order)
            return new_order
    except Exception as e:
        raise e

def find_all():
    query = db.select(Order)
    orders = db.session.execute(query).scalars().all()
    return orders