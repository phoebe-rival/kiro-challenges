import boto3
from botocore.exceptions import ClientError
from typing import List, Optional
import uuid
import os


class DynamoDBClient:
    def __init__(self):
        self.table_name = os.getenv("DYNAMODB_TABLE_NAME", "events")
        self.dynamodb = boto3.resource(
            "dynamodb",
            region_name=os.getenv("AWS_REGION", "us-east-1"),
            endpoint_url=os.getenv("DYNAMODB_ENDPOINT_URL")  # For local development
        )
        self.table = self.dynamodb.Table(self.table_name)

    def create_event(self, event_data: dict) -> dict:
        """Create a new event in DynamoDB"""
        # Use provided eventId or generate new one
        if "eventId" not in event_data or not event_data["eventId"]:
            event_data["eventId"] = str(uuid.uuid4())
        
        try:
            self.table.put_item(Item=event_data)
            return event_data
        except ClientError as e:
            raise Exception(f"Error creating event: {e.response['Error']['Message']}")

    def get_event(self, event_id: str) -> Optional[dict]:
        """Get an event by ID"""
        try:
            response = self.table.get_item(Key={"eventId": event_id})
            return response.get("Item")
        except ClientError as e:
            raise Exception(f"Error getting event: {e.response['Error']['Message']}")

    def list_events(self, status_filter: Optional[str] = None) -> List[dict]:
        """List all events, optionally filtered by status"""
        try:
            if status_filter:
                # Use ExpressionAttributeNames to handle reserved keyword "status"
                response = self.table.scan(
                    FilterExpression="#status_attr = :status_val",
                    ExpressionAttributeNames={"#status_attr": "status"},
                    ExpressionAttributeValues={":status_val": status_filter}
                )
            else:
                response = self.table.scan()
            return response.get("Items", [])
        except ClientError as e:
            raise Exception(f"Error listing events: {e.response['Error']['Message']}")

    def update_event(self, event_id: str, update_data: dict) -> Optional[dict]:
        """Update an event"""
        if not update_data:
            return self.get_event(event_id)
        
        # Build update expression
        update_expr = "SET "
        expr_attr_values = {}
        expr_attr_names = {}
        
        for idx, (key, value) in enumerate(update_data.items()):
            if value is not None:
                attr_name = f"#{key}"
                attr_value = f":val{idx}"
                update_expr += f"{attr_name} = {attr_value}, "
                expr_attr_names[attr_name] = key
                expr_attr_values[attr_value] = value
        
        update_expr = update_expr.rstrip(", ")
        
        try:
            response = self.table.update_item(
                Key={"eventId": event_id},
                UpdateExpression=update_expr,
                ExpressionAttributeNames=expr_attr_names,
                ExpressionAttributeValues=expr_attr_values,
                ReturnValues="ALL_NEW"
            )
            return response.get("Attributes")
        except ClientError as e:
            raise Exception(f"Error updating event: {e.response['Error']['Message']}")

    def delete_event(self, event_id: str) -> bool:
        """Delete an event"""
        try:
            self.table.delete_item(Key={"eventId": event_id})
            return True
        except ClientError as e:
            raise Exception(f"Error deleting event: {e.response['Error']['Message']}")


# Singleton instance
db_client = DynamoDBClient()
