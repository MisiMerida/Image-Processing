#Copy image path at line 84.
import cv2 as cv
import matplotlib.pyplot as plt
from skimage.exposure import match_histograms

def display_image(img, title):
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def img_negative(img):
    negative_img = 255 - img
    display_image(negative_img, 'Negative Image')
    
def img_blur(img):
    while True:
        print('\n')
        print('a. Apply soft filtering (3x3)')
        print('b. Apply medium filtering (9x9)')
        print('c. Apply hard filtering (15x15)')
        print('Type any other key to exit')
        choice = input("Enter your choice: ").lower()
        print('\n')

        if choice == 'a':
            blurred_img = cv.blur(img, (3, 3))
            display_image(blurred_img, 'Blurred Image (3x3)')
        elif choice == 'b':
            blurred_img = cv.blur(img, (9, 9))
            display_image(blurred_img, 'Blurred Image (9x9)')
        elif choice == 'c':
            blurred_img = cv.blur(img, (15, 15))
            display_image(blurred_img, 'Blurred Image (15x15)')
        else:
            break
    return blurred_img

def img_sharpen(img):
    laplacian = cv.Laplacian(img, cv.CV_64F)
    sharpened_img = cv.convertScaleAbs(img-laplacian)
    display_image(sharpened_img, 'Sharpened Image')
    return sharpened_img
    
def img_histogram(img):
    plt.hist(img.ravel(), 256, [0, 256], color='grey')
    plt.title('Image Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()

def img_match_histograms(img):
    while True:
        print('1. Blurred Image')
        print('2. Sharpened Image')
        print('Type any other key to exit')
        choise = input('Enter your choise: ')
        print('\n')
        if choise == '1':
            img2 = img_blur(img)
            matched = match_histograms(img2,img)
            display_image(matched, 'Blurred Matched Histogram')
            
            plt.hist(matched.ravel(), 256, [0, 256], color='black')
            plt.title('Matched Image Histogram')
            plt.xlabel('Pixel Value')
            plt.ylabel('Frequency')
            plt.show()
            
        elif choise == '2':
            img2 = img_sharpen(img)
            matched = match_histograms(img2,img)
            display_image(matched, 'Sharpened Matched Histogram')
            
            plt.hist(matched.ravel(), 256, [0, 256], color='black')
            plt.title('Matched Image Histogram')
            plt.xlabel('Pixel Value')
            plt.ylabel('Frequency')
            plt.show()
            
        else:
            break
         
img_path = r"The path goes here"
img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

if img is None:
    print("There was a problem with the path.")
else:

    while True:
        print('\n')
        print('***Menu***')
        print('a. Show negative of the image')
        print('b. Blur the image')
        print('c. Sharpen the image')
        print('d. Create histogram')
        print('e. Match histograms with filtered image') 
        print('f. Exit')
        choice = input("Enter your choice: ").lower()
        print('\n')

        if choice == 'a':
            img_negative(img)
        elif choice == 'b':
            img_blur(img)
        elif choice == 'c':
            img_sharpen(img)
        elif choice == 'd':
            img_histogram(img)
        elif choice == 'e':
            img_match_histograms(img)
        elif choice == 'f':   
            break
        else:
            print("Invalid input. Please pick a, b, c, d, e, or f.")