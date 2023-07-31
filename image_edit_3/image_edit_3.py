"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from typing import List
from PIL import Image
import cv2
import reflex as rx
import numpy as np

options: List[str] = [
    "LAB",
    "HSV",
    "Greyscale",
    "LUV",
    "YUV",
    "BayerGBRG",
    "NV21"
]

class State(rx.State):
    """The app state."""
    option: str = "No selection yet."
    img : str = "/trees.png"
    newimg: str = "/trees.png"
    def updateImage(self):
        path = "image_edit_3/trees.png"
        with Image.open(path) as im:
            openCVIm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
            impath = f"/{self.option}Image.png"
            cv2.imwrite(impath, openCVIm)
        self.newimg = impath
        return;

    @rx.var
    def img_to_show(self) -> str:
        return self.newimg

def index():
    """The main view."""
    return rx.hstack(
        rx.vstack(        
            rx.image(src=State.img, width="200px", height="auto"),
            rx.text("Your Image",
                    height = "30px",
                    width = "auto"
                    ),
            padding="10em",
        ),
        rx.vstack(
        rx.hstack(
            rx.select(
                options,
                placeholder="Change the color space.",
                value=State.option,
                on_change=State.set_option,
                width = "auto", 
                height = "30px",
                color="white"
            ),
            rx.button("Show!", on_click=State.updateImage),
        ),
        rx.text(State.img_to_show),
        rx.image(src=State.img_to_show, width="200px", height="auto"),
        padding="10em",
        ),
    )

# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.compile()
