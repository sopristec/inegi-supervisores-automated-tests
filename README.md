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

# Run coordinator (master)
```sh
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
```

# Cron jobs

Kill a cron job:
```sh
ps aux | grep python
kill {pid} (coordinator_async)
```

OPERA Supervisores:

0 0 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 00.json
0 1 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 01.json
0 5 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 05.json
0 7 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 07.json
0 8 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 08.json
0 9 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 09.json
0 10 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 10.json
0 11 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 11.json
0 12 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 12.json
0 13 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 13.json
0 14 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 14.json
0 15 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 15.json
0 16 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 16.json
0 17 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 17.json
0 18 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 18.json
0 19 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 19.json
0 20 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 20.json
0 21 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 21.json
0 22 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 22.json
0 23 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_supervisores.sh 23.json


Entrevistas:

0 8 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 08.json
0 9 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 09.json
0 10 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 10.json
0 11 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 11.json
0 12 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 12.json
0 13 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 13.json
0 14 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 14.json
0 15 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 15.json
0 16 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 16.json
0 17 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 17.json
0 18 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 18.json
0 20 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 20.json
0 21 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 21.json
0 22 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 22.json
0 23 9 10 * /home/ltaas/inegi-supervisores-automated-tests/start_job_entrevistas.sh 23.json


# Steps to monitor load test

1. SSH to master-0 and master-1. Master 0 runs supervisores (selenium), master 1 runs entrevistas (requests)
2. sudo su - ltaas
3. See logs on workers:
```sh
    cd inegi-supervisores-automated-tests
    tail -f gunicorn.log
```
4. See logs on master supervisores:
```sh
    cd inegi-supervisores-automated-tests
    tail -f supervisores_cron.log
```
5. See logs on master entrevistas:
```sh
    cd inegi-supervisores-automated-tests
    tail -f entrevistas_cron.log
```


Julio: 
Checar en master-0 que no esté mandando a localhost
Tiene que ser:
Sending to: http://10.128.0.19:8000/supervisores
Y la respuesta viene como:
Response: {'message': 'Message processed successfully', 'status': 200}

Checar en master-1 que no esté mandando a localhost
Tiene que ser:
Sending to: http://10.128.0.19:8000/entrevistas
Y la respuesta viene como:
Response: {'message': '"20"', 'status': 200}


# NR dashboards
SELECT host, request.method, response.status, request.uri FROM Transaction WHERE appName = 'inegi-censos' 
SELECT count(externalCallCount) FROM Transaction FACET host WHERE appName = 'inegi-censos' 
SELECT count(externalCallCount), average(externalDuration) FROM Transaction FACET host WHERE appName = 'inegi-censos' 
SELECT count(externalCallCount), average(externalDuration) FROM Transaction WHERE appName = 'inegi-censos' FACET host, request.uri

SELECT count(*), average(externalDuration) 
FROM Transaction 
WHERE appName = 'inegi-censos' 
FACET host, request.uri
SINCE '2024-10-08T17:55:00Z' UNTIL '2024-10-08T18:55:00Z'