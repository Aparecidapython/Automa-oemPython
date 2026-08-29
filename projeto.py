import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

tabela_vendas = pd.read_excel('vendas.xlsx')
pd.set_option('display.max_columns', None)
print(tabela_vendas)
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)
produto = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(produto)
print('_' *50)
ticket_medio = (faturamento['Valor Final']/produto['Quantidade']).to_frame()

tabela_vendas = pd.read_excel('vendas.xlsx')
pd.set_option('display.max_columns', None)
print(tabela_vendas)
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)
produto = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(produto)
print('_' *50)
ticket_Médio = (faturamento['Valor Final']/produto['Quantidade']).to_frame()
ticket_Médio = ticket_Médio.rename(columns={0:'ticket_Médio'})
print(ticket_Médio)


# Configurações do servidor do Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_REMETENTE = "aparecidadagda@gmail.com"
SENHA_REMETENTE = "wutrmaxlnjxinhiw"  # Cole aqui a senha que você copiou (tudo junto, sem espaços)

# Configuração dos dados do e-mail
msg = MIMEMultipart()
msg['From'] = EMAIL_REMETENTE
msg['To'] = "cida.dagda1994@gmail.com"  # Altere para o e-mail de quem vai receber o teste
msg['Subject'] = "Relatorio de vendas por loja"

# Corpo do e-mail
corpo = f'''
<p>Prezados,</p>

<p>Segue o relatório de vendas por Loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{produto.to_html()}

<p>Ticket Médio dos Produto em cada Loja:</p>
{ticket_medio.to_html(formatters={'ticket Médio': 'R${:,.2f}'.format})}
            
<p>Qualquer dúvida estou a disposição</p>    
<p>Aparecida.</p>
'''
msg.attach(MIMEText(corpo, 'html'))

try:
    # Conectando com segurança ao servidor do Gmail
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_REMETENTE, SENHA_REMETENTE)

    # Realizando o envio
    server.sendmail(EMAIL_REMETENTE, msg['To'], msg.as_string())
    server.quit()
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao tentar enviar o e-mail: {e}")







