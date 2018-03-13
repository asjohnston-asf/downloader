import boto3
from urlparse import urlparse
from os import environ, path
from logging import getLogger


log = getLogger()
log.setLevel(environ['LOG_LEVEL'])

def lambda_handler(event, context):
    batch = boto3.client('batch')
    for url in event['urls']:
        url_path = urlparse(url).path
        file_name = path.split(url_path)[-1]
        product_name = path.splitext(file_name)[0]
        log.info('Submitting job for %s', product_name)
        batch.submit_job(
            jobName=product_name,
            jobQueue=environ['JOB_QUEUE'],
            jobDefinition=environ['JOB_DEFINITION'],
            parameters={'url': url},
        )
