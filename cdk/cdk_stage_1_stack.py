from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct
import os

from constants import API_PREFIX, SERVICE_NAME

def get_stack_name() -> str:
    return f'{SERVICE_NAME}-{API_PREFIX}'

class CdkStage1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        my_lambda = _lambda.Function(
            self,
            f"HelloHandler-{API_PREFIX}",
            runtime=_lambda.Runtime.PYTHON_3_11,
            code=_lambda.Code.from_asset("lambda"),
            handler="hello.handler",
            function_name="Hello_func-" + API_PREFIX,
        )
        dev_deployment = apigw.StageOptions(
            stage_name=API_PREFIX,
            variables={"lambdaAlias": API_PREFIX},
        )

        api = apigw.LambdaRestApi(
            self,
            get_stack_name(),
            handler=my_lambda,
            deploy_options=dev_deployment,
            proxy=False,
        )

        prod_deployment = apigw.Deployment(
            self,
            "ProdDeployment08052021",  # change the date here
            api=api,
            retain_deployments=True,
            # Change the description here as well for our reference
            description="Production API deployment as 08-05-2021 Live version",
        )

        prod_stage = apigw.Stage(
            self,
            "ProdStage",
            deployment=prod_deployment,
            stage_name="prod",
            variables={"lambdaAlias": "prod"},
        )

        hello = api.root.add_resource("hello")
        hello.add_method("GET")
