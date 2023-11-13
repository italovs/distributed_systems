# Trabalho 2 - Kafka e gRPC

- Implementação do trabalho
  - Kafka: Sensores
  - GRPC: Atuadores
  - Socket: Interface
  - Estrutura do projeto
  - Inicializando o projeto
- Formato das mensagens trocadas
- Linguagens utilizadas, frameworks e libs
 
## Implementação do trabalho

### Kafka

Criamos um arquivo Docker para inicializar o servidor Kafka. Acessamos o servidor através das portas expostas pelo Docker.

Utilizamos 3 **topics**, um para cada tipo de sensor. *Temperature, presence e luminosity*. A partir disso inicializamos 3 sensores que irão ficar responsáveis por enviar mensagens para o Kafka a cada um segundo com seus respectivos valores e são armazenados nos **topics** relacionados ao tipo do sensor.

### GRPC

Inicializamos os atuadores que irão ser servidores do **GRPC**. A partir disso, criamos clientes com o *servidor principal* para iteragir com esses atuadores. Os clients têm acesso às funções disponíveis nos servidores, o que permite a interação com eles(atuadores). 

Agora para exemplificar, todos os atuadores(servidores) possuem funções *turnOn e turnOff* as quais nos temos também nos clients para fazer a chamada remota.

### Socket

Utilizamos sockets nas iterações com o front-end, para receber e atualizar os valores em tempo real e para enviar requisição para o servidor principal afim de fazer uma comunicação com nossos atuadores.

### Estrutura do projeto

Seguimos a seguinte estura no nosso repositório:

- ``/actuators_servers/``: É onde está contido nossos atuadores(server);
- ``/app/sensors/``:  Onde ficam localizados os sensores;
- ``/app/assets/``: Ficamos os clients dos atuadores e os arquivos de definição proto;
- ``/app/__init_.py``: Onde inicializamos o servidor e as threads dos consumers;
- ``/app/home_assistant.py`` : Onde fica nosso arquivo de rotas e funcionalidades do servidor;
- ``docker-compose.yml``: Arquivo qual estamos iniciando o Kafka;
- ``requirements.txt``: Arquivo que contém as libs utilizadas.
 
### Inicialização

Para caso esteja utilizando **mac OS**, você pode utilizar o arquivo script ``start_script.sh`` para iniciar o projeto. Caso o contrário, faça os passos a seguir:

- Primeiro passo: Abrimos um terminal para rodar o Docker e ligarmos nosso servidor Kafka. ``docker compose up -d``;
- Segundo passo: Utilizaremos 3 novos terminais para iniciarmos os atuadores. ``python3 ./actuators_servers/{atuador}_server.py``;
- Terceiro passo: Utilizaremos 3 novos terminais para inciarmos os sensores. Iremos iniciar todos para exibir as informações para usuário. ``python3 app/sensors/{sensor}_sensor.py``
- Quarto passo: Assim que o terminal do Docker for liberado, utilize-o para inicializar o servidor flask. ``flask run``;


## Formato das menssagens trocadas

- Socket: utilizamos JSON;
- Kafka: Fazemos o encode utf-8 para enviar para Kafka e quando resgatavamos nos consumers fazemos o decode;
- GRPC: Recebemos e enviamos parâmetros utilizando o formato estabelecido no Protobuffer.

## Linguangens, frameworks e libs

- Linguagens: Python;
- Frameworks: Flask;
- Lib: GRPC, Flask-SocketIO, confluent_kafka.
