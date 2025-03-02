def calculate_EMA(VWMA, DV, window_size):
    """
    Calculate the Exponential Moving Average (EMA) of VWMA * DV.

    Parameters:
        VWMA (list or np.array): The list of numerical values.
        DV (list or np.array): The list of numerical values.
        window_size (int): The size of the moving average (smoothing factor).
    
    Returns:
        list: The EMA values.

    Note:
        The length of VWMA and DV must be at least 3 times the window_size.
    """
    
    if not VWMA or window_size <= 0 or not DV:
        raise ValueError("calculate_EMA: VWMA and DV must be non-empty lists, and window_size must be a positive integer.")
    
    if len(VWMA) != len(DV):
        raise ValueError("calculate_EMA: VWMA and DV must be equal in length.")

    if len(VWMA) < window_size * 3:
        raise ValueError("calculate_EMA: VWMA and DV must each be at least 3 times the size of the window.")

    # Calculate the values
    values = [VWMA[i] * DV[i] for i in range(len(VWMA))]

    # Initialize EMA values
    ema_values = []
    alpha = 2 / (window_size + 1)  # Smoothing factor
    
    # Start EMA with the first value
    ema_values.append(values[0])

    # Calculate the EMA iteratively
    for i in range(1, len(values)):
        ema = (values[i] * alpha) + (ema_values[-1] * (1 - alpha))
        ema_values.append(ema)

    return ema_values
