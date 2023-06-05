-- 1. List the employee number, last name, first name, sex, and salary of each employee.

-- Query Tables

SELECT * FROM "Employees";
SELECT * FROM "Salaries";

-- Query employee number, last name, first name and sex from Employees table
-- Left join salary from Salaries table on emp_no

SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
	FROM "Employees" e
	LEFT JOIN "Salaries" s
		ON s.emp_no = e.emp_no;


-- 2. List the first name, last name, and hire date for the employees who were hired in 1986.

-- Query first_name, last_name and hire_date from Employees table where hired_date includes 1986

SELECT first_name, last_name, hire_date
	FROM "Employees"
		WHERE hire_date LIKE '%1986';


-- 3. List the manager of each department along with their department number, department name, employee number, last name, and first name.

-- Query Tables

SELECT * FROM "Department_Managers";
SELECT * FROM "Departments";

-- Left join dept_name from Departments table to Departments_Manager table on dept_no
-- Left join last_name and first_name from Employees table on emp_no

SELECT dm.dept_no, d.dept_name, dm.emp_no, e.last_name, e.first_name
	FROM "Department_Managers" dm
	LEFT JOIN "Departments" d
		ON d.dept_no = dm.dept_no
	LEFT JOIN "Employees" e
		ON e.emp_no = dm.emp_no;


-- 4. List the department number for each employee along with that employee’s employee number, last name, first name, and department name.

-- Query Table
SELECT * FROM "Department_Employees";

-- Left join dept_name from Departments table to Departments_Employees table on dept_no
-- Left join last_name and first_name from Employees table on emp_no

SELECT de.dept_no, de.emp_no, e.last_name, e.first_name, d.dept_name
	FROM "Department_Employees" de
	LEFT JOIN "Departments" d
		ON d.dept_no = de.dept_no
	LEFT JOIN "Employees" e
		ON e.emp_no = de.emp_no;
		
		
-- 5. List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B.

-- Select first_name, last_name and sex columns from the Employees table
-- Where first_name = 'Hercules' and last_name starts with 'B' and ends with wildcard character

SELECT first_name, last_name, sex
	FROM "Employees"
		WHERE first_name = 'Hercules' and last_name LIKE 'B%';


-- 6. List each employee in the Sales department, including their employee number, last name, and first name.

-- Select emp_no, last_name and first_name columns from the Employees table
-- Subquery the emp_no from the "Department_Employees" table
-- Subquery the dept_no from the "Departments" table where dept_name = Sales

SELECT emp_no, last_name, first_name
	FROM "Employees"
		WHERE emp_no
		IN(
			SELECT emp_no
				FROM "Department_Employees"
					WHERE dept_no
					IN (
						SELECT dept_no
							FROM "Departments"
								WHERE dept_name = 'Sales'));


-- 7. List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name.

-- Select emp_no, last_name and first_name columns from the Employees table and dept_name column from Departments table
-- Left join Department_Employees table to Employees table on emp_no
-- Left join Departments table to Department_Employees table on dept_no where dept_name = Sales or Development

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
	FROM "Employees" e 
	LEFT JOIN "Department_Employees" de
		ON de.emp_no = e.emp_no
	LEFT JOIN "Departments" d
		On d.dept_no = de.dept_no
			WHERE d.dept_name = 'Sales' OR d.dept_name = 'Development';
			

-- 8. List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name).

-- Select last_name column from Employees table counting frequency of last_name values as new column "last_name_count"
-- Group rows by unique last_name values
-- Order rows by last_name_count in descending order

SELECT last_name, COUNT(last_name) AS "last_name_count"
	FROM "Employees"
		GROUP BY last_name
		ORDER BY "last_name_count" DESC;