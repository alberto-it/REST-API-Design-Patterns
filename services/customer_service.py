from sqlalchemy.orm import Session
from database import db
from models.models import Customer
from circuitbreaker import circuit

def fallback_func():
    print('The fallback function is being executed')
    return None

@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_func)
def save(customer_data):
    try:
        if customer_data['name'] == 'Failure':
            raise Exception("Failure condition triggered") 
        
        with Session(db.engine) as session:
            with session.begin():
                new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
                session.add(new_customer)
                session.commit()
            session.refresh(new_customer)
            return new_customer
    except Exception as e:
        raise e

def find_all():
    query = db.select(Customer)
    customers = db.session.execute(query).scalars().all()
    return customers