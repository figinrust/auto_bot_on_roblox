import time
import cv2
from core.window import WindowManager
from core.capture import ScreenCapture
from config import WINDOW_NAME
from config import DEBUG
from config import STOP_KEY
import win32api
import win32con

window = WindowManager(WINDOW_NAME)
window.focus()
capture = ScreenCapture()

while True:
    start_time = time.time()
    rect = window.get_client_rect()
    frame = capture.get_frame(rect)
    fps = 1 / (time.time() - start_time)
    cv2.putText(frame, f"FPS: {int(fps)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # Единая проверка для выхода (работает и при DEBUG=True, и при DEBUG=False)
    if win32api.GetAsyncKeyState(STOP_KEY) & 0x8000:
        print("Бот остановлен пользователем (F12).")
        break

    if DEBUG:
        cv2.imshow("Blox Fruits Vision", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # Если окно скрыто, даем процессору отдохнуть
        time.sleep(0.01)

cv2.destroyAllWindows()
