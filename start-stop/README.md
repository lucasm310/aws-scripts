Estes scritps tem como objetivo iniciar e desligar uma instancia na amazon web services

Para o correto funcionamento é necessario:

- python
- pip
- awscli
  - para instalar pode usar: *apt-get install awscli*
- boto3
  - para instalar pode usar: pip install boto3
- AWSAccessKeyId com permissoes para:
  - Ligar Instâncias
  - Desligar Instâncias
  - Criar snapshots
  - Deletar snapshots
  - Atualizar Records sets no Route53

Para configurar executar os comandos no terminal:
- **$** aws configure
  - Digitar a *AWSAccessKeyId*
  - Digitar a *AWSSecretKey*
  - Digitar a region da Instância
- **#** mkidr /var/log/script/aws-auto.log
- **#** chmod 777 /var/log/script/aws-auto.log
- **$** crontab -e
  - agendar conforme a necessidade e local dos scripts ex:
    - **0 6 * * * /script/start.py**
    - **0 19 * * * /script/stop.py**
