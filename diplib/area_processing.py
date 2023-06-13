import cv2
import numpy as np

def mean_filter(image, size, color_type=None):
    total_size = size**2
    radius = int((size-1)/2)
    if(len(image.shape)==2):
        width, height = image.shape[0], image.shape[1]
        result = np.zeros((width-2*radius, height-2*radius))
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                result[i,j] = np.sum(image[i:i+size,j:j+size])/total_size
    elif(len(image.shape)==3 and color_type=="RGB"):
        width, height, channel = image.shape[0], image.shape[1], image.shape[2]
        result = np.zeros((width-2*radius, height-2*radius, channel))
        for ch in range(channel):
            for i in range(width-2*radius):
                for j in range(height-2*radius):
                    result[i,j,ch] = np.sum(image[i:i+size,j:j+size,ch])/total_size
    elif(len(image.shape)==3 and color_type=="HSI"):
        width, height = image.shape[0], image.shape[1]
        result = image[radius:width-radius+1, radius:height-radius+1, :].copy()
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                result[i,j,2] = np.sum(image[i:i+size,j:j+size,2])/total_size
        result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)
    return np.array(result, dtype='uint8')

def median_filter(image, size, color_type=None):
    radius = int((size-1)/2)
    if(len(image.shape)==2):
        width, height = image.shape[0], image.shape[1]
        result = np.zeros((width-2*radius, height-2*radius))
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                result[i,j] = np.median(image[i:i+size,j:j+size])
    elif(len(image.shape)==3 and color_type=="RGB"):
        width, height, channel = image.shape[0], image.shape[1], image.shape[2]
        result = np.zeros((width-2*radius, height-2*radius, channel))
        for ch in range(channel):
            for i in range(width-2*radius):
                for j in range(height-2*radius):
                    result[i,j,ch] = np.median(image[i:i+size,j:j+size,ch])
    elif(len(image.shape)==3 and color_type=="HSI"):
        width, height = image.shape[0], image.shape[1]
        result = image[radius:width-radius+1, radius:height-radius+1, :].copy()
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                result[i,j,2] = np.median(image[i:i+size,j:j+size,2])
        result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)
    return np.array(result, dtype='uint8')

def gaussian_filter(image, size, sigma, color_type=None):
    kernel1d = cv2.getGaussianKernel(size, sigma)
    kernel2d = np.outer(kernel1d, kernel1d.transpose())
    radius = int((size-1)/2)
    if(len(image.shape)==2):
        width, height = image.shape[0], image.shape[1]
        result = np.zeros((width-2*radius, height-2*radius))
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                result[i,j] = np.sum(np.multiply(image[i:i+size,j:j+size], kernel2d))
    elif(len(image.shape)==3 and color_type=="RGB"):
        width, height, channel = image.shape[0], image.shape[1], image.shape[2]
        result = np.zeros((width-2*radius, height-2*radius, channel))
        for ch in range(channel):
            for i in range(width-2*radius):
                for j in range(height-2*radius):
                    result[i,j,ch] = np.sum(np.multiply(image[i:i+size,j:j+size,ch], kernel2d))
    elif(len(image.shape)==3 and color_type=="HSI"):
        width, height = image.shape[0], image.shape[1]
        result = image[radius:width-radius+1, radius:height-radius+1, :].copy()
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                result[i,j,2] = np.sum(np.multiply(image[i:i+size,j:j+size,2], kernel2d))
        result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)
    return np.array(result, dtype='uint8')

def highboost_filter(image, alpha, highpass, color_type=None):
    size = 3
    radius = int((size-1)/2)
    if(highpass==4):
        kernel = np.zeros((size, size))
        kernel[radius-1, radius] = kernel[radius+1, radius] = -1
        kernel[radius, radius-1] = kernel[radius, radius+1] = -1
        kernel[radius, radius] = 4 + alpha
    elif(highpass==8):
        kernel = -np.ones((size, size))
        kernel[radius, radius] = 8 + alpha
    
    if(len(image.shape)==2):
        width, height = image.shape[0], image.shape[1]
        result = np.zeros((width-2*radius, height-2*radius))
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                result[i,j] = np.sum(np.multiply(image[i:i+size,j:j+size], kernel))
    elif(len(image.shape)==3 and color_type=="RGB"):
        width, height, channel = image.shape[0], image.shape[1], image.shape[2]
        result = image[radius:width-radius+1, radius:height-radius+1, :].copy()
        for ch in range(channel):
            for i in range(width-2*radius):
                for j in range(height-2*radius):
                    result[i,j,ch] = np.sum(np.multiply(image[i:i+size,j:j+size,ch], kernel))
    elif(len(image.shape)==3 and color_type=="HSI"):
        width, height = image.shape[0], image.shape[1]
        result = image[radius:width-radius+1, radius:height-radius+1, :].copy()
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                result[i,j,2] = np.sum(np.multiply(image[i:i+size,j:j+size,2], kernel))
        result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)
    return np.clip(np.array(result, dtype='uint8'), 0, 255)