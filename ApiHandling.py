import requests

def fetch_users() -> list[str]:
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    try:
        res = requests.get(url, timeout=10) 
        res.raise_for_status() 
        data = res.json()

        if data.get("success") and "data" in data:
            user_data = data["data"].get("data", [])
            usernames = [user["login"]["username"] for user in user_data]
            return usernames
        else:
            print("API response is not in the expected format.")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users: {e}")
        return []

if __name__ == "__main__":
    usernames = fetch_users()
    if usernames:
        print("Usernames:")
        for username in usernames:
            print(username)
    else:
        print("No usernames found.")