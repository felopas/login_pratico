import customtkinter as ctk # type: ignore

## Configurações do tema
ctk.set_appearance_mode("dark")

#definindo a função de validação de login
def validar_login():
   Usuario = Campo_usuario.get()
   senha = Campo_Senha.get()

   if Usuario == "adm" and senha == "123":
       login_feito.configure(text="Login feito com sucesso", text_color="green")
   else:
       login_feito.configure(text="Login ou senha inválidos", text_color="red")

# Definindo a janela principal
app = ctk.CTk()
app.title("sistema de login")
app.geometry("400x300")

# Definindo o título 
label_Usuario = ctk.CTkLabel(app,text="Usuário:")
label_Usuario.pack(pady=10)
# Definindo o campo de entrada do usuário
Campo_usuario = ctk.CTkEntry(app,placeholder_text="Digite seu usuário")
Campo_usuario.pack(pady=10)
# Definindo o título de entrada da senha
label_Senha = ctk.CTkLabel(app,text="Senha:")
label_Senha.pack(pady=10)
# Definindo o campo de entrada da senha
Campo_Senha = ctk.CTkEntry(app,placeholder_text="Digite sua senha",show="*")
Campo_Senha.pack(pady=10)

ctk.CTkButton(app,text="login",command=validar_login).pack(pady=10)

login_feito = ctk.CTkLabel(app,text="")
login_feito.pack(pady=10)

app.mainloop()