import boto3
from uuid import uuid4
from os import environ
from logging import getLogger


log = getLogger()


def lambda_handler(event, context):
    batch = boto3.client('batch')
    for url in event['urls']:
        batch.submit_job(
            jobName=str(uuid4()),
            jobQueue=environ['JOB_QUEUE'],
            jobDefinition=environ['JOB_DEFINITION'],
            parameters={'url': url},
        )
