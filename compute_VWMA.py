def calculate_vwma(TP_prices, volume, n):
    """
    Calculate the Volume Weighted Moving Average (VWMA) for a given list of typical prices (TP)
    and volume values over a period of n.

    Parameters:
        TP_prices (list): A list of typical prices (TP).
        volume (list): A list of corresponding volume values (V).
        n (int): The number of periods over which to calculate the VWMA.

    Returns:
        list: A list containing the calculated VWMA values. The first `n-1` values will be None.
    """

    # Ensure the inputs are of the same length
    if len(TP_prices) != len(volume):
        raise ValueError("calculate_vwma: TP_prices and volume lists must be of the same length.")

    # Ensure the window size is valid
    if n > len(TP_prices):
        raise ValueError("calculate_vwma: The window size n cannot exceed the length of the input lists.")
    #To calculate the VWMA we lose data length and to calculate the EMA we need 3 times
    # the data desired, the initial input should be 4-5 times the result.

    vwma = []

    for i in range(len(TP_prices)):
        if i < n - 1:
            # Not enough data to calculate VWMA for the first n-1 periods
            # vwma.append(None)
            continue
        else:
            # Define the current window
            TP_subset = TP_prices[i - n + 1:i + 1]
            volume_subset = volume[i - n + 1:i + 1]

            # Apply the VWMA formula
            numerator = sum(tp * v for tp, v in zip(TP_subset, volume_subset))
            denominator = sum(volume_subset)

            # Handle division by zero gracefully
            vwma.append(numerator / denominator if denominator != 0 else None)

    return vwma

