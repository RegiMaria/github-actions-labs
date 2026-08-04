# GitHub Actions Labs

Repositório de estudo prático de GitHub Actions. Cada lab isola um conceito - estrutura de workflow, jobs, variáveis, secrets, deploy - com o passo a passo documentado e o porquê de cada decisão.

## Baseado no curso

Este material acompanha o curso **[GitHub Actions: Guia Completo - Do Zero ao Deploy](https://www.udemy.com/course/github-actions-guia-completo-do-zero-ao-deploy/)**, do instrutor **Ieso**, na Udemy.

Os labs aqui são minhas anotações e experimentações práticas em cima do conteúdo do curso, não uma cópia do material oficial. Recomendo fortemente fazer o curso original pra ter o contexto completo de cada aula.

## Como usar este repositório

1. Clone o repositório
2. Cada lab tem seu próprio arquivo de workflow em `.github/workflows/`
3. Siga o passo a passo de cada lab (na seção correspondente abaixo ou no arquivo `labs/lab-XX.md`, se houver)
4. Depois do `git push`, acompanhe a execução na aba **Actions** do seu fork/repositório

## Índice de Labs

| Lab | Tópico | Workflow | Status |
|---|---|---|---|
| 01 | Estrutura de diretórios e arquivos, elementos obrigatórios (`name`, `on`, `jobs`), variáveis de ambiente | [`lab-01.yaml`](.github/workflows/lab-01.yaml) | ✅ |
| 02 | *(a definir)* | — | ⬜ |
| 03 | *(a definir)* | — | ⬜ |
| 04 | *(a definir)* | — | ⬜ |
| 05 | *(a definir)* | — | ⬜ |

> Vou atualizando essa tabela conforme avanço nos labs. Cada linha aponta pro arquivo de workflow correspondente.

## Requisitos

- Conta no GitHub
- Repositório próprio (fork ou novo repo) pra testar os workflows na prática, Actions só roda em repositórios de verdade, não dá pra simular localmente sem ferramentas extras (tipo [act](https://github.com/nektos/act))

## Créditos

- Curso: [GitHub Actions: Guia Completo - Do Zero ao Deploy](https://www.udemy.com/course/github-actions-guia-completo-do-zero-ao-deploy/) - Ieso (Udemy)

- Anotações e labs práticos: elaborados por mim durante o estudo do curso
