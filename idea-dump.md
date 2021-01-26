### Motion Compensated Filtering

We need to extract the trajectory of each pixel along time and we use this information to perform better filtering.

### Pipeline

- Import the video
- Extract the trajectory of each block inside the video by estimating the motion and perform the filtering according to the temporal pipes
- Export the filtered video

Measure the variation between blocks in RGB gamma or luminance gamma and set a threshold.

Motion-estimation or optical flow estimation starting from the frame we want to filter and we go backward and forward looking at the motion vector, calculating the motion vectors corresponding to a given area of the frame. These motion vectors allow us to create the pipe, by tracking the movements in the scene.