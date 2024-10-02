# Run workers with NR

```sh
export NEW_RELIC_LICENSE_KEY=<your_license_key>
export NEW_RELIC_APP_NAME="inegi-censos"
export ENTREVISTAS_PASSWORD=<password>

newrelic-admin run-program gunicorn -b 0.0.0.0:8000 -w 20 app:app --timeout 200
newrelic-admin run-program gunicorn app:app --worker-class gevent --workers 8 --threads 2 --bind 0.0.0.0:8000 --timeout 300
```

# Run workers without NR
```sh
gunicorn -b 0.0.0.0:8000 -w 20 app:app --timeout 200
gunicorn app:app --worker-class gevent --workers 8 --threads 2 --bind 0.0.0.0:8000 --timeout 300
```

# Try workers
```sh
curl -X POST http://localhost:8000/supervisor -H "Content-Type: application/json" -d '{"username": "USUARIO.SIM10","file_name": "Eenvio_102111110_20240814_154132728_PVOLUMEN.zip"}'
```
