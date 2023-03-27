import tkinter as tk

def cifrar(frase, chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    cifrado = ''
    for letra in frase:
        if letra in alfabeto:
            posicao = alfabeto.find(letra)
            nova_posicao = (posicao + chave) % 26
            cifrado += alfabeto[nova_posicao]
        else:
            cifrado += letra
    return cifrado

def cifrar_frase():
    frase = entrada_frase.get()
    chave = int(entrada_chave.get())
    cifrado = cifrar(frase, chave)
    texto_cifrado.config(text=cifrado)

# Criação da janela principal
janela = tk.Tk()
janela.title('Cifra de César')

# Criação dos widgets da interface
rotulo_frase = tk.Label(janela, text='Digite a frase:')
rotulo_frase.pack()
entrada_frase = tk.Entry(janela)
entrada_frase.pack()

rotulo_chave = tk.Label(janela, text='Digite a chave:')
rotulo_chave.pack()
entrada_chave = tk.Entry(janela)
entrada_chave.pack()

botao_cifrar = tk.Button(janela, text='Cifrar', command=cifrar_frase)
botao_cifrar.pack()

texto_cifrado = tk.Label(janela, text='')
texto_cifrado.pack()

# Inicia a execução da interface
janela.mainloop()
