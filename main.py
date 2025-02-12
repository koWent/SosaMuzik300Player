from views.home import (
    Home,
    ft
)

def main(page:ft.Page):
    page.title="Sosa Muzik 300"
    page.theme_mode=ft.ThemeMode.DARK
    page.padding=ft.padding.all(0)

    home=Home(page=page)

    def router(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(home)

        page.update()

    page.on_route_change = router
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)