import cv2 as cv
import threading
import time


class ImageCapturer:

    instance = None

    @staticmethod
    def get_instance():
        if ImageCapturer.instance is None:
            ImageCapturer.instance = ImageCapturer()
        return ImageCapturer.instance

    def __init__(self):
        self.thread = threading.Thread(target=self.infinite_loop_capture)
        self.thread.daemon = True

    def start_infinite_loop_capture(self):
        self.thread.start()

    def infinite_loop_capture(self):

        while True:
            self.capture_image()
            time.sleep(0.1)

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
