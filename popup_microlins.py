from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import time
import AllWhatsPy as awp



class popup():     
    
    
    def __init__(self):
        popup.janela_grafica()
        

    def janela_grafica():

        # Define o título da janela
        janela.title("PDP")

        # Define o tamanho da janela
        janela.geometry("800x600+300+0")

        # Carrega a imagem de fundo e cria um objeto ImageTk
        imagem_fundo = Image.open('img.jpg')
        imagem_fundo = imagem_fundo.resize((800, 600), Image.Resampling.LANCZOS)
        imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

        # Cria um label com a imagem de fundo
        label_fundo = tk.Label(janela, image=imagem_fundo)
        label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        # Cria o botão
        botao_para_janela_qrcode = tk.Button(janela, text="CLIQUE AQUI PARA GARANTIR SUA VAGA", command=janela_qrcode, bg='green', fg='white', font=fonte_negrito)
        botao_para_janela_qrcode.place(x=25, y=550)

        # Inicia o loop principal da janela
        janela.mainloop()
        



class janela_qrcode():
    
    
    def __init__(self):
        janela_qrcode.janela_grafica_qrcode()
                
        
    def janela_grafica_qrcode():
        
        # Define o tamanho da janela
        janela.geometry("800x700+300+0")
        
        
        # Carrega a imagem de fundo e cria um objeto ImageTk
        imagem_fundo = Image.open('qrcode_img.jpg')
        imagem_fundo = imagem_fundo.resize((800, 700), Image.Resampling.LANCZOS)
        imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

        
        # Cria um label com a imagem de fundo
        label_fundo = tk.Label(janela, image=imagem_fundo)
        label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        # Botão para abrir o Whatsapp Web
        botao_para_janela_qrcode = tk.Button(janela, text="Whatsapp Web", command=janela_qrcode.script_webwpp, bg='red', fg='white', font=fonte_negrito)
        botao_para_janela_qrcode.place(x=50, y=650)
        
        
        
        # Botão de voltar
        botao_retorno = tk.Button(janela, text= 'Voltar',command=popup,bg='red', fg='white',  font=fonte_negrito)
        botao_retorno.place(x=15, y=25)

        

        janela.mainloop()


    def script_webwpp():
        validacao = janela_qrcode.mensagem_aguarde()        
        
        if validacao:
            awp.conexao(2)
            messagebox.showinfo('Aguarde','Aguarde enquanto a tela é carregada.')
            nome = awp.nome_usuario()
            awp.encontrar_usuario('21966549910')
            awp.enviar_mensagem(f'Olá, me chamo {nome}! Gostaria de estar recebendo novas informações do PDP')
            awp.desconectar()
            
            janela.destroy()
                    
       
        
    def mensagem_aguarde():
        resultado = messagebox.askyesno('Ler QRcode com o Whatsapp', texto_janela_grafica)
        
        return resultado
    
    
    
# Dados
with open('texto.txt', 'r', encoding='utf-8') as file:
    texto_janela_grafica = file.read()



# Utilidades 
fonte_negrito = ("Arial", 16, "bold")
tempo_de_aguardo = 90*60 
    
    
# Execução
janela = tk.Tk()

while True:    
    popup()

    time.sleep(tempo_de_aguardo)