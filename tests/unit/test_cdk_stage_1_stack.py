import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk.cdk_stage_1_stack import CdkStage1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk/cdk_stage_1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkStage1Stack(app, "cdk-stage-1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
