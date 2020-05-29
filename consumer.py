import numpy as np
import cvxpy as cp

class Consumer:
    """
    A class that model a consumer in the Arrow-Debreu Economy
    """

    def __init__(self, endowment, valuation, rho):
        self.endowment = endowment # consumer's endowment of commodities
        self.valuation = valuation # consumer's valuation of goods
        self.rho = rho # parameter for the CES utility function

    def get_endowment(self):
        """
        Return endowment of consumer
        """
        return self.endowment
        
    def get_utility(self, bundle):
        """
        A function that calculates the (CES) utility of a consumer for a bundle
        """
        return ( self.valuation.T @ np.power(bundle, self.rho) )**(1/self.rho)

    def get_demand(self, prices):
        """
        Function that calculates the demand of the consumer for goods
        at gives prices
        """

        # Declare program variable
        opt_bundle = cp.Variable(self.valuation.shape[0])
        
        # Declare utility maximization objective
        obj = cp.Maximize( (self.valuation.T @ cp.power(opt_bundle, self.rho))**(1/self.rho) )
        
        # Declare budget constraint and allocation constraint
        constraints = [opt_bundle.T @ prices <= self.endowment.T @ prices,
                        opt_bundle >= 0] 

        # Declare program
        program = cp.Problem(obj, constraints)

        # Solve Program
        program.solve()  # Returns the optimal value.
        # print(f"Convex program solution is: {opt_bundle.value}")
        return opt_bundle.value
