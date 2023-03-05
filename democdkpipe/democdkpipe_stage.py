from aws_cdk import (
    Stack,
    Stage,
)
from constructs import Construct

from democdkpipe.democdkpipe.lambda_stack import LambdaStack


class PipelineAppStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        demo_lambda_stack = LambdaStack(self, "demo_lambda_stack")