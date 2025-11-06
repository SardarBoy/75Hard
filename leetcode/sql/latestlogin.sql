with cte as (select *,row_number() over(partition by user_id order by time_stamp desc) as rnk
 from Logins where year(time_stamp)=2020)

 select user_id, time_stamp as last_stamp from cte where rnk=1
