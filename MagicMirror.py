import sys
import time

from DetectMotion import DetectMotion

class Main:
    def __init__(self):
        self.detectGesture = DetectMotion()

    def main(self):
        # Look for gesture
        for i in range(0, 100):
            gesture = self.detectGesture.detectMotion()
            if gesture is not None:
                print gesture
     #        time.sleep(.05)

if __name__ == "__main__":
    main = Main()
    main.main()

