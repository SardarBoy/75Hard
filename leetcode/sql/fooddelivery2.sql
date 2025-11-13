with cte as (select *, rank() over (partition by customer_id order by order_date asc) as rnk
from delivery )


select ROUND((sum(case when order_date=customer_pref_delivery_date then 1 else 0 END)/count(*)) *100.0,2) as immediate_percentage
from cte 
where rnk=1