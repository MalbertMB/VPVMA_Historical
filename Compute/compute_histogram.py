import numpy as np

def calculate_histogram(VPVMA, VPVMAS):
    """
    Calculate the difference (histogram) between two lists or arrays.

    Parameters:
        VPVMA (list or np.array): The first list or array of numerical values.
        VPVMAS (list or np.array): The second list or array of numerical values.
    
    Returns:
        list: A list containing the differences (VPVMA - VPVMAS) element-wise.

    Note:
        Both VPVMA and VPVMAS must have the same length.
    """
    
    if len(VPVMA) != len(VPVMAS):
        raise ValueError("calculate_histogram: VPVMA and VPVMAS must have the same length.")
    
    # Convert to numpy arrays for better performance
    VPVMA = np.array(VPVMA)
    VPVMAS = np.array(VPVMAS)
    
    # Calculate the differences element-wise
    result = VPVMA - VPVMAS
    return result.tolist()