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
    
    # Input validation
    if len(VPVMA) != len(VPVMAS):
        raise ValueError("calculate_histogram: VPVMA and VPVMAS must have the same length.")
    
    # Calculate the differences element-wise
    result = [VPVMA[i] - VPVMAS[i] for i in range(len(VPVMA))]
    return result
