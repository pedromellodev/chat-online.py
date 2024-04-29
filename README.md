# chat-online.py
Criando um chat online com Django

## Primeiros passos
### Instalando o Django
Para iniciar um projeto em Django, você precisa ter certeza que tem o mesmo instalado.

=> pip install Django

=> python -m django --version

### Criando o projeto

django-admin startproject pedromellodev .

### Rodando o projeto
python manage.py runserver

Para derrubar a aplicação, digite
=> ctrl + c ou ^C

### Migrações
As migrações Django são direcionadas através da ORM, e por padrão algumas migrações pendentes no começo do projeto são: admin, content types, auth, sessions

Para executar as migrações, execute
=> python manage.py migrate

Agora as migrações, estão armazenadas dentro do banco de dados db.sqlite3

## Criando um superuser
O super usuário é aquele que tem permissão de entrar no painel admnistrativo do Django,

Para criar um superuser, execute o comando

=> python manage.py createsuperuser
