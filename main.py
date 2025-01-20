import flet as ft

def main(page: ft.Page):
    page.title = "Validação de Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_100

    def validar_login(e):
        usuario = usuario_input.value
        senha = senha_input.value

        if usuario == "Misuraca" and senha == "12345":
            mensagem.value = "Login bem-sucedido"
            mensagem.color = ft.colors.GREEN
        else:
            mensagem.value = "Usuário ou senha incorretos"
            mensagem.color = ft.colors.RED
        page.update()

    def toggle_senha_visivel(e):
        senha_input.password = not senha_input.password
        senha_visivel_btn.icon = "visibility_off" if senha_input.password else "visibility"
        page.update()

    titulo = ft.Text("Tela de Login", size=30, weight=ft.FontWeight.BOLD)

    usuario_input = ft.TextField(label="Usuário", width=280)
    
    senha_input = ft.TextField(label="Senha", password=True, width=280)
    senha_visivel_btn = ft.IconButton(
        icon="visibility",
        on_click=toggle_senha_visivel,
        icon_size=18,
        style=ft.ButtonStyle(padding=5)
    )
    usuario_row = ft.Row(
        [usuario_input, ft.Container(width=38)],
        alignment=ft.MainAxisAlignment.CENTER
    )
    senha_row = ft.Row(
        [senha_input, ft.Container(width=38, content=senha_visivel_btn)],
        alignment=ft.MainAxisAlignment.CENTER
    )

    mensagem = ft.Text("", color=ft.colors.RED, size=16)

    login_card = ft.Container(
        content=ft.Column(
            [
                titulo,
                usuario_row,
                senha_row,
                mensagem,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=400,
        padding=40,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.colors.BLUE_GREY_300,
            offset=ft.Offset(0, 0),
        )
    )

    login_btn = ft.ElevatedButton(
        "Login",
        on_click=validar_login,
        width=300,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20),
        )
    )

    page.add(
        login_card,
        ft.Container(height=20),  
        login_btn
    )

ft.app(target=main)

