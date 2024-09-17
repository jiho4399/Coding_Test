-- 코드를 입력하세요
SELECT distinct(cc.CAR_ID)
from CAR_RENTAL_COMPANY_CAR cc
join CAR_RENTAL_COMPANY_RENTAL_HISTORY ch
on cc.car_id = ch.car_id
where month(ch.start_date) = 10 and cc.car_type = '세단'
order by cc.car_id desc 