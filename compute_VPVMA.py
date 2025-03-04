def calculate_VPVMA(ESV, ELV):
    """
    Calculate the VPVMA, the difference between EMAs.

    Parameters:
        ESV (list): EMA using the short window
        ELV (list): EMA using the long window

    Returns:
        VPVMA (list): The calculated VPVMA value.
    """
    
    if len(ESV) != len(ELV):
        raise ValueError("calculate_VPVMA: The length of ESV must be equal to the length of ELV.")
    
    # Calculate VPVMA using list comprehension
    VPVMA = [esv - elv for esv, elv in zip(ESV, ELV)]

    return VPVMA