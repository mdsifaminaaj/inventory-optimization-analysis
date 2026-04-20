import numpy as np

def calculate_eoq(D, S, H):
    """
    D = demand
    S = ordering cost
    H = holding cost
    """
    return np.sqrt((2 * D * S) / H)


def calculate_rop(avg_demand, lead_time, safety_stock=0):
    """
    avg_demand = average daily demand
    lead_time = days
    """
    return (avg_demand * lead_time) + safety_stock