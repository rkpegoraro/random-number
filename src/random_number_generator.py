import random
import time
from flask import Flask

app = Flask(__name__)

@app.route('/random')
def get_random_number():
    return str(random.randint(1, 100))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

while True:
    print(random.randint(1, 100))
    time.sleep(2)
