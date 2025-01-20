import flet as ft

def main(page: ft.Page):
    page.title = "Atividade 2"
    
    layout = ft.Column(
        controls=[
            ft.Text("Janela Principal", size=50, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("Botão 1", bgcolor="blue", color="white", ),
            ft.ElevatedButton("Botão 1", bgcolor="yellow", color="black"),
            ft.ElevatedButton("Botão 1", bgcolor="black", color="gray"),
        ]
    )

    page.add(layout)

ft.app(target=main)