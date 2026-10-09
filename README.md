# Base — Controle De Treinos

Esta é a aplicação-base da avaliação de reposição.

Ela já possui CRUD de treinos com SQLite. O arquivo `auth.py` também já foi iniciado com Blueprint, mas a autenticação com `session` ainda precisa ser implementada.

## Executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Acesse `http://127.0.0.1:5000`.

## Arquivos Principais

- `app.py`: rotas Flask.
- `auth.py`: módulo de autenticação já iniciado, ainda sem rotas cadastradas.
- `database.py`: funções de banco de dados.
- `templates/`: páginas HTML.

## Observação

Não substitua a aplicação por outro projeto. A tarefa é adaptar esta base para autenticação com `session`, completando o módulo `auth.py` e mantendo as rotas de treinos em `app.py`.
