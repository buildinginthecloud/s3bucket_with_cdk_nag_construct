from aws_cdk import (
    Aspects,
    Stack,
    aws_s3 as s3,
)
from constructs import Construct
from secure_bucket_construct import SecureBucket
import cdk_nag

class S3BucketWithCfnNagConstructStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        SecureBucket(self, 'SecureS3Bucket')
        Aspects.of(self).add(cdk_nag.AwsSolutionsChecks())