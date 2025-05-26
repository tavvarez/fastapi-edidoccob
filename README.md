# FastAPI-EDI

Sistema de geração de arquivos EDI DOCCOB 3.0 com base em arquivos XML de CT-e (Conhecimento de Transporte Eletrônico).

## Funcionalidades

* Upload de múltiplos XMLs de CT-e (via `/upload-xml`)
* Armazenamento das informações no banco de dados PostgreSQL
* Registro do input do usuário com vinculação a diversos CT-es
* Geração do arquivo EDI conforme layout DOCCOB Proceda 3.0 (registros 000 a 355)
* Download do arquivo gerado via endpoint dedicado
* Armazenamento em disco e controle de logs

## 📂 Requisitos

* Python 3.12+
* PostgreSQL
* WSL2 com Ubuntu (para ambientes Windows)

## Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/tavvarez/fastapi-edibialog.git
cd fastapi-edibialog
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o arquivo `.env` com sua conexão PostgreSQL:

```env
DATABASE_URL=postgresql+psycopg2://usuario:senha@localhost:5432/your_db
```

5. Rode as migrations:

```bash
alembic upgrade head
```

6. Inicie o servidor:

```bash
uvicorn app.main:app --reload
```

7. Acesse a documentação:
   [http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints principais

* `POST /upload-xml`: Envia um ou mais arquivos XML
* `POST /user-input/`: Recebe dados do usuário e vincula aos CT-es
* `POST /gerar-edi/{user_input_id}`: Gera o arquivo EDI
* `GET /download-edi/{user_input_id}`: Faz o download do EDI gerado

## Tecnologias

* FastAPI + Pydantic
* SQLAlchemy + Alembic
* PostgreSQL
* lxml (parsing de XML)
* Uvicorn

## Observações

* Os arquivos gerados seguem fielmente o layout DOCCOB conforme a documentação do Proceda 3.0
* A aplicação pode ser expandida com autenticação, UI em React ou Streamlit, integração direta com Protheus, etc...

---

Desenvolvido para automatizar e facilitar meu trabalho na geração de EDI.
