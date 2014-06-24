from sqlsetup import connect, run, commit, tbl, close, sel

connect('bank')

sel("SHOW TABLES;")

sel("SELECT fname, lname FROM employee;")

sel("SELECT * FROM department;")

sel("SELECT * FROM employee;")

sel("SELECT emp_id, 'Active', emp_id * .5, UPPER(lname) FROM employee")

sel("SELECT VERSION(), USER(), DATABASE();")  # no FROM needed

sel("""SELECT UPPER(lname) AS last_name_upper,
emp_id AS employee_id FROM employee""")

sel("SELECT DISTINCT cust_id FROM account")

run("""CREATE VIEW employee_vw AS
SELECT emp_id, fname, lname, YEAR(start_date) start_year
FROM employee;""")

commit()

sel("""SELECT employee.emp_id, employee.fname,
department.name dept_name
FROM employee INNER JOIN department
ON employee.dept_id = department.dept_id;""")

sel("""SELECT emp_id, fname, start_date, title
FROM employee
WHERE title = 'Head Teller';""")

sel("""SELECT d.name, count(e.emp_id)
FROM department d INNER JOIN employee e
ON d.dept_id = e.dept_id
GROUP BY d.name""")

sel("""SELECT open_emp_id, product_cd
FROM account
ORDER BY open_emp_id DESC, product_cd;""")

sel("""SELECT cust_id FROM customer ORDER BY RIGHT(fed_id, 3);""")

# p. 60 ex. 3-1
sel("""SELECT emp_id, fname, lname
FROM employee
ORDER BY lname, fname;""")

sel("""SELECT account_id, cust_id, avail_balance
FROM account
WHERE status = 'ACTIVE' AND avail_balance > 2500;""")

sel("""SELECT DISTINCT open_emp_id FROM account;""")

sel("""SELECT p.product_cd, a.cust_id, a.avail_balance
FROM product p INNER JOIN account a
ON p.product_cd = a.product_cd
WHERE p.product_type_cd = 'ACCOUNT'
ORDER BY p.product_cd, a.cust_id;""")

