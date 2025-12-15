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
tela.geometry("500x500")
#tela.state('zoomed')
tela.title("Produto educacional")


# função linear: y = a*x + b
def func_linear(x, a, b):
    """Função linear para ajuste."""
    return a * x + b

def arquivo(a):
    if a==1:
        receber=cb.get()
        if receber=="Linear":
            
            """Abre a janela de seleção de arquivo e exibe o caminho escolhido."""
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um Arquivo",
        filetypes=(("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*"))
    )
    if caminho_arquivo:
        messagebox.showinfo("Arquivo Selecionado", f"Você selecionou:\n{caminho_arquivo}")
        lb2=Label(tela, text="ARQUIVO SELECIONADO COM SUCESSO!", font=("Fixedsys", 18), fg="green", width=50, height=3)
        lb2.pack()
        
    #listas
        qnt_tempos_inic = 10
        tempos1 = []
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for i in range(qnt_tempos_inic):
                linha = arquivo.readline()
                if not linha:
                    break
                valor = float(linha.strip())
                tempos1.append(valor)
                
            #MEDIA DOS TEMPOs
            soma_elementos = sum(tempos1)
            quantidade_elementos = len(tempos1)
            mediadostempos = soma_elementos / quantidade_elementos
            print(f"O array do tempo 1 é: {tempos1}")
            print(f"A média aritmética é: {mediadostempos}")
            
            x_data = np.array(tempos1)
            y_data = np.array([0.018, 0.036, 0.054, 0.072, 0.090, 0.108, 0.126, 0.144, 0.162, 0.180])
            x_sigma = np.array([0.0002466441431, 0.0004618802154, 0.000692820323, 0.0009096702699,0.001140540807,0.001216552506, 0.03184102438,0.03104726236, 0.03077313493, 0.03026809376])  # Desvio padrão (incerteza) de x


            params, pcov = curve_fit(func_linear, x_data, y_data, sigma= x_sigma)
            a, b = params
            perr = np.sqrt(np.diag(pcov))

            print(f"Parâmetros do ajuste:")
            print(f"  - Coeficiente angular (a): {a:.4f} +/- {perr[0]:.4f}")
            print(f"  - Coeficiente linear (b): {b:.4f} +/- {perr[1]:.4f}")

            x_fit = np.linspace(min(x_data),max(x_data),100)
            y_fit = func_linear(x_fit, a, b)

            plt.figure(figsize=(8, 6))
            plt.errorbar(x_data, y_data, xerr=x_sigma, fmt='o', capsize=4, label='Dados com incerteza em t')
            plt.plot(x_fit, y_fit, '-', label=f'Ajuste linear: y = {a:.2f}x + {b:.2f}')

            
            plt.title('Ajuste Linear com Desvio Padrão')
            plt.xlabel('Variável X')
            plt.ylabel('Variável Y')
            plt.legend()
            plt.grid(True)
            plt.show()
            
    else:
        messagebox.showwarning("Seleção Cancelada", "Nenhum arquivo selecionado.")
            

lb=Label(tela, text="Escolha o FIT polinomial", font=("Fixedsys", 18), fg="black", width=50, height=3)
lista=["Linear","Polinomial grau 2"]
cb=ttk.Combobox(tela, values=lista, font=("Fixedsys", 18), width=20, height=10)
cb.set("Linear")
botaofit= Button(tela, text="Escolher arquivo",bg="green",fg="white",width=20, height=2, font=("Fixedsys", 9), command= lambda: arquivo(1))

#Posicionamento dos componentes da tela 3:

lb.pack()
cb.pack()
botaofit.pack(padx=0, pady=10)


tela.mainloop()
