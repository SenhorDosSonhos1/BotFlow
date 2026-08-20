# 🤖 BotFlow

BotFlow é uma API REST desenvolvida com FastAPI para gerenciamento de usuários, com autenticação e autorização baseada em JWT. O projeto está sendo evoluído para incluir gerenciamento de produtos, pedidos, pagamentos e integração com Telegram.

------------------------------------------------------------------------

## 🛠️ Tecnologias

-   Python 3.13
-   FastAPI
-   Pydantic
-   SQLAlchemy
-   PostgreSQL
-   Alembic
-   JWT / OAuth2
-   pwdlib
-   Pytest
-   Docker
-   Poetry

------------------------------------------------------------------------

## 🏗️ Arquitetura e Roadmap

A arquitetura abaixo representa a evolução planejada do BotFlow e a
relação entre as principais partes do sistema.

O fluxo de autenticação começa no gerenciamento de usuários e segurança,
passa pela geração e validação do JWT e permite proteger as rotas da
API.

O Alembic funciona como uma camada de infraestrutura para controlar e
versionar as alterações do banco de dados.

``` text
                         BOTFLOW
                            │
              ┌─────────────┴─────────────┐
              ↓                           ↓
            USERS                      SECURITY
              │                           │
             CRUD                        HASH
              │                           │
              └─────────────┬─────────────┘
                            ↓
                           JWT
                            ↓
                    get_current_user
                            ↓
                    ROTAS PROTEGIDAS
                            │
              ┌─────────────┴─────────────┐
              ↓                           ↓
          PRODUCTS                      ORDERS
                                          │
                                          ↓
                                      PAYMENTS
                                          │
                                          ↓
                                       TELEGRAM


        ALEMBIC
           │
           └── Controle e versionamento do schema do banco
```

### 🔐 Fluxo de autenticação

``` text
Login
  ↓
Email + senha
  ↓
Validação da senha
  ↓
Criação do JWT
  ↓
Access Token
  ↓
Authorization: Bearer <token>
  ↓
get_current_user
  ↓
Usuário autenticado
  ↓
Rota protegida
```

### 📦 Fluxo das entidades

``` text
User
 ↓
Products
 ↓
Orders
 ↓
Payments
 ↓
Telegram
```

Os relacionamentos entre essas entidades serão implementados conforme a
evolução do projeto.

------------------------------------------------------------------------

## 🗄️ Banco de dados

O PostgreSQL é utilizado como banco de dados da aplicação.

O SQLAlchemy é responsável pelo mapeamento entre os modelos Python e as
tabelas do banco.

O Alembic controla as alterações do schema através de migrations,
permitindo versionar e aplicar mudanças de forma controlada.

O PostgreSQL é executado através de Docker para facilitar a configuração
do ambiente de desenvolvimento.

------------------------------------------------------------------------

## 📊 Status do projeto

### ✅ Implementado

-   Users CRUD
-   Password Hash com `pwdlib`
-   Login
-   JWT
-   Access Token
-   `get_current_user`
-   Proteção de rotas
-   Autorização por usuário
-   Alembic
-   Migration inicial
-   PostgreSQL via Docker

### 🚧 Em desenvolvimento

-   Testes automatizados com Pytest e TestClient
-   Banco de testes
-   Refatoração

### 📋 Roadmap

-   [ ] Relacionamentos entre entidades
-   [ ] Products
-   [ ] Orders
-   [ ] Payments
-   [ ] Integração com Telegram
-   [ ] Melhorias e refatoração

------------------------------------------------------------------------

## ▶️ Executando o projeto

Instale as dependências:

``` bash
poetry install
```

Suba os serviços com Docker:

``` bash
docker compose up -d
```

Execute as migrations:

``` bash
alembic upgrade head
```

Inicie a aplicação:

``` bash
fastapi dev app/main.py
```

A documentação interativa da API estará disponível em:

``` text
http://127.0.0.1:8000/docs
```

------------------------------------------------------------------------

## 🎯 Objetivo

O BotFlow é um projeto prático para consolidar conhecimentos em
desenvolvimento de APIs REST com Python, autenticação, autorização,
banco de dados, migrations, testes e integração entre serviços.
