import tkinter as tk
from tkinter import ttk
import re

class App(tk.Tk):

    def __init__(self):
        super().__init__()
       
        self.title("Cadastro - Produto")
        #label de Resultado
        self.varResultado = tk.StringVar(self)
        self.lblResultado = ttk.Label(
            self, textvariable=self.varResultado,
            font=("Arial", 18),
            background="#DDDDDD"
        )
        self.lblResultado.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="ewns")

        self.iconbitmap("C:/Users/Jorge/Documents/DEV/python_/projeto-python/imagens/javamelhorquepython.ico")


        # label Nome
        self.lblNome = ttk.Label(
            self, text="Nome",
            font=("Arial", 18, "bold")
        )
        # chamada e posicionamento do label Nome
        self.lblNome.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        # input Nome
        self.varNome = tk.StringVar(self)
        self.txtNome = ttk.Entry(
            self, textvariable=self.varNome,
            font=("Arial", 18)
        )
        self.txtNome.grid(row=1, column=1, sticky="we", padx=5, pady=5)
        self.txtNome.focus()

        # label Valor
        self.lblValor = ttk.Label(
            self, text="Valor",
            font=("Arial", 18, "bold")
        )
        # chamada e posicionamento do label E-mail
        self.lblValor.grid(row=2, column=0, sticky="w", padx=20, pady=5)
        # input Email
        self.varValor = tk.StringVar(self)
        self.txtValor = ttk.Entry(
            self, textvariable=self.varValor,
            font=("Arial", 18)
        )
        self.txtValor.grid(row=2, column=1, sticky="we", padx=5, pady=5)

        #label Quantidade
        self.lblQuantidade = ttk.Label(
            self, text="Quantidade",
            font=("Arial", 18, "bold")
        )
        # chamada e posicionamento do label E-mail
        self.lblQuantidade.grid(row=3, column=0, sticky="w", padx=20, pady=5)
        # input Email
        self.varQuantidade = tk.StringVar(self)
        self.txtQuantidade = ttk.Entry(
            self, textvariable=self.varQuantidade,
            font=("Arial", 18)
        )
        self.txtQuantidade.grid(row=3, column=1, sticky="we", padx=5, pady=5)
       
        # Lista resultados
        # chamada e posicionamento da lista de clientes
        self.frameLista = ttk.Frame(self)
        self.frameLista.grid(row=4, column=0, columnspan=3, rowspan=4, sticky="nwes", padx=20, pady=10)

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

        # Botões
        self.btnCadastrar = ttk.Button(
            self, text="Cadastrar",
            command=self.btnCadastrar_click,
        )
        self.btnCadastrar.grid(row=1, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)
        
        self.btnCadastrar = ttk.Button(
            self, text="Limpar",
            command=self.btnLimpar_Click,
        )
        self.btnCadastrar.grid(row=2, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)
        
        self.btnCadastrar = ttk.Button(
            self, text="Excluir",
             command=self.btnExcluir_Click,
        )
        self.btnCadastrar.grid(row=3, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        
    #Metados
    def btnCadastrar_click(self):
        
        nome = self.varNome.get().strip()
        valor = self.varValor.get().strip()
        quantidade = self.varQuantidade.get().strip()
        
        reNome = re.fullmatch(r"\b[\w.%+\-\s]+\b", nome,flags=re.UNICODE)
        reValor = re.fullmatch(r"\b\d+(,\d{1,2})?\b", valor)
        reQuantidade = re.fullmatch(r"\b[0-9]+\b", quantidade)
        
        if nome.strip() == "":
            self.varResultado.set("O campo nome é obrigatório.")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
        elif reNome is None:
            self.varResultado.set("O campo nome não segue o formato válido.")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()   
        if reValor is None:
            self.varResultado.set("Insira um valor válido")
            self.lblResultado.configure(background="#FF9999")
            self.txtValor.focus()
        elif float(valor.replace(',', '.')) <= 0:
            self.varResultado.set("Insira um valor válido")
            self.lblResultado.configure(background="#FF9999")
            self.txtValor.focus()
        elif reQuantidade is None:
            self.varResultado.set("Insira uma quantidade válida")
            self.lblResultado.configure(background="#FF9999")
            self.txtQuantidade.focus()
        else:
            produtoCadastrado = [self.varNome.get(), self.varValor.get(), self.varQuantidade.get(), '0']
            listaProdutos = []
            listaProdutos.append(produtoCadastrado)
            for produtos in listaProdutos:
                self.txtLista.insert('', tk.END, values=produtos)
            self.varResultado.set("O cadastro foi realizado com sucesso!")
            self.lblResultado.configure(background="#71E964")
                
    def btnLimpar_Click(self):
        self.varNome.set("")
        self.varValor.set("")
        self.varQuantidade.set("")
        self.txtNome.focus()
        
    def btnExcluir_Click(self):
        selected_item = self.txtLista.selection()
        if selected_item:
             self.txtLista.delete(selected_item)
        self.varNome.set("")
        self.varValor.set("")
        self.varQuantidade.set("")
        self.txtNome.focus()
        
        self.varResultado.set("A exclusão foi realizado com sucesso!")
        self.lblResultado.configure(background="#FF9999")
        
           
if __name__ == "__main__":
    app = App()
    app.mainloop()
    