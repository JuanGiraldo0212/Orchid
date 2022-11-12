import json

from flask import Blueprint, request, Response, jsonify
from ..services.job_service import *

jobs = Blueprint('jobs', __name__)


@jobs.route('/jobs', methods=['POST'])
def create_job():
    content = request.json
    data = content['sequence']
    metadata = content['metadata']
    priority = content['priority']
    if input_validation_service(data):
        job_id = create_job_service(data, metadata, priority)
        return Response(response=json.dumps({'job_id': str(job_id), 'status': 'CREATED'}), status=200,
                        mimetype='application/json')
    else:
        return Response(response=json.dumps({'error': 'Input has to be a valid RNA sequence'}), status=400,
                        mimetype='application/json')


@jobs.route('/jobs/<job_id>')
def get_job_status(job_id):
    job = get_job_status_service(job_id)
    if job:
        return jsonify(job)
    else:
        return Response(response=json.dumps({'error': 'The Job with the specified Id does not exist'}), status=400,
                        mimetype='application/json')

