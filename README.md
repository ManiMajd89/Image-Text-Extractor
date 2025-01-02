# Image Text Extractor

## Project Overview
This project uses OpenCV and Tesseract OCR to detect and extract text from images. The program preprocesses images, identifies text regions, and converts them into readable text, which is saved to a file and optionally displayed. This project is ideal for automating text recognition tasks in scanned documents, photographs, or other image files.

---

## Features

- **Preprocessing**:
  - Converts images to grayscale for simpler processing.
  - Uses adaptive thresholding to binarize the image and make text regions prominent.
  - Applies dilation to expand text regions for better detection.
- **Text Detection**:
  - Finds contours to identify potential text regions.
  - Filters out small contours to remove irrelevant areas.
- **Text Extraction**:
  - Crops and resizes text regions for improved OCR accuracy.
  - Extracts text using Tesseract OCR.
- **Output**:
  - Saves the extracted text to `detected text.txt`.
  - Prints the extracted text directly to the terminal.

---

## Getting Started

### Prerequisites

1. **Python** (3.x recommended)
2. **Required Libraries**:
   - Install using pip:
     ```bash
     pip install opencv-python pytesseract
     ```
3. **Tesseract OCR**:
   - **macOS**:
     ```bash
     brew install tesseract
     ```
   - **Linux**:
     ```bash
     sudo apt update
     sudo apt install tesseract-ocr
     ```
   - **Windows**:
     - Download and install from [Tesseract OCR GitHub](https://github.com/UB-Mannheim/tesseract/wiki).

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-extraction-opencv.git
   cd text-extraction-opencv
   ```
2. Ensure Tesseract is installed and accessible. Update the path to Tesseract in the script if necessary:
   ```python
   pytesseract.pytesseract.tesseract_cmd = '/path/to/tesseract'
   ```

---

### Usage

1. Add your input image (e.g., `sample.jpg`) to the project directory.
2. Run the script:
   ```bash
   python text_extraction.py
   ```
3. Output:
   - The extracted text will be saved in `detected text.txt`.
   - Detected text will also be displayed in the terminal.

---

### Example

#### Input Image:
![Input Image](https://github.com/ManiMajd89/Image-Text-Extractor/blob/main/image2.png)


#### Output:
![Output Sample](https://github.com/ManiMajd89/Image-Text-Extractor/blob/main/output%20sample.png)

---

## Code Explanation

The program works as follows:

1. **Load and Preprocess the Image**:
   - Converts the input image to grayscale.
   - Applies adaptive thresholding to binarize the image.
   - Uses dilation to merge close text components.

2. **Detect Text Regions**:
   - Finds contours in the processed image.
   - Filters small contours to avoid noise.
   - Crops and resizes potential text regions.

3. **Extract and Output Text**:
   - Passes the cropped regions to Tesseract for text recognition.
   - Writes the detected text to a file and displays it in the terminal.

---

## Future Possible Enhancements

1. **Improved OCR Accuracy**:
   - Implement advanced preprocessing techniques like noise reduction, skew correction, and edge enhancement for cleaner text regions.
   - Experiment with different OCR configurations for handling complex layouts.

2. **Multi-Language Support**:
   - Extend Tesseract's language models to support text extraction in languages other than English.

3. **Support for Curved Text**:
   - Enhance the program to detect and process curved or rotated text using tools like Hough Transform or deskewing algorithms.

4. **Error Handling and Validation**:
   - Add error handling for missing dependencies, invalid input files, and unreadable text regions.
