from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import webview
import tkinter.font as TkFont
from tkinter import filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#import tkinter as tk

#COMPONENTES DA TELA INICIAL

tela = Tk()
"""is_fullscreen = False
def toggle_fullscreen(event=None):
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    tela.attributes('-fullscreen', is_fullscreen)

tela.bind('<F11>', toggle_fullscreen)
tela.bind('<Escape>', lambda e: tela.attributes('-fullscreen', False))"""
#tela.geometry("700x1200")
tela.state('zoomed')
tela.title("Produto educacional")

#TESTE DE ALTERAÇÃO
# função linear: y = a*x + b
def func_linear(x, a, b):
    """Função linear para ajuste."""
    return a * x + b
    #return a*x**2 + b*x + c

"""global receber

def recebimento():
    global receber
    receber=cb.get()
    pontos = int(receber)
"""

#tela 2 - configurações iniciais
def arquivo(a):
    if a==1:

        #recebimento das variaveis da tela 1:

        global recebersiglay
        global recebersiglax
        global receber
        global receber2
        global receberrotuloy
        global receberrotulox
        global eixorepetido
        
        eixorepetido = cb2.get()
        recebersiglay=cx2_1
        recebersiglax=cx1_1
        receber2=cb5.get()
        receber=cb4.get()
        receberrotuloy= cx2.get()
        receberrotulox= cx1.get()
        pontos = int(receber)
        pontos2 = int(receber2)
    
        #componentes da tela 2
        tela2=Tk()
        tela2.title("INSIRA OS DADOS DO EXPERIMENTO")
        tela2.state("zoomed")
        #textofinalrotulo1 = f"{receberrotuloy} {recebersiglay}"
        lbl_id = Label(tela2, text= receberrotuloy, font=("Arial", 10, "bold"), fg="blue")
        lbl_id.place(x=0, y=0)

        lbl_id2 = Label(tela2, text=receberrotulox, font=("Arial", 10, "bold"), fg="blue")
        lbl_id2.grid(row=0, column=3, columnspan=1, pady=(5, 5))

        botaogerador= Button(tela2, text="GERAR GRAFICO", command= lambda: gerador(1))
        botaogerador.place(x=0, y=600)
        
        #criaçao das caixas de textos para a inserção de dados:
        for l in range(pontos):
            for c in range(pontos2 + 1):
                caixa = Entry(tela2, width=10)
                #espaco_x = 2
                if c == 0:
                    padding_personalizado = (4, 100) 
                else:
                    padding_personalizado = 4
            
                caixa.grid(row=l + 1, column=c, padx=padding_personalizado, pady=10)

                
                #caixa.insert(0, f"linha{l} coluna{c}")

        #troca os rotulos na tela2 ao mudar a opção da variavel que foi medida varias vezes na tela1:
        if eixorepetido == "Apenas y":
            lbl_id = Label(tela2, text= receberrotulox, font=("Arial", 10, "bold"), fg="blue")
            lbl_id.place(x=0, y=0)

            lbl_id2 = Label(tela2, text=receberrotuloy, font=("Arial", 10, "bold"), fg="blue")
            lbl_id2.grid(row=0, column=3, columnspan=1, pady=(5, 5))

    lista_entries = []
        
    def gerador(b):
        if b==1:
            lista_entries.append(caixa)
            def coletar_dados():

                dados = [entrada.get() for entrada in lista_entries]
                lbldados = Label(tela2, text=dados, font=("Arial", 10, "bold"), fg="blue")
                lbldados.place(x=0, y=500)
                print("Dados coletados:", dados)





        #botao11.pack()


"""
def arquivo(a):
    if a==1:
        receber=cb.get()
        if receber=="Linear":
            
            Abre a janela de seleção de arquivo e exibe o caminho escolhido.
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um Arquivo",
        filetypes=(("Arquivo de Dados", "*.dat"),("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*"))
    )
    if caminho_arquivo:
        messagebox.showinfo("Arquivo Selecionado", f"Você selecionou:\n{caminho_arquivo}")
        lb2=Label(tela, text="ARQUIVO SELECIONADO COM SUCESSO!", font=("Fixedsys", 18), fg="green", width=50, height=3)
        lb2.pack()

    #Carregamento do arquivo de dados experimentais
        data = np.loadtxt(caminho_arquivo)
        dados_medios = np.mean(data, axis=0)
        dados_desvio = np.std(data, axis=0)

        x_data = dados_medios
        y_data = np.array([0.018, 0.036, 0.054, 0.072, 0.090, 0.108, 0.126, 0.144, 0.162, 0.180])
        x_sigma = dados_desvio

        params, pcov = curve_fit(func_linear, x_data, y_data, sigma= x_sigma)
        a, b = params
        perr = np.sqrt(np.diag(pcov))

        print(f"Parâmetros do ajuste:")
        print(f"  - Coeficiente angular (a): {a:.4f} +/- {perr[0]:.4f}")
        print(f"  - Coeficiente linear (b): {b:.4f} +/- {perr[1]:.4f}")
        #print(f"  - Coeficiente (c): {c:.4f} +/- {perr[1]:.4f}")

        x_fit = np.linspace(min(x_data),max(x_data),200)
        y_fit = func_linear(x_fit, a, b)


        plt.figure(figsize=(8, 6))
        plt.errorbar(x_data, y_data, xerr=x_sigma, fmt='o', capsize=4, label='Dados com incerteza em t')
        plt.plot(x_fit, y_fit, '-', label=f'Ajuste linear: {cx2_1.get()} = {a:.2f}{cx1_1.get()} + {b:.2f}' )


        plt.title('Ajuste Linear com Desvio Padrão')
        plt.xlabel(cx1.get())
        plt.ylabel(cx2.get())
        plt.legend()
        plt.grid(True)
        plt.show()

    else:     
        messagebox.showwarning("Seleção Cancelada", "Nenhum arquivo selecionado.")

"""
frame_moldura = Canvas(tela, bg="lightblue", bd=4, relief="groove", highlightthickness=0)
frame_moldura.pack(fill=BOTH, expand=True)
frame_moldura.create_rectangle(400, 10, 1150, 750, outline="red", width=4)
            
lb1=Label(frame_moldura, text="Selecione a quantidade de curvas no gráfico", font=("Fixedsys", 12), fg="black", width=50, height=3, bd=2, bg="lightblue")
lista1=["1"]
cb1=ttk.Combobox(frame_moldura, values=lista1, font=("Fixedsys", 12), width=5, height=10)
cb1.set("1")
lb=Label(frame_moldura, text="Selecione o tipo de ajuste (fit)", font=("Fixedsys", 12), fg="black", width=50, height=3,  bg="lightblue")
lista2=["Linear","Polinomial grau 2"]
cb=ttk.Combobox(frame_moldura, values=lista2, font=("Fixedsys", 12), width=20, height=10)
cb.set("Linear")
lb2=Label(frame_moldura, text="Quais os eixos que foram medidos várias vezes?", font=("Fixedsys", 12), fg="black", width=50, height=3, bg="lightblue")
lista3=["Apenas x","Apenas y", "Ambos"]
cb2=ttk.Combobox(frame_moldura, values=lista3, font=("Fixedsys", 12), width=10, height=10)
cb2.set("Apenas x")
lb3=Label(frame_moldura, text="Qual o rótulo do eixo x?", font=("Fixedsys", 12), fg="black", width=50, height=3, bg="lightblue")
cx1= Entry(frame_moldura)
lb4=Label(frame_moldura, text="Qual o rótulo do eixo y?", font=("Fixedsys", 12), fg="black", width=50, height=3, bg="lightblue")
cx2= Entry(frame_moldura)
lb3_1=Label(frame_moldura, text="E sua sigla?", font=("Fixedsys", 12), fg="black", width=50, height=3, bg="lightblue")
cx1_1= Entry(frame_moldura)
lb4_1=Label(frame_moldura, text="E sua sigla?", font=("Fixedsys", 12), fg="black", width=50, height=3, bg="lightblue")
cx2_1= Entry(frame_moldura)
lb5_1=Label(frame_moldura, text="Quantos pontos no gráfico?", font=("Fixedsys", 12), fg="black", width=50, height=3, bg="lightblue")
lista4=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
cb4=ttk.Combobox(tela, values=lista4, font=("Fixedsys", 12), width=5, height=10)
cb4.set("1")
lb6_1=Label(frame_moldura, text="Quantas medidas foram feitas?", font=("Fixedsys", 12), fg="black", width=50, height=3, bg="lightblue")
lista4=["1", "2", "3", "4", "5"]
cb5=ttk.Combobox(frame_moldura, values=lista4, font=("Fixedsys", 12), width=5, height=10)
cb5.set("1")
botaofit= Button(frame_moldura, text="Inserir dados experimentais",bg="green",fg="white",width=50, height=2, font=("Fixedsys", 9), command= lambda: arquivo(1))

#Posicionamento dos componentes da tela 3:
lb1.pack()
cb1.pack()
lb.pack()
cb.pack()
lb2.pack()
cb2.pack()
lb3.place(x=440, y=250)
cx1.place(x=580, y=300)
lb4.place(x=440, y=350)
cx2.place(x=580, y=400)

lb3_1.place(x=740, y=250)
cx1_1.place(x=880, y=300)
lb4_1.place(x=740, y=350)
cx2_1.place(x=880, y=400)

lb5_1.place(x=590, y=500)
cb4.place(x=760, y=550)
lb6_1.place(x=590, y=630)
cb5.place(x=760, y=680)

botaofit.place(x=595, y=770)


tela.mainloop()
