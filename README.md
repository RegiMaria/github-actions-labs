<p align="center">
  <img src="https://github.com/user-attachments/assets/9d13006c-edef-4a9f-8b3f-e378645e018b" width="120" alt="GitHub Actions Labs">
</p>

# GitHub Actions Labs

Repositório de estudo prático de GitHub Actions. Cada lab isola um conceito - estrutura de workflow, jobs, variáveis, secrets, deploy - com o passo a passo documentado e o porquê de cada decisão.

## Baseado no curso

Este material acompanha o curso **[GitHub Actions: Guia Completo - Do Zero ao Deploy](https://www.udemy.com/course/github-actions-guia-completo-do-zero-ao-deploy/)**, do instrutor **Ieso**, na Udemy.

- [Conteúdo teórico](https://devopsautomation.com.br/udemy/github-actions-automacao/modulo-01-fundamentos/devops-intro)
- [Laboratórios](https://github.com/iesodias/ghc-repo)

Os labs aqui são minhas anotações e experimentações práticas em cima do conteúdo do curso, não uma cópia do material oficial. Recomendo fortemente fazer o curso original pra ter o contexto completo de cada aula.

## Como usar este repositório

1. Clone o repositório
2. Cada lab tem seu próprio arquivo de workflow em `.github/workflows/`
3. Siga o passo a passo de cada lab (na seção correspondente abaixo ou no arquivo `labs/lab-XX.md`, se houver)
4. Depois do `git push`, acompanhe a execução na aba **Actions** do seu fork/repositório

## Índice de Labs

| Lab | Tópico | Workflow | Status |
|:---:|---|:---:|:---:|
| **01** | Estrutura de diretórios e arquivos; elementos obrigatórios (`name`, `on`, `jobs`); variáveis de ambiente | [`lab-01.yaml`](.github/workflows/lab-01.yaml) | ✅ |
| **02** | Eventos de trigger (`push` + `paths`, `workflow_dispatch` + `inputs`, `schedule`/cron); condicionais com `if:` | [`lab-02.yaml`](.github/workflows/lab-02.yaml) | ✅ |
| **03** | Jobs em paralelo e dependências (`needs`); `if: always()` | [`lab-03.yaml`](.github/workflows/lab-03.yaml) | ✅ |
| **04** | Permissões e `GITHUB_TOKEN`; princípio do menor privilégio (`permissions:`) | [`lab-04.yaml`](.github/workflows/lab-04.yaml) | ✅ |
| **05** | Variáveis, `vars`, `secrets` e `Environments` (dev/homologação/produção); precedência de `env` | [`lab-05.yaml`](.github/workflows/lab-05.yaml) | ✅ |
| **06** | Contextos e expressões (`github`, `runner`, `steps.outputs`, `matrix`); funções `toJSON`/`hashFiles` | [`lab-06.yaml`](.github/workflows/lab-06.yaml) | ✅ |

> Vou atualizando essa tabela conforme avanço nos labs. Cada linha aponta pro arquivo de workflow correspondente.

## Requisitos

- Conta no GitHub
- Repositório próprio (fork ou novo repo) pra testar os workflows na prática, Actions só roda em repositórios de verdade, não dá pra simular localmente sem ferramentas extras (tipo [act](https://github.com/nektos/act))

## Créditos

- Curso: [GitHub Actions: Guia Completo - Do Zero ao Deploy](https://www.udemy.com/course/github-actions-guia-completo-do-zero-ao-deploy/) - Ieso (Udemy)
- Anotações e labs práticos: elaborados por mim durante o estudo do curso
