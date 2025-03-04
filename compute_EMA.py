import numpy as np

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
    
    
    if len(VWMA) != len(DV):
        raise ValueError("calculate_EMA: VWMA and DV must be equal in length.")

    if len(VWMA) < window_size * 3:
        raise ValueError("calculate_EMA: VWMA and DV must each be at least 3 times the size of the window.")

    # Convert to numpy arrays for better performance
    VWMA = np.array(VWMA)
    DV = np.array(DV)

    # Calculate the values
    values = VWMA * DV

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
