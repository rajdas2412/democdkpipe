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
        # Create Access Key in Githut
        # Store the access key in Secrets Manager under the name github-token
        # Store the token in plain text with no key or quotes
        demo_cicd_pipe = CodePipeline(self, "demo_cicd_pipe",
                                      synth=ShellStep("Synth",
                                                      input=CodePipelineSource.git_hub(
                                                          "rajdas2412/democdkpipe", "main",
                                                      ),
                                                      commands=[
                                                          "npm install -g aws-cdk",
                                                          "pip install -r requirements.txt",
                                                          "cdk synth"
                                                      ]
                                                      )
                                      )
