# Pega_cot_envia_email

-----------------------------------------

Para fazer deploy do seu código:

-----------------------------------------

- Criar pasta: .github/workflows/agendar.yml

- Dentro do arq yml utilize essa estrutura:

      name: Executar script Python diariamente # nome que você dará; 
      
      on:
        schedule:
          - cron: '0 10 * * *'  # Executa todos os dias às 7h da manhã (horário de Brasília)
        workflow_dispatch:  # Permite rodar manualmente também
      
      jobs:
        run-script:
          runs-on: ubuntu-latest
      
          steps:
            - uses: actions/checkout@v4
      
            - name: Configurar Python
              uses: actions/setup-python@v5
              with:
                python-version: '3.x'
      
            - name: Instalar dependências
              run: pip install -r requirements.txt # adiciona o arq riquerements.txt
      
            - name: Executar script
              env:
                EMAIL_REMETENTE: ${{ secrets.EMAIL_REMETENTE }}
                EMAIL_SENHA: ${{ secrets.EMAIL_SENHA }}
                EMAIL_DESTINATARIO: ${{ secrets.EMAIL_DESTINATARIO }}
              run: python enviar_email.py

-----------------------------------------
- Para verificar quais libs incluídas no seu projeto que são necessárias para adicionar ao arquivo "riquerements.txt" para o deploy utilize a lib:

        - pip install pipreqs
    
- Em seguida vá até o diretório do projeto através do terminal:
  
        - cd /home/seu/projeto
  
- No terminal, dentro da pasta digite:
  
        - pipreqs . --force 
-----------------------------------------

- Para adicionar SEGREDOS E VARIÁVEIS:

      - No repositório do Github vá até SETTINGS/CONFIGURAÇÕES,
        em seguida vá até SEGREDOS E VARIÁVIES, lá você encontrará onde adicionar.
-----------------------------------------

