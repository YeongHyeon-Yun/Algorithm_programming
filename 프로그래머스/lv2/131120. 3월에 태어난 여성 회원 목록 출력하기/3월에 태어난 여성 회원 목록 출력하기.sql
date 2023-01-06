-- 코드를 입력하세요
SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth, '%Y-%m-%d') AS DATE_OF_BIRTH
from member_profile
where month(date_of_birth) = 3
and tlno is not null
and gender = 'w'
order by member_id;