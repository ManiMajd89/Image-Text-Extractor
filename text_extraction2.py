"""
Basically, this project involves 3 main steps:
- detecting the region of text in an image
- extracting the text from the region
- saving and displaying the extracted text
"""

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# Load the image and read it 
image = cv2.imread("/Users/mani/Documents/Python Greenoly/open cv/image1.png")

# cv2.imshow("Original Image", image)
# cv2.waitKey(0)  # Wait for a key press
# cv2.destroyAllWindows()  # Close the window

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Grayscale Image", gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Apply adaptive thresholding
threshold_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# expand text regions
rectangle = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
dilation = cv2.dilate(threshold_image, rectangle, iterations=1)

# Find contours
contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Create and clear the text file
file = open("detected text.txt", "w+")
file.write("")
file.close()

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)

    # Filter small contours (small regions probably do not contain meaningful text)
    if w < 20 or h < 10:
        continue

    # Crop the text region
    cropped = image[y:y+h, x:x+w]

    # Resize for better OCR
    cropped = cv2.resize(cropped, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    file = open("detected text.txt", "a")

    # Apply OCR to the cropped region
    text = pytesseract.image_to_string(cropped, config="--oem 3 --psm 6").strip()

    # Write valid text to file
    if text:
        file.write(text + "\n")

    # Close the file
    file.close()

# print the extracted to the screeen as well
with open("detected text.txt", "r") as file:
    print("Text Detected: ")
    print(file.read())