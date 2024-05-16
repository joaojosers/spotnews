# spotnews

## Contexto
- Desenvolver aplicação que armazena notícias que podem ser categorizadas por um usuário cadastrado.
- Utilizar Django e Django Rest Framework

## Habilidades a serem trabalhadas
- Escrever aplicações usando Django e Django Rest Framework
- A aplicação deve usar a arquitetura Model-View-Template
- Trabalhar com banco de dados MYSQL
## Crie o ambiente virtual para o projeto
```
python3 -m venv .venv && source .venv/bin/activate
```
## Instalando Dependências
```
python3 -m pip install -r dev-requirements.txt
```
## Usar Docker
```
docker-compose up -d
```
## Executando o projeto
- Para a realização deste projeto, utilizaremos um banco de dados chamado spotnews_database.
- Existem funções prontas no arquivo `news/scripts/seeds.py`que não devem ser alteradas.

* Para rodar o MySQL via Docker execute os seguintes comandos na raiz do projeto
```
docker build -t spotnews-db .
docker run -d -p 3306:3306 --name=spotnews-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=spotnews_database spotnews-db
```
* Ao criar/modificar um modelo, é necessário criar as migrações para espelhar as modificações para os bancos de dados, inclusive o banco de testes contam com estas modificações. O comando para gerar a migration a partir dos modelos criados é:
````
python3 manage.py makemigrations
```
* após criar os modelos é preciso executar os comandos: o primeiro para criar as tabelas no banco e o segundo comando irá popular o banco.
```
python3 manage.py migrate
python3 manage.py runscript seeds
```
## Executando Testes
* executando todos os testes
 ```
 python3 -m pytest
```
* Caso precise executar apenas um arquivo de testes basta executar o comando:
```
python3 -m pytest tests/nomedoarquivo.py
```
## Arquivos desenvolvidos pela Trybe
* src:
  - dev-requirements.txt
  - requirements.txt