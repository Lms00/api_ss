from curses.ascii import NUL
import email
from enum import unique
from lib2to3.pytree import convert
import string
from unicodedata import name
from settings import *
import json
from datetime import datetime

db = SQLAlchemy(app)

class Employees(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    department = db.Column(db.String(80), nullable=False)
    salary = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.String(80), nullable=False)

    def json(self):
        return{'id':self.id, 'name':self.name,
        'email':self.email, 'department':self.department,
        'salary':self.salary, 'birth_date':self.birth_date}

    #post 
    def add_employee(_name, _email, _depar, _salary, _birth):
        new_emp = Employees(name=_name, email=_email, department=_depar,
        salary=_salary, birth_date=_birth)
        db.session.add(new_emp)
        db.session.commit()
    
    #get - employee list
    def get_all_employees():
        return [Employees.json(employee) for employee in Employees.query.all()]

    #get
    def get_employees(_id):
        return [Employees.json(Employees.query.filter_by(id=_id).first())]

    #put
    def update_employees(_id, _name = None, _email = None, _depar = None, _salary = None, _birth = None):
        updte_employee = Employees.query.filter_by(id=_id).first()
        if updte_employee == []:
            return None
        if  _name != None:
            updte_employee.name = _name
        if  _email != None:
            updte_employee.email = _email
        if  _depar != None:
            updte_employee.department = _depar
        if  _salary != None:
            updte_employee.salary = _salary
        if  _birth != None:
            updte_employee.birth_date = _birth
        db.session.commit()
    
    #delete
    def delete_employee(_id):
        Employees.query.filter_by(id=_id).delete()
        db.session.commit()

    def salary_range_report():
        employees = Employees.get_all_employees()
        menor = 99999999999
        maior = 0
        json_menor = {}
        json_maior = {}
        for employee in employees:
            if float(employee['salary'])>maior:
                maior = float(employee['salary'])
                json_maior['lowest'] = employee
            if float(employee['salary'])<menor:
                menor = float(employee['salary'])
                json_menor['highest']  = employee
        saida = []
        saida.append(json_menor)
        saida.append(json_maior)

        return json.dumps(saida)
        
    def age_range_report():
        employees = Employees.get_all_employees()
        menor = '01-01-2500'
        maior = '01-01-1500'
        json_menor = {}
        json_maior = {}
        for employee in employees:
            if datetime.strptime(employee['birth_date'], '%d-%m-%Y').date() > datetime.strptime(maior, '%d-%m-%Y').date():
                maior = employee['birth_date']
                json_maior['younger'] = employee

            if datetime.strptime(employee['birth_date'], '%d-%m-%Y').date() < datetime.strptime(menor, '%d-%m-%Y').date():
                maior = employee['birth_date']
                json_maior['older'] = employee

        saida = []
        saida.append(json_menor)
        saida.append(json_maior)

        return json.dumps(saida)