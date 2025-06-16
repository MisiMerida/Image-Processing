import cv2
import matplotlib.pyplot as plt
from skimage.util import random_noise
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
from scipy.ndimage import gaussian_filter, median_filter, uniform_filter

def show_image(image, title, cmap='gray'):
    plt.figure()
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis('off')
    plt.show()

def gaussian_noise(image, mean=0, var=0.01):
    return random_noise(image, mode='gaussian', mean=mean, var=var)

def salt_pepper_noise(image, amount=0.05):
    return random_noise(image, mode='s&p', amount=amount)

def mean_fil(image, kernel_size):
    return uniform_filter(image, size=kernel_size)

def median_fil(image, kernel_size):
    return median_filter(image, size=kernel_size)

def gaussian_fil(image, sigma):
    return gaussian_filter(image, sigma=sigma)

def evaluate(original, restored):
    p = psnr(original, restored, data_range=1.0)
    s = ssim(original, restored, data_range=1.0)
    return p, s

img_path = r"Image path"
original = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) / 255.0

gauss1 = gaussian_noise(original, var=0.01)
gauss2 = gaussian_noise(original, var=0.03)

sp1 = salt_pepper_noise(original, amount=0.03)
sp2 = salt_pepper_noise(original, amount=0.01)

show_image(original, 'Original')
show_image(gauss1, 'Gaussian 0.01')
show_image(gauss2, 'Gaussian 0.03')
show_image(sp1, 'Salt & Pepper 0.03')
show_image(sp2, 'Salt & Pepper 0.01')

mean3_1 = mean_fil(gauss1, 3)
gauss_1 = gaussian_fil(gauss1, sigma=1)
mean3_2 = mean_fil(gauss2, 3)
gauss_2 = gaussian_fil(gauss2, sigma=1)

for img, label in [(mean3_1, "Mean 3x3 1"), (gauss_1, "Gaussian 1"), (mean3_2, "Mean 3x3 2"), (gauss_2, "Gaussian 2")]:
    show_image(img, label)
    p, s = evaluate(original, img)
    print(f"{label}: PSNR={p}, SSIM={s}")

mean5_1 = mean_fil(sp1, 3)
median_1 = median_fil(sp1, 1)
mean5_2 = mean_fil(sp2, 3)
median_2 = median_fil(sp2, 1)

for img, label in [(mean5_1, "Mean 5x5 S&P1"), (median_1, "Median S&P1"), (mean5_2, "Mean 5x5 S&P2"), (median_2, "Median S&P2")]:
    show_image(img, label)
    p, s = evaluate(original, img)
    print(f"{label}: PSNR={p}, SSIM={s}")
