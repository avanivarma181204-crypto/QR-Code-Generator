import cv2

img = cv2.imread("generated_qr.png")

detector = cv2.QRCodeDetector()

data, bbox, straight_qrcode = detector.detectAndDecode(img)

print("QR Code Data:", data)
 
cv2.imshow("QR Code", img)

cv2.waitKey(0)
cv2.destroyAllWindows()