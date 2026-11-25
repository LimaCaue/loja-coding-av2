"""Testes automatizados: execute python -m unittest -v."""

import unittest

from regras import (
    alterar_cliente, alterar_produto, buscar_cliente, buscar_produto,
    cadastrar_cliente, cadastrar_produto, excluir_cliente, excluir_produto,
)


class TesteProdutos(unittest.TestCase):
    def setUp(self):
        self.produtos = []

    def test_crud_produto(self):
        cadastrar_produto(self.produtos, "abc", "Caneta", "2,50", "10")
        self.assertEqual(buscar_produto(self.produtos, "ABC")["preco"], 2.5)
        alterar_produto(self.produtos, "abc", "Caneta azul", "3", "5")
        self.assertEqual(buscar_produto(self.produtos, "ABC")["estoque"], 5)
        excluir_produto(self.produtos, "abc")
        self.assertIsNone(buscar_produto(self.produtos, "ABC"))

    def test_codigo_duplicado(self):
        cadastrar_produto(self.produtos, "A", "Caneta", "2", "1")
        with self.assertRaises(ValueError):
            cadastrar_produto(self.produtos, "a", "Lápis", "1", "2")
        self.assertEqual(len(self.produtos), 1)

    def test_preco_e_estoque_invalidos(self):
        for preco, estoque in [("0", "1"), ("-1", "2"), ("nan", "1"),
                               ("inf", "1"), ("2", "-1"), ("2", "1.5")]:
            with self.subTest(preco=preco, estoque=estoque):
                with self.assertRaises(ValueError):
                    cadastrar_produto(self.produtos, "B", "Borracha", preco, estoque)
        self.assertEqual(self.produtos, [])

    def test_alteracao_invalida_nao_muda_produto(self):
        cadastrar_produto(self.produtos, "A", "Caneta", "2", "1")
        with self.assertRaises(ValueError):
            alterar_produto(self.produtos, "A", "Outro", "0", "3")
        self.assertEqual(self.produtos[0]["nome"], "Caneta")

    def test_alterar_ou_excluir_produto_inexistente(self):
        cadastrar_produto(self.produtos, "A", "Caneta", "2", "1")
        with self.assertRaises(ValueError):
            alterar_produto(self.produtos, "Z99", "Lápis", "1", "1")
        with self.assertRaises(ValueError):
            excluir_produto(self.produtos, "Z99")
        self.assertEqual(len(self.produtos), 1)


class TesteClientes(unittest.TestCase):
    def setUp(self):
        self.clientes = []

    def test_crud_cliente(self):
        cadastrar_cliente(self.clientes, "Ana", "ANA@EXEMPLO.COM", "83999999999")
        self.assertEqual(buscar_cliente(self.clientes, "ana@exemplo.com")["nome"], "Ana")
        alterar_cliente(self.clientes, "ANA@EXEMPLO.COM", "Ana Silva", "8333333333")
        self.assertEqual(self.clientes[0]["telefone"], "8333333333")
        excluir_cliente(self.clientes, "ana@exemplo.com")
        self.assertIsNone(buscar_cliente(self.clientes, "ana@exemplo.com"))

    def test_email_duplicado_ou_invalido(self):
        cadastrar_cliente(self.clientes, "Ana", "ana@exemplo.com", "123")
        for email in ("ANA@EXEMPLO.COM", "sem-arroba"):
            with self.subTest(email=email):
                with self.assertRaises(ValueError):
                    cadastrar_cliente(self.clientes, "Bia", email, "456")
        self.assertEqual(len(self.clientes), 1)

    def test_campos_obrigatorios(self):
        with self.assertRaises(ValueError):
            cadastrar_cliente(self.clientes, " ", "teste@exemplo.com", "123")
        with self.assertRaises(ValueError):
            cadastrar_cliente(self.clientes, "Teste", "teste@exemplo.com", " ")

    def test_alterar_ou_excluir_cliente_inexistente(self):
        cadastrar_cliente(self.clientes, "Ana", "ana@exemplo.com", "83999999999")
        with self.assertRaises(ValueError):
            alterar_cliente(self.clientes, "outro@exemplo.com", "Bia", "83988888888")
        with self.assertRaises(ValueError):
            excluir_cliente(self.clientes, "outro@exemplo.com")
        self.assertEqual(len(self.clientes), 1)


if __name__ == "__main__":
    unittest.main()
