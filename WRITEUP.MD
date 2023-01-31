# Vibrio Counter

## Flow
- Masking the color(yellow or green)
- Image processing to find contours (GaussianBlur, Canny, dilate)
- Calculate the number of vibrio based on the number of contours.

## Bottleneck
- Difficult to get parameters that can perfectly describe the contours of the pond.
- There are several pools that are not detected due to inappropriate contours.

## Area Improvement
- Crop the image to get the whole cup 
- Perform parameter analysis
- Uses an object detection model to detect vibrios
