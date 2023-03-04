#!/usr/bin/env python3
import os

import aws_cdk as cdk

from democdkpipe.democdkpipe_stack import DemocdkpipeStack

app = cdk.App()
DemocdkpipeStack(app, "DemocdkpipeStack",
                 env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

                 )

app.synth()
