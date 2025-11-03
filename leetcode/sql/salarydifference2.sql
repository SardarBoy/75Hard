SELECT 
    ABS(MAX(CASE WHEN d.department = 'marketing' THEN e.salary END)
      - MAX(CASE WHEN d.department = 'engineering' THEN e.salary END)) AS salary_difference
FROM db_employee e
JOIN db_dept d ON e.department_id = d.id
WHERE d.department IN ('marketing', 'engineering');