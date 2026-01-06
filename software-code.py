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
is_fullscreen = False
def toggle_fullscreen(event=None):
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    tela.attributes('-fullscreen', is_fullscreen)

tela.bind('<F11>', toggle_fullscreen)
tela.bind('<Escape>', lambda e: tela.attributes('-fullscreen', False))
# tela.geometry("700x700")
#tela.state('zoomed')
tela.title("Produto educacional")

#TESTE DE ALTERAÇÃO
# função linear: y = a*x + b
def func_linear(x, a, b):
    """Função linear para ajuste."""
    return a * x + b
    #return a*x**2 + b*x + c


def arquivo(a):
    if a==1:
        receber=cb.get()
        if receber=="Linear":
            
            """Abre a janela de seleção de arquivo e exibe o caminho escolhido."""
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
            
lb1=Label(tela, text="Selecione a quantidade de curvas no gráfico", font=("Fixedsys", 12), fg="black", width=50, height=3)
lista1=["1","2","3","4"]
cb1=ttk.Combobox(tela, values=lista1, font=("Fixedsys", 12), width=5, height=10)
cb1.set("1")
lb=Label(tela, text="Selecione o tipo de ajuste (fit)", font=("Fixedsys", 12), fg="black", width=50, height=3)
lista2=["Linear","Polinomial grau 2"]
cb=ttk.Combobox(tela, values=lista2, font=("Fixedsys", 12), width=20, height=10)
cb.set("Linear")
lb2=Label(tela, text="Quais os eixos que foram medidos várias vezes?", font=("Fixedsys", 12), fg="black", width=50, height=3)
lista3=["Apenas x","Apenas y", "Ambos"]
cb2=ttk.Combobox(tela, values=lista3, font=("Fixedsys", 12), width=10, height=10)
cb2.set("Apenas x")
lb3=Label(tela, text="Qual o rótulo do eixo x?", font=("Fixedsys", 12), fg="black", width=50, height=3)
cx1= Entry(tela)
lb3_1=Label(tela, text="E sua sigla?", font=("Fixedsys", 12), fg="black", width=50, height=3)
cx1_1= Entry(tela)
lb4=Label(tela, text="Qual o rótulo do eixo y?", font=("Fixedsys", 12), fg="black", width=50, height=3)
cx2= Entry(tela)
lb4_1=Label(tela, text="E sua sigla?", font=("Fixedsys", 12), fg="black", width=50, height=3)
cx2_1= Entry(tela)
botaofit= Button(tela, text="Escolher arquivo",bg="green",fg="white",width=20, height=2, font=("Fixedsys", 9), command= lambda: arquivo(1))

#Posicionamento dos componentes da tela 3:
lb1.pack()
cb1.pack()
lb.pack()
cb.pack()
lb2.pack()
cb2.pack()
lb3.pack()
cx1.pack()
lb3_1.pack()
cx1_1.pack()
lb4.pack()
cx2.pack()
lb4_1.pack()
cx2_1.pack()

botaofit.pack(padx=0, pady=10)


tela.mainloop()
