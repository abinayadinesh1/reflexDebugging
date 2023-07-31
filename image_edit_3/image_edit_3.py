"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
class State(rx.State):
    """The app state."""

    # The images to show.
    img: list[str]

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)


color = "rgb(107,99,246)"

def index():
    """The main view."""
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    color=color,
                    bg="white",
                    border=f"1px solid {color}",
                ),
                rx.text(
                    "Drag and drop files here or click to select files"
                ),
            ),
            border=f"1px dotted {color}",
            padding="5em",
        ),
        rx.button(
            "Upload",
            on_click=lambda: State.handle_upload(
                rx.upload_files()
            ),
        ),
        rx.foreach(
            State.img, lambda img: rx.image(src=img)
        ),
        padding="5em",
    )

# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.compile()
