
select cnt as tweet_bucket, count(user_id) as users_num
from 
(select count(*) as cnt, user_id from tweets where
extract(YEAR FROM tweet_date)=2022
group by user_id) t2

group by cnt