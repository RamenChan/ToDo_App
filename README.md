# FastAPI + RabbitMQ Example (Python)

FastAPI üzerinden gelen istekleri RabbitMQ kuyruğuna koyar ve ayrı bir worker bu kuyruğu tüketir.

Çalıştırma (lokalde):

1. RabbitMQ başlatın (docker kullanıyorsanız):

```bash
docker-compose up -d
```

2. Sanal ortam oluşturup bağımlılıkları kurun:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Uvicorn ile API'yi başlatın:

```bash
uvicorn app.main:app --reload --port 8000
```

4. Worker'ı çalıştırın (ayrı terminal):

```bash
python worker/consumer.py
```

5. Örnek istek (curl):

```bash
curl -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d '{"title":"Platform Solutions Team","description":"RabbitMQ test"}'
```

Dosyalar:
- `app/main.py`: FastAPI uygulaması
- `app/producer.py`: RabbitMQ'a mesaj yayınlama yardımcı fonksiyonu
- `worker/consumer.py`: Kuyruktan mesaj tüketen worker
- `docker-compose.yml`: RabbitMQ servisi
- `requirements.txt`: Python bağımlılıkları
