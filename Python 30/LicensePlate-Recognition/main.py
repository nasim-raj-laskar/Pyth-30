import matplotlib.pyplot as plt
import cv2
import pytesseract

def show_image(image, title):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

# Set up Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


image = cv2.imread('LicensePlate-Recognition/4.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny_edge = cv2.Canny(gray_image, 170, 200)

contours, _ = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:150]
license_plate = None

for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(contour)
        license_plate = gray_image[y:y + h, x:x + w]
        license_plate = cv2.resize(license_plate, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        license_plate = cv2.bilateralFilter(license_plate, 11, 17, 17)
        #if some images doesnt show the license plate text , change the threshold (eg 1.jpg-85,2.jpg-125,3.jpg-130,4.jpg-150)
        (thresh, license_plate) = cv2.threshold(license_plate, 100, 255, cv2.THRESH_BINARY)
        break

#OCR
if license_plate is not None:
    config = '--psm 6'
    text = pytesseract.image_to_string(license_plate, config=config).strip()
    print("Detected Text:", text)

    
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    image = cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    
    show_image(image, f"License Plate with Detected Text: {text}")
else:
    print("License plate not detected.")
