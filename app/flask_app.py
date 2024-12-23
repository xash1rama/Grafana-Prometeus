from random import randint, choice
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route("/random")
@metrics.counter('cnt_random', "Count invocation /random", labels={'collection': 'random', 'status': lambda f:f.status_code == 200})
def randindon():
    random_num = randint(1, 10)
    if random_num % 2 == 0:
        return f"Выпало {random_num} четное", 200
    return f"Выпало {random_num} НЕ четное", 400

@app.route("/hello")
@metrics.counter('hello_requests_total', 'Общее количество запросов к эндпоинту /hello', labels={'status': lambda f:f.status_code == 200})
def hello():
    random_num = randint(1, 2)
    random_name = choice(["bob", "dilon", "shon", "GGG"])
    if random_num % 2 == 0:
        return f"hello {random_name} (200)", 200
    return f"Baye {random_name} (400)", 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, threaded=True)