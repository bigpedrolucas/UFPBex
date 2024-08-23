# UFPBex
Projeto da disciplina de Especificação de Requisitos de Software, que visa auxiliar os estudantes em geral na pesquisa de informações acerca dos cursos de graduação da universidade Federal da Paraíba (UFPB)

## Instruções para rodar o projeto (Windows)

### Download do PostgreSQL 16:
https://www.postgresql.org/download/windows/

Na instalação: configurar senha, porta, etc. conforme DATABASES em "settings.py", ou alterar o arquivo de configuração para corresponder aos valores definidos no postgres.

### Acessar o PgAdmin4, entrar com o usuario "postgres" (utilizar senha definida na instalação) e criar o database "ufpbex"

### Acessar o QueryTool no database "ufpbex" e digitar o seguinte comando:
```
CREATE EXTENSION unaccent;
```

## Clonar o repositório onde se deseja armazenar os arquivos do projeto

## Criar um ambiente virtual
```
python -m venv .venv
.venv\Scripts\activate
```

## Instalar as dependencias do projeto nesse ambiente
```
pip install -r requirements.txt
```

## Criar as tabelas do banco de dados, preencher com as informações e rodar o projeto
```
python manage.py makemigrations
python manage.py migrate
python manage.py fill_database
python manage.py runserver
```
