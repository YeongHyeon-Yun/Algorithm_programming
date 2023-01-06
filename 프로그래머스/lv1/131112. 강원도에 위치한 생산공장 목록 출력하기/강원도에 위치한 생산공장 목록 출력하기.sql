select FACTORY_ID, FACTORY_NAME, ADDRESS from food_factory
WHERE ADDRESS LIKE '강원도 %'
order by factory_id