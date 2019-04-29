import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _, img = cap.read()

    # raspberry çözünürlüğü 3280 × 2464 pixels
    # 720px ile sınırlandırırsak 720 x 540,87 pixels
    img = cv2.resize(img, (720, 540))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #pencere orta noktaları 360 x 270 px
    #window center noktları

    wcx = 360
    wcy = 270

    cv2.circle(img, (wcx, wcy), 5, (255, 255, 255), -1)

    yellow_lower = np.array([41, 39, 64], np.uint8)
    yellow_upper = np.array([80, 255, 255], np.uint8)

    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

    kernel = np.ones((5, 5), "uint8")

    yellow = cv2.dilate(yellow, kernel)
    res = cv2.bitwise_and(img, img, mask=yellow)

    contours, hierarchy = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        cnt = contours[0]
        M = cv2.moments(cnt)

        # tespit edilen rengin x ve ye coord.
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])
        print(x, y)
        cv2.circle(img, (x, y), 5, (255, 255, 255), -1)

        area = cv2.contourArea(contour)
        if (area > 400):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "YESIL", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

    cv2.imshow("Color Tracking", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
