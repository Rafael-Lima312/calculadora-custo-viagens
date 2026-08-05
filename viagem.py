import customtkinter as ctk
ctk.set_appearance_mode('dark')

#funções = As funções sempre devem vir antes da janela

def viagem():
    d = int(distancia.get())
    c = float(consumo.get())
    p = float(preco.get())
    calculo = (d/c)*p
    resultado.configure(text=f'O gasto para essa viagem será de R$ {calculo:.2f}')


#janela
janela = ctk.CTk()
janela.geometry("600x450")
janela.resizable(False,False)
janela.title("App Viagem 2026")
janela.iconbitmap('Combustivel.ico')

#Elementos da janela

titulo = ctk.CTkLabel(janela,
                      text= 'App Viagem 2026',
                      text_color= 'green',
                      font=('Verdana', 50))
titulo.pack(pady = 10)



distancia = ctk.CTkEntry(janela,
                         width= 400,
                         height= 40,
                         placeholder_text='Digite a distância da viagem',
                         border_color='light green')
distancia.pack(pady = 10)



consumo = ctk.CTkEntry(janela,
                         width= 400,
                         height= 40,
                         placeholder_text='Digite o consumo do veiculo',
                         border_color='light green')
consumo.pack(pady = 10)



preco = ctk.CTkEntry(janela,
                         width= 400,
                         height= 40,
                         placeholder_text='Digite o preço do combustível',
                         border_color='light green')
preco.pack(pady= 10)



botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text='Calcular',
                      font=('verdant', 30,'bold'),
                      text_color='black',
                      fg_color='light green',
                      command= viagem)
botao.pack(pady = 10)



resultado = ctk.CTkLabel(janela,
                         text='',
                         text_color ='yellow',
                         font=('verdana',20))
resultado.pack(pady = 20)

janela.mainloop()