import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)
# https://developer.github.com/v3/activity/events/

if __name__ == "__main__":
    username = sys.argv[1]

    response = requests.get(f"https://api.github.com/users/{username}/events")
    try:
        latest_event = response.json()[0]
        print(f'Latest event from {username}: ' + latest_event['created_at'])
    except TypeError:
        print("User does not exist in github")
    


