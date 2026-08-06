from app.models.cidade import Cidade

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



class Cidade_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._fornecedores = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("CRUD de Cidade")
        self.root.geometry("800x600")
        self.root.resizable(False, False)


    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = "Cadastro de Cidade",
            font = ("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 4,
            padx = 5,
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = "Dados da cidade"
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            padx = 10,
            pady = 5,
            sticky = "ew"
        )
        self.lbl_id = tk.Label(
            self.frm_dados,
            text = "ID:"
        )
        self.lbl_id.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width = 10,
            state = "readonly"
        )
        self.txt_id.grid(
            row = 0,
            column= 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text = "Nome:"
        )
        self.lbl_nome.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_nome.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_estados = tk.Label(
            self.frm_dados,
            text = "Estados:"
        )
        self.lbl_estados.grid(
            row = 1,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.cmb_estados = ttk.Combobox(
            self.frm_dados,
            width = 37,
            state = "readonly"
        )
        self.cmb_estados.grid(
            row = 1,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border = 2,
            relief = "groove"
        )
        self.frm_botoes.grid(
            row = 4,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 4,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text = "Novo",
            width = 15
        )
        self.btn_novo.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text = "Salvar",
            width = 15
        )
        self.btn_salvar.grid(
            row = 0,
            column = 1,
            padx = 5,
            pady = 5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text = "Alterar",
            width = 15
        )
        self.btn_alterar.grid(
            row = 0,
            column = 2,
            padx = 5,
            pady = 5
        )
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text = "Excluir",
            width = 15
        )
        self.btn_excluir.grid(
            row = 0,
            column = 3,
            padx = 5,
            pady = 5
        )
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text = "Fechar",
            width = 15
        )
        self.btn_fechar.grid(
            row = 0,
            column = 4,
            padx = 5,
            pady = 5
        )
        self.tbl_cidades = ttk.Treeview(
            self.root,
            height = 10

        )
        self.tbl_cidades.grid(
            row = 3,
            column = 0,
            columnspan = 4,
            padx = 10,
            sticky = "nsew"
        )
    def configurar_treeview(self):
        self.tbl_cidades["columns"] = (
                "id",
                "nome",
                
            )
        self.tbl_cidades.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_cidades.column(
            "id",
            width = 10
        )
        self.tbl_cidades.column(
            "nome",
            width = 50
        )
        self.tbl_cidades.heading(
            "id",
            text = "ID"
        )
        self.tbl_cidades.heading(
            "nome",
            text = "Nome"
        )
        
        
    def configurar_eventos(self):
        self.btn_novo.config(
            command = self.controller.new
        )
        self.btn_salvar.config(
            command = self.controller.save
        )
        self.btn_alterar.config(
            command = self.controller.update
        )
        self.btn_excluir.config(
            command = self.controller.delete
        )
        self.btn_fechar.config(
            command = self.fechar
        )
        self.tbl_cidades.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_cidade

        )
    def carregar_estado(self, estados):
        self._estados = estados
        valores = []
        for estado in estados:
            valores.append(
                f"{estado.id} - {estado.nome}"
            )
        self.cmb_estados["values"] = valores
        self.cmb_estados.set("")

    def preencher_campos(self, cidade):

        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(cidade.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_nome.insert(
            0,
            cidade.nome
        )

        self.txt_sigla.insert(
            0,
            str(cidade.nome)
        )
        
        for indice, estado in enumerate(self._estados):
            if estado.id == cidade.fornecedor.id:
                self.cmb_estados.current(indice)
                break

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome.delete(0, tk.END)
        

    def limpar_treeview(self):
        for item in self.tbl_cidades.get_children():
            self.tbl_cidades.delete(item)


    def get_id_selecionado(self):

        item = self.tbl_cidades.selection()[0]

        return self.tbl_cidades.item(item)["values"][0]

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir esta cidade?"
        )

    def ler_dados_produto(self):
        nome = self.txt_nome.get()
        indice = self.cmb_estados.current()
        if indice < 0:
            raise ValueError("Selecione um estado.")
        estado = self._estados[indice]
        return nome, estado

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(
                "Mini ERP",
                mensagem
            )
        else:
            messagebox.showerror(
                "Mini ERP",
                mensagem
            )
    def exibir_cidade(self, cidades):

        self.limpar_treeview()

        for cidade in cidades:

            self.tbl_cidade.insert(
                "",
                tk.END,
                values=(
                    cidade.id,
                    cidade.nome,
                    cidade.estado.nome
                )
            )

   
    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_cidades()
        self.controller.get_all()
        self.root.mainloop()


        