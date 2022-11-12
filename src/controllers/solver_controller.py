import json

from flask import Blueprint, request, Response, jsonify

solver = Blueprint('solver', __name__)


@solver.route('/solve/<backend>', methods=['POST'])
def solve(backend):
    content = request.json
    as_job = request.args.get('as_job') == "True"
    print(content)
    return Response(response=json.dumps({'status': 'testing'}), status=400,
                    mimetype='application/json')
