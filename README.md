# Sistema de Loja — Projeto Avaliativo de Coding (AV2)

[![Testes](https://github.com/LimaCaue/loja-coding-av2/actions/workflows/testes.yml/badge.svg)](https://github.com/LimaCaue/loja-coding-av2/actions/workflows/testes.yml)

Sistema simples de gerenciamento de **produtos e clientes**, desenvolvido em Python para funcionar exclusivamente no terminal. Seu objetivo é organizar o cadastro e a consulta de informações de uma pequena loja durante uma sessão de uso.

## Funcionalidades

- Produtos: cadastrar, listar, consultar pelo código, alterar nome/preço/estoque e excluir.
- Clientes: cadastrar, listar, consultar pelo e-mail, alterar nome/telefone e excluir.
- Validações: códigos e e-mails não podem se repetir; campos não podem ficar vazios; e-mail deve ter formato básico válido; telefone deve ter DDD e 8 ou 9 dígitos (espaços, parênteses e hífens são aceitos e removidos ao salvar); preço deve ser numérico, finito e maior que zero; estoque deve ser inteiro não negativo; exclusões exigem confirmação.

Os códigos dos produtos e e-mails dos clientes são identificadores e **não são alterados**. Para mudá-los, exclua o registro e cadastre novamente. O preço é arredondado a duas casas decimais e exibido em reais (ex.: `R$ 15,90`); este projeto não implementa vendas nem pagamentos.

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
- `test_interface.py`: testes da exibição de produtos e preços no terminal.
- `ROTEIRO_VIDEO.md`: guia para a gravação real da demonstração de 5 a 10 minutos.
- `.github/workflows/testes.yml`: executa os testes automaticamente no GitHub Actions.
- `.github/pull_request_template.md`: modelo com o checklist usado nos Pull Requests.

Para executar os testes:

```bash
python -m unittest -v
```

Os mesmos testes rodam automaticamente no GitHub Actions (Python 3.10 e 3.13) a cada push na `main` e em todo Pull Request. O resultado aparece na aba **Actions** e no selo do topo deste README.

## Uso de IA durante o desenvolvimento

**Prompt 1 — Planejamento e estruturação do sistema**

Estou desenvolvendo um projeto acadêmico em Python para a disciplina de Coding, cujo objetivo é criar um sistema de gerenciamento de uma loja. O sistema deverá funcionar exclusivamente pelo terminal, utilizando funções e listas para armazenamento dos dados em memória.

Sugira uma estrutura de organização do código em módulos, considerando as funcionalidades de cadastro, consulta, alteração e exclusão de produtos e clientes. Utilize conceitos básicos de programação em Python e priorize uma estrutura de fácil compreensão e manutenção.

- **Objetivo:** definir, antes de programar, como dividir o sistema em módulos e funções respeitando as restrições da atividade: uso só do terminal e dados em listas na memória.
- **Resultado:** o código foi separado em `main.py` (menus, `input()`/`print()` e listas da sessão) e `regras.py` (CRUD e validações), com uma função para cada operação de produtos e de clientes. Essa divisão permite testar as regras sem passar pelos menus.

**Prompt 2 — Regras de negócio e validação de dados**

Considerando um sistema de gerenciamento de loja desenvolvido em Python, quais regras de negócio e validações devem ser aplicadas nas operações de cadastro, consulta, alteração e exclusão de produtos e clientes?

Considere situações como campos obrigatórios, registros duplicados, preços negativos, quantidades inválidas em estoque e tentativas de alteração ou exclusão de registros inexistentes. Apresente exemplos utilizando funções, listas e estruturas condicionais em Python.

- **Objetivo:** levantar as regras de negócio coerentes com uma loja e entender como tratá-las com funções, listas e condicionais.
- **Resultado:** `regras.py` passou a validar campos obrigatórios, códigos e e-mails únicos, formato do e-mail, preço numérico maior que zero e estoque inteiro não negativo. Alterar ou excluir um registro inexistente gera mensagem de erro, e as exclusões pedem confirmação no menu.

**Prompt 3 — Revisão de código e testes**

Analise o código-fonte do nosso sistema de gerenciamento de loja em Python, verificando possíveis erros de lógica, repetição de código, problemas de organização e falhas nas validações.

Sugira melhorias que respeitem os requisitos do projeto acadêmico, mantendo a execução pelo terminal e o armazenamento exclusivamente em listas. Apresente também cenários de teste para verificar o funcionamento das operações de cadastro, consulta, alteração e exclusão de produtos e clientes. Explique as sugestões sem alterar diretamente o código original.

- **Objetivo:** revisar o código já escrito e planejar cenários de teste, recebendo explicações em vez de código pronto, para entender cada mudança antes de aplicá-la.
- **Resultado:** os cenários sugeridos viraram testes automatizados em `test_regras.py` e `test_interface.py` (CRUD, duplicidades, valores inválidos, registros inexistentes e exibição de preços). A revisão também levou à validação do telefone com DDD e à execução automática dos testes no GitHub Actions a cada Pull Request.

## Entrega e colaboração

Repositório público: https://github.com/LimaCaue/loja-coding-av2. O projeto está sendo desenvolvido individualmente. O histórico público do GitHub documenta as contribuições realizadas.

### Fluxo de trabalho no GitHub

1. Cada mudança é feita em uma branch própria criada a partir da `main`, com um prefixo que indica o tipo: `feature/` (funcionalidade), `ci/` (automação) ou `docs/` (documentação).
2. Os commits são pequenos e usam o mesmo padrão na mensagem: `feat`, `test`, `ci` ou `docs`, seguido de uma descrição curta.
3. A branch é enviada ao GitHub e integrada à `main` por um Pull Request, que segue o checklist do modelo do repositório e só é mesclado depois que os testes do GitHub Actions passam.
4. Depois da mesclagem, a `main` atualizada é o ponto de partida da próxima branch.
