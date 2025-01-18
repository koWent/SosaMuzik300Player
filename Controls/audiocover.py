import flet as ft

class AudioCover(ft.Container):
    def __init__(
            self,
            page:ft.Page,
            image_src:str,
    ):
        super().__init__()
        self.bgcolor = ft.Colors.BLUE_50
        self.width = page.width
        self.height = page.height
        self.content = ft.Stack(
            controls=[
                ft.Container(
                    image=ft.DecorationImage(
                        src=image_src,
                        fit=ft.ImageFit.COVER
                    ),
                    width=page.width * 0.20,
                    height=page.height * 0.40,
                    border_radius=page.width * 0.40,
                    left=(page.width * 0.8 / 2),
                    top=(page.width * 0.10)
                )
            ]
        )

class ProgressBar(ft.Container):
    def __init__(
            self,
            width:int,
            height:int=2,
            bgcolor:ft.Colors=ft.Colors.with_opacity(0.25,'black'),


    ):
        super().__init__()
        self.width = width
        self.bgcolor = bgcolor,
        self.height  = height