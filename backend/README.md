# Backend - FastAPI Application

Event Management API with CRUD operations backed by DynamoDB.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your AWS configuration
```

3. Ensure DynamoDB table exists with `eventId` as the partition key.

## Run

```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

### Interactive Documentation

Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Static Documentation

Static HTML documentation is available in the `docs/` folder. Open `docs/index.html` in your browser to view:
- Module documentation for `main.py`, `models.py`, and `database.py`
- Function signatures and docstrings
- Type annotations and parameter descriptions

To regenerate the documentation:
```bash
pdoc main.py models.py database.py -o docs/
```

## API Endpoints

### Events

- `POST /events` - Create a new event
- `GET /events` - List all events (supports `?status=<value>` query parameter)
- `GET /events/{event_id}` - Get a specific event
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

## Project Structure

```
backend/
├── main.py              # FastAPI application with API endpoints
├── models.py            # Pydantic models for request/response validation
├── database.py          # DynamoDB client and operations
├── lambda_handler.py    # AWS Lambda entry point using Mangum
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── docs/                # Generated API documentation (HTML)
└── README.md            # This file
```

## Modules

### main.py
Contains the FastAPI application with all REST API endpoints, CORS configuration, error handlers, and logging setup.

### models.py
Defines Pydantic models for data validation:
- `EventBase`: Base event fields
- `EventCreate`: Model for creating events
- `EventUpdate`: Model for updating events (all fields optional)
- `Event`: Complete event model with eventId

### database.py
DynamoDB client wrapper with methods:
- `create_event()`: Create a new event
- `get_event()`: Retrieve an event by ID
- `list_events()`: List all events with optional status filter
- `update_event()`: Update event fields
- `delete_event()`: Delete an event

### lambda_handler.py
AWS Lambda handler that wraps the FastAPI app using Mangum for serverless deployment.

## Local Development with DynamoDB Local

To test locally without AWS:

1. Run DynamoDB Local:
```bash
docker run -p 8000:8000 amazon/dynamodb-local
```

2. Create the table:
```bash
aws dynamodb create-table \
    --table-name events \
    --attribute-definitions AttributeName=eventId,AttributeType=S \
    --key-schema AttributeName=eventId,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --endpoint-url http://localhost:8000
```

3. Set `DYNAMODB_ENDPOINT_URL=http://localhost:8000` in your .env file

## Features

- ✅ Full CRUD operations
- ✅ Input validation with Pydantic
- ✅ Query parameter filtering (by status)
- ✅ Proper error handling and logging
- ✅ CORS support
- ✅ DynamoDB reserved keyword handling
- ✅ AWS Lambda compatible (via Mangum)
- ✅ Comprehensive API documentation
