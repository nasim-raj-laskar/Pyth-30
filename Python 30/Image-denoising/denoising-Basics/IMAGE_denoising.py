from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_ubyte, img_as_float
from matplotlib import pyplot as plt
from skimage import io
import numpy as np
from scipy import ndimage as nd

img = img_as_float(io.imread("nosy.png"))

gaussian_img = nd.gaussian_filter(img, sigma=3)
plt.imsave("gaussian1.png", gaussian_img)

median_img = nd.median_filter(img, size=3)
plt.imsave("denoise1.png", median_img)

sigma_est = np.mean(estimate_sigma(img, channel_axis=-1))

denoise_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=False,
                               patch_size=5, patch_distance=3)

denoise_img_as_8byte = img_as_ubyte(denoise_img)

plt.imshow(denoise_img)
plt.imsave("denoise2.png", denoise_img)
