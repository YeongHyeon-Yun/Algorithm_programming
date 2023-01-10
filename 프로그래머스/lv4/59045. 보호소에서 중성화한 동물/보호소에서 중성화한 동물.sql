select i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from animal_ins i
join animal_outs o
on i.animal_id = o.animal_id

where i.sex_upon_intake != o.sex_upon_outcome

order by i.animal_id
