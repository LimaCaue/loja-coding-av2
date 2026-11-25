# Roteiro para gravação — demonstração real (5 a 10 minutos)

Este arquivo é um guia; **não é o vídeo exigido**. Grave sua voz e a tela do terminal, com sua participação. Duração sugerida: 7 minutos. Confira o tempo final antes de entregar.

## 0:00–0:45 — Abertura

Apresente-se, diga que este é o projeto avaliativo de Coding (AV2), e explique o problema: controlar produtos e clientes de uma pequena loja em uma sessão de terminal.

## 0:45–1:30 — Estrutura e execução

Mostre `main.py` (interface e listas), `regras.py` (validação e CRUD), `test_regras.py` e `test_interface.py` (testes) e `README.md`. Execute `python main.py`.

## 1:30–3:10 — Produtos

Cadastre `C01`, `Caderno`, preço `15,90`, estoque `10`. Liste e consulte por `C01`. Altere nome, preço e estoque; consulte novamente. Tente repetir `C01`, usar preço `0` e estoque `-1`, explicando as mensagens de erro. Exclua `C01` com confirmação e mostre a lista vazia.

## 3:10–4:50 — Clientes

Cadastre `Ana`, `ana@exemplo.com`, telefone `83999999999`. Liste e consulte pelo e-mail. Altere nome e telefone; consulte novamente. Demonstre e-mail duplicado e e-mail sem `@`. Exclua a cliente com confirmação.

## 4:50–6:15 — Funcionamento interno e testes

Explique como as listas são passadas às funções, como `buscar_produto`/`buscar_cliente` identificam registros e como as alterações e exclusões afetam as listas. Rode `python -m unittest -v`. Feche e reabra o programa e mostre que os dados não persistem.

## 6:15–7:15 — GitHub e encerramento

Mostre o repositório público, a branch `main` e as branches `feature/`, `ci/` e `docs/`. Abra um Pull Request mesclado e mostre seus commits, o checklist preenchido e os testes do GitHub Actions aprovados. Cite os três prompts registrados no README, com o objetivo e o resultado de cada um. Finalize resumindo funcionalidades e limites: não há venda nem armazenamento permanente.

## Checklist antes da entrega

- [ ] Vídeo real gravado, com sua voz, imagem do terminal e duração entre 5 e 10 minutos.
- [ ] Testes demonstrados e CRUD das duas entidades visível.
- [ ] Branches, commits, Pull Requests e testes do GitHub Actions mostrados no GitHub.
- [ ] Link do repositório e link/arquivo do vídeo enviados na plataforma, conforme o método aceito pelo professor.
- [ ] Apresentação presencial preparada: você consegue explicar o código sem depender de leitura integral deste roteiro.
