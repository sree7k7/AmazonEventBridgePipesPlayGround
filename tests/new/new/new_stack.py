from aws_cdk import Stack
import aws_cdk as cdk
import aws_cdk.aws_iam as iam
import aws_cdk.aws_lambda as aws_lambda
import aws_cdk.aws_pipes as pipes
import aws_cdk.aws_sqs as sqs
from constructs import Construct
from aws_cdk import CfnDeletionPolicy

class NewStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # Resources
    iamManagedPolicy00policyserviceroleAwsLambdaBasicExecutionRole68397c9137f047bab5a2535c46b23661003Rqu9 = iam.CfnManagedPolicy(self, 'IAMManagedPolicy00policyserviceroleAWSLambdaBasicExecutionRole68397c9137f047bab5a2535c46b23661003RQU9',
          managed_policy_name = 'AWSLambdaBasicExecutionRole-68397c91-37f0-47ba-b5a2-535c46b23661',
          path = '/service-role/',
          description = '',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': 'arn:aws:logs:eu-central-1:619831221558:*',
                'Action': 'logs:CreateLogGroup',
                'Effect': 'Allow',
              },
              {
                'Resource': [
                  'arn:aws:logs:eu-central-1:619831221558:log-group:/aws/lambda/helloworld:*',
                ],
                'Action': [
                  'logs:CreateLogStream',
                  'logs:PutLogEvents',
                ],
                'Effect': 'Allow',
              },
            ],
          },
          roles = [
            'helloworld-role-cmn3q4vc',
          ],
          users = [
          ],
        )
    iamManagedPolicy00policyserviceroleAwsLambdaBasicExecutionRole68397c9137f047bab5a2535c46b23661003Rqu9.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    iamManagedPolicy00policyserviceroleLambdaPipeTargetTemplate35ae232d00K2npc = iam.CfnManagedPolicy(self, 'IAMManagedPolicy00policyserviceroleLambdaPipeTargetTemplate35ae232d00K2npc',
          managed_policy_name = 'LambdaPipeTargetTemplate-35ae232d',
          path = '/service-role/',
          description = '',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': [
                  'arn:aws:lambda:eu-central-1:619831221558:function:helloworld',
                ],
                'Action': [
                  'lambda:InvokeFunction',
                ],
                'Effect': 'Allow',
              },
            ],
          },
          roles = [
            'Amazon_EventBridge_Pipe_Execution_40238cd4',
          ],
          users = [
          ],
        )
    iamManagedPolicy00policyserviceroleLambdaPipeTargetTemplate35ae232d00K2npc.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    iamManagedPolicy00policyserviceroleSqsPipeSourceTemplate4ae0b53100mKqrk = iam.CfnManagedPolicy(self, 'IAMManagedPolicy00policyserviceroleSqsPipeSourceTemplate4ae0b53100mKqrk',
          managed_policy_name = 'SqsPipeSourceTemplate-4ae0b531',
          path = '/service-role/',
          description = '',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': [
                  'arn:aws:sqs:eu-central-1:619831221558:testqueue',
                ],
                'Action': [
                  'sqs:ReceiveMessage',
                  'sqs:DeleteMessage',
                  'sqs:GetQueueAttributes',
                ],
                'Effect': 'Allow',
              },
            ],
          },
          roles = [
            'Amazon_EventBridge_Pipe_Execution_40238cd4',
          ],
          users = [
          ],
        )
    iamManagedPolicy00policyserviceroleSqsPipeSourceTemplate4ae0b53100mKqrk.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    sqsQueue00testqueue00rMvxl = sqs.CfnQueue(self, 'SQSQueue00testqueue00rMvxl',
          sqs_managed_sse_enabled = True,
          receive_message_wait_time_seconds = 0,
          delay_seconds = 0,
          message_retention_period = 345600,
          maximum_message_size = 262144,
          visibility_timeout = 30,
          queue_name = 'testqueue',
        )
    sqsQueue00testqueue00rMvxl.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    iamRole00AmazonEventBridgePipeExecution40238cd400fpYFk = iam.CfnRole(self, 'IAMRole00AmazonEventBridgePipeExecution40238cd400fpYFk',
          path = '/service-role/',
          managed_policy_arns = [
            iamManagedPolicy00policyserviceroleLambdaPipeTargetTemplate35ae232d00K2npc.ref,
            iamManagedPolicy00policyserviceroleSqsPipeSourceTemplate4ae0b53100mKqrk.ref,
          ],
          max_session_duration = 3600,
          role_name = 'Amazon_EventBridge_Pipe_Execution_40238cd4',
          assume_role_policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Condition': {
                  'StringEquals': {
                    'aws:SourceAccount': '619831221558',
                    'aws:SourceArn': 'arn:aws:pipes:eu-central-1:619831221558:pipe/eventBridge-pipe',
                  },
                },
                'Action': 'sts:AssumeRole',
                'Effect': 'Allow',
                'Principal': {
                  'Service': 'pipes.amazonaws.com',
                },
              },
            ],
          },
        )
    iamRole00AmazonEventBridgePipeExecution40238cd400fpYFk.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    iamRole00helloworldrolecmn3q4vc008WNcG = iam.CfnRole(self, 'IAMRole00helloworldrolecmn3q4vc008WNcG',
          path = '/service-role/',
          managed_policy_arns = [
            iamManagedPolicy00policyserviceroleAwsLambdaBasicExecutionRole68397c9137f047bab5a2535c46b23661003Rqu9.ref,
          ],
          max_session_duration = 3600,
          role_name = 'helloworld-role-cmn3q4vc',
          assume_role_policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Action': 'sts:AssumeRole',
                'Effect': 'Allow',
                'Principal': {
                  'Service': 'lambda.amazonaws.com',
                },
              },
            ],
          },
        )
    iamRole00helloworldrolecmn3q4vc008WNcG.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    lambdaFunction00helloworld00Y3Ryc = aws_lambda.CfnFunction(self, 'LambdaFunction00helloworld00Y3Ryc',
          memory_size = 128,
          description = '',
          tracing_config = {
            'mode': 'PassThrough',
          },
          timeout = 3,
          runtime_management_config = {
            'updateRuntimeOn': 'Auto',
          },
          handler = 'lambda_function.lambda_handler',
          props = {}  # Define the "props" variable
                    code = {
                      's3Bucket': props['lambdaFunction00helloworld00Y3RycCodeS3BucketOneOfT8EsW'].value_as_string,
                      's3Key': props['lambdaFunction00helloworld00Y3RycCodeS3KeyOneOfrnHIc'].value_as_string,
                    },
          role = iamRole00helloworldrolecmn3q4vc008WNcG.attr_arn,
          file_system_configs = [
          ],
          function_name = 'helloworld',
          runtime = 'python3.12',
          package_type = 'Zip',
          logging_config = {
            'logFormat': 'Text',
            'logGroup': '/aws/lambda/helloworld',
          },
          ephemeral_storage = {
            'size': 512,
          },
          architectures = [
            'x86_64',
          ],
        )
    lambdaFunction00helloworld00Y3Ryc.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    pipesPipe00eventBridgepipe0069JRv = pipes.CfnPipe(self, 'PipesPipe00eventBridgepipe0069JRv',
          target = lambdaFunction00helloworld00Y3Ryc.attr_arn,
          desired_state = 'RUNNING',
          log_configuration = {
            'includeExecutionData': [
            ],
            'cloudwatchLogsLogDestination': {
              'logGroupArn': 'arn:aws:logs:eu-central-1:619831221558:log-group:/aws/vendedlogs/pipes/eventBridge-pipe',
            },
            'level': 'ERROR',
          },
          enrichment_parameters = {
          },
          role_arn = iamRole00AmazonEventBridgePipeExecution40238cd400fpYFk.attr_arn,
          source = sqsQueue00testqueue00rMvxl.attr_arn,
          name = 'eventBridge-pipe',
        )
    pipesPipe00eventBridgepipe0069JRv.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN


