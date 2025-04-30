import numpy as np

# Define basic color names with their BGR values
COLOR_LIST = [
    ("Black",   (0, 0, 0)),
    ("White",   (255, 255, 255)),
    ("Red",     (0, 0, 255)),
    ("Lime",    (0, 255, 0)),
    ("Blue",    (255, 0, 0)),
    ("Yellow",  (0, 255, 255)),
    ("Cyan",    (255, 255, 0)),
    ("Magenta", (255, 0, 255)),
    ("Gray",    (128, 128, 128)),
    ("Silver",  (192, 192, 192)),
    ("Maroon",  (0, 0, 128)),
    ("Olive",   (0, 128, 128)),
    ("Green",   (0, 128, 0)),
    ("Purple",  (128, 0, 128)),
    ("Teal",    (128, 128, 0)),
    ("Navy",    (128, 0, 0)),
]

# Convert to NumPy for fast distance calculation
color_names = [name for name, _ in COLOR_LIST]  # color name matra leko for name in name, _ denotes that you take only name and ignore the bgr valur after the comma
color_values = np.array([bgr for _, bgr in COLOR_LIST])  # yesma simply bgr value matra leko and completely ignoring the color name


'''
    yo function le simply webcam ko feed ma mouse le jun object lai click garxa tesko value liyera ,
    mathi defined color_values sanga check garxa ani jun sanga close aauxa tai display garxa 
'''
def get_color_name(b, g, r):
    input_color = np.array([b, g, r])  #converts the BGR values of the pixel you clicked 
    distances = np.sum((color_values - input_color) ** 2, axis=1)  ## yesle simply euclidean distance calculate garxa color_values ra input_color bich 
    closest_index = np.argmin(distances)  # distances ma min value kun xa tyo index linxa 
    return color_names[closest_index]   # ani tyo index ko color name return garxa 


def display_color_info(frame, x, y):
    b, g, r = frame[y, x]  # Extracts BGR values from the pixel at coordinates (x, y)
    color_name = get_color_name(b, g, r)  # Calls the get_color_name function to get the closest color name
    print(f"BGR at ({x}, {y}): ({b}, {g}, {r}) - Closest color name: {color_name}")  # Displays the BGR values and color name
    return b, g, r, color_name  # Returns the BGR values and the closest color name

