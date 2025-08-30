from PIL import Image
import numpy as np


class ColorAverager:

    @staticmethod
    def get_average_central_color(path_image, proportion=0.05):

        image = Image.open(path_image).convert('RGB')
        width, height = image.size

        window_width = int(width * proportion)
        window_height = int(height * proportion)

        x0 = (width - window_width) // 2
        y0 = (height - window_height) // 2
        x1 = x0 + window_width
        y1 = y0 + window_height

        window = image.crop((x0, y0, x1, y1))

        pixels = np.array(window)

        # Calculate average of every channel
        avg = pixels.mean(axis=(0, 1))  # Average in height and width

        # Transform to integers
        return tuple(int(x) for x in avg)

