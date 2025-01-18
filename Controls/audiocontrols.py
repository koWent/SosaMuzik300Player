from Controls.controls import (
    ft,
    IconButton,
    Text
)

class AudioControl(ft.Container):
    def __init__(
            self,
            page:ft.Page
    ):
        super().__init__()
        self.width=page.width
        self.height=page.height * 0.25
        self.bgcolor = ft.Colors.with_opacity(0.5,'purple')
        self.top=page.height - (self.height + 30)
        self.border_radius = ft.border_radius.only(
            top_left=8,
            top_right=8
        )
        self.padding=ft.padding.all(8)
        self.content=ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        Text(
                            value="Трек",
                            size=14
                        ),
                        Text(
                            value="Артист",
                            size=12,
                            color=ft.Colors.with_opacity(0.8,'white')
                        ),
                        Text(
                            value="Альбом",
                            size=12,
                            color=ft.Colors.with_opacity(0.8, 'white')
                        )
                    ],
                    spacing=0
                ),
                ft.Column(
                    controls=[
                        ft.Stack(
                            controls=[
                                ProgressBar(
                                    width=page.width
                                ),
                                ProgressBar(
                                    width=page.width * 0.3,
                                    bgcolor=ft.Colors.RED
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[
                                Text(
                                    value="00:00",
                                    size=12,
                                ),
                                Text(
                                    value="06:07",
                                    size=12,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        IconButton(
                            icon=ft.Icons.MENU,
                            color=ft.Colors.WHITE
                        ),
                        ft.Row(
                            controls=[
                                IconButton(
                                    icon=ft.Icons.SKIP_PREVIOUS,
                                    color=ft.Colors.WHITE
                                ),
                                IconButton(
                                    icon=ft.Icons.PLAY_ARROW,
                                    color=ft.Colors.WHITE
                                ),
                                IconButton(
                                    icon=ft.Icons.SKIP_NEXT,
                                    color=ft.Colors.WHITE
                                )
                            ]
                        ),
                        IconButton(
                            icon=ft.Icons.FAVORITE_BORDER,
                            color=ft.Colors.WHITE
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )

            ],
            spacing=15
        )

class ProgressBar(ft.Container):
    def __init__(
            self,
            width:int,
            height:int=2,
            bgcolor:ft.Colors=ft.Colors.with_opacity(0.25,'black')
    ):
        super().__init__()
        self.width = width
        self.bgcolor = bgcolor,
        self.height  = height