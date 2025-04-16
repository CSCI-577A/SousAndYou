import redis
import requests

EC2_HOST = 'https://44.237.212.169:5001'
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
        self.history = []


    def _get_query_cache_key(self):
        return f"user:{self.user_id}:queries"

    def cache_query(self, query):
        key = self._get_query_cache_key()
        redis_client.lpush(key, query)
        redis_client.ltrim(key, 0, 49)  # keep only the 50 most recent queries

    def get_cached_queries(self):
        key = self._get_query_cache_key()
        return redis_client.lrange(key, 0, -1)


    def get_recipe_suggestions(self, user_input):
        # cache the query
        self.cache_query(user_input)
        url = f"{EC2_HOST}/chat"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "message": user_input
        }

        try:
            response = requests.post(url, headers=headers, json=payload, verify=False)
            print("Raw response:", response.text)
            response.raise_for_status()
            data = response.json()
            print("Parsed JSON:", data)
            return data.get("response", "No response field in result.")
        except Exception as e:
            print("Error in get_recipe_suggestions:", e)
            return None

