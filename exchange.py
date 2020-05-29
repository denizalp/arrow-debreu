import numpy as np
import consumer

class Exchange:
    def __init__(self, consumers, num_commods):
        self.consumers = consumers
        self.num_commods = num_commods


    def get_demand(self, prices):
        """
        Function that calculates the total demand (i.e. for all consumers) for commodities at given prices
        """
        demand = np.zeros(self.num_commods)
        for consumer in self.consumers:
            demand = demand + consumer.get_demand(prices)

        return demand

    def get_supply(self):
        supply = np.zeros(self.num_commods)
        for consumer in self.consumers:
            supply = supply + consumer.get_endowment()

        return supply 
    
    def get_excess(self, prices):
        """
        Function that calculates the excess demand at given prices
        """
        return self.get_demand(prices) - self. get_supply()

    def tatonnement(self, learning_rate):
        """
        Function that runs the tatonnement process
        """
        prices = np.repeat(1/self.num_commods, self.num_commods)*100
        excess = self.get_excess(prices)
        iter = 1

        while (np.sum(np.abs(excess)) > 0.01 and iter <= 1000):
            print(f"The excess demand is {excess}\n Prices are {prices}")
            excess = self.get_excess(prices)
            prices += learning_rate*excess
            prices = np.clip(prices, 0, 100) + 0.001
            prices = prices/np.sum(prices)*100
            prices = np.round(prices, decimals = 3) 
            iter += 1
            

        return prices




