-- 코드를 입력하세요
SELECT distinct CART_ID
from CART_PRODUCTS 
where name = 'Milk'
intersect
select distinct cart_id
from cart_products
where name = 'Yogurt'