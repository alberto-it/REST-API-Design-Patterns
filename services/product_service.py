from sqlalchemy.orm import Session
from database import db
from models.product import Product
from circuitbreaker import circuit

def fallback_func():
    print('The fallback function is being executed')
    return None

@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_func)
def save(product_data):
    try:
        if product_data['name'] == 'Failure':
            raise Exception("Failure condition triggered") 
        
        with Session(db.engine) as session:
            with session.begin():
                new_product = Product(name=product_data['name'], price=product_data['price'])
                session.add(new_product)
                session.commit()
            session.refresh(new_product)
            return new_product
    except Exception as e:
        raise e

def find_all():
    query = db.select(Product)
    products = db.session.execute(query).scalars().all()
    return products