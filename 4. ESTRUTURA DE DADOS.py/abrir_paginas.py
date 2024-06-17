import os
import time

def abrir_whatsapp():
    # Abrir WhatsApp Web em uma janela anônima
    os.startfile('https://web.whatsapp.com')

def abrir_email():
    # Abrir email em uma janela normal
    os.startfile('https://mail.google.com')

def abrir_github():
    # Abrir GitHub em uma janela normal
    os.startfile('https://github.com')

if __name__ == "__main__":
    # Abrir WhatsApp Web e email em uma tela (monitor primário)
    abrir_whatsapp()
    abrir_email()

    # Pausa para permitir que as janelas sejam abertas
    time.sleep(2)

    # Abrir GitHub em outra tela (monitor secundário)
    abrir_github()

    # Pausa opcional para manter as janelas abertas (opcional)
    input("Pressione Enter para fechar o programa...")
