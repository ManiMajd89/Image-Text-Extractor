# Image Text Extractor

## Project Overview
This project uses OpenCV and Tesseract OCR to detect and extract text from images. The program preprocesses images, identifies text regions, and converts them into readable text, which is saved to a file and optionally displayed. This project is ideal for automating text recognition tasks in scanned documents, photographs, or other image files.

---

## Features

- **Preprocessing**:
  - Converts images to grayscale.
  - Uses adaptive thresholding for binarization.
  - Applies dilation to enhance text regions.
- **Text Detection**:
  - Finds contours to identify potential text areas.
  - Filters small or irrelevant regions.
- **Text Extraction**:
  - Crops and processes text regions.
  - Uses Tesseract OCR to extract readable text.
- **Output**:
  - Saves detected text to a file (`detected text.txt`).
  - Displays detected text in the terminal.
  - Optionally visualizes text regions on the image.

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

The project consists of the following main steps:

1. **Image Preprocessing**:
   - Converts the image to grayscale.
   - Applies adaptive thresholding and dilation to highlight text regions.

2. **Text Region Detection**:
   - Detects contours to identify potential text blocks.
   - Filters out small, irrelevant contours.

3. **Text Extraction**:
   - Crops each text region and resizes it for better OCR accuracy.
   - Uses Tesseract to extract text from the cropped regions.

4. **Output**:
   - Writes the detected text to a file and optionally displays it in a window.

---

## Future Enhancements
1. **Improved OCR**:
   - Adjust Tesseract configurations for better results with specific text types.
   - Resize text regions before OCR for improved accuracy.
2. **Multi-Language Support**:
   - Add support for non-English languages by specifying the language model:
     ```python
     text = pytesseract.image_to_string(cropped, lang="spa")
     ```
3. **Error Handling**:
   - Handle invalid images or missing dependencies gracefully.

