from utils.ImagePositionDiscoverer import ImagePositionDiscoverer
from utils.ColorDeterminer import ColorDeterminer


image_path = "C:/Alex/Dev/data_corpus/VideoCamera/cube1.jpg"
average_position = ImagePositionDiscoverer.get_central_position_of_filtered_pixels(image_path=image_path, filter_of_pixels=ColorDeterminer.is_red)

print(f"average_position = {average_position}")

