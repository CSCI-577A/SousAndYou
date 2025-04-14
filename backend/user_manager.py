import uuid
import pickle
from user import User, redis_client


def create_user(name="Guest"):
    user_id = str(uuid.uuid4())  # unique id
    new_user = User(user_id=user_id, name=name)
    # store user in Redis
    redis_client.set(user_id, pickle.dumps(new_user))
    return new_user
