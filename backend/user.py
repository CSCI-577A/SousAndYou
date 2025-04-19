import json

import redis
import requests

EC2_HOST = 'http://44.237.212.169:5001'
# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=False)
print("Redis ping:", redis_client.ping())
redis_client.set("test_key", "test_value")
print("Value for test_key:", redis_client.get("test_key"))
class User:
    def __init__(self, user_id, name, preferences=None):
        self.user_id = user_id
        self.name = name
        self.preferences = preferences if preferences else {
            "dietary_restrictions": [],
            "cooking_skill": "",
            "time_available": "",
            "ingredient_availability": []
        }


    def _get_query_cache_key(self):
        return f"user:{self.user_id}:queries"

    def cache_query(self, query):
        key = self._get_query_cache_key()
        redis_client.lpush(key, query)
        redis_client.ltrim(key, 0, 49)  # keep only the 50 most recent queries

    def get_cached_queries(self):
        key = self._get_query_cache_key()
        return redis_client.lrange(key, 0, -1)

    def get_conversation_history(self):
        history = redis_client.get(f"chat_history:{self.user_id}")
        print(history)
        return json.loads(history) if history else ""
    def save_conversation_history(self, messages):
        print("Convo history ")
        redis_client.set(f"chat_history:{self.user_id}", json.dumps(messages))
        print(json.dumps(messages))

    def get_recipe_suggestions(self, user_input):
        # cache the query
        self.cache_query(user_input)
        url = f"{EC2_HOST}/chat"
        history = self.get_conversation_history()
        message = user_input + history
        print("history" + history)
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "message": message
        }
        print("sent Message")

        try:
            response = requests.post(url, headers=headers, json=payload)
            print("response ")
            print(response)
            response.raise_for_status()
            data = response.json()
            return_val = data.get("response", "No response field in result.")
            print(data)
            full_response = "User asked: " + user_input + "\nClaude says: " + json.dumps(data) #data.get("response", "No response field in result.")
            print("full response")
            self.save_conversation_history(full_response)
            return return_val
        except Exception as e:
            print("Error:", e)
            return None

