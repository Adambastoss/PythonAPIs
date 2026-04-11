##### Structure for creating docker file 

 1 - Preparar distro + instalação do python
 `FROM python:3.13`

 2 - Instalar dependências a nível de aplicação (pip install)
 `RUN pip install flask` OR 
 
 3 - Copiar a aplicação para o contexto da imagem
`RUN mkdir /app` > Criar pasta dentro do container
`COPY ./app.py /app` > Copiar a aplicação do dir local para dentro do container
`WORKDIR /app` > Quando o container for inicializado, o diretório raiz /app sobe de cara

 4 - Configurar porta de conexão da app (5000)
`EXPOSE 5000`

 5 - Executar comando para subir server flask
 `CMD flask run -h '0.0.0.0'`


##### CREATING IMAGE
`docker build -t flaskapp .`

##### CHECKING IF THE IMAGE WAS CREATED SUCCESSFULLY
`docker image ls`

##### RUNNING CONTAINER 
`docker run -d --name flaskapp_1 flaskapp`

##### SEE THE CONTAINER RUNNING
`docker container ls`

##### IF I WANTED TO INSTALL DEPENDENCIES THROUGH THE REQUIREMENTS.txt FILE
1 - Generate file > `pip freeze > requirements.txt`

"2 -  Instalar dependências a nível de aplicação (pip install)"
 `COPY ./requirements.txt /tmp`
 `RUN pip install -r /tmp/requirements.txt`


##### EXCLUDING UNIMPORTANT FILES
create .dockerignore
	|--venv/
	|--__pycache__
	|--dockerfile


##### AFTER MODIFYING THE DOCKERFILE, RUN THE COMMAND
`docker build -t flaskapp .`

##### CHECK THE CONTAINER LOGS
`docker logs -f flaskapp1`

