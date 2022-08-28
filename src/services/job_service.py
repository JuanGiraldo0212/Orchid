import uuid

import bson

from ..constants import *
from ..database import mongodb_helper


def input_validation_service(sequence):
    allowed_bases = 'AaUuGgCc'
    return all(ch in allowed_bases for ch in sequence)


def create_job_service(data, metadata, priority):
    job = {
        '_id': uuid.uuid4(),
        'status': JOB_STATUS[0],
        'data': data,
        'metadata': metadata,
        'priority': priority
    }
    return mongodb_helper.insert_job(job)


def get_job_status_service(job_id):
    job = mongodb_helper.retrieve_job(job_id)
    response = None
    if job:
        response = {
            "id": job_id,
            "status": job["status"]
        }
    return response
