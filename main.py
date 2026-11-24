"""Interface de terminal da loja (sem persistência em arquivos)."""

from regras import (
    alterar_cliente,
    alterar_produto,
    buscar_cliente,
    buscar_produto,
    cadastrar_cliente,
    cadastrar_produto,
    excluir_cliente,
    excluir_produto,
)


def formatar_preco(valor):
    """Mostra valores em reais com vírgula decimal."""
    inteiro, centavos = f"{valor:.2f}".split(".")
    return f"R$ {inteiro},{centavos}"


def mostrar_produto(produto):
    print(f"Código: {produto['codigo']} | Nome: {produto['nome']} | "
          f"Preço: {formatar_preco(produto['preco'])} | Estoque: {produto['estoque']}")


def mostrar_cliente(cliente):
    print(f"Nome: {cliente['nome']} | E-mail: {cliente['email']} | "
          f"Telefone: {cliente['telefone']}")


def menu_produtos(produtos):
    while True:
        print("\n=== PRODUTOS ===\n1. Cadastrar\n2. Listar\n3. Consultar por código"
              "\n4. Alterar\n5. Excluir\n0. Voltar")
        opcao = input("Escolha: ").strip()
        try:
            if opcao == "0":
                return
            if opcao == "1":
                produto = cadastrar_produto(produtos, input("Código: "), input("Nome: "),
                                            input("Preço (ex.: 19,90): "), input("Estoque: "))
                print("Produto cadastrado:")
                mostrar_produto(produto)
            elif opcao == "2":
                if not produtos:
                    print("Nenhum produto cadastrado.")
                for produto in produtos:
                    mostrar_produto(produto)
            elif opcao == "3":
                produto = buscar_produto(produtos, input("Código: "))
                mostrar_produto(produto) if produto else print("Produto não encontrado.")
            elif opcao == "4":
                codigo = input("Código do produto: ")
                produto = buscar_produto(produtos, codigo)
                if produto is None:
                    print("Produto não encontrado.")
                    continue
                mostrar_produto(produto)
                print("Preencha os novos dados (código permanece igual).")
                produto = alterar_produto(produtos, codigo, input("Novo nome: "),
                                          input("Novo preço: "), input("Novo estoque: "))
                print("Produto alterado:")
                mostrar_produto(produto)
            elif opcao == "5":
                codigo = input("Código do produto: ")
                produto = buscar_produto(produtos, codigo)
                if produto is None:
                    print("Produto não encontrado.")
                elif input(f"Excluir {produto['nome']}? (s/n): ").strip().lower() == "s":
                    excluir_produto(produtos, codigo)
                    print("Produto excluído.")
                else:
                    print("Exclusão cancelada.")
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Erro: {erro}")


def menu_clientes(clientes):
    while True:
        print("\n=== CLIENTES ===\n1. Cadastrar\n2. Listar\n3. Consultar por e-mail"
              "\n4. Alterar\n5. Excluir\n0. Voltar")
        opcao = input("Escolha: ").strip()
        try:
            if opcao == "0":
                return
            if opcao == "1":
                cliente = cadastrar_cliente(clientes, input("Nome: "), input("E-mail: "),
                                            input("Telefone: "))
                print("Cliente cadastrado:")
                mostrar_cliente(cliente)
            elif opcao == "2":
                if not clientes:
                    print("Nenhum cliente cadastrado.")
                for cliente in clientes:
                    mostrar_cliente(cliente)
            elif opcao == "3":
                cliente = buscar_cliente(clientes, input("E-mail: "))
                mostrar_cliente(cliente) if cliente else print("Cliente não encontrado.")
            elif opcao == "4":
                email = input("E-mail do cliente: ")
                cliente = buscar_cliente(clientes, email)
                if cliente is None:
                    print("Cliente não encontrado.")
                    continue
                mostrar_cliente(cliente)
                print("Preencha os novos dados (e-mail permanece igual).")
                cliente = alterar_cliente(clientes, email, input("Novo nome: "),
                                          input("Novo telefone: "))
                print("Cliente alterado:")
                mostrar_cliente(cliente)
            elif opcao == "5":
                email = input("E-mail do cliente: ")
                cliente = buscar_cliente(clientes, email)
                if cliente is None:
                    print("Cliente não encontrado.")
                elif input(f"Excluir {cliente['nome']}? (s/n): ").strip().lower() == "s":
                    excluir_cliente(clientes, email)
                    print("Cliente excluído.")
                else:
                    print("Exclusão cancelada.")
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Erro: {erro}")


def main():
    produtos = []
    clientes = []
    print("Bem-vindo ao sistema da loja!")
    while True:
        print("\n=== LOJA ===\n1. Produtos\n2. Clientes\n0. Sair")
        try:
            opcao = input("Escolha: ").strip()
            if opcao == "1":
                menu_produtos(produtos)
            elif opcao == "2":
                menu_clientes(clientes)
            elif opcao == "0":
                print("Até logo! Os dados desta sessão foram descartados.")
                return
            else:
                print("Opção inválida.")
        except (EOFError, KeyboardInterrupt):
            print("\nSessão encerrada. Os dados não foram salvos.")
            return


if __name__ == "__main__":
    main()
