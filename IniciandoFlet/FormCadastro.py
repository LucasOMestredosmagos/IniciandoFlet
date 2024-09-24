import flet as ft

def main(page: ft.page):
    page.title = "Formulário de Cadastro"

    nome = ft.TextField(label="Nome", width=300)
    sobrenome = ft.TextField(label="Sobrenome", width=300)
    email = ft.TextField(label="Email", width=300)


    form_layout = ft.Column(
        controls= [
        ft.Row([nome, sobrenome]),
        ft.Row([email])
       ] 
    )

    enviar =  ft.ElevatedButton("Enviar")

    def enviar_Click(e):
        dados_formulario = {
            "nome": nome.value,
            "sobrenome": sobrenome.value,
            "email": email.value
        }
        print("Formulário enviado!")
        print("Dados do formulário:")
        print(dados_formulario)

    enviar.on_click = enviar_Click
    page.add(form_layout)
    page.add(enviar)

ft.app(target=main)
