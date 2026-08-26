# 📊 Análise de Dados Automatizada: Excel para E-mail

Este projeto em Python automatiza o processo de leitura de planilhas do Excel, realiza análises de dados e envia os resultados (como relatórios ou tabelas) diretamente por e-mail.

## 🚀 Funcionalidades

- **Leitura de Dados:** Importação automática de arquivos Excel (.xlsx).
- **Análise Estatística:** Cálculo de métricas como faturamento total, ticket médio e produtos mais vendidos usando `pandas`.
- **Disparo Automatizado:** Envio de e-mails formatados (em HTML) utilizando bibliotecas nativas ou integração com servidores SMTP.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas:** Para manipulação e análise dos dados.
- **Openpyxl:** Engine necessária para a leitura de arquivos Excel modernos.
- **Smtplib / Email:** Para a lógica de conexão com o servidor de e-mail e envio do conteúdo.

## 📦 Como Instalar e Rodar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com
cd NOME_DO_REPOSITORIO
```

### 2. Instalar as dependências
Abra o terminal do seu PyCharm e instale as bibliotecas necessárias:
```bash
pip install pandas openpyxl
```

### 3. Configurar as credenciais de e-mail
No código principal, certifique-se de configurar as suas variáveis de ambiente ou os campos correspondentes de forma segura:
- `EMAIL_REMETENTE`: O seu endereço de e-mail.
- `SENHA_REMETENTE`: A sua senha de app (no caso do Gmail/Outlook) para conexões SMTP.

### 4. Executar o script
```bash
python main.py
```

## 📁 Estrutura do Projeto

```text
├── dados/
│   └── planilha.xlsx       # Base de dados em Excel
├── main.py                 # Código principal (Análise e Envio)
├── README.md               # Documentação do projeto
└── .gitignore              # Arquivos ignorados pelo Git (ex: senhas e ambientes virtuais)
```

---
Desenvolvido com 💙 para automatizar tarefas repetitivas.
