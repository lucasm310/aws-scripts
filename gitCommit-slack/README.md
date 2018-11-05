Está é uma função lambda que tem como objetivo enviar notificações para o [slack](https://slack.com/), quando algum repósitório do [codecommit](https://aws.amazon.com/pt/getting-started/projects/migrate-git-repository/) receber um novo commit.

Para o correto funcionamento é necessario:

- Criar no slack um novo webhook para o recebimento das mensagens, o destino das mensagens pode ser tanto um contato ou um channel.
- Configurar no AWS lambda uma nova função, o conteudo da função é o script desta pasta.
- Setar os gatilhos para ativar a função lambda.
  - Os gatilhos neste caso são alterações do codecommit, então deve-se escolher quais repósitórios que irão ativar a função.


Documentações

- [AWS Lambda](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/welcome.html)
- [Webhooks Slack](https://api.slack.com/incoming-webhooks)