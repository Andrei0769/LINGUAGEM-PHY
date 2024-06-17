import webbrowser
import os

def abrir_whatsapp():
    # Abrir WhatsApp Web em uma janela anônima
    webbrowser.get('windows-default').open_new_tab('https://web.whatsapp.com', autoraise=True)

def abrir_email():
    # Abrir email em uma janela normal
    webbrowser.open_new_tab('https://mail.google.com', autoraise=True)

def abrir_github():
    # Abrir GitHub em uma janela normal
    webbrowser.open_new_tab('https://github.com', autoraise=True)

if __name__ == "__main__":
    # Abrir WhatsApp Web e email em uma tela (monitor primário)
    abrir_whatsapp()
    abrir_email()

    # Abrir GitHub em outra tela (monitor secundário)
    abrir_github()

    # Pausa para manter as janelas abertas (opcional)
    input("Pressione Enter para fechar o programa...")
