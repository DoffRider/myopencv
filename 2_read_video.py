import cv2 as cv

tangkap = cv.VideoCapture('vid/cangkul.mp4')

while True:
    isTrue, frame = tangkap.read()

    cv.imshow('Cangkul Dibilang', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

tangkap.release()
cv.destroyAllWindows()


