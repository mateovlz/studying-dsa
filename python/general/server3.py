import threading
import time
import pyautogui
import mouse
import random 

class MouseMover(threading.Thread):
    def __init__(self, interval, x_range, y_range):
        threading.Thread.__init__(self)
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
                pyautogui.scroll(10)
            except Exception as e:
                print(f"Error moving mouse: {e}")
            time.sleep(self.interval)

    def stop(self):
        self.running = False

if __name__ == "__main__":
    mover = MouseMover(interval=0.5, x_range=50, y_range=50)
    mover.start()

    try:
        while True:
            if mouse.is_pressed(button='left'):
                print("Stopping mouse mover...")
                mover.stop()
                mover.join()
                print("Mouse mover stopped.")
                break
            time.sleep(0.1)  # Check for left click more frequently
    except KeyboardInterrupt:
        print("Stopping mouse mover...")
        mover.stop()
        mover.join()
        print("Mouse mover stopped.")