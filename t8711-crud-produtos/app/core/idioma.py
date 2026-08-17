class Idioma:

    ATUAL = "pt"

    TEXTOS = {
        "pt": {

            # Comuns a várias telas
            "comum.id": "ID",
            "comum.nome": "Nome",
            "comum.novo": "Novo",
            "comum.salvar": "Salvar",
            "comum.alterar": "Alterar",
            "comum.excluir": "Excluir",
            "comum.fechar": "Fechar",
            "comum.cancelar": "Cancelar",
            "comum.confirmacao": "Confirmação",
            "comum.erro_prefixo": "Erro: ",

            # Tela de Estados
            "estado.janela_titulo": "CRUD de Estados",
            "estado.titulo": "Cadastro de Estados",
            "estado.dados_frame": "Dados do estado",
            "estado.sigla": "Sigla",
            "estado.confirmar_exclusao": "Deseja realmente excluir este estado?",
            "estado.cadastrado_sucesso": "Estado cadastrado com sucesso!",
            "estado.atualizado_sucesso": "Estado atualizado com sucesso!",
            "estado.excluido_sucesso": "Estado excluído com sucesso!",
            "estado.nao_encontrado": "Estado não encontrado.",
            "estado.selecione_da_lista": "Selecione um estado na lista.",
            "estado.erro_ao_excluir": "Problemas ao excluir estado",
            "estado.erro_sigla_tamanho": "A sigla deve possuir exatamente 2 caracteres.",

            
            # Menu principal
            "menu.cadastros_basicos": "Cadastros básicos",
            "menu.estados": "Estados",
            "menu.cidades": "Cidades",
            "menu.acessos": "Acessos",
            "menu.usuarios": "Usuários",
            "menu.perfis": "Perfis",
            "menu.gestao_estoque": "Gestão de estoque",
            "menu.clientes": "Clientes",
            "menu.fornecedores": "Fornecedores",
            "menu.produtos": "Produtos",
            "menu.categorias": "Categorias",
            "menu.idioma": "Idioma",
            "menu.sair": "Sair",

            #Tela de Cidades
            "janela.cidade": "CRUD de cidades",
            "cadastro.cidades": "Cadastro de cidades",
            "dados.cidades": "Dados da cidade",
            "cidade.estado": "Estado",
            "cidade.confirmacao": "Confirmação",
            "cidade.excluir": "Deseja realmente excluir esta cidade?",
            "cidade.selecionar_estado": "Selecione um estado",
            "cidade.sucesso": "Mini ERP",
            "cidade.cadastro_sucesso": "Cidade cadastrada com sucesso!",
            "cidade.atualizada_sucesso": "Cidade atualizada com sucesso!",
            "cidade.selecionar": "Selecione uma cidade na lista.",
            "cidade.excluida_sucesso": "Cidade excluída com sucesso!",
            "cidade.nao_encotrada": "Cidade não encontrada",
            "cidade.problemas": "Problemas ao excluir cidade",

            #Tela de Categorias
            #view
            "categoria.janela": "CRUD de Categorias",
            "categoria.cadastro": "Cadastro de Categorias",
            "categoria.dados": "Dados da categoria",
            "categoria.confirmacao": "Deseja realmente excluir esta categoria?",
            #controller
            "categoria.cadastrada_sucesso": "Categoria cadastrada com sucesso!",
            "categoria.selecionar": "Selecione uma categoria na lista",
            "categoria.atualizada_sucesso": "Categoria atualizada com sucesso!",
            "categoria.excluida_sucesso": "Categoria excluída com sucesso!",
            "categoria.nao_encontrada": "Categoria não encontrada",
            "categoria.problemas": "Problemas ao excluir categoria",



        },
        "en": {

            # Common to several screens
            "comum.id": "ID",
            "comum.nome": "Name",
            "comum.novo": "New",
            "comum.salvar": "Save",
            "comum.alterar": "Edit",
            "comum.excluir": "Delete",
            "comum.fechar": "Close",
            "comum.cancelar": "Cancel",
            "comum.confirmacao": "Confirmation",
            "comum.erro_prefixo": "Error: ",

            # States screen
            "estado.janela_titulo": "State Management",
            "estado.titulo": "State Registration",
            "estado.dados_frame": "State data",
            "estado.sigla": "Abbreviation",
            "estado.confirmar_exclusao": "Do you really want to delete this state?",
            "estado.cadastrado_sucesso": "State registered successfully!",
            "estado.atualizado_sucesso": "State updated successfully!",
            "estado.excluido_sucesso": "State deleted successfully!",
            "estado.nao_encontrado": "State not found.",
            "estado.selecione_da_lista": "Select a state from the list.",
            "estado.erro_ao_excluir": "Problem deleting state",
            "estado.erro_sigla_tamanho": "The abbreviation must have exactly 2 characters.",

            # Main menu
            "menu.cadastros_basicos": "Basic registrations",
            "menu.estados": "States",
            "menu.cidades": "Cities",
            "menu.acessos": "Access",
            "menu.usuarios": "Users",
            "menu.perfis": "Roles",
            "menu.gestao_estoque": "Inventory management",
            "menu.clientes": "Customers",
            "menu.fornecedores": "Suppliers",
            "menu.produtos": "Products",
            "menu.categorias": "Categories",
            "menu.idioma": "Language",
            "menu.sair": "Exit",

            #Cities screen
            "janela.cidade": "City CRUD",
            "cadastro.cidades": "City registration",
            "dados.cidades": "City data",
            "cidade.estado": "State",
            "cidade.confirmacao": "Confirmation",
            "cidade.excluir": "Do you really want to delete this city?",
            "cidade.selecionar_estado": "Select a state",
            "cidade.sucesso": "Mini ERP",
            "cidade.cadastro_sucesso": "City successfully registered!",
            "cidade.atualizada_sucesso": "City successfully updated!",
            "cidade.selecionar": "Select a city from the list.",
            "cidade.excluida_sucesso": "City successfully deleted!",
            "cidade.nao_encotrada": "City not found",
            "cidade.problemas": "Problems deleting city",

            #Categories screen
            #view
            "categoria.janela": "Category CRUD",
            "categoria.cadastro": "Category registration",
            "categoria.dados": "Category data",
            "categoria.confirmacao": "Do you really want to delete this category?",
            #controller
            "categoria.cadastrada_sucesso": "Category successfully registered!",
            "categoria.selecionar": "Select a category from the list",
            "categoria.atualizada_sucesso": "Category successfully updated!",
            "categoria.excluida_sucesso": "Category successfully deleted!",
            "categoria.nao_encontrada": "Category not found",
            "categoria.problemas": "Problems deleting category",

        }
    }

    @classmethod
    def definir(cls, codigo):
        cls.ATUAL = codigo

    @classmethod
    def t(cls, chave):
        return cls.TEXTOS[cls.ATUAL].get(chave, chave)
