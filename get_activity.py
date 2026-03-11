import requests

def get_activity(username_to_search):
   res = requests.get(f"https://api.github.com/users/{username_to_search}/events")
   events = res.json()

   if res.status_code == 200:
      print("nice")
      filtered_events = []
      for event in events:
         event_id = event['id']
         event_type = event['type']
         event_name = event['repo']['name']
         event_created = event['created_at']
         temp = {event_id, event_type, event_name, event_created}
         filtered_events.append(temp)

      for event in filtered_events:
         created_at = event[3]

         created_at_formated = created_at.strftime('%Y-%m-%d')
         print(f"{event[1]} --- {event[4]} --- {created_at_formated}")


   else:
      print(f"{res.status_code}\n {username_to_search} not found.")
