#==========================================================================================

import smtplib # Para conectar-se ao servidor e enviar email
from email.mime.multipart import MIMEMultipart #Criar email com várias partes, texto, anexo, etc
from email.mime.text import MIMEText # Para colocar os textos dentros dos emails
import requests
from datetime import *


#==========================================================================================

api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

requisicao = requests.get(api)

requisicao_dic = requisicao.json()
cot_bitcoin = requisicao_dic["BTCBRL"]["bid"]

# data_atual = datetime.now()
# data_em_texto = datetime.strftime(data_atual, "%d/%m/%Y %H:%M") # Pega uma data/hora e transforma em texto;


# import pytz #Python timezone => tornar qqr data ciente do local dela. 
# # para saber qual sigla utilizar pesquise: "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"
# fuso_horario = pytz.timezone("America/Sao_Paulo") #UTC -> padrão 00h
# minha_data_com_fuso = fuso_horario.localize(data_atual) #dada minhda posição de greenwich
# conv_txt = str(minha_data_com_fuso)

texto = f"Cotação atualizada!\n\nData: \n\nValor da cotação: R$ {cot_bitcoin},00"


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

