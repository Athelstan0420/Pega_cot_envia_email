#==========================================================================================

import smtplib # Para conectar-se ao servidor e enviar email
from email.mime.multipart import MIMEMultipart #Criar email com várias partes, texto, anexo, etc
from email.mime.text import MIMEText # Para colocar os textos dentros dos emails
import requests
from datetime import datetime
import os


#==========================================================================================

api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

requisicao = requests.get(api)

requisicao_dic = requisicao.json()
cot_bitcoin = requisicao_dic["BTCBRL"]["bid"]

texto = f"Cotação atualizada!\n\nData: {datetime.now()}\n\nValor da cotação: R$ {cot_bitcoin},00"

#==========================================================================================

remetente = os.environ["EMAIL_REMETENTE"]
senha =  os.environ["EMAIL_SENHA"]
destinatario = os.environ["EMAIL_DESTINATARIO"]
assunto = "Cotação Bitcoin"
corpo = f"{texto}"
#Preenchimento de campos na prática:
mensagem = MIMEMultipart()
mensagem["from"] = remetente 
mensagem["to"] = destinatario
mensagem["subject"] = assunto
mensagem.attach(MIMEText(corpo, 'plain'))
#Protocolo de envio:
servidor = smtplib.SMTP("smtp.gmail.com", 587)
servidor.starttls() #Entra no servidor;
servidor.login(remetente, senha) #Acessa o email;
servidor.sendmail(remetente, destinatario,mensagem.as_string())#Envia o email;
servidor.quit() #Fecha o servidor
print("Enviado com sucesso!")

