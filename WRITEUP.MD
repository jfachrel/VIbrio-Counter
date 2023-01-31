# Vibrio Counter

## Flow
- Masking the color
- Image processing to find contours (GaussianBlur, Canny, dilate)
- Calculate the number of vibrio based on the number of contours.

## Bottleneck
- Difficult to get parameters that can perfectly describe the contours of the pond.
- There are several pools that are not detected due to inappropriate contours.

## Area Improvement
- crop
- Perform parameter analysis
- Uses an object detection model to detect vibrios
