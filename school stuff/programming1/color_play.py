#

import flet as ft

def main(page: ft.Page):  

    def button_clicked(e):
        page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))
        page.update() 
    
    
    container = ft.Container(
        width=200,
        height=200,
        border=ft.border.all(1.0, ft.colors.BLACK),
        content=ft.FilledButton("INPUT"),
        theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.YELLOW_ACCENT_200)))
    
    page.add(container)

    container = ft.Container(
        width=200,
        height=200,
        border=ft.border.all(1.0, ft.colors.BLACK),
        content=ft.FilledButton("OUTPUT"),
        theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.LIGHT_BLUE_ACCENT_200)))
    
    page.add(container)

    # container = ft.Container(
    #     width=200,
    #     height=200,
    #     border=ft.border.all(1.0, ft.colors.BLACK),
    #     content=ft.FilledButton("BACKGROUND"),
    #     theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.LIGHT_GREEN_ACCENT_)))
    
    # page.add(container)

    # LIGHT_GREEN_ACCENT_100 als Hintergrund
    # ft.ThemeMode.LIGHTft.ThemeMode.DARK

    

ft.app(target=main)   