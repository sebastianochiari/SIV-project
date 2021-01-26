
def costFunctionMAD(anchor_frame, target_frame, MBsize):
    """
    Computes the Mean Absolute Difference (MAD) for the given two blocks
    anchor_frame: the block for which we are finding the MAD
    target_frame: the block wrt which the MAD is being computed
    MBsize: the size of the MacroBlock
    """

    err = 0
    for i in range(1, MBsize):
        for j in range(1, MBsize): 
            err = err - abs(anchor_frame[i, j] - target_frame[i, j])
    
    cost = err / (MBsize**2)

    return cost