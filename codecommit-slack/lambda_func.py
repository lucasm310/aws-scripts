# Funcao aws lambda para enviar notificacao para o slack quando o codecommit receber um novo commit
# Autor: Lucas Augusto de Morais
# Email: lucasmorais.dev@gmail.com

import boto3
import json
from botocore.vendored import requests

codecommit = boto3.client('codecommit')
commits = []

print('Loading function')

def lambda_handler(event, context):
	for reference in event['Records'][0]['codecommit']['references']:
		commits.append(reference['commit'])
	repositorio = event['Records'][0]['eventSourceARN'].split(':')[5]
	info = codecommit.get_commit(repositoryName=repositorio,commitId=commits[0])

	autorNome = info['commit']['author']['name']
	autorEmail = info['commit']['author']['email']
	messagemCommit = info['commit']['message']

	mensagem = f"Novo Commit.\n Repositório: `{repositorio}`, Autor: {autorNome}, {autorEmail}\n Comentario: {messagemCommit}"

	corpo = {
		'text': mensagem
	}
        #url = *** Link do webhook criado no slack para o recebimento de mensagens ***
	r = requests.post(url,json=corpo)
	print(r)
