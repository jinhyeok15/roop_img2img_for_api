import base64
import numpy as np

def get_buffer_image(base64img: str):
    if base64img.startswith("data:image/"):
        base64img = base64img.split(";")[1].split(",")[1]
    image_data = base64.b64decode(base64img)
    nparr = np.frombuffer(image_data, np.uint8)

    return nparr


def get_base64_from_buffer(buffer):
    base64.b64encode(buffer).decode()
