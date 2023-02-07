from pen import Pen
from breed import Breed
from cow import Cow
from feed import Feed
from store import store
from farm_calcs import farm_gas, farm_costs, farm_milk, farm_costs, farm_gas_report, farm_milk_report, farm_costs_report

pen_1 = Pen()
pen_2 = Pen()

hay = Feed()
grass = Feed() 

brown = Breed('brown', hay)
calico = Breed('calico', grass)

cow_1 = Cow('Bessie', pen_1, brown)
cow_2 = Cow('Jenny', pen_2, calico)
cow_3 = Cow('Martha', pen_1, brown)