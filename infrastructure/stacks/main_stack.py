from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    CfnOutput,
    Duration,
    RemovalPolicy
)
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from constructs import Construct


class MainStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # DynamoDB Table for Events
        events_table = dynamodb.Table(
            self,
            "EventsTable",
            partition_key=dynamodb.Attribute(
                name="eventId",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,  # For dev/testing
            table_name="events"
        )

        # Lambda Function using PythonFunction for automatic dependency bundling
        api_lambda = PythonFunction(
            self,
            "EventsAPIFunction",
            entry="../backend",
            runtime=lambda_.Runtime.PYTHON_3_11,
            index="lambda_handler.py",
            handler="handler",
            timeout=Duration.seconds(30),
            memory_size=512,
            environment={
                "DYNAMODB_TABLE_NAME": events_table.table_name
                # AWS_REGION is automatically available in Lambda
            }
        )

        # Grant DynamoDB permissions to Lambda
        events_table.grant_read_write_data(api_lambda)

        # API Gateway
        api = apigateway.LambdaRestApi(
            self,
            "EventsAPI",
            handler=api_lambda,
            proxy=True,
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=apigateway.Cors.ALL_ORIGINS,
                allow_methods=apigateway.Cors.ALL_METHODS,
                allow_headers=["Content-Type", "Authorization", "Accept", "Origin"],
                allow_credentials=True
            ),
            description="Events Management API"
        )

        # Outputs
        CfnOutput(
            self,
            "APIEndpoint",
            value=api.url,
            description="API Gateway endpoint URL"
        )

        CfnOutput(
            self,
            "TableName",
            value=events_table.table_name,
            description="DynamoDB table name"
        )
