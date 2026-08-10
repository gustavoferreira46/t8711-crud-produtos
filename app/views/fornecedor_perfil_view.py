import tkinter as tk
from tkinter import messagebox



class Fornecedor_Perfil_View:
    def __init__(
        self,
        root,
        controller,
        fornecedor,
        perfis_disponiveis
    ):
        self.root = root
        self.controller = controller
        self.fornecedor = fornecedor
        self._perfis = perfis_disponiveis
        self.configurar_janela()
        self.criar_componentes()
        self.preencher_lista()

    def configurar_janela(self):
        self.root.title(f"Perfis de {self.fornecedor.nome_fantasia}")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = f"Perfis de {self.fornecedor.nome_fantasia}",
            font = ("Arial", 12, "bold"),
            wraplength = 380
        )
        self.lbl_titulo.pack(
            padx = 10,
            pady = 10
        )
        self.lbl_instrucao = tk.Label(
            self.root,
            text = "Clique para marcar/desmarcar os perfis deste fornecedor:"
        )
        self.lbl_instrucao.pack(
            padx = 10,
            anchor = "w"
        )
        self.lst_perfis = tk.Listbox(
            self.root,
            selectmode = tk.MULTIPLE,
            height = 15
        )
        self.lst_perfis.pack(
            padx = 10,
            pady = 10,
            fill = "both",
            expand = True
        )
        self.frm_botoes = tk.Frame(
            self.root
        )
        self.frm_botoes.pack(
            pady = 10
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text = "Salvar",
            width = 15,
            command = self.salvar
        )
        self.btn_salvar.grid(
            row = 0,
            column = 0,
            padx = 5
        )
        self.btn_cancelar = tk.Button(
            self.frm_botoes,
            text = "Cancelar",
            width = 15,
            command = self.fechar
        )
        self.btn_cancelar.grid(
            row = 0,
            column = 1,
            padx = 5
        )

    def preencher_lista(self):

        ids_associados = []
        for perfil in self.fornecedor.perfis:
            ids_associados.append(perfil.id)

        for indice, perfil in enumerate(self._perfis):
            self.lst_perfis.insert(tk.END, perfil.nome)
            if perfil.id in ids_associados:
                self.lst_perfis.selection_set(indice)

    def salvar(self):

        indices_selecionados = self.lst_perfis.curselection()

        perfis_selecionados = []
        for indice in indices_selecionados:
            perfis_selecionados.append(self._perfis[indice])

        self.controller.salvar_perfis(
            self,
            self.fornecedor,
            perfis_selecionados
        )

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(
                "Mini ERP",
                mensagem,
                parent=self.root
            )
        else:
            messagebox.showerror(
                "Mini ERP",
                mensagem,
                parent=self.root
            )

    def fechar(self):
        self.root.destroy()