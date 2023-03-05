from aws_cdk import (
    Stage,
)
from constructs import Construct

from democdkpipe.lambda_stack import LambdaStack


class PipelineAppStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Underscores are not allowed in ID.
        demo_lambda_stack = LambdaStack(self, "demo-lambda-stack")
