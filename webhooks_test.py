from flask import Flask, jsonify, request

# import json
#
app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def handle_webhook():
    # Retrieve the incoming JSON data payload
    data = request.json

    if not data:
        return jsonify({"error": "No data received"}), 400

    # Print the received data to your server logs
    print(f"Received Webhook Data: {data}")

    # Process the data here (e.g., update a database, trigger a build, etc.)

    # Always return a 200 OK response to let the sender know you got it
    return jsonify({"status": "success"}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)


#     curl -X POST http://127.0.0 \
# -H "Content-Type: application/json" \
# -d '{"event": "user_signup", "user": "John Doe"}'
