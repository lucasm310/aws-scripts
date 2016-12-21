#! /usr/bin/python
# -*- coding: utf-8 -*-
#Script para desligar um servidor da amazon automaticamente, cria uma rotina de backup de snapshot (deleta antiga - cria nova)
#versao: 0.1
#autor: Lucas Morais
#email: lucasmorais.dev@gmail.com

import	boto3
import logging
logging.basicConfig(filename='/var/log/script/aws-auto.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

id_instancia = #id da instancia para ser desligada
id_volume = #id do volume para criar snapshot


ec2 = boto3.resource('ec2')
servidor = ec2.Instance(id_instancia)
client = boto3.client('ec2')

response = client.describe_snapshots(
		DryRun=False,
		Filters=[{
			'Name' : 'description',
			'Values': [
				'bkp-aws-automatico'
			]
		}],
	)
try:
	snapshot_id = response['Snapshots'][0]['SnapshotId']
except:
	snapshot_id = None

if snapshot_id:
	deletar = client.delete_snapshot(
			DryRun=False,
			SnapshotId=snapshot_id
		)
	deletar_status = deletar['ResponseMetadata']['HTTPStatusCode']
	if deletar_status == '200':
		logging.info("Snapshot id: {0} deletada".format(snapshot_id))
	else:
		logging.info("Erro ao deletar snapshot")

criar_snap = client.create_snapshot(
    DryRun=False,
    VolumeId=id_volume,
    Description='bkp-aws-automatico'
)
try:
	status_criar = criar_snap['SnapshotId']
except:
	status_criar = None
if status_criar:
	logging.info("Snapshot id: {0} criada".format(status_criar))
else:
	logging.info("Erro ao criar snapshot")


resposta = servidor.stop(
		DryRun=False,
		Force=True
	)
try:
	status = resposta['StoppingInstances'][0]['CurrentState']['Name']
except:
	status = None

if status:
	logging.info("Servidor Desligado")
else:
	logging.info("Servidor não foi Desligado")
