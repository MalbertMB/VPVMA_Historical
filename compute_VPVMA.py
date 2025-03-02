def calculate_VPVMA(ESV,ELV):
    """
    Calculate the VPVMA, the difference between EMAs.

    Parameters:
        ESV (list): EMA using the short window
        ELV (list): EMA using the 

    Returns:
        VPVMA (list): The calculated VWMA value.
    """
    
    if len(ESV) != len(ELV):
        raise ValueError("calculate_VPVMA: The length of is ESV != length of ELV")
    
    VPVMA = []
    for i in range(len(ESV)):
        VPVMA.append(ESV[i]-ELV[i])

    return VPVMA