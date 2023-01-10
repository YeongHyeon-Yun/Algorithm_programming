select product.product_code as PRODUCT_CODE, sum(product.price * offline_sale.sales_amount) as SALES
from product
join offline_sale
on product.product_id = offline_sale.product_id
group by product.product_code
order by SALES desc, product.product_code