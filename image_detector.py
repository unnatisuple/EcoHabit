from PIL import Image
import numpy as np

def detect_image(uploaded_file):

    img = Image.open(uploaded_file)

    img_array = np.array(img)

    # simple color check (green detection)
    green_pixels = np.sum(img_array[:,:,1] > 150)

    if green_pixels > 1000:
        return ["plant"]

    return ["object"]