"""ProgBoard - Projektmanagement für Solo Entwickler"""

import flet as ft


# Öffnet ein Flet Fenster
def main(page: ft.Page):
    page.title = "ProgBoard"
    page.vertical_alignment = ft.MainAxisAlignment.START
    # page.horizontal_alignment = ft.CrossAxisAlignment.END

    container_backlog = ft.Container(
        content=ft.Column(
            # width=200,
            # height=100,
            spacing=10,
            controls=[
                ft.Text(
                    "Backlog",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                    bgcolor="WHITE",
                ),
                ft.Text(
                    "Ticket 1",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
                ft.Text(
                    "Ticket 2",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
                ft.Text(
                    "Ticket 3",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
            ],
        ),
        padding=10,
        bgcolor="blue",
    )

    container_in_arbeit = ft.Container(
        content=ft.Column(
            # width=200,
            # height=100,
            spacing=10,
            controls=[
                ft.Text(
                    "In Arbeit",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                    bgcolor="white",
                ),
                ft.Text(
                    "Ticket 1",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
                ft.Text(
                    "Ticket 2",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
                ft.Text(
                    "Ticket 3",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
            ],
        ),
        padding=10,
        bgcolor="green",
    )
    container_in_pruefung = ft.Container(
        content=ft.Column(
            # width=200,
            # height=100,
            spacing=10,
            controls=[
                ft.Text(
                    "In Prüfung",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                    bgcolor="white",
                ),
                ft.Text(
                    "Ticket 1",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
                ft.Text(
                    "Ticket 2",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
                ft.Text(
                    "Ticket 3",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
            ],
        ),
        padding=10,
        bgcolor="blue",
    )
    container_abgeschlossen = ft.Container(
        content=ft.Column(
            # width=200,
            # height=100,
            spacing=10,
            controls=[
                ft.Text(
                    "Abgeschlossen",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                    bgcolor="white",
                ),
                ft.Text(
                    "Ticket 1",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
                ft.Text(
                    "Ticket 2",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
                ft.Text(
                    "Ticket 3",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
            ],
        ),
        padding=10,
        bgcolor="green",
    )
    container_verworfen = ft.Container(
        content=ft.Column(
            # width=200,
            # height=100,
            spacing=10,
            controls=[
                ft.Text(
                    "Verworfen",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                    bgcolor="white",
                ),
                ft.Text(
                    "Ticket 1",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
                ft.Text(
                    "Ticket 2",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
                ft.Text(
                    "Ticket 3",
                    size=20,
                    weight=ft.FontWeight.W_600,
                    color="purple",
                ),
            ],
        ),
        padding=10,
        bgcolor="blue",
    )
    # Reihe für Spalten
    reihe_Themenbereiche = ft.Row(
        controls=[
            container_backlog,
            container_in_arbeit,
            container_in_pruefung,
            container_abgeschlossen,
            container_verworfen,
        ]
    )

    page.add(reihe_Themenbereiche)
    page.update()


# Startet die App
ft.run(main)
