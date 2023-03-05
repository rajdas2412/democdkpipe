from aws_cdk import (
    Stack,
)
import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep, ManualApprovalStep
from democdkpipe.democdkpipe_stage import PipelineAppStage


class DemocdkpipeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(self, scope, construct_id, **kwargs)

        # Create the Pipeline
        # Create Access Key in GitHub
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

        # test_stage = demo_cicd_pipe.add_stage(PipelineAppStage(self,
        #                                                        "TEST",
        #                                                        env=cdk.Environment(account="684119280118",
        #                                                                            region="us-east-1")
        #                                                        ))
        # test_stage.add_post(ManualApprovalStep("Approval"))
        #
        # prod_stage = demo_cicd_pipe.add_stage(PipelineAppStage(self,
        #                                                        "PROD",
        #                                                        env=cdk.Environment(account="684119280118",
        #                                                                            region="us-east-1")
        #                                                        ))
