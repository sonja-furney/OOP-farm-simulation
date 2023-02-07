from store import store

class Pen:
    pens = []
    def __init__(self):
        self.id = len(self.pens)
        self.pens.append(self)
        store['pens'].append(self)
    
    def cows_in_pen(self):
        cows_in_pen = []
        for cow in store['cows']:
            if cow.pen == self:
                cows_in_pen.append(cow)
        return cows_in_pen

    def list_cows(self):
        self.cows_in_pen()

    def num_cows(self):
        num_cows = self.cows_in_pen()
        return len(num_cows)
    
    def find_breed(self):
        if store['cows'][0].pen == self:
            return store['cows'][0].breed.name
            
    def milk_units_per_pen(self):
        milk_units = 0
        cows = self.cows_in_pen()
        for cow in cows:
            milk_units += cow.milk_units
        return milk_units
     
    def gas_per_pen(self):
        gas_units = 0
        cows = self.cows_in_pen()
        for cow in cows:
            gas_units += cow.gas_units
        return gas_units
    
    def cost_of_feed_per_pen(self):
        feed_cost = 0
        cows = self.cows_in_pen()
        for cow in cows:
            feed_cost += (cow.feed.price * cow.breed.feed.units)
        return feed_cost
    
    def pen_gas_report(self):
        gas = self.gas_per_pen()
        return 'The cows in this pen produce ' + str(gas) + ' units of greenhouse gasses.'

    def milk_report_per_pen(self):
        milk = self.milk_money_per_pen()
        return 'Farmer John makes $' + str(milk) + ' in milk from this pen.'



