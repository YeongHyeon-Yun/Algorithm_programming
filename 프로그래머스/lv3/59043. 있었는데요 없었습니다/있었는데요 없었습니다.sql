select ins.ANIMAL_ID, ins.NAME
from animal_ins ins
join animal_outs outs
on ins.animal_id = outs.animal_id
where ins.datetime > outs.datetime
order by ins.datetime;