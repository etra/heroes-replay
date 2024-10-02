
```python

export FLASK_DEBUG=1
export FLASK_ENV=dev
export FLASK_RUN_PORT=4432
export FLASK_RUN_HOST=0.0.0.0
FLASK_APP=admin.app:create_app 

flask run

```

Migrate
```
FLASK_APP=h3:h3_app flask db migrate
FLASK_APP=h3:h3_app flask db upgrade
```