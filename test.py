from utils.ImagePositionDiscoverer import ImagePositionDiscoverer
from utils.ColorDeterminer import ColorDeterminer

replacement = "######"
image_path_template = f"C:/Alex/Dev/data_corpus/VideoCamera/cube{replacement}.jpg"

for i in range(1, 4):
    image_path = image_path_template.replace(replacement, str(i))
    average_position = ImagePositionDiscoverer.get_central_position_of_filtered_pixels(image_path=image_path, filter_of_pixels=ColorDeterminer.is_red)
    print(f"average_position{i} = {average_position}")

