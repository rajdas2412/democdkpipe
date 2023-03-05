from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct


class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Lambda Function
        hello_function = _lambda.Function(self,
                                          id="hello_function",
                                          runtime=_lambda.Runtime.PYTHON_3_9,
                                          handler="lambda_handler.lambda_handler",
                                          code=_lambda.Code.from_asset("../services/")
                                          )
