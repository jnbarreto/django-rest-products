# django-rest-products
- Projeto de gerenciamento de produtos, com CRUD e Login

## Requisitos
### Depedências
- Antes de rodar o projeto instale esses programas.
  - Python ![Python](https://img.shields.io/badge/python-00677a?style=for-the-badge&logo=python&logoColor=white) versão = ^3.11
  - Docker <img src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" alt="Docker Logo" width="30px" />.



## Rodar o projeto
### passo a passo.
- Clonar o Projeto Backend do <img src="https://skillicons.dev/icons?i=github" height="25" alt="GitHub Icon" />.
- Instalar todas as dependencias
```
npm install
```


- Adicionar na raiz do projeto as enviroments ```.env```
- Rodar os comandos <img src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" alt="Docker Logo" width="30px" /> para subir o ambiente.
```
docker-compose up --build
```
Se já executou a primeira vez com o ```--build``` basta rodar apenas o ```docker-compose up``` e projeto já vai está rodando.

## Comandos Uteis
Buildar o projeto.
```
docker-compose up --build
```
Subir o projeto.
```
docker-compose up
```
Limpar os volumes do Docker (buildar depois de rodar esse comando).
```
docker system prune -fa --volumes
```
