#!/usr/bin/env python3
import os

import aws_cdk as cdk
from cdk.cdk_stage_1_stack import CdkStage1Stack, get_stack_name
from constants import CDK_DEFAULT_ACCOUNT, CDK_DEFAULT_REGION

app = cdk.App()

devStack = CdkStage1Stack(
    app,
    get_stack_name(),
    env=cdk.Environment(
        account=CDK_DEFAULT_ACCOUNT, region=CDK_DEFAULT_REGION
    ),
)


# prodStack = CdkStage1Stack(
#     app,
#     "MojStack-prod",
#     env=cdk.Environment(
#         account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
#     ),
# )

app.synth()
