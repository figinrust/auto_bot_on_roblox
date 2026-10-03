# Window handling and coordinate normalization
import win32gui

class WindowManager:
    def __init__(self, window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)
        if self.hwnd == 0:
            raise Exception('Игра не запущена')

    def is_active(self):
        return not win32gui.IsIconic(self.hwnd)

    def get_client_rect(self):
        _, _, width, height = win32gui.GetClientRect(self.hwnd)

        left, top = win32gui.ClientToScreen(self.hwnd, (0, 0))

        return {
            "left": left,
            "top": top,
            "width": width,
            "height": height
        }

    def focus(self):
        win32gui.SetForegroundWindow(self.hwnd)
