# Sistema de Loja — Projeto Avaliativo de Coding (AV2)

Sistema simples de gerenciamento de **produtos e clientes**, desenvolvido em Python para funcionar exclusivamente no terminal. Seu objetivo é organizar o cadastro e a consulta de informações de uma pequena loja durante uma sessão de uso.

## Funcionalidades

- Produtos: cadastrar, listar, consultar pelo código, alterar nome/preço/estoque e excluir.
- Clientes: cadastrar, listar, consultar pelo e-mail, alterar nome/telefone e excluir.
- Validações: códigos e e-mails não podem se repetir; campos não podem ficar vazios; e-mail deve ter formato básico válido; preço deve ser numérico, finito e maior que zero; estoque deve ser inteiro não negativo; exclusões exigem confirmação.

Os códigos dos produtos e e-mails dos clientes são identificadores e **não são alterados**. Para mudá-los, exclua o registro e cadastre novamente. O preço é arredondado a duas casas decimais; este projeto não implementa vendas nem pagamentos.

## Como executar

Requer Python 3.8 ou superior. Não é preciso instalar bibliotecas externas.

```bash
python main.py
```

No Windows, se `python` não funcionar, tente `py main.py`. Escolha `1` para produtos, `2` para clientes e `0` para sair. Em cada submenu, use as opções de cadastro, listagem, consulta, alteração ou exclusão. Exemplo: cadastre o produto de código `C01`, nome `Caderno`, preço `15,90` e estoque `10`. Depois, consulte-o por `C01`.

**Importante:** os dados são guardados somente em listas Python na memória. Ao fechar o programa, tudo é perdido. Não são utilizados arquivos, banco de dados, interface gráfica ou frameworks web.

## Organização

- `main.py`: menus, entrada e saída pelo terminal com `input()` e `print()`; contém as listas de produtos e clientes da sessão.
- `regras.py`: funções de CRUD, busca e validação das regras de negócio.
- `test_regras.py`: testes automatizados das operações e validações.
- `ROTEIRO_VIDEO.md`: guia para a gravação real da demonstração de 5 a 10 minutos.

Para executar os testes:

```bash
python -m unittest -v
```

## Uso de IA durante o desenvolvimento

**Prompt 1 — Planejamento e estruturação do sistema**

Estou desenvolvendo um projeto acadêmico em Python para a disciplina de Coding, cujo objetivo é criar um sistema de gerenciamento de uma loja. O sistema deverá funcionar exclusivamente pelo terminal, utilizando funções e listas para armazenamento dos dados em memória.

Sugira uma estrutura de organização do código em módulos, considerando as funcionalidades de cadastro, consulta, alteração e exclusão de produtos e clientes. Utilize conceitos básicos de programação em Python e priorize uma estrutura de fácil compreensão e manutenção.

**Prompt 2 — Regras de negócio e validação de dados**

Considerando um sistema de gerenciamento de loja desenvolvido em Python, quais regras de negócio e validações devem ser aplicadas nas operações de cadastro, consulta, alteração e exclusão de produtos e clientes?

Considere situações como campos obrigatórios, registros duplicados, preços negativos, quantidades inválidas em estoque e tentativas de alteração ou exclusão de registros inexistentes. Apresente exemplos utilizando funções, listas e estruturas condicionais em Python.

**Prompt 3 — Revisão de código e testes**

Analise o código-fonte do nosso sistema de gerenciamento de loja em Python, verificando possíveis erros de lógica, repetição de código, problemas de organização e falhas nas validações.

Sugira melhorias que respeitem os requisitos do projeto acadêmico, mantendo a execução pelo terminal e o armazenamento exclusivamente em listas. Apresente também cenários de teste para verificar o funcionamento das operações de cadastro, consulta, alteração e exclusão de produtos e clientes. Explique as sugestões sem alterar diretamente o código original.

## Entrega e colaboração

Repositório público: https://github.com/LimaCaue/loja-coding-av2 . O projeto está sendo desenvolvido individualmente. O histórico público do GitHub documenta as contribuições realizada.
