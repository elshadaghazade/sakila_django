SELECT t1.emp_no, 
	   t1.birth_date, 
       t1.first_name, 
       t1.last_name, 
       t1.gender,
       t1.hire_date,
       t2.title,
       t2.from_date,
       t2.to_date,
       t4.dept_name AS manager_dept_name,
       t6.dept_name AS emp_dept_name 
  FROM employees AS t1
LEFT JOIN titles AS t2 ON t1.emp_no = t2.emp_no
LEFT JOIN dept_manager AS t3 ON t1.emp_no = t3.emp_no
LEFT JOIN departments AS t4 ON t3.dept_no = t4.dept_no
LEFT JOIN dept_emp AS t5 ON t5.emp_no = t1.emp_no
LEFT JOIN departments AS t6 ON t6.dept_no = t5.dept_no
LIMIT 5