from aws_cdk import (
    Stack,
    Duration,
    aws_sqs as sqs,
    aws_events as events,
    aws_lambda as _lambda,
    aws_events_targets as targets,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
)
from constructs import Construct
import aws_cdk.aws_pipes as pipes
import aws_cdk.aws_iam as iam

class AmazonEventBridgePipesPlayGroundStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)



        # Step 1: Receive events from SQS
        queue = sqs.Queue(self, "MyQueue")

        # Step 2: Define an event pattern
        pattern = events.EventPattern(
            source=["aws.sqs"],
            detail_type=["AWS API Call via CloudTrail"],
            detail={
                "eventSource": ["sqs.amazonaws.com"],
                "eventName": ["SendMessage"],
                "requestParameters": {
                    "queueUrl": [queue.queue_url]
                }
            }
        )

        rule = events.Rule(
            self, "MyRule",
            event_pattern=pattern,
            # targets=[targets.SnsTopic(topic)]
        )

        # Step 3: Transform your event
        my_lambda = _lambda.Function(
            self, "MyLambda",
            code=_lambda.Code.from_inline('def handler(event, context): return "hi"'),
            handler="index.handler",
            runtime=_lambda.Runtime.PYTHON_3_12,
        )

        # # create role for the pipe
        role = iam.Role(self, "MyRole",
            assumed_by=iam.ServicePrincipal("pipes.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess"),
            ]
        )

        # # eventBridgePipes
        eventBridgePipes = pipes.CfnPipe(self, "EventBridgePipes",
            # destination=queue,
            source=queue.queue_arn,
            role_arn=role.role_arn,
            target=my_lambda.function_arn,
        )