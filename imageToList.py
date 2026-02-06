import cv2
import numpy as np

def image_preprocess(image_path):
    """
    Preprocess the image to extract the grid.
    This function reads the image, converts it to grayscale, and applies thresholding.
    """
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive thresholding to get a binary image
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    return thresh

def extract_boxes(thresh):
    # returns list[list] of images for identification
    pass

def identify_box(box_image):
    # returns int for the box
    pass

def image_to_grid(image_path):
    img = image_preprocess(image_path)
    boxes_img = extract_boxes(img)
    boxes_num = [[identify_box(box) for box in row] for row in boxes_img]
    return boxes_num
