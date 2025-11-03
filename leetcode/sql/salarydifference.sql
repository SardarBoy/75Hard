with cte as(
select d.department,max(e.salary) as salary
from db_employee e
join db_dept d
on e.department_id=d.id
where d.department in('marketing','engineering')
group by d.department
)

select max(salary)-min(salary) as salary_difference  from cte

