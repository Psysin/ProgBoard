"""ProgBoard - Projektmanagement für Solo Entwickler"""

import flet as ft


# Öffnet ein Flet Fenster
def main(page: ft.Page):
    page.title = "ProgBoard"
    page.vertical_alignment = ft.MainAxisAlignment.START
    # page.horizontal_alignment = ft.CrossAxisAlignment.END

    # Liste aktueller Tickets Anzahl
    backlog_karten: list[str] = ["Ticket 1", "Ticket 2", "Ticket 3", "Ticket 4"]
    # Liste wird gefüllt mit ft.Text Elementen anhand Anzahl backlog_karten
    backlog_leere_karten: list[ft.Text] = []
    # Liste mit einer Position, enthällt nur die Überschrift, wird später mit neuen Elementen (Tickets) zusammengesetzt
    backlog_titel: list[ft.Control] = [
        ft.Text(
            "Backlog",
            size=20,
            weight=ft.FontWeight.W_600,
            color="purple",
            bgcolor="white",
        )
    ]
    # Durchläuft backlog_karten, und erstellt anhand der Anzahl neue ft.Text Elemente für backlog_leere_Karten
    for ticket in backlog_karten:
        backlog_leere_karten.append(
            ft.Text(ticket, size=20, color="purple", weight=ft.FontWeight.W_600)
        )

    container_backlog = ft.Container(
        content=ft.Column(
            # width=200,
            # height=100,
            spacing=10,
            # Erzeugt dauerhaften Spaltenname + Tickets
            controls=backlog_titel + backlog_leere_karten,
        ),
        padding=10,
        bgcolor="blue",
    )

    # Liste aktueller Tickets Anzahl
    in_arbeit_karten: list[str] = [
        "Ticket 1",
        "Ticket 2",
        "Ticket 3",
        "Ticket 4",
        "Ticket 5",
    ]

    in_arbeit_leere_karten: list[ft.Text] = []

    in_arbeit_titel: list[ft.Control] = [
        ft.Text(
            "In Arbeit",
            size=20,
            weight=ft.FontWeight.W_600,
            color="purple",
            bgcolor="white",
        )
    ]

    for ticket in in_arbeit_karten:
        in_arbeit_leere_karten.append(
            ft.Text(ticket, size=20, color="purple", weight=ft.FontWeight.W_600)
        )

    container_in_arbeit = ft.Container(
        content=ft.Column(
            # width=200,
            # height=100,
            spacing=10,
            controls=in_arbeit_titel + in_arbeit_leere_karten,
        ),
        padding=10,
        bgcolor="green",
    )
    in_pruefung_karten: list[str] = [
        "Ticket 1",
        "Ticket 2",
        "Ticket 3",
        "Ticket 4",
        "Ticket 5",
        "Ticket 6",
    ]
    in_pruefung_leere_karten: list[ft.Text] = []
    in_pruefung_titel: list[ft.Control] = [
        ft.Text(
            "In Prüfung",
            size=20,
            weight=ft.FontWeight.W_600,
            color="purple",
            bgcolor="white",
        )
    ]
    for ticket in in_pruefung_karten:
        in_pruefung_leere_karten.append(
            ft.Text(ticket, size=20, color="purple", weight=ft.FontWeight.W_600)
        )
    container_in_pruefung = ft.Container(
        content=ft.Column(
            # width=200,
            # height=100,
            spacing=10,
            controls=in_pruefung_titel + in_pruefung_leere_karten,
        ),
        padding=10,
        bgcolor="blue",
    )

    abgeschlossen_karten: list[str] = [
        "Ticket 1",
        "Ticket 2",
        "Ticket 3",
        "Ticket 4",
        "Ticket 5",
    ]
    abgeschlossene_leere_karten: list[ft.Text] = []
    abgeschlossene_titel: list[ft.Control] = [
        ft.Text(
            "Abgeschlossen",
            size=20,
            weight=ft.FontWeight.W_600,
            color="purple",
            bgcolor="white",
        )
    ]
    for ticket in abgeschlossen_karten:
        abgeschlossene_leere_karten.append(
            ft.Text(ticket, size=20, color="purple", weight=ft.FontWeight.W_600)
        )
    container_abgeschlossen = ft.Container(
        content=ft.Column(
            # width=200,
            # height=100,
            spacing=10,
            controls=abgeschlossene_titel + abgeschlossene_leere_karten,
        ),
        padding=10,
        bgcolor="green",
    )
    verworfen_karten: list[str] = [
        "Ticket 1",
        "Ticket 2",
        "Ticket 3",
        "Ticket 4",
    ]
    verworfen_leere_karten: list[ft.Text] = []
    verworfen_titel: list[ft.Control] = [
        ft.Text(
            "Verworfen",
            size=20,
            weight=ft.FontWeight.W_600,
            color="purple",
            bgcolor="white",
        )
    ]
    for ticket in verworfen_karten:
        verworfen_leere_karten.append(
            ft.Text(ticket, size=20, color="purple", weight=ft.FontWeight.W_600)
        )
    container_verworfen = ft.Container(
        content=ft.Column(
            # width=200,
            # height=100,
            spacing=10,
            controls=verworfen_titel + verworfen_leere_karten,
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
