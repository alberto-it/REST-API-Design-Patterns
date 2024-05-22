from sqlalchemy.orm import Session
from database import db
from models.employee_model import Employee
from circuitbreaker import circuit

def fallback_func():
    print('The fallback function is being executed')
    return None

@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_func)
def save(empl_data):
    try:
        if empl_data['name'] == 'Failure':
            raise Exception("Failure condition triggered") 
        
        with Session(db.engine) as session:
            with session.begin():
                new_empl = Employee(name=empl_data['name'], position=empl_data['position'])
                session.add(new_empl)
                session.commit()
            session.refresh(new_empl)
            return new_empl
    except Exception as e:
        raise e

def find_all():
    query = db.select(Employee)
    employees = db.session.execute(query).scalars().all()
    return employees