## 🏗️ Arquitetura / Fluxo do Projeto

```text
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
                         ALEMBIC
                            ↓
                    RELACIONAMENTOS
                            ↓
                         ORDERS
                            ↓
                        PAYMENTS
                            ↓
                        TELEGRAM
Status atual
✅ Implementado
- Users CRUD
- Password Hash com pwdlib
- Autenticação com JWT
- Login com access token
- get_current_user
- Proteção de rotas
- Autorização por usuário
- Alembic para controle de migrations
🚧 Em desenvolvimento
- Testes automatizados com pytest e TestClient
- Banco de testes
- Refatoração e melhorias na arquitetura
📋 Próximas etapas
- Relacionamentos entre entidades
- Products
- Orders
- Payments
- Integração com Telegram
- Melhorias no README e documentação
