curl 'https://opera.inegi.org.mx/opera.api/api/updown/upload' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryxV6JttSdnkvhse24' \
  -H 'Cookie: BIGipServerLB_opera=2405749258.37407.0000' \
  -H 'Origin: https://opera.inegi.org.mx' \
  -H 'Referer: https://opera.inegi.org.mx/opera.web/int/integraciones/todo' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' \
  -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkIwQUIyN0IyQ0Q2Q0M4QUU4Q0NEQkFDNEJDNEQ0MzJBIiwidHlwIjoiSldUIn0.eyJuYmYiOjE3MjYyNDcyNjQsImV4cCI6MTcyNjI1NDUyNCwiaXNzIjoiaHR0cHM6Ly9vcGVyYS5pbmVnaS5vcmcubXgvb3BlcmEuYXV0aCIsImF1ZCI6Im9wZXJhLndlYiIsImlhdCI6MTcyNjI0NzI2NCwiYXRfaGFzaCI6IjNUaUtyV3E2T19CVTY3YjFOQ2ZDVUEiLCJzX2hhc2giOiJwRWtObUxjSFduQ2hJdDI2SW4wdXJRIiwic2lkIjoiRDUyNzZDQjY4NjdGMEY1NTM5M0IwNUNGQkJFOUU2NzYiLCJzdWIiOiI5NjUiLCJhdXRoX3RpbWUiOjE3MjYyNDcyNjAsImlkcCI6ImxvY2FsIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiVVNVQVJJTy5TSU0xMCIsIm5hbWUiOiJVU1VBUklPLlNJTTEwIiwiZXZ0IjoiNDgiLCJudiI6IkMiLCJjciI6IjEwIiwicmciOiIwMyIsImZnIjoiMzE4IiwibW9kcyI6IjciLCJyb2wiOiIxNCIsIm1vZCI6IjciLCJwZXIiOlsiNjciLCIyOCJdLCJjdmUiOiIxMEkxMTEwMDAiLCJhbXIiOlsicHdkIl19.VDzQgbQtC3NG42oQUDQ334fLwg8s0HV7bq60jGiKHKV59cxJuIE734PywMIFi8yLpxRjEFFRgY1ey4FGV-DUHsh5E05ewTpgod0t5WpqlLD7CVKt886oTli4yDr-wROyD5JbDEz6UIC366GdjypQgt5Vcv4fFGOT7vct_IXALS2lRmB33UMerOWOYCxZMH_O6V1WaekIN71omM-VIBb3IYDsl10lJWqHF_56aBwOF_aAAqOCvGBjZxA1DHuGgpHvW6P474tV93al8SGykMEwvSeSxcG_8dKg0NK_CsNItwRXEpCC_yby2yT4x2R-zc4oYvARz0KJslwMgM_kv21Edw' \
  -H 'sec-ch-ua: "Not;A=Brand";v="24", "Chromium";v="128"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw $'------WebKitFormBoundaryxV6JttSdnkvhse24\r\nContent-Disposition: form-data; name="file"; filename="Eenvio_242111110_20240814_153833115_PVOLUMEN.zip"\r\nContent-Type: application/zip\r\n\r\n\r\n------WebKitFormBoundaryxV6JttSdnkvhse24\r\nContent-Disposition: form-data; name="filename"\r\n\r\nEenvio_242111110_20240814_153833115_PVOLUMEN.zip\r\n------WebKitFormBoundaryxV6JttSdnkvhse24\r\nContent-Disposition: form-data; name="nasbase"\r\n\r\n\\\\powerscalesmb.inegi.gob.mx\\eic2025\\opera\\produccion\\eventos\\pvolumen\\int\\24\\242111100\r\n------WebKitFormBoundaryxV6JttSdnkvhse24--\r\n'

curl 'https://opera.inegi.org.mx/opera.api/api/integraciones/invoke-ws?paquete=Eenvio_242111110_20240814_153833115_PVOLUMEN.zip&idPaquete=7976&idEvento=48&evento=pvolumen' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: BIGipServerLB_opera=2405749258.37407.0000' \
  -H 'Referer: https://opera.inegi.org.mx/opera.web/int/integraciones/todo' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' \
  -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkIwQUIyN0IyQ0Q2Q0M4QUU4Q0NEQkFDNEJDNEQ0MzJBIiwidHlwIjoiSldUIn0.eyJuYmYiOjE3MjYyNDcyNjQsImV4cCI6MTcyNjI1NDUyNCwiaXNzIjoiaHR0cHM6Ly9vcGVyYS5pbmVnaS5vcmcubXgvb3BlcmEuYXV0aCIsImF1ZCI6Im9wZXJhLndlYiIsImlhdCI6MTcyNjI0NzI2NCwiYXRfaGFzaCI6IjNUaUtyV3E2T19CVTY3YjFOQ2ZDVUEiLCJzX2hhc2giOiJwRWtObUxjSFduQ2hJdDI2SW4wdXJRIiwic2lkIjoiRDUyNzZDQjY4NjdGMEY1NTM5M0IwNUNGQkJFOUU2NzYiLCJzdWIiOiI5NjUiLCJhdXRoX3RpbWUiOjE3MjYyNDcyNjAsImlkcCI6ImxvY2FsIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiVVNVQVJJTy5TSU0xMCIsIm5hbWUiOiJVU1VBUklPLlNJTTEwIiwiZXZ0IjoiNDgiLCJudiI6IkMiLCJjciI6IjEwIiwicmciOiIwMyIsImZnIjoiMzE4IiwibW9kcyI6IjciLCJyb2wiOiIxNCIsIm1vZCI6IjciLCJwZXIiOlsiNjciLCIyOCJdLCJjdmUiOiIxMEkxMTEwMDAiLCJhbXIiOlsicHdkIl19.VDzQgbQtC3NG42oQUDQ334fLwg8s0HV7bq60jGiKHKV59cxJuIE734PywMIFi8yLpxRjEFFRgY1ey4FGV-DUHsh5E05ewTpgod0t5WpqlLD7CVKt886oTli4yDr-wROyD5JbDEz6UIC366GdjypQgt5Vcv4fFGOT7vct_IXALS2lRmB33UMerOWOYCxZMH_O6V1WaekIN71omM-VIBb3IYDsl10lJWqHF_56aBwOF_aAAqOCvGBjZxA1DHuGgpHvW6P474tV93al8SGykMEwvSeSxcG_8dKg0NK_CsNItwRXEpCC_yby2yT4x2R-zc4oYvARz0KJslwMgM_kv21Edw' \
  -H 'sec-ch-ua: "Not;A=Brand";v="24", "Chromium";v="128"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'

curl 'https://opera.inegi.org.mx/opera.api/api/integraciones' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: BIGipServerLB_opera=2405749258.37407.0000' \
  -H 'Origin: https://opera.inegi.org.mx' \
  -H 'Referer: https://opera.inegi.org.mx/opera.web/int/integraciones/todo' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' \
  -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkIwQUIyN0IyQ0Q2Q0M4QUU4Q0NEQkFDNEJDNEQ0MzJBIiwidHlwIjoiSldUIn0.eyJuYmYiOjE3MjYyNDcyNjQsImV4cCI6MTcyNjI1NDUyNCwiaXNzIjoiaHR0cHM6Ly9vcGVyYS5pbmVnaS5vcmcubXgvb3BlcmEuYXV0aCIsImF1ZCI6Im9wZXJhLndlYiIsImlhdCI6MTcyNjI0NzI2NCwiYXRfaGFzaCI6IjNUaUtyV3E2T19CVTY3YjFOQ2ZDVUEiLCJzX2hhc2giOiJwRWtObUxjSFduQ2hJdDI2SW4wdXJRIiwic2lkIjoiRDUyNzZDQjY4NjdGMEY1NTM5M0IwNUNGQkJFOUU2NzYiLCJzdWIiOiI5NjUiLCJhdXRoX3RpbWUiOjE3MjYyNDcyNjAsImlkcCI6ImxvY2FsIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiVVNVQVJJTy5TSU0xMCIsIm5hbWUiOiJVU1VBUklPLlNJTTEwIiwiZXZ0IjoiNDgiLCJudiI6IkMiLCJjciI6IjEwIiwicmciOiIwMyIsImZnIjoiMzE4IiwibW9kcyI6IjciLCJyb2wiOiIxNCIsIm1vZCI6IjciLCJwZXIiOlsiNjciLCIyOCJdLCJjdmUiOiIxMEkxMTEwMDAiLCJhbXIiOlsicHdkIl19.VDzQgbQtC3NG42oQUDQ334fLwg8s0HV7bq60jGiKHKV59cxJuIE734PywMIFi8yLpxRjEFFRgY1ey4FGV-DUHsh5E05ewTpgod0t5WpqlLD7CVKt886oTli4yDr-wROyD5JbDEz6UIC366GdjypQgt5Vcv4fFGOT7vct_IXALS2lRmB33UMerOWOYCxZMH_O6V1WaekIN71omM-VIBb3IYDsl10lJWqHF_56aBwOF_aAAqOCvGBjZxA1DHuGgpHvW6P474tV93al8SGykMEwvSeSxcG_8dKg0NK_CsNItwRXEpCC_yby2yT4x2R-zc4oYvARz0KJslwMgM_kv21Edw' \
  -H 'sec-ch-ua: "Not;A=Brand";v="24", "Chromium";v="128"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '[{"idIntegracion":0,"idEvento":48,"cveoper":"242111110","cveoperIntegra":"10I111000","archivo":"Eenvio_242111110_20240814_153833115_PVOLUMEN.zip","idEstatus":1,"fechaIntegracion":"2024-09-13T17:08:05.614Z","estatusDescCorta":"Transferencia correcta"}]'