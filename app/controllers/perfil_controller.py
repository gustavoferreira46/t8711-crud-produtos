from app.models.perfil import Perfil


class Perfil_Controller:

    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.perfil_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome, descricao = self.view.ler_dados_perfil()
            perfil = Perfil(
                None,
                nome,
                descricao
            )
            self.dao.save(perfil)
            self.get_all()
            self.view.exibir_mensagem("Perfil cadastrado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao salvar os dados: {str(e)}", False)

    def get_all(self):
        perfis = self.dao.get_all()
        self.view.exibir_perfis(perfis)

    def selecionar_perfil(self, event):
        try:
            id_perfil = self.view.get_id_selecionado()
            self.perfil_selecionado = self.dao.get_by_id(
                id_perfil
            )
            self.view.preencher_campos(
                self.perfil_selecionado
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.perfil_selecionado is None:
                self.view.exibir_mensagem("Selecione um perfil na lista.", False)
                return
            nome, descricao = self.view.ler_dados_perfil()
            self.perfil_selecionado.atualizar_dados(nome, descricao)
            self.dao.update(self.perfil_selecionado)
            self.get_all()
            self.view.exibir_mensagem("Perfil atualizado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao salvar os dados: {str(e)}", False)

    def delete(self):
        if self.perfil_selecionado is None:
            self.view.exibir_mensagem("Selecione um perfil na lista.", False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.perfil_selecionado.id)
            if sucesso:
                self.perfil_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Perfil excluído com sucesso!")
            else:
                self.view.exibir_mensagem("Perfil não encontrado.", False)
        except Exception as e:
            self.view.exibir_mensagem("Problemas ao excluir perfil", False)