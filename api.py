from crypt import methods
from email.policy import default
from employees import *

@app.route('/employees/', methods=['GET'])
def get_employees():
    return jsonify({'Employees': Employees.get_all_employees()})

@app.route('/employees/<int:id>/', methods=['GET'])
def get_employees_by_id(id):
    return jsonify(Employees.get_employees(id))

@app.route('/employees/', methods = ['POST'])
def add_employees():
    req = request.get_json()
    Employees.add_employee(req['name'], req['email'], 
    req['department'], req['salary'], req['birth_date'])
    return Response('Employee inserted', 201, mimetype='application/json')

@app.route('/employees/<int:id>/', methods=['PUT'])
def update_employees():
    req = request.get_json()
    Employees.update_employees(id, req['name'], req['email'], 
    req['department'], req['salary'], req['birth_date'])
    return Response('Emplyees', status=200, mimetype='application/json')

@app.route('/employees/<int:id>/', methods=['DELETE'])
def remove_employee(id):
    Employees.delete_employee(id)
    return Response("Employee Deleted", status=200, mimetype='application/json')

@app.route('/reports/employees/salary/', methods=['GET'])
def report_employee_salary():
    return Employees.salary_range_report()

@app.route('/reports/employees/age/', methods=['GET'])
def report_employee_age():
    return Employees.age_range_report()

if __name__ == '__main__':
    app.run(debug=True, port=8000)