import customtkinter as ctk

#Configurações da UI

ctk.set_appearance_mode("light")
janela = ctk.CTk()
janela.geometry("850x950")
janela.title("Correction-IA")


# Crie uma caixa de texto
caixa_texto = ctk.CTkTextbox(janela, width=400,)

# Insira algum texto na caixa de texto
caixa_texto.insert("0.0", "Olá, mundo!")


caixa_texto.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)





janela.mainloop()
