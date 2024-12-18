
# License Plate Recognition

This [project](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/LicensePlate-Recognition/main.py) implements a Python-based solution for automatic license plate recognition (ALPR) using Tesseract OCR and OpenCV. It extracts license plate information from images by detecting contours, isolating the license plate region, and performing text recognition. The script is designed to process images of vehicles efficiently, making it useful for applications like traffic monitoring, parking management, and law enforcement.

The workflow begins by preprocessing the input image to enhance features like edges and contours. The algorithm then identifies potential license plate regions by examining the geometric properties of detected contours. Once the license plate region is isolated, it undergoes further refinement through resizing, noise reduction, and thresholding. Finally, Tesseract OCR extracts the text from the processed region, which is displayed and annotated on the original image.

## Tools Used

- **Python**: Programming language for integrating various libraries and managing the workflow.
- **OpenCV**: A computer vision library used for preprocessing images, detecting contours, and drawing annotations.
- **Tesseract OCR**: A robust OCR tool for extracting text from images, integrated via the `pytesseract` Python library.
- **Matplotlib**: For visualizing and displaying images with annotations.

