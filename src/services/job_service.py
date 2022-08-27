import uuid
from ..constants import *


def input_validation_service(sequence):
    allowed_bases = 'AaUuGgCc'
    return all(ch in allowed_bases for ch in sequence)


def create_job_service(data, metadata, priority):
    job = {
        'id': uuid.uuid4(),
        'status': JOB_STATUS[0],
        'data': data,
        'metadata': metadata,
        'priority': priority
    }

    return job["id"]
