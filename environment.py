import numpy as np
import cv2

class Environment:

    def __init__(self, map, magnification=500):
        # Set magnification factor of the display
        self.magnification = magnification
        # Set width and height of the environment
        self.width = 1.0
        self.height = 1.0
        # Create image of the environment for display
        self.image = np.zeros([int(self.magnification * self.height), int(self.magnification * self.width), 3], dtype=np.uint8)
        # Set map
        self.map = map

    def color_cell(self, cell, color, fill=False):
        width, height = self.map.shape
        x, y = cell
        if fill:
            p1 = (int(x * self.width / width * self.magnification), int(y * self.height / height * self.magnification))
            p2 = (int((x + 1) * self.width / width * self.magnification), int((y + 1) * self.height / height * self.magnification))
            cv2.rectangle(self.image, p1, p2, color, cv2.FILLED)
        else:
            p = (int((x + 0.5) * self.width / width * self.magnification), int((y + 0.5) * self.height / height * self.magnification))
            r = int((0.5) * self.width / width * self.magnification)
            cv2.circle(self.image, p, r, color, cv2.FILLED)

    def show(self, queue, visited, path=None):
        # Create white background
        self.image.fill(255)
        # Draw grid
        width, height = self.map.shape
        # Draw starting position
        self.color_cell((0, 0), (0, 0, 255))
        # Draw ending position
        self.color_cell((width - 1, height - 1), (0, 255, 0))
        # Draw walls
        for y in range(height):
            for x in range(width):
                if self.map[y][x] == 0:
                    self.color_cell((x, y), (100, 100, 100), fill=True)
        # Draw path if given
        if path:
            for cell in path:
                self.color_cell(cell.position, (153, 204, 0))
        else:
            # Draw visited cells
            for cell in visited:
                self.color_cell(cell.position, (85, 17, 221))
            # Draw to be visit cells
            for cell in queue:
                self.color_cell(cell.position, (136, 238, 255))
        # Show image
        cv2.imshow("Environment", self.image)
        # Give time for image to be rendered on screen
        cv2.waitKey(1)
