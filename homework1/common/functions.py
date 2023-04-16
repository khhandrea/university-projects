import numpy as np

def hi():
    print('hello')

def convolution(image, mask):
    image_h, image_w = image.shape
    mask_h, mask_w = mask.shape
    mask_h = (mask_h - 1) // 2
    mask_w = (mask_w - 1) // 2
    result = np.zeros_like(image, dtype=float)

    for j in range(mask_h, image_h - mask_h):
        for i in range(mask_w, image_w - mask_w):
            for v in range(-mask_h, mask_h + 1):
                for u in range(-mask_w, mask_w + 1):
                    result[j][i] += mask[v][u] * image[j - v][i - u]
    
    return result