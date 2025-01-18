import flet as ft
from Controls.appbar import (
    Appbar
)
from Controls.audiocover import AudioCover
from Controls.audiocontrols import AudioControl

class Home(ft.View):
    def __init__(
            self,
            page:ft.Page
    ):
        self.image_src='https://i.pinimg.com/736x/89/cb/34/89cb341a675d2812b34d1f802d40a904.jpg'
        super().__init__()
        self.route = '/'
        self.padding=ft.padding.all(0)
        self.appbar = Appbar(page=page)
        self.controls = [
            ft.Stack(
                controls=[
                    AudioCover(page=page,image_src=self.image_src),
                    AudioControl(page=page)
                ]
            )
        ]
