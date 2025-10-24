select studentid,courseid, grade 
from 
(select studentid,courseid, grade , rank() over (partition by student_id order by grade desc, course_id asc) as rnk 
from enrollments ) as ranktable

where rnk=1
order by student_id

# learnt how to use window functions, here we use to solve tie cases
# in this question we can either use rank ,denserank, rownumber 
