---
inclusion: fileMatch
fileMatchPattern: '*(main|api|routes|endpoints|handler)*.py'
---

# REST API Standards

Apply these REST API conventions when working with API code.

## HTTP Methods

- **GET**: Retrieve resources (idempotent, no body)
- **POST**: Create new resources (returns 201 with resource)
- **PUT**: Update entire resource (idempotent)
- **PATCH**: Partial update of resource
- **DELETE**: Remove resource (returns 204 or 200)

## Status Codes

### Success Codes
- `200 OK`: Successful GET, PUT, PATCH, or DELETE with response body
- `201 Created`: Successful POST, include Location header or resource in body
- `204 No Content`: Successful DELETE or update with no response body

### Client Error Codes
- `400 Bad Request`: Invalid request body or parameters
- `404 Not Found`: Resource doesn't exist
- `422 Unprocessable Entity`: Validation errors

### Server Error Codes
- `500 Internal Server Error`: Unexpected server errors

## Error Response Format

All error responses should follow this structure:

```json
{
  "detail": "Human-readable error message",
  "errors": [
    {
      "field": "field.name",
      "message": "Specific validation error",
      "type": "error_type"
    }
  ]
}
```

For simple errors, just use:
```json
{
  "detail": "Error message"
}
```

## JSON Response Standards

### Naming Conventions
- Use camelCase for JSON keys (e.g., `eventId`, `firstName`)
- Be consistent across all endpoints

### Response Structure
- Return objects for single resources: `{ "id": 1, "name": "..." }`
- Return arrays for collections: `[{ "id": 1 }, { "id": 2 }]`
- Include relevant metadata when needed

### Timestamps
- Use ISO 8601 format: `2024-12-15T10:30:00Z`
- Be consistent with timezone handling

## Query Parameters

- Use query parameters for filtering: `GET /events?status=active`
- Use query parameters for pagination: `GET /events?page=1&limit=20`
- Use query parameters for sorting: `GET /events?sort=date&order=desc`

## CORS

- Configure CORS appropriately for web access
- Specify allowed origins, methods, and headers
- Include credentials support if needed

## Validation

- Validate all input data using Pydantic models
- Return 422 status code with detailed validation errors
- Include field names and error types in validation responses

## Best Practices

- Keep endpoints RESTful and resource-oriented
- Use plural nouns for collections: `/events` not `/event`
- Use path parameters for resource IDs: `/events/{id}`
- Return appropriate status codes consistently
- Include proper error messages for debugging
