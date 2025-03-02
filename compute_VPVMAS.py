def calculate_VPVMAS(VPVMA, n):
    """
    Calculate the simple moving average of a list.
    
    Parameters:
        VPVMA (list): A list of numerical values.
        n (int): The period for the moving average.
    
    Returns:
        list: A list containing the simple moving averages for each valid period.
    """
    
    if n <= 0:
        raise ValueError("calculate_VPVMAS: The period 'n' must be a positive integer.")
    if n > len(VPVMA):
        raise ValueError("calculate_VPVMAS: The period 'n' cannot be greater than the length of the VPVMA list.")
    
    moving_averages = []
    for i in range(len(VPVMA)):
        if i < n - 1:
            # Not enough data to calculate MA for the first n-1 periods
            continue
        else:
            # Define the current window
            window = VPVMA[i - n + 1:i + 1]

            # Apply the MA formula
            moving_average = sum(window)/n

            moving_averages.append(moving_average)        
    
    return moving_averages
