SELECT candidate_id from candidates
group by candidate_id
having sum(case when skill like '%Python%'  then 1 else 0 end)>=1 
AND sum(case when skill like '%Tableau%' then 1 else 0 end)>=1 
AND sum(case when skill like '%PostgreSQL%' then 1 else 0 END)>=1
order by candidate_id