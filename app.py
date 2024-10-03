import os
from flask import Flask, request, jsonify
import requests

from selenium_script import upload_file

app = Flask(__name__)


def get_token_entrevistas():
    url = "https://opera.inegi.org.mx/opera.auth/connect/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "BIGipServerLB_opera=4093810954.37407.0000",
    }
    ENTREVISTAS_PASSWORD = os.environ.get("ENTREVISTAS_PASSWORD", "")
    data = {
        "client_id": "sistema.verifica",
        "grant_type": "password",
        "username": "cen_gpo_verif",
        "password": f"{ENTREVISTAS_PASSWORD}",
        "scope": "operaapi",
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        # Parse the JSON response
        token_info = response.json()
        # Extract the access token
        access_token = token_info.get("access_token")
        print(f"Access Token: {access_token}")
        return access_token
    else:
        print(f"Failed to retrieve token: {response.status_code}")
        print(response.text)
        return ""


@app.route("/entrevistas", methods=["POST"])
def entrevistas():
    try:
        access_token = get_token_entrevistas()
        # Add Bearer token to headers
        headers = {"Authorization": f"Bearer {access_token}"}

        url = "https://opera.inegi.org.mx/opera.api/api/updown/uploadEntrevistaCompleta/48"

        # Get the JSON data from the request
        message = request.get_json()

        if not message:
            return jsonify({"error": "No message data received"}), 400

        file_path = message["file_name"]

        files = {"file": open(file_path, "rb")}

        response = requests.post(url, files=files, headers=headers)

        return (
            jsonify({"status": "success", "inegi_response": response.text}),
            response.status_code,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/supervisores", methods=["POST"])
def supervisor():
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

        upload_file(message)

        # Return a success response
        return (
            jsonify({"status": "success", "message": "Message processed successfully"}),
            200,
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
