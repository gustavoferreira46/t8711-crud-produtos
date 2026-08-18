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

            # Tela de Cidades
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

            # Tela de Categorias
            "categoria.janela": "CRUD de Categorias",
            "categoria.cadastro": "Cadastro de Categorias",
            "categoria.dados": "Dados da categoria",
            "categoria.confirmacao": "Deseja realmente excluir esta categoria?",
            "categoria.cadastrada_sucesso": "Categoria cadastrada com sucesso!",
            "categoria.selecionar": "Selecione uma categoria na lista",
            "categoria.atualizada_sucesso": "Categoria atualizada com sucesso!",
            "categoria.excluida_sucesso": "Categoria excluída com sucesso!",
            "categoria.nao_encontrada": "Categoria não encontrada",
            "categoria.problemas": "Problemas ao excluir categoria",

            # Fornecedor categoria
            "fcategoria.janela": "Categorias de ",
            "fcategoria.instrucao": "Clique para marcar/desmarcar as categorias deste fornecedor:",

            # Tela de Fornecedores
            "fornecedor.janela": "CRUD de Fornecedores",
            "fornecedor.titulo": "Cadastro de Fornecedores",
            "fornecedor.dados": "Dados do fornecedor",
            "fornecedor.razao_social": "Razão social:",
            "fornecedor.nome_fantasia": "Nome fantasia:",
            "fornecedor.cnpj": "CNPJ:",
            "fornecedor.sla": "SLA de atendimento:",
            "fornecedor.categorias": "Categorias",
            "fornecedor.confirmar_exclusao": "Deseja realmente excluir este fornecedor?",
            "fornecedor.sucesso": "Mini ERP",
            "fornecedor.razao_social_coluna": "Razão Social",
            "fornecedor.cnpj_coluna": "CNPJ",

            # Controller de Fornecedores
            "fornecedor.cadastrado_sucesso": "Fornecedor cadastrado com sucesso!",
            "fornecedor.entrada_invalida": "Erro: Entrada inválida. Tente novamente.",
            "fornecedor.selecionar": "Selecione um fornecedor na lista.",
            "fornecedor.atualizado_sucesso": "Fornecedor atualizado com sucesso!",
            "fornecedor.excluido_sucesso": "Fornecedor excluído com sucesso!",
            "fornecedor.nao_encontrado": "Fornecedor não encontrado.",
            "fornecedor.problemas": "Problemas ao excluir fornecedor",
            "fornecedor.cadastrar_categorias": "Cadastre categorias antes de associá-las a um fornecedor.",
            "fornecedor.categorias_atualizadas_sucesso": "Categorias do fornecedor atualizadas com sucesso!",
            "fornecedor.categorias_erro": "Não foi possível salvar as categorias do fornecedor.",

            # Perfil
            "perfil.janela": "CRUD de Perfis",
            "perfil.titulo": "Cadastro de Perfis",
            "perfil.dados": "Dados do perfil",
            "perfil.descricao": "Descrição",
            "perfil.fornecedores": "Fornecedores",
            "perfil.confirmar_exclusao": "Deseja realmente excluir este perfil?",
            "perfil.cadastrado_sucesso": "Perfil cadastrado com sucesso!",
            "perfil.selecionar": "Selecione um perfil na lista.",
            "perfil.atualizado_sucesso": "Perfil atualizado com sucesso!",
            "perfil.excluido_sucesso": "Perfil excluído com sucesso!",
            "perfil.nao_encontrado": "Perfil não encontrado.",
            "perfil.problemas": "Problemas ao excluir perfil",
            "perfil.cadastrar_fornecedores": "Cadastre fornecedores antes de associá-los a um perfil.",
            "perfil.id_coluna": "ID",
            "perfil.nome_coluna": "Nome",
            "perfil.descricao_coluna": "Descrição",

            # Perfil fornecedor
            "perfil_fornecedor.janela": "Fornecedores do perfil",
            "perfil_fornecedor.titulo": "Fornecedores do perfil",
            "perfil_fornecedor.instrucao": "Clique para marcar/desmarcar os fornecedores deste perfil:",
            "perfil_fornecedor.sucesso": "Mini ERP",
            "perfil_fornecedor.atualizados_sucesso": "Fornecedores do perfil atualizados com sucesso!",
            "perfil_fornecedor.erro": "Não foi possível salvar os fornecedores do perfil.",
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

            # Cities screen
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

            # Categories screen
            "categoria.janela": "Category CRUD",
            "categoria.cadastro": "Category registration",
            "categoria.dados": "Category data",
            "categoria.confirmacao": "Do you really want to delete this category?",
            "categoria.cadastrada_sucesso": "Category successfully registered!",
            "categoria.selecionar": "Select a category from the list",
            "categoria.atualizada_sucesso": "Category successfully updated!",
            "categoria.excluida_sucesso": "Category successfully deleted!",
            "categoria.nao_encontrada": "Category not found",
            "categoria.problemas": "Problems deleting category",

            # Supplier category
            "fcategoria.janela": "Categories of ",
            "fcategoria.instrucao": "Click to mark/unmark this supplier's categories:",

            # Suppliers screen
            "fornecedor.janela": "Supplier CRUD",
            "fornecedor.titulo": "Supplier Registration",
            "fornecedor.dados": "Supplier data",
            "fornecedor.razao_social": "Company name:",
            "fornecedor.nome_fantasia": "Trade name:",
            "fornecedor.cnpj": "CNPJ:",
            "fornecedor.sla": "Service SLA:",
            "fornecedor.categorias": "Categories",
            "fornecedor.confirmar_exclusao": "Do you really want to delete this supplier?",
            "fornecedor.sucesso": "Mini ERP",
            "fornecedor.razao_social_coluna": "Company Name",
            "fornecedor.cnpj_coluna": "CNPJ",

            # Supplier Controller
            "fornecedor.cadastrado_sucesso": "Supplier registered successfully!",
            "fornecedor.entrada_invalida": "Error: Invalid input. Please try again.",
            "fornecedor.selecionar": "Select a supplier from the list.",
            "fornecedor.atualizado_sucesso": "Supplier updated successfully!",
            "fornecedor.excluido_sucesso": "Supplier deleted successfully!",
            "fornecedor.nao_encontrado": "Supplier not found.",
            "fornecedor.problemas": "Problems deleting supplier",
            "fornecedor.cadastrar_categorias": "Register categories before associating them with a supplier.",
            "fornecedor.categorias_atualizadas_sucesso": "Supplier categories updated successfully!",
            "fornecedor.categorias_erro": "Could not save the supplier categories.",

            # Profile
            "perfil.janela": "Profile CRUD",
            "perfil.titulo": "Profile Registration",
            "perfil.dados": "Profile data",
            "perfil.descricao": "Description",
            "perfil.fornecedores": "Suppliers",
            "perfil.confirmar_exclusao": "Do you really want to delete this profile?",
            "perfil.cadastrado_sucesso": "Profile registered successfully!",
            "perfil.selecionar": "Select a profile from the list.",
            "perfil.atualizado_sucesso": "Profile updated successfully!",
            "perfil.excluido_sucesso": "Profile deleted successfully!",
            "perfil.nao_encontrado": "Profile not found.",
            "perfil.problemas": "Problems deleting profile",
            "perfil.cadastrar_fornecedores": "Register suppliers before associating them with a profile.",
            "perfil.id_coluna": "ID",
            "perfil.nome_coluna": "Name",
            "perfil.descricao_coluna": "Description",

            # Profile supplier
            "perfil_fornecedor.janela": "Suppliers of profile",
            "perfil_fornecedor.titulo": "Suppliers of profile",
            "perfil_fornecedor.instrucao": "Click to mark/unmark the suppliers of this profile:",
            "perfil_fornecedor.sucesso": "Mini ERP",
            "perfil_fornecedor.atualizados_sucesso": "Profile suppliers updated successfully!",
            "perfil_fornecedor.erro": "Could not save the profile suppliers.",
        }
    }

    @classmethod
    def definir(cls, codigo):
        cls.ATUAL = codigo

    @classmethod
    def t(cls, chave):
        return cls.TEXTOS[cls.ATUAL].get(chave, chave)