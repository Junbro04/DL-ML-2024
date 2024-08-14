from tensorflow.keras.models import load_model
import numpy as np
import cv2
model = load_model('WEEK1_CNN/s6xybr8in/mnist_cnn_model.keras')
image = cv2.imread('WEEK1_CNN/s6xybr8in/image2.jpg')

height = 720
width = 1024
image= image[20:-1,:2000]
image = cv2.resize(image, (width, height))


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threadhold = 127
_, thresholded_image = cv2.threshold(gray_image, threadhold, 255, cv2.THRESH_BINARY)
bitwise_not = cv2.bitwise_not(thresholded_image)

contours, _ = cv2.findContours(bitwise_not, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
L = []
for idx,contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    if w < 10 or h < 10:
        continue
    cv2.rectangle(image, (x, y), (x + max(w,h), y + max(w,h)), (0, 255, 0), 2)
    name = 'caped_image' + str(idx) + '.jpg'
    cap_image = bitwise_not[y:y+max(w,h), x:x+max(w,h)]
    cap_image = cv2.resize(cap_image, (28, 28))
    cv2.imwrite(name,cap_image)
    roi = cap_image.astype('float32') / 255
    roi = roi.reshape(1, 28, 28, 1)
    prediction = np.argmax(model.predict(roi), axis=-1)[0]
    cv2.putText(image, str(prediction), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow('image', image)
cv2.imshow('bitwise_not', bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()