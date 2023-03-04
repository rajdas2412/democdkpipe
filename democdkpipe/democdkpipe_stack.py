from aws_cdk import (
    Stack,
    aws_codepipeline,
)
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep


class DemocdkpipeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the Pipeline
        demo_cicd_pipe = CodePipeline(self, "demo_cicd_pipe",
                                      synth=ShellStep("Synth",
                                                      input=CodePipelineSource.git_hub(
                                                          "rajdas2412/democdkpipe", "main",
                                                      ),
                                                      commands=["npm ci", "npm run build", "npx cdk synth"]
                                                      )
                                      )
