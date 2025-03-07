def buy_sell_analysis_timeframe(VPVMA,VPVMAS,bandwidth):
    """
    Identify buying and selling points based on trading logic.
    The logic is based on the comparison of two moving averages, VPVMA and VPVMAS.
    The function returns the indices of the buying and selling points.

    Parameters:
        VPVMA (list or np.array): The first list or array of numerical values, typically the shorter moving average.
        VPVMAS (list or np.array): The second list or array of numerical values, typically the longer moving average.
        bandwidth (float): A percentage threshold that influences buy and sell conditions.
    
    Returns:
        tuple: Two lists containing the indices of buy points and sell points, respectively.

    Note:
        Both VPVMA and VPVMAS must have the same length.
    """
    
    length = len(VPVMA)
    buy_points = []
    sell_points = []
    buy = False
    sell = False

    for t in range(1,length):
        if (VPVMA[t] > (1+bandwidth)*VPVMAS[t]) and (VPVMA[t-1] < VPVMAS[t-1]) and (sell or not buy) :
            buy_points.append(t)
            if sell:
                sell = False
            elif not sell:
                buy = True
        
        if (VPVMA[t] < (1+bandwidth)*VPVMAS[t]) and (VPVMA[t-1] > VPVMAS[t-1]) and (buy or not sell):
            sell_points.append(t)
            if buy:
                buy = False
            elif not buy:
                sell = True
    
    return buy_points, sell_points
