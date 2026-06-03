import requests
import json


def fetch_and_display_users(num_users):
    try:
        url = f"https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: Received HTTP status code{response.status_code}")
            return None
        users=response.json()
        users = users[:num_users]

        for user in users:
            try:
                name = user.get("name", "N/A")
                email = user.get("email", "N/A")
                city = user.get("address", {}).get("city", "N/A")
                print(f"Name:{name},Email:{email},City:{city}")
            except KeyError:
                print("Error: Missing expected keys in user data")
                continue
            return users
    except requests.exceptions.RequestException as e:
        print(f"Error:Network error occured-{e}")
        return None
    except json.JSONDecodeError:
        print("Error:Failed to decode JSON response")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occured-{e}")
        return None


if __name__ == "__main__":
    fetch_and_display_users(4)
    fetch_and_display_users(16)
