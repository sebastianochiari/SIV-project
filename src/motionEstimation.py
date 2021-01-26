import numpy as np
import math
import cv2
from costFunctionMAD import costFunctionMAD

def motionEstimation(anchor_frame, target_frame, macroBlock_dimension):

    row, columns = target_frame.shape

    # block size
    MBsize = macroBlock_dimension

    search_range = macroBlock_dimension

    # build the matrix where the MotionVector will be stored
    vectors = np.zeros((2, int(row*columns/MBsize**2)))

    # computational cost
    computations = 0

    # we start off from the top left of the image
    # we will walk in steps of 16
    # for every macroblock that we look for
    # a close match 16 pixels on the left, right, top, bottom of it
    mbCount = 1

    # cycle over each row with a step equal to MBsize
    for i in range(0, row - MBsize, MBsize):
        #cycle over each column with a step equal to MBsize
        for j in range(0, columns - MBsize, MBsize):

            # for every block in the anchor frame
            MAD_min = 256 * MBsize**2
            mvx = 0
            mvy = 0

            # cycle over each row pixel inside the MacroBlock
            for k in range(-search_range, search_range, 1):
                # cycle over each column pixel inside the MacroBlock
                for l in range(-search_range, search_range, 1):
                    
                    refBlkVer = i + k # row / vertical co-ordinate for ref block
                    refBlkHor = j + l # col / horizontal co-ordinate
                    
                    # border conditions
                    if(refBlkVer < 1 or refBlkVer+16-1 > row or refBlkHor < 1 or refBlkHor+16-1 > columns):
                        continue
                    
                    macroBlock_anchorFrame = anchor_frame[i:(i + 16), j:(j + 16)]
                    macroBlock_targetFrame = target_frame[refBlkVer:(refBlkVer + 16), refBlkHor:(refBlkHor + 16)]

                    MAD = costFunctionMAD(macroBlock_anchorFrame, macroBlock_targetFrame, 16);

                    computations = computations + 1

                    if (MAD < MAD_min):
                        MAD_min = MAD
                        dy = k
                        dx = l
            
            vectors[0, mbCount] = dx;
            vectors[1, mbCount] = dy;
            mbCount = mbCount + 1;
    
    motionVectors = vectors;
    EScomputations = computations/(mbCount - 1);

    return motionVectors, EScomputations