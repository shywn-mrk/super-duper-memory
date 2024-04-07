### Run these commands in order

```bash
docker-compose up -d
```

```bash
python3 -m venv env
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
celery -A tasks worker --loglevel=info
```
