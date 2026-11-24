"""Testes da apresentação de dados no terminal."""

import contextlib
import io
import unittest

from main import formatar_preco, mostrar_produto


class TesteInterface(unittest.TestCase):
    def test_preco_em_reais(self):
        self.assertEqual(formatar_preco(15.9), "R$ 15,90")
        self.assertEqual(formatar_preco(2), "R$ 2,00")

    def test_produto_apresenta_preco_formatado(self):
        saida = io.StringIO()
        with contextlib.redirect_stdout(saida):
            mostrar_produto({"codigo": "C01", "nome": "Caderno", "preco": 15.9, "estoque": 10})
        self.assertIn("Preço: R$ 15,90", saida.getvalue())
        self.assertIn("Estoque: 10", saida.getvalue())


if __name__ == "__main__":
    unittest.main()
