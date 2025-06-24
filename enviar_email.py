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

data_atual = datetime.now()
fuso_horario = pytz.timezone("America/Sao_Paulo")
minha_data_com_fuso = fuso_horario.localize(data_atual)
conv_txt = str(minha_data_com_fuso)

imagem = "https://cdn.investing.com/crypto-logos/20x20/v2/bitcoin.png"


texto_html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>Cotação Bitcoin</title>
</head>
<body>
  <div class="container">
    <div> 
      <hr>
        <h2 class="container pt-3 pb-3"> Olá! este email envia diariamente a cotação do bitcoin para você.
          <img src="https://cdn.investing.com/crypto-logos/20x20/v2/bitcoin.png">
        </h2>
      <hr>
      <ul class="container pt-3 pb-3">
        <li> 
          <h3 class="container"> Data de atualização: </h3>
          <ul>
              <li>
                  <p>{conv_txt[:19]} - {conv_txt[-5:]}</p>
              </li>
          </ul>
        </li>
        <li>
          <h3 class="container">Valor da cotação:</h3>
          <ul>
            <li>
                <p><b>Bitcoin:</b> R${fatiamento}</p>
            </li>
            <li>
              <p><b>Sobre Bitcoin:</b> 
                <a href="https://www.infomoney.com.br/guias/o-que-e-bitcoin/">https://www.infomoney.com.br/guias/o-que-e-bitcoin/</a>
              </p>
            </li>
            <li>                 
              <button style="background-color: black;">
                <a style="color: white;" href="https://br.investing.com/crypto"><b>Para mais cotações clique AQUI</b></a>
              </button>
            </li>
          </ul>
        </li>
        <br>
        <li>
          <h3>Sites - Notícias sobre economia:</h3>
            <ul>
              <li><a href="https://economia.uol.com.br/">https://economia.uol.com.br/</a></li>
              <li><a href="https://g1.globo.com/economia/">https://g1.globo.com/economia/</a></li>
              <li><a href="https://www.cnnbrasil.com.br/economia/">https://www.cnnbrasil.com.br/economia/</a></li>
              <li><a href="https://www.estadao.com.br/economia/">https://www.estadao.com.br/economia/</a></li>
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

remetente = "adrielmedeirosaraujo@gmail.com"
senha = 
destinatario = 
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
