import sqlite3

connection = sqlite3.connect("CameronCompany") 
pointer = connection.cursor()

pointer.execute('DROP TABLE IF EXISTS employee')
connection.commit()

pointer.execute('CREATE TABLE employee(emp_num INTEGER NOT NULL PRIMARY KEY,emp_fname CHAR(40),emp_lname CHAR(40),dept_num CHAR(2),FOREIGN KEY(dept_num)REFERENCES department(dept_num))')
connection.commit()

pointer.execute("INSERT INTO employee(emp_num, emp_fname, emp_lname, dept_num) VALUES('253348','Matthew','Smith','d1')")
connection.commit()

pointer.execute("INSERT INTO employee(emp_num, emp_fname, emp_lname, dept_num) VALUES('10102','Ann','Jones','d2')")
connection.commit()

pointer.execute("INSERT INTO employee(emp_num, emp_fname, emp_lname, dept_num) VALUES('18316','Elizabeth','Smith','d3')")
connection.commit()

pointer.execute("INSERT INTO employee(emp_num, emp_fname, emp_lname, dept_num) VALUES('29346','James','James','d1')")
connection.commit()

pointer.execute("INSERT INTO employee(emp_num, emp_fname, emp_lname, dept_num) VALUES('12325','Alex','Lopez','d2')")
connection.commit()

pointer.execute("INSERT INTO employee(emp_num, emp_fname, emp_lname, dept_num) VALUES('90042','John','Barrimore','d1')")
connection.commit()

pointer.execute("INSERT INTO employee(emp_num, emp_fname, emp_lname, dept_num) VALUES('9031','Elke','Hansel','d3')")
connection.commit()

pointer.execute("INSERT INTO employee(emp_num, emp_fname, emp_lname, dept_num) VALUES('2581','Elsa','Bertoni','d2')")
connection.commit()

pointer.execute("INSERT INTO employee(emp_num, emp_fname, emp_lname, dept_num) VALUES('28559','Sybill','Moser','d1')")
connection.commit()

pointer.execute("DELETE FROM employee WHERE emp_num='29346'")
connection.commit()

print("\nEmployees:")

pointer.execute('SELECT * FROM employee')
for row in pointer:
    print(row)















pointer.execute('DROP TABLE IF EXISTS department')
connection.commit()

pointer.execute('CREATE TABLE department(dept_num CHAR(2)NOT NULL PRIMARY KEY,dept_name CHAR(40),location CHAR(40))')
connection.commit()

pointer.execute("INSERT INTO department(dept_num, dept_name, location) VALUES('d1','Mathematics','Dallas')")
connection.commit()

pointer.execute("INSERT INTO department(dept_num, dept_name, location) VALUES('d2','Accounting','Seattle')")
connection.commit()

pointer.execute("INSERT INTO department(dept_num, dept_name, location) VALUES('d3','Marketing','Dallas')")
connection.commit()

pointer.execute("UPDATE department SET location = 'Washington' WHERE dept_num = 'd1'")
connection.commit()

print("\nDepartment:")

pointer.execute('SELECT * FROM department')
for row in pointer:
    print(row)

















pointer.execute('DROP TABLE IF EXISTS works_on')
connection.commit()

pointer.execute('CREATE TABLE works_on(emp_num INTEGER,project_name CHAR(40),job CHAR(40),enter_date CHAR(40),FOREIGN KEY(emp_num)REFERENCES department(emp_num),FOREIGN KEY(project_name)REFERENCES department(project_name))')
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('10102','p1','Analyst','2021.10.1')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('10102','p3','Manager','2021.1.1')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('25348','p2','Clerk','2020.7.15')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('18316','p2','','2007.6.1')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('29346','p3','','2020.10.11')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('2581','p2','Analyst','2020.10.25')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('9031','p1','Manager','2018.2.13')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('28559','p2','','2019.4.7')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('28559','p3','Clerk','2015.3.14')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('9031','p2','Manager','2016.4.7')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('29346','p1','Analyst','2007.1.4')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('12325','p1','Clerk','2020.12.1')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('12325','p2','','2002.5.16')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('90042','p2','Analyst','2012.6.18')")
connection.commit()

pointer.execute("INSERT INTO works_on(emp_num, project_name, job, enter_date) VALUES('9031','p3','Manager','2016.4.18')")
connection.commit()

pointer.execute("DELETE FROM works_on WHERE emp_num='29346'")
connection.commit()

print("\nworks_on:")

pointer.execute('SELECT * FROM works_on')
for row in pointer:
    print(row)















pointer.execute('DROP TABLE IF EXISTS project')
connection.commit()

pointer.execute('CREATE TABLE project(project_num CHAR (40)NOT NULL PRIMARY KEY,project_name CHAR(40),budget INTEGER)')
connection.commit()

pointer.execute("INSERT INTO project(project_num,project_name,budget) VALUES('p1','Apollo','120000')")
connection.commit()

pointer.execute("INSERT INTO project(project_num,project_name,budget) VALUES('p2','Gemini','95000')")
connection.commit()

pointer.execute("INSERT INTO project(project_num,project_name,budget) VALUES('p3','Mercury','186500')")
connection.commit()

print("\nProject Apollo:")

pointer.execute("SELECT emp_fname,emp_lname,dept_name,location FROM department JOIN employee ON department.dept_num = employee.dept_num JOIN works_on ON employee.emp_num = works_on.emp_num JOIN project ON works_on.project_name = project.project_num WHERE project.project_name='Apollo'")
for row in pointer:
    print(row)