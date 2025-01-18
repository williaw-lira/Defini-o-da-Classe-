import tkinter as tk
from tkinter import messagebox

# Classe ContaBancaria
class ContaBancaria:
    def __init__(self, numero, titular, senha, saldo=0):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R$ {valor:.2f} efetuado com sucesso."

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} efetuado com sucesso."
        else:
            return "Saldo insuficiente para realizar o saque."

    def consultar_saldo(self):
        return f"Saldo atual: R$ {self.saldo:.2f}"

# Sistema bancário
contas = {}

def cadastrar_usuario(numero, titular, senha):
    if numero in contas:
        return "Número da conta já cadastrado."
    contas[numero] = ContaBancaria(numero, titular, senha)
    return "Cadastro realizado com sucesso!"

def verificar_login(numero, senha):
    if numero in contas and contas[numero].senha == senha:
        return contas[numero]
    return None

# Interface Gráfica
def tela_login():
    def tentar_login():
        numero = entry_numero.get()
        senha = entry_senha.get()
        conta = verificar_login(numero, senha)
        if conta:
            tela_principal(conta)
        else:
            messagebox.showerror("Erro", "Número da conta ou senha inválidos.")
    
    def abrir_tela_cadastro():
        tela_cadastro()

    janela_login = tk.Tk()
    janela_login.title("Login - Sistema Bancário")
    janela_login.configure(bg="#DDEEFF")

    tk.Label(janela_login, text="Número da Conta:", bg="#DDEEFF").grid(row=0, column=0)
    entry_numero = tk.Entry(janela_login)
    entry_numero.grid(row=0, column=1)

    tk.Label(janela_login, text="Senha:", bg="#DDEEFF").grid(row=1, column=0)
    entry_senha = tk.Entry(janela_login, show="*")
    entry_senha.grid(row=1, column=1)

    tk.Button(janela_login, text="Login", command=tentar_login, bg="#88CC88").grid(row=2, column=0, pady=10)
    tk.Button(janela_login, text="Cadastrar", command=abrir_tela_cadastro, bg="#88CC88").grid(row=2, column=1)

    janela_login.mainloop()

def tela_cadastro():
    def realizar_cadastro():
        numero = entry_numero.get()
        titular = entry_titular.get()
        senha = entry_senha.get()
        mensagem = cadastrar_usuario(numero, titular, senha)
        messagebox.showinfo("Cadastro", mensagem)
        janela_cadastro.destroy()

    janela_cadastro = tk.Tk()
    janela_cadastro.title("Cadastro - Sistema Bancário")
    janela_cadastro.configure(bg="#FFEEDD")

    tk.Label(janela_cadastro, text="Número da Conta:", bg="#FFEEDD").grid(row=0, column=0)
    entry_numero = tk.Entry(janela_cadastro)
    entry_numero.grid(row=0, column=1)

    tk.Label(janela_cadastro, text="Nome:", bg="#FFEEDD").grid(row=1, column=0)
    entry_titular = tk.Entry(janela_cadastro)
    entry_titular.grid(row=1, column=1)

    tk.Label(janela_cadastro, text="Senha:", bg="#FFEEDD").grid(row=2, column=0)
    entry_senha = tk.Entry(janela_cadastro, show="*")
    entry_senha.grid(row=2, column=1)

    tk.Button(janela_cadastro, text="Cadastrar", command=realizar_cadastro, bg="#88CC88").grid(row=3, column=0, columnspan=2, pady=10)

    janela_cadastro.mainloop()

def tela_principal(conta):
    def atualizar_saldo():
        saldo.set(conta.consultar_saldo())

    def realizar_deposito():
        try:
            valor = float(entry_valor.get())
            mensagem.set(conta.depositar(valor))
            atualizar_saldo()
        except ValueError:
            mensagem.set("Por favor, insira um valor válido.")

    def realizar_saque():
        try:
            valor = float(entry_valor.get())
            mensagem.set(conta.sacar(valor))
            atualizar_saldo()
        except ValueError:
            mensagem.set("Por favor, insira um valor válido.")

    janela_principal = tk.Tk()
    janela_principal.title("Conta Bancária")
    janela_principal.configure(bg="#EEDDFF")

    saldo = tk.StringVar()
    mensagem = tk.StringVar()

    atualizar_saldo()

    tk.Label(janela_principal, text=f"Bem-vindo, {conta.titular}!", bg="#EEDDFF").grid(row=0, column=0, columnspan=2)
    tk.Label(janela_principal, textvariable=saldo, bg="#EEDDFF").grid(row=1, column=0, columnspan=2)

    tk.Label(janela_principal, text="Valor:", bg="#EEDDFF").grid(row=2, column=0)
    entry_valor = tk.Entry(janela_principal)
    entry_valor.grid(row=2, column=1)

    tk.Button(janela_principal, text="Depósito", command=realizar_deposito, bg="#88CC88").grid(row=3, column=0)
    tk.Button(janela_principal, text="Saque", command=realizar_saque, bg="#FF8888").grid(row=3, column=1)

    tk.Label(janela_principal, textvariable=mensagem, bg="#EEDDFF").grid(row=4, column=0, columnspan=2)

    janela_principal.mainloop()

# Inicia o sistema com a tela de login
tela_login()
