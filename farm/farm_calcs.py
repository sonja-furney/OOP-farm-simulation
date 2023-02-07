from pen import Pen
import random

# Greenhouse gas emissions: Overall, how much 
#   greenhouse gases does this scenario generate?

# Cost estimation: Based on the type and amount 
#    of the consumed feeds, how much does it cost 
#    John to implement this scenario in his farm?

milk_price = random.randrange(50, 75)

def farm_gas():
    total = 0
    for pen in Pen.pens:
        total += pen.gas_per_pen()
    return total

def farm_milk():
    total = 0
    for pen in Pen.pens:
        total += pen.milk_units_per_pen()
    return total

def farm_costs():
    total = 0
    for pen in Pen.pens:
        total += (pen.milk_units_per_pen() - pen.cost_of_feed_per_pen())
    return total

def farm_gas_report():
    gas = farm_gas()
    return 'The cows on this farm produce ' + str(gas) + ' units of greenhouse gasses.'

def farm_milk_report():
    milk = farm_milk()
    return 'Farmer John makes $' + str(milk*milk_price) + ' in milk from this farm.'

def farm_costs_report():
    profit = farm_costs()
    return 'Farmer John makes $' + str(profit) + ' from this farm.'


