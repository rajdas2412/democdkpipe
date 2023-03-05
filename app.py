#!/usr/bin/env python3
import os

import aws_cdk as cdk

from democdkpipe.democdkpipe_stack import DemocdkpipeStack

app = cdk.App()
DemocdkpipeStack(app, "DemocdkpipeStack",
                 env=cdk.Environment(account="684119280118", region="us-east-1"),

                 )

app.synth()
