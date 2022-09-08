from collections import deque
from ..constants import *


job_queue = deque([])


def insert_job(new_job):
    job_queue.appendleft(new_job)


def process_jobs():
    while True:
        if len(job_queue) > 0:
            current_job = job_queue.pop()
            status = current_job['status']
            match status:
                case 'CREATED':
                    current_job['status'] = 'PRE-PROCESSING'
                    # preprocess
                    print('Pre-processing...')

                case 'PRE-PROCESSING':
                    current_job['status'] = 'HARDWARE-SELECTION'
                    # hardware selection
                    print('Selecting Hardware...')

                case 'HARDWARE-SELECTION':
                    current_job['status'] = 'EXECUTING'
                    # Execute
                    print('Executing...')

                case 'EXECUTING':
                    current_job['status'] = 'POST-PROCESSING'
                    # postprocessor
                    print('Post-processing...')

                case 'POST-PROCESSING':
                    current_job['status'] = 'DONE'
                    print('Done')

            if current_job['status'] != 'DONE':
                job_queue.appendleft(current_job)

