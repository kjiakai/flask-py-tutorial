#master changed
#m1
#m2
#dev changed
#d1
#d2

import time


import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    # return 'Hello from Docker!~!~'
    count = get_hit_count()
    return 'Hello from Docker! I have been seen {} times.\n'.format(count)