from datetime import datetime

import requests

def generate_log(data):
    """Write log entries to a date-stamped text file.

    Args:
        data: A list of values to write, one value per line.

    Returns:
        The name of the generated log file.

    Raises:
        ValueError: If ``data`` is not a list.
    """
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetch a sample post from the JSONPlaceholder API.

    Returns an empty dictionary when the API does not return a successful
    response, matching the behavior described in the lab instructions.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    post = fetch_data()
    title = post.get("title", "No title found")
    print("Fetched Post Title:", title)
    generate_log(["User logged in", "User updated profile", "Report exported"])
