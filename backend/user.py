import redis

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=False)

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
        # TODO: Do stuff with Claude
        # TODO: call recipe manager
        print(f'User Input: {user_input}')
        return user_input

