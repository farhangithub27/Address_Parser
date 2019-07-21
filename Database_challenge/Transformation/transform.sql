with tempTable as (
select b.id, b.pid,b.my_name,b.startdate,b.enddate,a.count,b.row_number,
	case 
	 	when enddate <='3000-12-31' and row_number<=count and row_number !=1 then 'UPDATE' 
	 	else 'INSERT'
	 end as temp_action
from
	(select distinct pid, count(pid) 
	 from my_name
	 group by pid) as a
	inner join
	(select *, row_number() over (partition by pid)
	 from my_name
	 order by pid ASC) as b ON a.pid=b.pid
order by pid,startdate ASC

)
INSERT into my_name_2 SELECT id,pid,my_name,startdate,enddate,temp_action from tempTable;
-- Only one Select,insert,update and delete statement can be written with with clause


