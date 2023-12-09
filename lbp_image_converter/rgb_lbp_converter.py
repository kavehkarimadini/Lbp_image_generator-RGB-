import numpy as np


def get_pixel3d(img, center, x, y, z):
    new_value = 0
    try:
        if img[x][y][z] >= center:
            new_value = 1
    except:
        pass
    return new_value


def lbp_calculated_pixel3d(img, x, y, z):
    center = img[x][y][z]
    val_ar = [get_pixel3d(img, center, x-1, y+1, z)]
    val_ar.append(get_pixel3d(img, center, x, y+1, z))       # right
    val_ar.append(get_pixel3d(img, center, x+1, y+1, z))     # bottom_right
    val_ar.append(get_pixel3d(img, center, x+1, y, z))       # bottom
    val_ar.append(get_pixel3d(img, center, x+1, y-1, z))     # bottom_left
    val_ar.append(get_pixel3d(img, center, x, y-1, z))       # left
    val_ar.append(get_pixel3d(img, center, x-1, y-1, z))     # top_left
    val_ar.append(get_pixel3d(img, center, x-1, y, z))       # top
    arr = np.array(val_ar)
    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
    arr_1 = np.array(power_val)
    mularr = np.multiply(arr, arr_1)
    return np.sum(mularr)


def convlbp3d(img):
    height, width, channel = img.shape
    img_lbp = np.zeros((height, width, 3), np.uint8)
    for k in range(channel):
        for i in range(height):
            for j in range(width):
                img_lbp[i, j, k] = lbp_calculated_pixel3d(img, i, j, k)
    return img_lbp
