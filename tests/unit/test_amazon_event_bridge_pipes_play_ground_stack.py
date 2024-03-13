import aws_cdk as core
import aws_cdk.assertions as assertions

from amazon_event_bridge_pipes_play_ground.amazon_event_bridge_pipes_play_ground_stack import AmazonEventBridgePipesPlayGroundStack

# example tests. To run these tests, uncomment this file along with the example
# resource in amazon_event_bridge_pipes_play_ground/amazon_event_bridge_pipes_play_ground_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AmazonEventBridgePipesPlayGroundStack(app, "amazon-event-bridge-pipes-play-ground")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
