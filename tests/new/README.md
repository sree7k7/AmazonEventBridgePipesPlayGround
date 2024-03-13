
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


## Warnings
### Write-only properties
Write-only properties are resource property values that can be written to but can't be read by AWS CloudFormation or CDK Migrate. For more information, see [IaC generator and write-only properties](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC-write-only-properties.html).


Write-only properties discovered during migration are organized here by resource ID and categorized by write-only property type. Resolve write-only properties by providing property values in your CDK app. For guidance, see [Resolve write-only properties](https://docs.aws.amazon.com/cdk/v2/guide/migrate.html#migrate-resources-writeonly).
### LambdaFunction00helloworld00Y3Ryc
- **UNSUPPORTED_PROPERTIES**: 
  - SnapStart/ApplyOn: Set ``ApplyOn`` to ``PublishedVersions`` to create a snapshot of the initialized execution environment when you publish a function version.Possible values: [PublishedVersions, None]
This property can be replaced with other types
  - Code/S3ObjectVersion: For versioned objects, the version of the deployment package object to use.
This property can be replaced with other exclusive properties
- **MUTUALLY_EXCLUSIVE_PROPERTIES**: 
  - Code/S3Bucket: An Amazon S3 bucket in the same AWS-Region as your function. The bucket can be in a different AWS-account.
This property can be replaced with other exclusive properties
  - Code/S3Key: The Amazon S3 key of the deployment package.
This property can be replaced with other exclusive properties
### PipesPipe00eventBridgepipe0069JRv
- **UNSUPPORTED_PROPERTIES**: 
  - SourceParameters/ManagedStreamingKafkaParameters/BatchSize: 
  - SourceParameters/SelfManagedKafkaParameters/ConsumerGroupID: 
  - TargetParameters/LambdaFunctionParameters/InvocationType: Possible values: [REQUEST_RESPONSE, FIRE_AND_FORGET]
This property can be replaced with other types
  - TargetParameters/SqsQueueParameters/MessageDeduplicationId: 
  - SourceParameters/SelfManagedKafkaParameters/AdditionalBootstrapServers: 
  - TargetParameters/EcsTaskParameters/PlacementStrategy: 
  - TargetParameters/RedshiftDataParameters/StatementName: A name for Redshift DataAPI statement which can be used as filter of ListStatement.
  - SourceParameters/KinesisStreamParameters/MaximumRecordAgeInSeconds: 
  - TargetParameters/CloudWatchLogsParameters/Timestamp: 
  - TargetParameters/EcsTaskParameters/NetworkConfiguration/AwsvpcConfiguration/Subnets: 
  - SourceParameters/KinesisStreamParameters/ParallelizationFactor: 
  - TargetParameters/SageMakerPipelineParameters/PipelineParameterList: 
  - TargetParameters/EcsTaskParameters/PropagateTags: Possible values: [TASK_DEFINITION]
This property can be replaced with other types
  - SourceParameters/SelfManagedKafkaParameters/BatchSize: 
  - SourceParameters/RabbitMQBrokerParameters/VirtualHost: 
  - SourceParameters/SqsQueueParameters/MaximumBatchingWindowInSeconds: 
  - TargetParameters/EventBridgeEventBusParameters/Source: 
  - SourceParameters/KinesisStreamParameters/MaximumBatchingWindowInSeconds: 
  - SourceParameters/SelfManagedKafkaParameters/StartingPosition: Possible values: [TRIM_HORIZON, LATEST]
This property can be replaced with other types
  - SourceParameters/KinesisStreamParameters/DeadLetterConfig/Arn: 
  - SourceParameters/DynamoDBStreamParameters/BatchSize: 
  - TargetParameters/RedshiftDataParameters/Database: Redshift Database
  - TargetParameters/EcsTaskParameters/NetworkConfiguration/AwsvpcConfiguration/SecurityGroups: 
  - TargetParameters/InputTemplate: 
  - TargetParameters/BatchJobParameters/DependsOn: 
  - SourceParameters/DynamoDBStreamParameters/MaximumRetryAttempts: 
  - SourceParameters/FilterCriteria/Filters: 
  - TargetParameters/RedshiftDataParameters/SecretManagerArn: Optional SecretManager ARN which stores the database credentials
  - SourceParameters/KinesisStreamParameters/OnPartialBatchItemFailure: Possible values: [AUTOMATIC_BISECT]
This property can be replaced with other types
  - SourceParameters/ManagedStreamingKafkaParameters/ConsumerGroupID: 
  - SourceParameters/ActiveMQBrokerParameters/BatchSize: 
  - TargetParameters/EcsTaskParameters/PlacementConstraints: 
  - TargetParameters/KinesisStreamParameters/PartitionKey: 
  - SourceParameters/SelfManagedKafkaParameters/Credentials: 
  - SourceParameters/KinesisStreamParameters/StartingPositionTimestamp: 
  - TargetParameters/EcsTaskParameters/Overrides/InferenceAcceleratorOverrides: 
  - SourceParameters/RabbitMQBrokerParameters/BatchSize: 
  - SourceParameters/KinesisStreamParameters/BatchSize: 
  - TargetParameters/EcsTaskParameters/Overrides/Memory: 
  - TargetParameters/BatchJobParameters/ContainerOverrides/Environment: 
  - SourceParameters/ActiveMQBrokerParameters/MaximumBatchingWindowInSeconds: 
  - SourceParameters/ManagedStreamingKafkaParameters/Credentials: 
  - SourceParameters/DynamoDBStreamParameters/MaximumRecordAgeInSeconds: 
  - TargetParameters/EventBridgeEventBusParameters/Resources: 
  - TargetParameters/EcsTaskParameters/TaskCount: 
  - TargetParameters/EcsTaskParameters/Overrides/TaskRoleArn: 
  - SourceParameters/ManagedStreamingKafkaParameters/StartingPosition: Possible values: [TRIM_HORIZON, LATEST]
This property can be replaced with other types
  - TargetParameters/EcsTaskParameters/Overrides/EphemeralStorage/SizeInGiB: 
  - TargetParameters/EcsTaskParameters/LaunchType: Possible values: [EC2, FARGATE, EXTERNAL]
This property can be replaced with other types
  - TargetParameters/EcsTaskParameters/TaskDefinitionArn: 
  - TargetParameters/EventBridgeEventBusParameters/DetailType: 
  - SourceParameters/RabbitMQBrokerParameters/Credentials: 
  - SourceParameters/DynamoDBStreamParameters/DeadLetterConfig/Arn: 
  - SourceParameters/ActiveMQBrokerParameters/Credentials: 
  - TargetParameters/BatchJobParameters/ContainerOverrides/ResourceRequirements: 
  - TargetParameters/BatchJobParameters/ContainerOverrides/InstanceType: 
  - TargetParameters/HttpParameters/PathParameterValues: 
  - TargetParameters/BatchJobParameters/ArrayProperties/Size: 
  - TargetParameters/CloudWatchLogsParameters/LogStreamName: 
  - TargetParameters/EcsTaskParameters/Overrides/ContainerOverrides: 
  - TargetParameters/BatchJobParameters/RetryStrategy/Attempts: 
  - SourceParameters/ManagedStreamingKafkaParameters/MaximumBatchingWindowInSeconds: 
  - SourceParameters/RabbitMQBrokerParameters/QueueName: 
  - SourceParameters/SelfManagedKafkaParameters/ServerRootCaCertificate: Optional SecretManager ARN which stores the database credentials
  - SourceParameters/DynamoDBStreamParameters/ParallelizationFactor: 
  - TargetParameters/BatchJobParameters/JobDefinition: 
  - TargetParameters/RedshiftDataParameters/Sqls: A list of SQLs.
  - TargetParameters/EcsTaskParameters/NetworkConfiguration/AwsvpcConfiguration/AssignPublicIp: Possible values: [ENABLED, DISABLED]
This property can be replaced with other types
  - SourceParameters/RabbitMQBrokerParameters/MaximumBatchingWindowInSeconds: 
  - TargetParameters/StepFunctionStateMachineParameters/InvocationType: Possible values: [REQUEST_RESPONSE, FIRE_AND_FORGET]
This property can be replaced with other types
  - TargetParameters/EcsTaskParameters/Tags: 
  - SourceParameters/SelfManagedKafkaParameters/Vpc/SecurityGroup: List of SecurityGroupId.
  - SourceParameters/SelfManagedKafkaParameters/Vpc/Subnets: List of SubnetId.
  - TargetParameters/EventBridgeEventBusParameters/EndpointId: 
  - TargetParameters/EcsTaskParameters/Group: 
  - SourceParameters/DynamoDBStreamParameters/OnPartialBatchItemFailure: Possible values: [AUTOMATIC_BISECT]
This property can be replaced with other types
  - TargetParameters/SqsQueueParameters/MessageGroupId: 
  - SourceParameters/ManagedStreamingKafkaParameters/TopicName: 
  - SourceParameters/DynamoDBStreamParameters/MaximumBatchingWindowInSeconds: 
  - TargetParameters/RedshiftDataParameters/WithEvent: 
  - SourceParameters/SqsQueueParameters/BatchSize: 
  - SourceParameters/KinesisStreamParameters/StartingPosition: Possible values: [TRIM_HORIZON, LATEST, AT_TIMESTAMP]
This property can be replaced with other types
  - TargetParameters/EcsTaskParameters/EnableECSManagedTags: 
  - SourceParameters/DynamoDBStreamParameters/StartingPosition: Possible values: [TRIM_HORIZON, LATEST]
This property can be replaced with other types
  - TargetParameters/EventBridgeEventBusParameters/Time: 
  - TargetParameters/BatchJobParameters/JobName: 
  - TargetParameters/EcsTaskParameters/EnableExecuteCommand: 
  - SourceParameters/SelfManagedKafkaParameters/MaximumBatchingWindowInSeconds: 
  - TargetParameters/EcsTaskParameters/Overrides/ExecutionRoleArn: 
  - TargetParameters/EcsTaskParameters/CapacityProviderStrategy: 
  - TargetParameters/EcsTaskParameters/Overrides/Cpu: 
  - SourceParameters/SelfManagedKafkaParameters/TopicName: 
  - TargetParameters/EcsTaskParameters/PlatformVersion: 
  - TargetParameters/BatchJobParameters/ContainerOverrides/Command: 
  - SourceParameters/KinesisStreamParameters/MaximumRetryAttempts: 
  - TargetParameters/RedshiftDataParameters/DbUser: Database user name
  - SourceParameters/ActiveMQBrokerParameters/QueueName: 
  - TargetParameters/EcsTaskParameters/ReferenceId: 
Enjoy!
