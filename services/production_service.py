from sqlalchemy.orm import Session
from database import db
from models.productions_model import Production
from circuitbreaker import circuit

def fallback_func():
    print('The fallback function is being executed')
    return None

@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_func)
def save(production_data):
    try:
        if production_data['name'] == 'Failure':
            raise Exception("Failure condition triggered") 
        
        with Session(db.engine) as session:
            with session.begin():
                new_production = Production(name=production_data['name'], product_id=production_data['product_id'], quantity_produced=production_data['quantity_produced'], date_produced=production_data['date_produced'])
                session.add(new_production)
                session.commit()
            session.refresh(new_production)
            return new_production
    except Exception as e:
        raise e

def find_all():
    query = db.select(Production)
    productions = db.session.execute(query).scalars().all()
    return productions