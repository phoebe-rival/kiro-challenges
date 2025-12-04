# Kiro Challenges - Event Management System

A serverless event management application built with FastAPI, AWS Lambda, API Gateway, and DynamoDB.

## Project Overview

This project provides a REST API for managing events with full CRUD operations. Events are stored in DynamoDB and the API is deployed as a serverless application using AWS Lambda and API Gateway.

## Architecture

- **Backend**: FastAPI REST API
- **Database**: AWS DynamoDB
- **Compute**: AWS Lambda (Python 3.11)
- **API Gateway**: AWS API Gateway (REST API)
- **Infrastructure**: AWS CDK (Python)

## Project Structure

```
kiro-challenges/
├── backend/              # FastAPI application
│   ├── main.py          # API endpoints
│   ├── models.py        # Pydantic models
│   ├── database.py      # DynamoDB client
│   ├── lambda_handler.py # Lambda entry point
│   └── requirements.txt # Python dependencies
├── infrastructure/       # AWS CDK infrastructure
│   ├── app.py           # CDK app entry point
│   └── stacks/          # CDK stack definitions
└── README.md            # This file
```

## API Endpoints

**Base URL**: `https://dz8jlmj7je.execute-api.us-east-1.amazonaws.com/prod/`

### Events

- `GET /events` - List all events (supports `?status=<status>` query parameter)
- `GET /events/{event_id}` - Get a specific event
- `POST /events` - Create a new event
- `PUT /events/{event_id}` - Update an event
- `DELETE /events/{event_id}` - Delete an event

### Event Schema

```json
{
  "eventId": "string (optional on create, auto-generated if not provided)",
  "title": "string (required, 1-200 chars)",
  "description": "string (required, max 1000 chars)",
  "date": "string (required, ISO format)",
  "location": "string (required, 1-200 chars)",
  "capacity": "integer (required, > 0)",
  "organizer": "string (required, 1-100 chars)",
  "status": "string (required, 1-50 chars, e.g., 'active', 'draft', 'cancelled')"
}
```

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 20+ (for AWS CDK)
- AWS CLI configured with appropriate credentials
- Docker (for CDK bundling)

### Local Development

1. **Install backend dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Run locally** (requires DynamoDB Local or AWS credentials):
   ```bash
   uvicorn main:app --reload
   ```

4. **Access API documentation**:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Deployment

1. **Install infrastructure dependencies**:
   ```bash
   cd infrastructure
   pip install -r requirements.txt
   npm install -g aws-cdk
   ```

2. **Bootstrap CDK** (first time only):
   ```bash
   cdk bootstrap
   ```

3. **Deploy**:
   ```bash
   cdk deploy
   ```

4. **Get the API endpoint**:
   The deployment will output the API Gateway URL.

## API Usage Examples

### Create an Event

```bash
curl -X POST https://dz8jlmj7je.execute-api.us-east-1.amazonaws.com/prod/events \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Tech Conference 2024",
    "description": "Annual technology conference",
    "date": "2024-12-15",
    "location": "San Francisco, CA",
    "capacity": 500,
    "organizer": "Tech Events Inc",
    "status": "active"
  }'
```

### List All Events

```bash
curl https://dz8jlmj7je.execute-api.us-east-1.amazonaws.com/prod/events
```

### Filter Events by Status

```bash
curl https://dz8jlmj7je.execute-api.us-east-1.amazonaws.com/prod/events?status=active
```

### Get a Specific Event

```bash
curl https://dz8jlmj7je.execute-api.us-east-1.amazonaws.com/prod/events/{event_id}
```

### Update an Event

```bash
curl -X PUT https://dz8jlmj7je.execute-api.us-east-1.amazonaws.com/prod/events/{event_id} \
  -H "Content-Type: application/json" \
  -d '{
    "capacity": 600,
    "status": "published"
  }'
```

### Delete an Event

```bash
curl -X DELETE https://dz8jlmj7je.execute-api.us-east-1.amazonaws.com/prod/events/{event_id}
```

## Features

- ✅ Full CRUD operations for events
- ✅ Input validation with Pydantic
- ✅ Proper error handling and logging
- ✅ CORS support for web applications
- ✅ Query parameter filtering (by status)
- ✅ DynamoDB reserved keyword handling
- ✅ Serverless deployment with AWS Lambda
- ✅ Auto-scaling with API Gateway and DynamoDB on-demand billing

## Development

### Running Tests Locally

For local testing with DynamoDB Local:

```bash
# Start DynamoDB Local
docker run -p 8000:8000 amazon/dynamodb-local

# Create the table
aws dynamodb create-table \
    --table-name events \
    --attribute-definitions AttributeName=eventId,AttributeType=S \
    --key-schema AttributeName=eventId,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --endpoint-url http://localhost:8000

# Set environment variable
export DYNAMODB_ENDPOINT_URL=http://localhost:8000
```

### API Documentation

API documentation is automatically generated and available at:
- `/docs` - Interactive Swagger UI
- `/redoc` - ReDoc documentation
- `backend/docs/` - Static HTML documentation (generated with pdoc)

To regenerate the static documentation:
```bash
cd backend
pdoc main.py models.py database.py -o docs/
```

## Infrastructure

The infrastructure is defined using AWS CDK and includes:

- **DynamoDB Table**: `events` table with `eventId` as partition key
- **Lambda Function**: Python 3.11 runtime with 512MB memory
- **API Gateway**: REST API with CORS enabled
- **IAM Roles**: Least-privilege permissions for Lambda to access DynamoDB

## Troubleshooting

### Common Issues

1. **CORS errors**: Ensure the API Gateway CORS settings match your frontend origin
2. **DynamoDB access denied**: Check Lambda execution role has proper permissions
3. **Validation errors**: Ensure request body matches the Event schema

### Logs

View Lambda logs in CloudWatch:
```bash
aws logs tail /aws/lambda/KiroChallengesStack-EventsAPIFunction --follow
```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
