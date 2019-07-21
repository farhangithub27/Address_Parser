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
),
deleted_items as (
	select id,pid,my_name,startdate,enddate,count,row_number,
		case temp_action
			when 'UPDATE' then 'DELETE' 
		end as action_deleted_items 
	from tempTable
	where enddate !='3000-12-31' and row_number = count 	
)
insert into my_name_2(pid,my_name,startdate,enddate,action) SELECT pid,my_name,startdate,enddate,action_deleted_items from deleted_items;

update my_name_2
set startdate = enddate
where action = 'DELETE';

alter table my_name_2
drop column enddate;