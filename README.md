              BOTFLOW
                 │
        ┌────────┴────────┐
        ↓                 ↓
      USERS            SECURITY
        │                 │
      CRUD              HASH
        │                 │
        └───────┬─────────┘
                ↓
               JWT
                ↓
       get_current_user
                ↓
             PRODUCT
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