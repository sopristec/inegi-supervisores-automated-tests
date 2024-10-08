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
curl -X POST http://localhost:8000/supervisores -H "Content-Type: application/json" -d '{"username": "USUARIO.SIM10","file_name": "Eenvio_102111250_20240920_185657315_PVOLUMEN.zip","no_requests":1}'
```



# Run master

export HOST_WS_1=
export HOST_WS_2=
export HOST_WS_3=
export HOST_WS_4=
export HOST_WS_5=
export HOST_WS_6=
export HOST_WS_7=
export HOST_WS_8=
export HOST_WS_9=
export HOST_WS_10=


python coordinator_async.py supervisores feeder_supervisores/00.json

python coordinator_async.py entrevistas feeder_entrevistas/00.json


./start_job_entrevistas 08.json
./start_job_supervisores 00.json



See logs on workers 
in project carpet:
tail -f gunicorn.log




Cron jobs

Entrevistas:

0 5 * * * cd /home/ltaas/inegi-supervisores-automated-tests && source .venv/bin/activate && python coordinator_async.py entrevistas feeder_entrevistas/08.json >> /home/ltaas/inegi-supervisores-automated-tests/entrevistas_cron.log 2>&1


10 19 * * * cd /home/ltaas/inegi-supervisores-automated-tests && source .venv/bin/activate && python coordinator_async.py entrevistas feeder_entrevistas/08.json >> /home/ltaas/inegi-supervisores-automated-tests/entrevistas_cron.log 2>&1

14 19 * * * cd ~/inegi-supervisores-automated-tests && source .venv/bin/activate && python coordinator_async.py entrevistas feeder_entrevistas/08.json >> ~/inegi-supervisores-automated-tests/entrevistas_cron.log 2>&1