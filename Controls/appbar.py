from Controls.controls import (
    Icon,
    IconButton,
    Text,
    ft
)

from Controls.musicselector import MusicSelector

class Appbar(ft.AppBar):
    def __init__(
            self,
            page: ft.Page
    ):
        fp = MusicSelector()
        page.overlay.append(fp)
        super().__init__()
        self.bgcolor = ft.Colors.with_opacity(0.4,'black')
        self.leading = ft.Row(
            controls=[
                Icon(
                    icon=ft.Icons.MUSIC_NOTE
                ),
                Text(
                    value=page.title,
                    size=18,
                    color=ft.Colors.with_opacity(0.8,'green')
                )
            ]
        )
        self.actions = [
            IconButton(
                icon=ft.Icons.FOLDER,
                on_click=lambda e:fp.pick_files(
                    dialog_title=page.title,
                    file_type=ft.FilePickerFileType.AUDIO,
                    allow_multiple=True,
                )
            )
        ]
        self.toolbar_height = 40