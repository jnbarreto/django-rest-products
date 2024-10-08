# Django-rest-products
- Projeto de gerenciamento de produtos, com CRUD e Login

## Requisitos
### Depedências
- Antes de rodar o projeto instale esses programas.
  - Python versão = ^3.11
  - Docker.
  - poetry (Também pode usar o pip mas eu vou utilizar o poetry por ser mais facil todo o gerenciamento)

### Install Poetry Com Pipx
link documentação pipx: https://github.com/pypa/pipx 
#### Instalação no Ubuntu pipx
```
  sudo apt update
  sudo apt install pipx
  pipx ensurepath
  sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
```

#### Instalação no MacOs pipx
```
  brew install pipx
  pipx ensurepath
  sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
```
#### Instalação poetry
link documentação poetry: https://python-poetry.org/docs/ 
```
  pipx install poetry
```
## Rodar o projeto
### passo a passo.
- Clonar o Projeto no Github. Entrar na pasta do backend
- Instalar todas as dependencias
```
  poetry install
```
- ativar o ambiente ( o poetry gerencia as enviroments )
```
  poetry shell
```

- Rodar os comandos docker para subir o ambiente.
```
docker compose up --build
```
Se já executou a primeira vez com o ```--build``` basta rodar apenas o ```docker compose up``` e projeto já vai está rodando.

Projeto Frontend link http://localhost:5000/users/auth/sign-in/
## Comandos Uteis
Buildar o projeto.
```
docker compose up --build
```
Subir o projeto.
```
docker compose up
```
Limpar os volumes do Docker (buildar depois de rodar esse comando).
```
docker system prune -fa --volumes
```
### Comandos criados com taskipy para ajudar no desenvolvimento

test = "docker exec backend python manage.py test"

migrate = "docker exec backend python manage.py migrate"

makemigrations = "docker exec backend python manage.py makemigrations"

createsuperuser = "docker exec -it backend python manage.py createsuperuser"

startapp = "docker exec backend python manage.py startapp {param}"

ip-database = "docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres-database"


#### Como executar

task + comando

exemplo: 
```
task test
```

