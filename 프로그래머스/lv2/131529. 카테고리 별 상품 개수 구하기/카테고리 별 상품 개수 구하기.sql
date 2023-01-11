select left(product_code, 2) as CATEGORY, count(product_id) as PRODUCTS
from product
group by CATEGORY