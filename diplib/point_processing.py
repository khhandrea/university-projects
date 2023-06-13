import cv2
import numpy as np

def negative_transformation(image, color_type=None):
    if(len(image.shape)==2):    
        width, height = image.shape[0], image.shape[1]
        result = np.ones((width, height))*np.max(image)
        result = result-image
    elif(len(image.shape)==3 and color_type=="RGB"):    
        width, height, channel = image.shape[0], image.shape[1], image.shape[2]
        result = np.ones((width, height, channel))
        for i in range(3):
            result[:, :, i] = result[:, :, i]*np.max(image[:, :, i])    # 각 채널 별 최대값
        result = result-image
    elif(len(image.shape)==3 and color_type=="HSI"):    
        width, height, channel = image.shape[0], image.shape[1], image.shape[2]
        result = image.copy()
        for i in range(1, 3):   # Saturation, Intensity Channel만 Transform
            result[:,:,i] = np.max(image[:,:,i]) - result[:,:,i]
        result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)
    return np.array(result, dtype='uint8')

def power_law_transformation(image, gamma, color_type=None):
    if(color_type=="GRAY" or color_type=="RGB"):
        result = np.array(255*(image/255)**gamma, dtype='uint8')
    elif(color_type=="HSI"):
        result = np.array(image, dtype='uint8')
        # result[:,:,0] = np.array(255*(image[:,:,0]/255)**gamma)
        result[:,:,1] = np.array(255*(image[:,:,1]/255)**gamma)
        result[:,:,2] = np.array(255*(image[:,:,2]/255)**gamma, dtype='uint8')
        result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)
    return result

def histogram_equalization(image, color_type=None):
    if(color_type=="GRAY"):
        channel = image
    elif(color_type=="HSI"):
        channel = image[:,:,2]

    width, height = channel.shape[0], channel.shape[1]
    max = np.max(channel) + 1
    min = np.min(channel)
    num_pixel = width*height

    hist = np.zeros(max)
    sum_hist = np.zeros(max)
    norm_hist = np.zeros(max)

    result = np.zeros((width, height))
    sum = 0
    for i in range(width):
        for j in range(height):
            hist[channel[i][j]] += 1
    min = sum_hist[min]
    for i in range(max):
        sum+=hist[i]
        sum_hist[i] = sum
        norm_hist[i] = np.around((max-1)*(sum_hist[i]-min)/(num_pixel-min))
    for i in range(width):
        for j in range(height):
            result[i][j] = norm_hist[channel[i][j]]
    if(color_type=="GRAY"):
        return np.array(result, dtype='uint8')
    elif(color_type=="HSI"):
        result_hsi = image
        result_hsi[:,:,2] = result
        result_hsi = cv2.cvtColor(result_hsi, cv2.COLOR_HSV2RGB)
        return result_hsi