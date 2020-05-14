from app import app
from flask import request, jsonify
import redis
from rq import Queue
from app.core.task import background_task

re = redis.Redis(host='redis://redis:6379/0', port=6379,password='@Sanal89')
requestQueue = Queue(re)


@app.route('/api/submit-task')
def submit_task():
    requestQueue.enqueue_call(func=background_task,
                              args=("hey.csv", "zcds", "123"),
                              job_id=request.args.get("n"))
    return jsonify({"response": 200,
                    "message": "task enqueued",
                    "queue len": len(requestQueue)})


@app.route('/hi')
def hi():
    job = requestQueue.enqueue(background_task, "1")
    return "task added to queue"


@app.route('/health')
def health():
    return "app health is oky"


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
