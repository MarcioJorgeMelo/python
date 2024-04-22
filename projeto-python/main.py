import tkinter as tk
from tkinter import ttk
import re

class App(tk.Tk):

    def __init__(self):
        super().__init__()
       
        self.title("Cadastro - Produto")
    
        self.varResultado = tk.StringVar(self)
        self.lblResultado = ttk.Label(
            self, textvariable=self.varResultado,
            font=("Arial", 18),
            background="#DDDDDD"
        )
        self.lblResultado.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="ewns")

        #self.iconbitmap("C:/Users/Jorge/Documents/DEV/python_/projeto-python/imagens/javamelhorquepython.ico")


        self.lblNome = ttk.Label(
            self, text="Nome",
            font=("Arial", 18, "bold")
        )
        
        self.lblNome.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        
        self.varNome = tk.StringVar(self)
        self.txtNome = ttk.Entry(
            self, textvariable=self.varNome,
            font=("Arial", 18)
        )
        self.txtNome.grid(row=1, column=1, sticky="we", padx=5, pady=5)
        self.txtNome.focus()

        
        self.lblValor = ttk.Label(
            self, text="Valor",
            font=("Arial", 18, "bold")
        )
        
        self.lblValor.grid(row=2, column=0, sticky="w", padx=20, pady=5)
        
        self.varValor = tk.StringVar(self)
        self.txtValor = ttk.Entry(
            self, textvariable=self.varValor,
            font=("Arial", 18)
        )
        self.txtValor.grid(row=2, column=1, sticky="we", padx=5, pady=5)

        
        self.lblQuantidade = ttk.Label(
            self, text="Quantidade",
            font=("Arial", 18, "bold")
        )
        
        self.lblQuantidade.grid(row=3, column=0, sticky="w", padx=20, pady=5)
        
        self.varQuantidade = tk.StringVar(self)
        self.txtQuantidade = ttk.Entry(
            self, textvariable=self.varQuantidade,
            font=("Arial", 18)
        )
        self.txtQuantidade.grid(row=3, column=1, sticky="we", padx=5, pady=5)

        self.lbl = ttk.Label(
            self, text="",
            font=("Arial", 18, "bold")
        )
        self.lbl.grid(row=4, column=0, sticky="w", padx=20, pady=5)
       
        
        self.frameLista = ttk.Frame(self)
        self.frameLista.grid(row=5, column=0, columnspan=3, rowspan=4, sticky="nwes", padx=20, pady=10)

        self.txtLista = ttk.Treeview(
            self.frameLista, columns=('nome','valor','quantidade', 'valorfinal'),
            show="headings", height=7
        )
        self.txtLista.heading('nome', text='Nome')
        self.txtLista.heading('valor', text='Valor')
        self.txtLista.heading('quantidade', text='Quantidade')
        self.txtLista.heading('valorfinal', text='Valor Final')


        def item_selected(event):
            for selected_item in self.txtLista.selection():
                item = self.txtLista.item(selected_item)
                record = item['values']
                self.varNome.set(record[0])
                self.varValor.set(record[1])
                self.varQuantidade.set(record[2])
       
        self.txtLista.bind('<<TreeviewSelect>>', item_selected)

        self.txtLista.grid(row=0, column=0, sticky="nwes")

        scrollbar = ttk.Scrollbar(
            self.frameLista, orient=tk.VERTICAL,
            command=self.txtLista.yview)
        self.txtLista.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        
        self.btnCadastrar = ttk.Button(
            self, text="Cadastrar",
            command=self.btnCadastrar_click,
        )
        self.btnCadastrar.grid(row=1, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)
        
        self.btnLimpar = ttk.Button(
            self, text="Limpar",
            command=self.btnLimpar_Click,
        )
        self.btnLimpar.grid(row=2, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)
        
        self.btnExcluir = ttk.Button(
            self, text="Excluir",
             command=self.btnExcluir_Click,
        )
        self.btnExcluir.grid(row=3, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        self.btnEditar = ttk.Button(
            self, text="Editar",
             command=self.btnEditar_Click,
        )
        self.btnEditar.grid(row=4, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        
    #Metodos
    def calcularImposto(self, valor, quantidade):
        
        valor_float = float(valor.replace(',', '.'))
        quantidade_int = int(quantidade)
        valor_imp = valor_float * quantidade_int * 0.15
        valor_total_com_imposto = valor_float * quantidade_int + valor_imp
        return valor_total_com_imposto
    
    def btnCadastrar_click(self):
        nome = self.varNome.get().strip()
        valor = self.varValor.get().strip()
        quantidade = self.varQuantidade.get().strip()
        
        reNome = re.fullmatch(r"\b[\w.%+\-\s]+\b", nome, flags=re.UNICODE)
        
        
        if nome.strip() == "":
            self.varResultado.set("O campo nome é obrigatório.")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
            return
        elif reNome is None:
            self.varResultado.set("O campo nome não segue o formato válido.")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()   
            return
        
        try:
            valor_float = float(valor.replace(',', '.'))
            if valor_float <= 0:
                raise ValueError("O valor deve ser maior que zero")
        except ValueError:
            self.varResultado.set("Insira um valor válido")
            self.lblResultado.configure(background="#FF9999")
            self.txtValor.focus()
            return
        
        try:
            quantidade_int = int(quantidade)
            if quantidade_int <= 0:
                raise ValueError("A quantidade deve ser maior que zero")
        except ValueError:
            self.varResultado.set("Insira uma quantidade válida")
            self.lblResultado.configure(background="#FF9999")
            self.txtQuantidade.focus()
            return
        
        valor_total_com_imposto = self.calcularImposto(valor, quantidade)
        
        produtoCadastrado = [self.varNome.get(), valor, quantidade, valor_total_com_imposto]
        listaProdutos = []
        listaProdutos.append(produtoCadastrado)
        for produtos in listaProdutos:
            self.txtLista.insert('', tk.END, values=produtos)
        self.varResultado.set("O cadastro foi realizado com sucesso!")
        self.lblResultado.configure(background="#71E964")
        self.after(1000, self.limparMensagem)
        self.varNome.set("")
        self.varValor.set("")
        self.varQuantidade.set("")
        self.txtNome.focus()
                
    def btnLimpar_Click(self):
        try:
            if self.varNome.get() or self.varValor.get() or self.varQuantidade.get():
                self.varNome.set("")
                self.varValor.set("")
                self.varQuantidade.set("")
                self.varResultado.set("Os campos foram limpos com sucesso")
                self.lblResultado.configure(background="#71E964")
                self.txtNome.focus()
                self.after(1000, self.limparMensagem) 
        except AttributeError:
            self.varResultado.set("Os campos estão vazios")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()   
            return
            
    def btnExcluir_Click(self):
        item_selecionado = self.txtLista.selection()
       
        if item_selecionado:
            self.txtLista.delete(item_selecionado)
            self.varNome.set("")
            self.varValor.set("")
            self.varQuantidade.set("")
           
            self.varResultado.set("A exclusão foi realizado com sucesso!")
            self.lblResultado.configure(background="#FF9999")
            self.after(1000, self.limparMensagem)

    def btnEditar_Click(self):
        item_selecionado = self.txtLista.selection()
        try:
            if item_selecionado:
                valores = self.txtLista.item(item_selecionado)['values']
                valores[0] = self.varNome.get()
                valores[1] = self.varValor.get()
                valores[2] = self.varQuantidade.get()
                valores[3] = self.calcularImposto(valores[1], valores[2])
                
                self.txtLista.item(item_selecionado, values=valores)
                self.varNome.set("")
                self.varValor.set("")
                self.varQuantidade.set("")
                self.txtNome.focus()
                                
                self.varResultado.set("O cadastro foi editado com sucesso!")
                self.lblResultado.configure(background="#71E964")
                self.after(1000, self.limparMensagem)
        except IndexError:
            self.varResultado.set("Selecione um produto para editar.")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
        except ValueError:
            self.varResultado.set("Valores inválidos. Verifique novamente.")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
        except Exception as e:
            print(f"Erro desconhecido ao editar produto: {e}")
        
    def limparMensagem(self):
        self.varResultado.set("")
        self.lblResultado.configure(background="#DDDDDD")
       
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
    