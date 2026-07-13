# Enviando E-mails SMTP com Python
# Obs: Este conteúdo é antigo, então o que está informando aqui não condiz com as novas configurações do Google para configurações SMTP
# Foi usado o Gmail da Google para exemplo nesta aula
import os
import pathlib
import smtplib
from string import Template
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

CAMINHO_ARQUIVO_TEMPLATE = pathlib.Path(__file__).parent / 'template_email.html'

print(CAMINHO_ARQUIVO_TEMPLATE)

# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')

destinatario = remetente

# Configurações do servidor 

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smpt_user = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto

with open(CAMINHO_ARQUIVO_TEMPLATE, 'r') as arquivo:
    conteudo_arquivo = arquivo.read()
    template = Template(conteudo_arquivo)
    conteudo_email = template.substitute(nome="André")

# Transformar nosa mensagem em MIMEultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Conteúdo para o email'

corpo_email = MIMEText(conteudo_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Envia o e-mail
with smtplib.SMTP(smtp_server) as server:
    server.ehlo()
    server.starttls()
    server.login(smpt_user, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso')
