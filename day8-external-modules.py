import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    for user in users:
        print(f"Name:{user['name'].title()} - Email: {user['email']}")
except Exception as ex:
    print("Something wrong happend!")