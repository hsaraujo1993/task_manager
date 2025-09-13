# Task Manager

Este projeto é um gerenciador de tarefas construído com Django. Ele permite que usuários criem, editem, excluam e organizem tarefas, tags e contas de usuário.

## Estrutura do Projeto
- `accounts/`: Gerenciamento de usuários (login, registro, modelos, views, templates)
- `tasks/`: CRUD de tarefas, formulários, modelos, views, templates
- `tags/`: CRUD de tags, modelos, views, templates
- `task_tags/`: Relacionamento entre tarefas e tags
- `app/`: Configurações principais do Django (settings, urls, wsgi, asgi)
- `db.sqlite3`: Banco de dados SQLite padrão
- `requirements.txt`: Dependências do projeto

## Como rodar o projeto
1. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
2. Execute as migrações:
   ```powershell
   python manage.py migrate
   ```

3. Crie um superusuário para acessar o admin:
   ```powershell
   python manage.py createsuperuser
   ```

4. Inicie o servidor de desenvolvimento:
   ```powershell
   python manage.py runserver
   ```
5. Acesse o sistema em `http://127.0.0.1:8000/`


## Convenções
- Templates HTML estão em cada app, na pasta `templates/`
- As migrations estão em `migrations/` dentro de cada app
- O projeto segue a estrutura padrão de apps Django