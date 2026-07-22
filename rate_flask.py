from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Track limits using the client's remote IP address
limiter = Limiter(
    get_remote_address, app=app, default_limits=["2 per day", "1 per hour"]
)


@app.route("/api/resource")
@limiter.limit("3 per minute")  # Overrides default limit for this route
def dynamic_endpoint():
    return jsonify({"message": "Success! You have remaining quota."})


if __name__ == "__main__":
    app.run(debug=True)
