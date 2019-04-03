import cv2
import numpy as np

def playVideo():
    vid = cv2.VideoCapture(0)

    while True:
        gordu = False  # belirttiğimiz nesneyi gördüğümüzü anlamamız için değişken kamera görüntüyü görmediği sürece False olarak kalacak
        
        _, img = vid.read()
        
        # renk uzayı değişimi
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # mavi renk sınırları belirleniyor
        mavi_alt = np.array([99, 115, 150], np.uint8)
        mavi_ust = np.array([110, 255, 255], np.uint8)

        mavi = cv2.inRange(hsv, mavi_alt, mavi_ust)

        (kontur, hiyerarsi) = cv2.findContours(mavi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for res, kont in enumerate(kontur):
            area = cv2.contourArea(kont)
            if area > 300:
                # konturlenmiş alanın ortasını buluyoruz.
                M = cv2.moments(kont)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
                cv2.putText(img, "cntr", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                ##################################################################################
                gordu = True  # belirttiğimiz renkteki nesneyi gördüyse değişkenimiz True değeri alıyor.
                # x, y, w, h = cv2.boundingRect(kont)
                # print("x:" + str(x) + "y:" + str(y) + "w:" + str(w) + "h:" + str(h))
                # img = cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
                # cv2.putText(img, "mavi", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

        cv2.imshow("goruntu", img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            vid.release()
            cv2.destroyAllWindows()
            break