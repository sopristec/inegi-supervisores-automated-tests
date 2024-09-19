import os
from flask import Flask, request, jsonify
import requests

from selenium_script import upload_file

app = Flask(__name__)


@app.route("/entrevistas", methods=["POST"])
def entrevistas():
    try:
        url = "https://opera.inegi.org.mx/opera.api/api/updown/uploadEntrevistaCompleta/48"

        file_path = "Entrevistas/Tenvio_012111111_20240813_55805750_PVOLUMEN.zip"

        files = {"file": open(file_path, "rb")}

        response = requests.post(url, files=files)

        return (
            jsonify({"status": "success", "inegi_response": response.text}),
            response.status_code,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/supervisor", methods=["POST"])
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
