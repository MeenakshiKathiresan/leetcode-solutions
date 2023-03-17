# Write your MySQL query statement below

select session_id from
Playback left join Ads
on Playback.customer_id = Ads.customer_id
and Ads.timestamp between Playback.start_time and Playback.end_time
where ads.customer_id is Null