#! /usr/bin/python
# -*- coding: utf-8 -*-
#Script para ligar um servidor na amazon e atualizar automaticamente um subdominio com o ip publico do servidor
#versao: 0.1
#autor: Lucas Morais
#email: lucasmorais.dev@gmail.com

import	boto3
from time import sleep
import logging

logging.basicConfig(filename='/var/log/script/aws-auto.log',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

id_instancia = #id da instancia para ser ligada
id_zona_dns = #id da zona de dns para ser atualizada
subdns = #full subdns para ser atualizada
ec2 = boto3.resource('ec2')
servidor = ec2.Instance(id_instancia)
route53 = boto3.client('route53')

def update_dns(ip):
	response = route53.change_resource_record_sets(
	    HostedZoneId=id_zona_dns,
	    ChangeBatch={
	        'Changes': [
	            {
	                'Action': 'UPSERT',
	                'ResourceRecordSet': {
	                    'Name': subdns,
	                    'Type': 'A',
	                    'TTL': 300,
	                    'ResourceRecords': [
	                        {
	                            'Value': ip
	                        },
	                    ],
	                }
	            },
	        ]
	    }
	)
	status_dns = response['ChangeInfo']['Status']
	logging.info("Status DNS: {0}".format(status_dns))
	return status_dns

resposta = servidor.start(
		DryRun=False,
	)
start_status = resposta['StartingInstances'][0]['CurrentState']['Name']

if start_status == 'pending' or start_status == 'running':
	sleep(120)
	ip = servidor.public_ip_address
	update_dns(ip)
	logging.info("Servidor Iniciado IP: {0}".format(ip))
else: 
	logging.info("Erro ao iniciar o servidor")
