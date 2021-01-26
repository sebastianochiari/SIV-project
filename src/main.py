
# Motion-Compensated Video Filtering
# Author: Sebastiano Chiari

import numpy as np
import cv2
from motionEstimation import motionEstimation

## CONFIGURATION SECTION ##
input_video = './local/'+ 'foreman_cif.mov'
output_video = './local/'+ 'output-foreman_cif' + '.avi'
# define how bigger will be the macroblock in order to compute the motion estimation
macroBlock_dimension = 16
# define how much frame will be considered forward and backward in order to compute the filtering
temporal_displacement = 2

## SETUP SECTION ##
print('## Start SETUP section ##')

# Importing video and retrieve meaningful parameters
video = cv2.VideoCapture(input_video)
fps = video.get(cv2.CAP_PROP_FPS)
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Open the video encoder, define the codec and create VideoWriter object
output = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width, frame_height))

# Setting variables
frame_counter = 0
previous_frame = None
current_frame = None
future_frame = None

print('## End SETUP section ##' + '\n')

## VIDEO PROCESSING SECTION ##
print('## Start VIDEO PROCESSING section ##')

# copy every frame into a list for better usage
frames = []
while(True):
    ret, frame = video.read()
    if ret == True:
        # if the frame is correctly extracted, save in the frames List
        frames.append(frame)
        frame_counter += 1
    else:
        break

# computing the motion estimation and the filtering according to the motion vectors
for i in range(0, total_frames):
    anchor_index = i
    # compute impulse in the anchor frame

    # compute the motion estimation starting from the anchor frame with the selected window
    for k in range(-temporal_displacement, temporal_displacement + 1):
        # remove the identity frame
        if k == 0:
            continue

        # check for list index overflow
        target_index = i + k
        if (target_index) >= total_frames or (target_index) < 0:
            continue

        
        # motionVector, EScomputations = motionEstimation(frames[anchor_index], frames[target_index], macroBlock_dimension)


# while(True):
#     ret, frame = video.read()
#     if ret == True:

#         # conversion from RGB to YCBCR
#         frame_YCBCR = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)            
#         # extract the single channel components from the frame
#         Y, Cb, Cr = cv2.split(frame_YCBCR)

#         if frame_counter == 1:
#             print('Frame: ', frame_counter)
#             previous_frame = Y
#             frame_counter += 1
#         else:
#             print('Frame: ', frame_counter)
#             current_frame = Y

#             motionEstimationVector = motionEstimation(current_frame, previous_frame)

#             previous_frame = frame
#             frame_counter += 1

#             # Press Q on keyboard to stop recording
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#             ## MOTION ESTIMATION SECTION ##

#             ## FILTERING SECTION BASED OVER MOTION ESTIMATION ##
#     else:
#         break

print('## End VIDEO PROCESSING section ##' + '\n')

# Write the new video
# while(True):
#   ret, frame = cap.read()

#   if ret == True: 
    
#     # Write the frame into the file 'output.avi'
#     out.write(frame)

#     # Display the resulting frame    
#     cv2.imshow('frame',frame)

#     # Press Q on keyboard to stop recording
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#       break

#   # Break the loop
#   else:
#     break 

# When everything done, release the video capture and video write objects
video.release()
output.release()

# Closes all the frames
cv2.destroyAllWindows()