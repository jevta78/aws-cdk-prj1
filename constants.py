import os
from os.path import join, dirname, exists
from dotenv import load_dotenv

env = os.getenv('ENV') or 'dev'
env_filename = ".env." + env
dotenv_path = join(dirname(__file__), env_filename)
if exists(dotenv_path):
    load_dotenv(dotenv_path)


SERVICE_NAME=os.getenv('SERVICE_NAME')
API_PREFIX=os.getenv('API_PREFIX') or 'dev'
CDK_DEFAULT_ACCOUNT=os.getenv('CDK_DEFAULT_ACCOUNT')
CDK_DEFAULT_REGION=os.getenv('CDK_DEFAULT_REGION')