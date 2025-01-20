import flet as ft

def main(page: ft.Page):
    page.title = "Atividade 1"

    page.add(
        ft.Text("Texto Vermelho", color="red", size=20),
        ft.Text("Texto Amarelo e itálico", color="yellow", italic=True, size=40),
        ft.Text("Texto Laranja e negrito", color="orange", weight="bold", size=30)
    )
ft.app(target=main)