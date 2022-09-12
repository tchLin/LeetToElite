# Write your MySQL query statement below
SELECT employee_id,
IF (employee_id%2 AND name not like "M%", salary, 0) as bonus
FROM Employees order by employee_id;

select employee_id, 
case 
    when employee_id%2 != 0 and name NOT LIKE 'M%' then salary
    else 0
end as bonus
from employees order by employee_id;
