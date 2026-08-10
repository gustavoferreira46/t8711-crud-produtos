from app.models.perfil import Perfil


class Fornecedor_Perfil_DAO:

    def __init__(self, database):
        self._database = database

    def get_perfis_por_fornecedor(self, fornecedor):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:

            sql = """
                    SELECT
                        P.ID,
                        P.NOME,
                        P.DESCRICAO
                    FROM
                        PERFIL P
                    INNER JOIN
                        FORNECEDOR_PERFIL FP
                        ON FP.ID_PERFIL = P.ID
                    WHERE
                        FP.ID_FORNECEDOR = %s
                    ORDER BY
                        P.NOME
                  """

            cursor.execute(sql, (fornecedor.id,))

            registros = cursor.fetchall()

            perfis = []

            for registro in registros:

                perfis.append(
                    Perfil(
                        registro[0],
                        registro[1],
                        registro[2]
                    )
                )

            return perfis

        finally:
            self._database.desconectar(cursor, conexao)

    def substituir_perfis_do_fornecedor(self, fornecedor, perfis):

        conexao = self._database.conectar()
        cursor = conexao.cursor()

        try:

            cursor.execute(
                """
                    DELETE FROM FORNECEDOR_PERFIL
                    WHERE ID_FORNECEDOR = %s
                """,
                (fornecedor.id,)
            )

            for perfil in perfis:

                cursor.execute(
                    """
                        INSERT INTO FORNECEDOR_PERFIL
                        (
                            ID_FORNECEDOR,
                            ID_PERFIL
                        )
                        VALUES
                        (
                            %s,
                            %s
                        )
                    """,
                    (fornecedor.id, perfil.id)
                )

            conexao.commit()

        except Exception:
            conexao.rollback()
            raise

        finally:
            self._database.desconectar(cursor, conexao)