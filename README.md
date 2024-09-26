gunicorn -b 0.0.0.0:8000 -w 20 app:app --timeout 200

curl -X POST http://localhost:8000/supervisor -H "Content-Type: application/json" -d '{"username": "USUARIO.SIM10","file_name": "Eenvio_102111110_20240814_154132728_PVOLUMEN.zip"}'


python push_redis.py 