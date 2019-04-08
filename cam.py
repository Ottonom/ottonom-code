def cam():
    #sudo modprobe bcm2835-v4l2
    cap = cv2.VideoCapture(0)

    while (True):
        ret, frame = cap.read()
        frame = cv2.flip(frame, -1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()