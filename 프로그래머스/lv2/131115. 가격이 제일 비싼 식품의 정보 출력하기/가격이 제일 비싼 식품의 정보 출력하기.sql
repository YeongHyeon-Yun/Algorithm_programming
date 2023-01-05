select * from food_product
where price = (select max(price) from food_product);

/*
SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1;
*/