from dataclasses import asdict

from flask import Blueprint, request, Response
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
        return Response(f"Job created with id: {job_id}", status=200, mimetype='application/json')
    else:
        return Response("Input has to be a valid RNA sequence", status=400, mimetype='application/json')
