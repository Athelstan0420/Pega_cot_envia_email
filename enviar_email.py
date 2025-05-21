
#==========================================================================================
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from datetime import *
import os
import pytz
#==========================================================================================
api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
requisicao = requests.get(api)
requisicao_dic = requisicao.json()
cot_bitcoin = requisicao_dic["BTCBRL"]["bid"]
conv_str = str(cot_bitcoin)
fatiamento = conv_str[:3] + ',' + conv_str[3:] + ',00'
#==========================================================================================
data_atual = datetime.now()
fuso_horario = pytz.timezone("America/Sao_Paulo")
minha_data_com_fuso = fuso_horario.localize(data_atual)
conv_txt = str(minha_data_com_fuso)
#==========================================================================================
imagem = "https://cdn.investing.com/crypto-logos/20x20/v2/bitcoin.png"
#==========================================================================================
#==========================================================================================
texto_html = f"""
<!DOCTYPE html>
  <html lang="pt-br">
    <head>
      <meta charset="utf-8">
    </head>
    <body>
      <div>
        <div> 
          <hr>
          <h2> Olá! este email envia diariamente a cotação do bitcoin para você. <img src="{imagem}"> </h2>
          <hr>
          <ul>
            <li>
              <h3>Data de atualização:</h3>
              <ul>
                <li>
                  <p>{conv_txt[:19]} - {conv_txt[-5:]}</p>
                </li>
              </ul>
            </li>
            <li>
              <h3>Valor da cotação:</h3>
              <ul>
                <li>
                  <p><b>Bitcoin:</b> R${fatiamento}</p>
                </li>
                <li>                 
                  <a href="https://br.investing.com/crypto"><b>Para mais cotações clique AQUI</b></a>
                </li>
              </ul>
            </li>
          </ul> 
          <hr>
        </div> 
        <p>Atenciosamente,<br>Adriel Araújo</p>
      </div>
    </body>
  </html>
"""

# texto = f"Cotação atualizada!\n\nData: {conv_txt[:19]} - {conv_txt[-5:]} \n\nValor da cotação: R$ {fatiamento}"
# texto = {texto_html}

#==========================================================================================
#==========================================================================================

remetente = os.environ["EMAIL_REMETENTE"]
senha =  os.environ["EMAIL_SENHA"]
destinatario = os.environ["EMAIL_DESTINATARIO"]
assunto = "Atualizando a cotação: bitcoin" 

# Cria a mensagem com texto e anexo
mensagem = MIMEMultipart()
mensagem["from"] = remetente 
mensagem["to"] = destinatario
mensagem["subject"] = assunto
mensagem.attach(MIMEText(texto_html, 'html'))

# Envio do e-mail
servidor = smtplib.SMTP("smtp.gmail.com", 587)
servidor.starttls()
servidor.login(remetente, senha)
servidor.sendmail(remetente, destinatario, mensagem.as_string())
servidor.quit()
print("Enviado com sucesso!")

#==========================================================================================

