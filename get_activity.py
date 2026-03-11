import requests

def get_activity(username_to_search):
   res = requests.get(f"https://api.github.com/users/{username_to_search}/events")
   events = res.json()

   if res.status_code == 200:
      print("nice")
   else:
      print(f"{res.status_code}\n {username_to_search} not found.")
