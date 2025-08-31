from PIL import Image
import numpy as np


class ImagePositionDiscoverer:

    @staticmethod
    def get_central_position_of_filtered_pixels(image_path, filter_of_pixels):

        image = Image.open(image_path).convert('RGB')
        image_np = np.array(image)

        height, width, _ = image_np.shape

        filtered_pixels_coords = []

        # Iterate through all pixels
        for y in range(height):
            for x in range(width):
                pixel = tuple(image_np[y, x])  # (R, G, B)
                if filter_of_pixels(pixel):
                    filtered_pixels_coords.append((y, x))  # or (row, col)

        if len(filtered_pixels_coords) < 100:
            return None, height, width  # very few pixels passed the filter

        # Convert list to numpy array and calculate mean
        filtered_pixels_coords_np = np.array(filtered_pixels_coords)
        average_position = filtered_pixels_coords_np.mean(axis=0)

        return tuple(average_position), height, width

    @staticmethod
    def get_vectorial_position_of_filtered_pixels(image_path, filter_of_pixels):

        central_position, height, width = ImagePositionDiscoverer.get_central_position_of_filtered_pixels(image_path, filter_of_pixels)

        if central_position is None:
            return None

        x = (central_position[1] - width/2) / width
        y = (height - central_position[0] - height/2) / height
        return x, y
