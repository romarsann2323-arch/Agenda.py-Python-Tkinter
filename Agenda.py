import tkinter as tk
from tkinter import messagebox, simpledialog

# Estrutura de dados para armazenar contatos
agenda = {}

# Função para adicionar um contato
def adicionar_contato():
    nome = simpledialog.askstring("Nome", "Digite o nome do contato:")
    if nome:
        telefone = simpledialog.askstring("Telefone", f"Digite o telefone de {nome}:")
        if telefone:
            agenda[nome] = telefone
            atualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Telefone não pode estar vazio!")
    else:
        messagebox.showwarning("Aviso", "Nome não pode estar vazio!")

# Função para remover um contato
def remover_contato():
    selecionado = lista_contatos.curselection()
    if selecionado:
        nome = lista_contatos.get(selecionado)
        del agenda[nome]
        atualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Selecione um contato para remover!")

# Função para atualizar a lista na interface
def atualizar_lista():
    lista_contatos.delete(0, tk.END)
    for nome in agenda:
        lista_contatos.insert(tk.END, nome)

# Função para mostrar detalhes do contato
def mostrar_contato(event):
    selecionado = lista_contatos.curselection()
    if selecionado:
        nome = lista_contatos.get(selecionado)
        telefone = agenda[nome]
        messagebox.showinfo(nome, f"Telefone: {telefone}")

# Configuração da janela principal
root = tk.Tk()
root.title("Agenda de Contatos")
root.geometry("300x400")

# Lista de contatos
lista_contatos = tk.Listbox(root)
lista_contatos.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
lista_contatos.bind("<Double-Button-1>", mostrar_contato)

# Botões
btn_adicionar = tk.Button(root, text="Adicionar Contato", command=adicionar_contato)
btn_adicionar.pack(side=tk.LEFT, padx=10, pady=10)

btn_remover = tk.Button(root, text="Remover Contato", command=remover_contato)
btn_remover.pack(side=tk.RIGHT, padx=10, pady=10)

# Inicializa a interface
root.mainloop()
