import aws_cdk as core
import aws_cdk.assertions as assertions

from s3bucket_with_cfn_nag_construct.s3bucket_with_cfn_nag_construct_stack import S3BucketWithCfnNagConstructStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3bucket_with_cfn_nag_construct/s3bucket_with_cfn_nag_construct_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3BucketWithCfnNagConstructStack(app, "s3bucket-with-cfn-nag-construct")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
