#!/usr/bin/env python3
"""
AWS CDK Application
cloud app
"""

import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy
)
from constructs import Construct


class Cloud_AppStack(Stack):
    """
    Main CDK Stack
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Example: Create an S3 bucket
        # You can customize this stack to add your own AWS resources
        bucket = s3.Bucket(
            self, "ExampleBucket",
            bucket_name=f"cloud-app-{{{cdk.Aws.ACCOUNT_ID}}}",
            removal_policy=RemovalPolicy.DESTROY,  # For development only
            auto_delete_objects=True,  # For development only
            versioned=False
        )

        # Add more resources here as needed
        # Examples:
        # - Lambda functions
        # - API Gateway
        # - DynamoDB tables
        # - ECS clusters
        # - etc.


app = cdk.App()
Cloud_AppStack(
    app, "Cloud-AppStack",
    env=cdk.Environment(
        account=app.node.try_get_context("account") or None,
        region=app.node.try_get_context("region") or "us-east-1"
    ),
    description="cloud app"
)

app.synth()
