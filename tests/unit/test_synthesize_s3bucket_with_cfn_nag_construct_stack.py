import aws_cdk as core
import aws_cdk.assertions as assertions

from s3bucket_with_cfn_nag_construct.s3bucket_with_cfn_nag_construct_stack import S3BucketWithCfnNagConstructStack

def test_synthesizes_properly():
    app = core.App()

    # Create the S3BucketWithCfnNagConstructStack.
    s3_bucket_stack = S3BucketWithCfnNagConstructStack(
        app, "S3BucketWithCfnNagConstructStack",
    )

    # Prepare the stack for assertions.
    template = assertions.Template.from_stack(s3_bucket_stack)