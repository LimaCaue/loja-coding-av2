"""Validações e operações da loja. Os dados vivem apenas em listas na memória."""

import math
import re


def validar_texto(valor, campo):
    valor = valor.strip()
    if not valor:
        raise ValueError(f"{campo} não pode ficar vazio.")
    return valor


def validar_email(email):
    email = validar_texto(email, "E-mail").lower()
    if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
        raise ValueError("Informe um e-mail válido.")
    return email


def validar_preco(preco):
    try:
        valor = float(str(preco).replace(",", "."))
    except ValueError as erro:
        raise ValueError("O preço deve ser um número.") from erro
    if not math.isfinite(valor) or valor <= 0:
        raise ValueError("O preço deve ser maior que zero e finito.")
    return round(valor, 2)


def validar_estoque(estoque):
    try:
        valor = int(str(estoque))
    except ValueError as erro:
        raise ValueError("O estoque deve ser um número inteiro.") from erro
    if valor < 0:
        raise ValueError("O estoque não pode ser negativo.")
    return valor


def buscar_produto(produtos, codigo):
    return next((p for p in produtos if p["codigo"] == codigo.strip().upper()), None)


def cadastrar_produto(produtos, codigo, nome, preco, estoque):
    codigo = validar_texto(codigo, "Código").upper()
    nome = validar_texto(nome, "Nome")
    preco = validar_preco(preco)
    estoque = validar_estoque(estoque)
    if buscar_produto(produtos, codigo):
        raise ValueError("Já existe um produto com esse código.")
    produto = {"codigo": codigo, "nome": nome, "preco": preco, "estoque": estoque}
    produtos.append(produto)
    return produto


def alterar_produto(produtos, codigo, nome, preco, estoque):
    produto = buscar_produto(produtos, codigo)
    if produto is None:
        raise ValueError("Produto não encontrado.")
    nome = validar_texto(nome, "Nome")
    preco = validar_preco(preco)
    estoque = validar_estoque(estoque)
    produto.update(nome=nome, preco=preco, estoque=estoque)
    return produto


def excluir_produto(produtos, codigo):
    produto = buscar_produto(produtos, codigo)
    if produto is None:
        raise ValueError("Produto não encontrado.")
    produtos.remove(produto)
    return produto


def buscar_cliente(clientes, email):
    return next((c for c in clientes if c["email"] == email.strip().lower()), None)


def cadastrar_cliente(clientes, nome, email, telefone):
    nome = validar_texto(nome, "Nome")
    email = validar_email(email)
    telefone = validar_texto(telefone, "Telefone")
    if buscar_cliente(clientes, email):
        raise ValueError("Já existe um cliente com esse e-mail.")
    cliente = {"nome": nome, "email": email, "telefone": telefone}
    clientes.append(cliente)
    return cliente


def alterar_cliente(clientes, email, nome, telefone):
    cliente = buscar_cliente(clientes, email)
    if cliente is None:
        raise ValueError("Cliente não encontrado.")
    nome = validar_texto(nome, "Nome")
    telefone = validar_texto(telefone, "Telefone")
    cliente.update(nome=nome, telefone=telefone)
    return cliente


def excluir_cliente(clientes, email):
    cliente = buscar_cliente(clientes, email)
    if cliente is None:
        raise ValueError("Cliente não encontrado.")
    clientes.remove(cliente)
    return cliente
