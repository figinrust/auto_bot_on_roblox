# High-speed screen capture module
import mss
import numpy as np
import cv2

class ScreenCapture:
    def __init__(self):
        self.sct = mss.mss()

    def get_frame(self, monitor_rect):
        raw_img = self.sct.grab(monitor_rect)
        frame = np.array(raw_img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        return frame
