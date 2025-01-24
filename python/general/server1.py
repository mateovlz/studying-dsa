import threading
import time
import pyautogui
import random

class MouseMover(threading.Thread):
    def __init__(self, interval_cycle, interval, x_range, y_range):
        threading.Thread.__init__(self)
        self.interval_cycle = interval_cycle
        self.interval = interval
        self.x_range = x_range
        self.y_range = y_range
        self.running = True

    def run(self):
        while self.running:
            try:
                pyautogui.moveTo(
                    x=pyautogui.position().x + random.randint(-self.x_range, self.x_range),
                    y=pyautogui.position().y + random.randint(-self.y_range, self.y_range),
                    duration=self.interval
                )
                #pyautogui.typewrite("Hi Working on it", )
                #pyautogui.scroll(2)
                #pyautogui.typewrite("DOD DOAs FHD We BVd LGD", interval=self.interval)
                pyautogui.typewrite(["ctrleft"], interval=self.interval)
                pyautogui.hotkey(["command", "c"], interval=self.interval)
                pyautogui.hotkey(["command", "cc"], interval=self.interval)
                pyautogui.hotkey(["command", "c"], interval=self.interval)
                pyautogui.hotkey(["command", "c"], interval=self.interval)
                #pyautogui.hotkey(["command", "v"], interval=self.interval)
                pyautogui.typewrite(["ctrleft"], interval=self.interval)
                #pyautogui.doubleClick()x
                #pyautogui.scroll(-1)
                pyautogui.moveTo(
                    x=pyautogui.position().x + random.randint(-self.x_range, self.x_range),
                    y=pyautogui.position().y + random.randint(-self.y_range, self.y_range),
                    duration=self.interval
                )
                pyautogui.moveTo(
                    x=pyautogui.position().x + random.randint(-self.x_range, self.x_range),
                    y=pyautogui.position().y + random.randint(-self.y_range, self.y_range),
                    duration=self.interval
                )
                pyautogui.moveTo(
                    x=pyautogui.position().x + random.randint(-self.x_range, self.x_range),
                    y=pyautogui.position().y + random.randint(-self.y_range, self.y_range),
                    duration=self.interval
                )
            except Exception as e:
                print(f"Error executing: {e}")
            time.sleep(self.interval_cycle)

    def stop(self):
        self.running = False

# Example usage:
if __name__ == "__main__":
    mover = MouseMover(interval_cycle=20 ,interval=0.5, x_range=100, y_range=200)
    mover.start()

    try:
        while True:
            time.sleep(1)  # Keep the main thread running
    except KeyboardInterrupt:
        print("Stopping ...")
        mover.stop()
        mover.join()
        print("Server stopped.")