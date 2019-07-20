/* 
31st December 3000 is taken to be 
condition for the most recent update
*/
select * from my_name
where enddate ='3000-12-31'
/*  OR other slightly complex way
where enddate::text like '3000-%'
*/
