"""ProgBoard - Projektmanagement für Solo Entwickler"""

import flet as ft


# Öffnet ein Flet Fenster
def main(page: ft.Page):
    page.title = "ProgBoard"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


# Startet die App
ft.run(main)
