import requests
from ratelimit import limits, sleep_and_retry

# Define limit: Maximum 5 calls per 10 seconds
CALLS = 5
PERIOD = 10


def __doc__():
    """useful for watching ou that we do not send too many requests to the outside API servers"""


@sleep_and_retry
@limits(calls=CALLS, period=PERIOD)
def fetch_data(url):
    """Fetches data from an API. If the limit is breached,
    @sleep_and_retry forces the script to wait before executing."""
    response = requests.get(url)
    return response.status_code


# Simulation loop
for i in range(7):
    # The first 5 requests will fire instantly.
    # Requests 6 and 7 will automatically trigger a pause.
    print(f"Request {i + 1} status: {fetch_data('https://httpbin.org')}")

if __name__ == "__main__":
    fetch_data("http://127.0.0.1:8080/users/001.html")
