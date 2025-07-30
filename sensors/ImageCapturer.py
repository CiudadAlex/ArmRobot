import cv2 as cv


class ImageCapturer:

    @staticmethod
    def capture_image():

        capture = cv.VideoCapture(0)
        while capture.isOpened():
            try:
                ret, img = capture.read()
                img = cv.resize(img, (640, 480))

                cv.imwrite('capture.jpg', img)

                return cv.imencode('.jpg', img)[1].tobytes()

            except KeyboardInterrupt:
                capture.release()
