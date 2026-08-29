# 🐍 Projetos de Automação com Python

Este repositório reúne meus projetos de **automação desenvolvidos em Python**, criados com o objetivo de automatizar tarefas repetitivas, manipular dados, trabalhar com planilhas, gerar relatórios e otimizar processos.

Os projetos fazem parte do meu desenvolvimento prático em **Python, automação e análise de dados**, permitindo aplicar conceitos de programação na solução de problemas reais.

## 🚀 Projetos

### 📊 1. Análise de Dados Automatizada — Excel para E-mail

Automação responsável por ler dados de uma planilha Excel, realizar análises utilizando Python e enviar automaticamente os resultados por e-mail.

**Funcionalidades:**

* Leitura automática de arquivos Excel (`.xlsx`)
* Tratamento e análise de dados
* Cálculo de faturamento total
* Cálculo de ticket médio
* Identificação de produtos mais vendidos
* Geração de relatórios
* Envio automático dos resultados por e-mail
* Formatação do conteúdo do e-mail em HTML

**Tecnologias utilizadas:**

* Python
* Pandas
* Openpyxl
* Smtplib
* Email

---

## 🤖 Outras Automações

Este repositório será atualizado com novos projetos de automação em Python.

Alguns exemplos de projetos que poderão fazer parte do repositório:

* 📊 Automação de planilhas Excel
* 📧 Automação de envio de e-mails
* 📁 Organização automática de arquivos
* 📈 Geração automática de relatórios
* 🔎 Tratamento e análise de dados
* 🌐 Automação de tarefas na Web
* 🖥️ Automação de tarefas administrativas
* ⚙️ Scripts para otimização de processos

---

## 🛠️ Tecnologias e Bibliotecas

As principais tecnologias utilizadas nos projetos são:

* **Python 3.x**
* **Pandas** — manipulação e análise de dados
* **Openpyxl** — leitura e edição de arquivos Excel
* **Smtplib** — envio automatizado de e-mails
* **Email** — criação e formatação das mensagens
* Outras bibliotecas serão adicionadas conforme o desenvolvimento de novos projetos.

---

## 📦 Instalação

Clone este repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd NOME_DO_REPOSITORIO
```

Instale as dependências necessárias para o projeto que deseja executar:

```bash
pip install -r requirements.txt
```

Caso o projeto não possua um arquivo `requirements.txt`, consulte o README específico dentro da pasta do projeto.

---

## 📁 Estrutura do Repositório

```text
automacoes-python/
│
├── analise_excel_email/
│   ├── dados/
│   ├── main.py
│   └── README.md
│
├── projeto_02/
│   ├── main.py
│   └── README.md
│
├── projeto_03/
│   ├── main.py
│   └── README.md
│
├── .gitignore
├── requirements.txt
└── README.md
```

Cada projeto possui sua própria pasta para facilitar a organização, manutenção e documentação.

---

## 🔐 Segurança

Informações confidenciais, como senhas, tokens, chaves de API e credenciais de e-mail, **não devem ser armazenadas diretamente no código ou enviadas para o GitHub**.

Sempre que necessário, os projetos utilizarão variáveis de ambiente para armazenar essas informações de forma mais segura.

Exemplo:

```python
import os

email = os.getenv("EMAIL_REMETENTE")
senha = os.getenv("SENHA_REMETENTE")
```

Arquivos como `.env` devem ser adicionados ao `.gitignore`.

---

## 🎯 Objetivo

O objetivo deste repositório é construir um **portfólio de projetos de automação com Python**, demonstrando na prática conhecimentos em:

* Programação em Python
* Automação de processos
* Manipulação de arquivos
* Excel
* Análise e tratamento de dados
* Integração entre sistemas
* Desenvolvimento de soluções para problemas reais

---

## 📚 Em Desenvolvimento

Este repositório está em constante evolução.

Novas automações e melhorias serão adicionadas conforme avanço nos estudos e desenvolvimento de novos projetos.

---

## 👩‍💻 Autora

**Aparecida Dagda dos Santos**

Estudante de Ciência da Computação, com interesse em **Python, Automação, Análise de Dados e Tecnologia**.

⭐ Este repositório faz parte do meu portfólio de projetos e estudos em desenvolvimento de software.
