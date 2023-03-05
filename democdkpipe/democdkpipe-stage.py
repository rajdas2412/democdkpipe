from aws_cdk import Stage
from constructs import Construct

class DemocdkpipeStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
