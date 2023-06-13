import cv2
import numpy as np

def prewitt_operator(self, image, threshold, background, color_type=None):
    size = 3
    radius = 1
    prewitt_hor = np.array([[-1, 0, 1],
                            [-1, 0, 1],
                            [-1, 0, 1]])
    prewitt_ver = np.array([[1, 1, 1],
                            [0, 0, 0],
                            [-1, -1, -1]])
    threshold = 50*threshold
    if(len(image.shape)==2):
        width, height = image.shape[0], image.shape[1]
        result = np.zeros((width-2*radius, height-2*radius))
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                horizon = np.sum(np.multiply(image[i:i+size,j:j+size], prewitt_hor))
                vertical = np.sum(np.multiply(image[i:i+size,j:j+size], prewitt_ver))
                magnitude = np.sqrt(horizon**2 + vertical**2)
                if magnitude>=threshold:
                    result[i,j] = 255
                elif(background=='X'):
                    result[i,j] = 0
                else:
                    result[i,j] = image[i+1, j+1]   #0으로 설정하면 테두리만 나옴
        return np.array(result, dtype='uint8')
    elif(len(image.shape)==3 and color_type=="RGB"):
        width, height, channel = image.shape[0], image.shape[1], image.shape[2]
        result = image[radius:width-radius+1, radius:height-radius+1, :].copy()
        for ch in range(channel):
            for i in range(width-2*radius):
                for j in range(height-2*radius):
                    horizon = np.sum(np.multiply(image[i:i+size,j:j+size,ch], prewitt_hor))
                    vertical = np.sum(np.multiply(image[i:i+size,j:j+size,ch], prewitt_ver))
                    magnitude = np.sqrt(horizon**2 + vertical**2)
                    if magnitude>=threshold:
                        result[i, j, ch] = 255
                    elif(background=='X'):
                        result[i, j, ch] = 0
        return np.array(result, dtype='uint8')
    elif(len(image.shape)==3 and color_type=="HSI"):
        width, height = image.shape[0], image.shape[1]
        result = image[radius:width-radius+1, radius:height-radius+1, :].copy()
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                horizon = np.sum(np.multiply(image[i:i+size,j:j+size,2], prewitt_hor))
                vertical = np.sum(np.multiply(image[i:i+size,j:j+size,2], prewitt_ver))
                magnitude = np.sqrt(horizon**2 + vertical**2)
                if magnitude>=threshold:
                    result[i,j,0], result[i,j,1], result[i,j,2] = 0, 0, 255
                elif(background=='X'):
                    result[i,j,0], result[i,j,1], result[i,j,2] = 0, 0, 0
        result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)
        return np.array(result, dtype='uint8')
    
#Sobel Operator
def sobel_operator(self, image, threshold, background, color_type=None):
    size = 3
    radius = 1
    sobel_hor = np.array([[-1, 0, 1],
                            [-2, 0, 2],
                            [-1, 0, 1]])
    sobel_ver = np.array([[1, 2, 1],
                            [0, 0, 0],
                            [-1, -2, -1]])
    threshold = 50*threshold
    if(len(image.shape)==2):
        width, height = image.shape[0], image.shape[1]
        result = np.zeros((width-2*radius, height-2*radius))
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                horizon = np.sum(np.multiply(image[i:i+size,j:j+size], sobel_hor))
                vertical = np.sum(np.multiply(image[i:i+size,j:j+size], sobel_ver))
                magnitude = np.sqrt(horizon**2 + vertical**2)
                if magnitude>=threshold:
                    result[i,j] = 255
                elif(background=='X'):
                    result[i,j] = 0
                else:
                    result[i,j] = image[i+1, j+1]   #0으로 설정하면 테두리만 나옴
        return np.array(result, dtype='uint8')
    elif(len(image.shape)==3 and color_type=="RGB"):
        width, height, channel = image.shape[0], image.shape[1], image.shape[2]
        result = image[radius:width-radius+1, radius:height-radius+1, :].copy()
        for ch in range(channel):
            for i in range(width-2*radius):
                for j in range(height-2*radius):
                    horizon = np.sum(np.multiply(image[i:i+size,j:j+size,ch], sobel_hor))
                    vertical = np.sum(np.multiply(image[i:i+size,j:j+size,ch], sobel_ver))
                    magnitude = np.sqrt(horizon**2 + vertical**2)
                    if magnitude>=threshold:
                        result[i, j, ch] = 255
                    elif(background=='X'):
                        result[i, j, ch] = 0
        return np.array(result, dtype='uint8')
    elif(len(image.shape)==3 and color_type=="HSI"):
        width, height = image.shape[0], image.shape[1]
        result = image[radius:width-radius+1, radius:height-radius+1, :].copy()
        for i in range(width-2*radius):
            for j in range(height-2*radius):
                horizon = np.sum(np.multiply(image[i:i+size,j:j+size,2], sobel_hor))
                vertical = np.sum(np.multiply(image[i:i+size,j:j+size,2], sobel_ver))
                magnitude = np.sqrt(horizon**2 + vertical**2)
                if magnitude>=threshold:
                    result[i,j,0], result[i,j,1], result[i,j,2] = 0, 0, 255
                elif(background=='X'):
                    result[i,j,0], result[i,j,1], result[i,j,2] = 0, 0, 0
        result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)
        return np.array(result, dtype='uint8')

#LoG Operator
def LoG_operator(self, image, size, sigma, color_type=None):
    if(len(image.shape)==3 and color_type=="HSI"):
        blur = cv2.GaussianBlur(image[:,:,2], (size, size), sigma)
        result = cv2.Laplacian(blur, cv2.CV_8U, ksize=size)
    else:
        blur = cv2.GaussianBlur(image, (size, size), sigma)
        result = cv2.Laplacian(blur, cv2.CV_8U, ksize=size)
    return result
    
#Canny Operator
def canny_operator(self, image, min_threshold, max_threshold, color_type=None):
    if(len(image.shape)==3 and color_type=="HSI"):
        result = cv2.Canny(image[:,:,2], min_threshold, max_threshold)
    else:
        result = cv2.Canny(image, min_threshold, max_threshold)
    return result