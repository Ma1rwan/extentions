import time
from PIL import ImageGrab
from pynput.mouse import Controller
import os

# Initialize mouse controller
mouse = Controller()

def get_pixel_color(image, x, y):
    """Get the RGB color of the pixel at position (x, y)."""
    return image.getpixel((x, y))

def main():
    while True:
        # Take a screenshot
        screenshot = ImageGrab.grab()

        # Get mouse position
        mouse_x, mouse_y = mouse.position

        # Get the color at the mouse position
        color = get_pixel_color(screenshot, mouse_x, mouse_y)

        # Print the color in RGB format
        print(f"Mouse position: ({mouse_x}, {mouse_y}), Color: RGB{color}")

        # Remove the screenshot object to free memory
        del screenshot

        # Wait for a second before the next iteration
        time.sleep(1)

if __name__ == "__main__":
    main()
