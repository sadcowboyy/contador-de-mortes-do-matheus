import tkinter as tk

# Função para aumentar a contagem de mortes
def aumentar_contagem():
    global mortes
    mortes += 1
    label_mortes.config(text=f"Total de mortes: {mortes}")

# Função para diminuir a contagem de mortes
def diminuir_contagem():
    global mortes
    if mortes > 0:
        mortes -= 1
    label_mortes.config(text=f"Total de mortes: {mortes}")

# Inicializa o contador de mortes
mortes = 0

# Cria a janela principal
janela = tk.Tk()
janela.title("Contador de Mortes")

# Cria o rótulo que mostrará a contagem de mortes
label_mortes = tk.Label(janela, text=f"Total de mortes: {mortes}", font=("Arial", 16))
label_mortes.pack(pady=20)

# Cria o botão para aumentar a contagem de mortes
botao_aumentar = tk.Button(janela, text="Adicionar Morte", command=aumentar_contagem, font=("Arial", 14))
botao_aumentar.pack(pady=10)

# Cria o botão para diminuir a contagem de mortes
botao_diminuir = tk.Button(janela, text="Diminuir Morte", command=diminuir_contagem, font=("Arial", 14))
botao_diminuir.pack(pady=10)

# Cria um botão para fechar o programa
botao_sair = tk.Button(janela, text="Sair", command=janela.quit, font=("Arial", 14))
botao_sair.pack(pady=10)

# Executa o loop principal da janela
janela.mainloop()