
3. Run virtual env & libs install

```sh
pipenv shell
pipenv install
```

3. Start server

```sh
--- For local usage ---
fastapi dev     # run in debug mode with auto-reload
fastapi run     # run in prod mode
```

4. Generate migrations

```sh
# --- Common migration ---
alembic -c app/database/alembic.ini revision --autogenerate -m "Migration name" --rev-id $(date +%Y%m%d%H%M%S)

# --- Merge migration
alembic -c app/database/alembic.ini merge heads -m "Merge migration" --rev-id $(date +%Y%m%d%H%M%S)
```

5. Run migrations

```sh
alembic -c app/database/alembic.ini upgrade head
```

6. Rollback last migration

```sh
alembic -c app/database/alembic.ini downgrade -1
```
