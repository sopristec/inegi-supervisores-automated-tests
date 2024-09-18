import os
from flask import Flask, request, jsonify
import requests

from opera2 import load_file_data, run_process

app = Flask(__name__)


def generate_hex_string(length):
    return os.urandom(length // 2).hex().upper()


def get_token(session):
    # Set the URL for the token request
    url = "https://opera.inegi.org.mx/opera.auth/connect/token"

    # Define the headers to mimic the curl request
    headers = {
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": ".AspNetCore.Antiforgery.4fJZDYJKlCY=CfDJ8FHncaVeJ7BGielGJsGKkEJ7xe9FZmdF4CFvejVTIexlMgw8QZ-9XLjz1A9RZPQM_uBg-qSDQ_Bss4qSnM47flWPMksF87n9xDzgpvOqDz_-lo4zwn3Fe0Dn1WGPtm22DxGSZFga-2O9EtgjJ98tDrpp6nX5UOMF17GMWvmxCQDZIj4y5VKVW1zX6emD9nB5TPg-oxlG_-3Ib54i0jMNmiHjOzU4QZkLCz_oMTnj2gkeLueaZ4U2pCfug47d-xDH-xlkZveo--h21pu-uCDaJVIkHZT53ZjO5d2KhWZ-HqLEGq2fSrrnQ8c1fiqi_h8Eo2L6ELDTJ2wxhqYS6QQn9dsf8et-cATYb3gZaIDUAOhibEggfotPNlhTFd5TzyWNwvYEAnSbUGtzn_UzDbJW2Wtrs3sVYmPIaBXlWAaYVLSAMFvtejX4KvuuLB4KoLFA027N4H93nvgFp-FbfRSdqWiqnQi5tabjaKPNiC-EQaYpp7yS-DOkkZWTN8VuAPufl8y5jkmz-fPJkQGkQIwq4r1Yf8WXusLbx_LSsNe7R91xnQvBZIRfwNLHefPNtuPa3ir9FWACWCVahjYiRFJhBmmcFNPEUpswF6_EgtgEG5dhwvGC_IV5-y15kmhEcXi4j5BzKklAs-pd79K7aS5cS3duAyleXW98kFWxvbdl9S-p; BIGipServerLB_opera=4093810954.37407.0000",
        "Origin": "https://opera.inegi.org.mx",
        "Referer": "https://opera.inegi.org.mx/opera.web/auth-callback?code=A111E2AF840E8CADB73156AA37183EB925F178B92C6B9C35D88B1F4F152EDD09&scope=openid%20profile%20access&state=c6fd9f28823047608e13e8eed3163d92&session_state=K3KfsHnS0y6VMf0EQZmpQTMVdLgDaheN63AZcGoaArA.759B2949BE8B8D9773D160AD11599767",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not;A=Brand";v="24", "Chromium";v="128"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
    }

    # Define the data payload for the token request
    data = {
        "grant_type": "authorization_code",
        "redirect_uri": "https://opera.inegi.org.mx/opera.web/auth-callback",
        "code": "A111E2AF840E8CADB73156AA37183EB925F178B92C6B9C35D88B1F4F152EDD09",
        "code_verifier": "7488708fc800426f867fb871ef4a4cea68c47fa8904a4b28a3226223f1280c4d799147c2dee441bf90d2f8a30e03b8e4",
        "client_id": "opera.web",
    }

    # Make the POST request to obtain the token
    response = session.post(url, headers=headers, data=data)

    # Print the response JSON
    print(response.json())
    print(response.text)
    print(response.status_code)


@app.route("/selenium", methods=["POST"])
def selenium():
    """
    Endpoint to receive messages from the worker.
    This expects a JSON payload in the POST request.
    """
    try:
        # Get the JSON data from the request
        message = request.get_json()

        if not message:
            return jsonify({"error": "No message data received"}), 400

        print(f"Received message: {message}")

        run_process(message)

        # Return a success response
        return (
            jsonify({"status": "success", "message": "Message processed successfully"}),
            200,
        )

    except Exception as e:
        print(f"ERROR:::: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/login", methods=["POST"])
def login():
    # print(generate_hex_string(64))  # Generates a 64-character hex string

    session = requests.Session()

    url = "https://opera.inegi.org.mx/opera.auth/Account/Login"

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": ".AspNetCore.Identity.Application=CfDJ8IFXttMfUvNPu988hw61AYjbhwM3FnviWK8Z6DsbgsSR9J8fDpMSFc8gC2JcVe4UIyZipq2GAHCZ7aZu4_xGpq4VvjYNbmyJjBW9unBOI_rIzdUor0JVF8oTl52e7h5voGLh2f-tKMJThdBFNkKCMwJmuroukFkKPaNZhnbgwXouf6_Aq05rtghM3ETXc5696SfEHOiX8bVK09trSmu2CDZ1ss-L6fstBAP7xIppvvtXEEnYbaR8vAPFuwbwC7UCQ_A9q98dZeqPdP5UGnmf16hjfSGN7XUHAUphQFpkP4PBEmUBkrqp_1oqs5ERMYts5_HbQ3MFaTvOyuqZZr1p8GzPYN_xcD0WWbqMENmClx5JlOH4WFdzclreckEKN1OQN_zpGHvNL9t2NugLV5jhny0Nr_57FXJM6kv8GLflsqjJLNDABcEuY5RgdIl_gwbe3vbmgwskOnjCbJoT7Gn4VPR0WVy-offOAJQMTSCSKtfazo4pWKkr-EkzdiUDI4HNMcqbW9ZPmslx0vVmvpdaUZINzJqxez18vxyDDJeVcC3nWVOQLWO6t0ihaVNvf_L7Adli740NTXVdDCL_JFgwGRqZd2hCX_q9rnCZI1OnSXJoATrw_J3RhhuO6HCQnX-bxLU3eVzRXTKSxEox8I5i9aX5gErfLof0J-LPfmF14TD-; .AspNetCore.Antiforgery.4fJZDYJKlCY=CfDJ8FHncaVeJ7BGielGJsGKkELdLgopwH_trbBonzLHmjvb1enCA1JtK93_BC_nMDni3AgGefdAiEJgGV6BAWVEr1lubbecyDnecZ6TbDLc7stD1bwIXXs1Gkbm6ky-vo6loo0KDlm8QRMzg7WXRcH3g-U; BIGipServerLB_opera=4093810954.37407.0000",
        "Origin": "https://opera.inegi.org.mx",
        "Referer": "https://opera.inegi.org.mx/opera.auth/Account/Login?ReturnUrl=%2Fopera.auth%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dopera.web...",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not;A=Brand";v="24", "Chromium";v="128"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
    }

    data = {
        "ReturnUrl": "/opera.auth/connect/authorize/callback?client_id=opera.web&redirect_uri=https%3A%2F%2Fopera.inegi.org.mx%2Fopera.web%2Fauth-callback&response_type=code&scope=openid%20profile%20access&state=85116a081bd3478faed688a1fe995c56&code_challenge=8hVCfjMLALMnHqR9_i_qN9aTi_cu95w21nYVo4ZN2ZE&code_challenge_method=S256&response_mode=query",
        "UserName": "USUARIO.SIM10",
        "Password": "Univers@l",
        "__RequestVerificationToken": "CfDJ8FHncaVeJ7BGielGJsGKkEJNQebZLiURpctQF2NVb4hebwROZw_MUL7rn9SSn1vK3X8YxwPaogJidoztAV--s7q44xAXY5BqAByJc45xIvpO59vKMOyqppnc57YSvQb7OOkaICrRMB6ycjWf8iQ7Oqw",
    }

    response = session.post(url, headers=headers, data=data)

    print(response.text)
    print(response.status_code)
    cookies = session.cookies.get_dict()
    jwt_token = cookies.get(".AspNetCore.Identity.Application")

    # Alternatively, if the JWT is returned in the response body:
    # You can parse the login_response.text or login_response.json() to extract the JWT.

    print(f"JWT Token: {jwt_token}")

    # Define the URL and headers
    url = "https://opera.inegi.org.mx/opera.api/api/updown/upload"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "multipart/form-data",
        "Cookie": "BIGipServerLB_opera=2405749258.37407.0000",
        "Origin": "https://opera.inegi.org.mx",
        "Referer": "https://opera.inegi.org.mx/opera.web/int/integraciones/todo",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        # 'authorization': 'Bearer YOUR_ACCESS_TOKEN',
        "sec-ch-ua": '"Not;A=Brand";v="24", "Chromium";v="128"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
    }

    # Define the file to upload and other form fields
    files = {
        "file": (
            "Eenvio_102111110_20240814_154132728_PVOLUMEN.zip",
            open("Eenvio_102111110_20240814_154132728_PVOLUMEN.zip", "rb"),
            "application/zip",
        ),
        "filename": (None, "Eenvio_102111110_20240814_154132728_PVOLUMEN.zip"),
        "nasbase": (
            None,
            "\\\\powerscalesmb.inegi.gob.mx\\eic2025\\opera\\produccion\\eventos\\pvolumen\\int\\24\\242111100",
        ),
    }

    # Make the POST request to upload the file
    response = session.post(url, headers=headers, files=files)

    # Print the response from the server
    print(response.text)
    print(response.status_code)

    return response.text, response.status_code


if __name__ == "__main__":
    app.run(debug=True)
