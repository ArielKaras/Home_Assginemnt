from flask import Flask, jsonify
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def list_containers():
    containers = client.containers.list()
    containers_info = [{'id': container.id, 'name': container.name, 'status': container.status} for container in containers]
    return jsonify(containers_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

