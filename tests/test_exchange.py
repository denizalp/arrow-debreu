import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir) 
sys.path.insert(0,parentdir) 
import exchange as e
import consumer as c
import numpy as np

# Declare number of goods, consumers and elasticity of substitution (rho) 
num_commods = 6
num_consumers = 4
rho = 1
supply = np.zeros(num_commods)

# Create consumers
consumers = []

for i in range(num_commods):
    endowment = np.random.randint(4, size=num_commods)
    valuation = np.random.randint(5, size=num_commods)
    supply += endowment
    consumers.append(c.Consumer(endowment, valuation, rho))


# Create economy
economy = e.Exchange(consumers, num_commods)
# print(f"The excess demand at low prices: {economy.get_excess()}")
economy.tatonnement(learning_rate = 0.1)
# print(f"The total supply of each commodity is {supply}")
