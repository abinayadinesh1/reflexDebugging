"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from typing import List
from PIL import Image

import reflex as rx

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
        with Image.open("image_edit_3/trees.png") as im:
            # im.show()
            im.save(f"assets/{self.option}Image.png")
        self.newimg = "background.png"
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
            rx.image(src=State.img_to_show, width="200px", height="auto"),
            padding="10em",
        ),
    )

# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.compile()
