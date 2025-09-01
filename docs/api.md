# API Reference

This document provides detailed information about the CDE550-sim API.

## Table of Contents

- [Authentication](#authentication)
- [Endpoints](#endpoints)
- [Data Types](#data-types)
- [Error Handling](#error-handling)
- [Rate Limiting](#rate-limiting)
- [Versioning](#versioning)
- [Examples](#examples)

## Authentication

All API requests require an API key for authentication.

```http
GET /api/endpoint
Authorization: Bearer your_api_key_here
```

## Endpoints

### 1. GET /api/status

Get the current status of the application.

**Request:**
```http
GET /api/status
```

**Response:**
```json
{
  "status": "operational",
  "version": "1.0.0",
  "timestamp": "2025-09-01T19:10:16Z"
}
```

### 2. POST /api/simulate

Run a simulation with the provided parameters.

**Request:**
```http
POST /api/simulate
Content-Type: application/json

{
  "parameters": {
    "param1": "value1",
    "param2": 42
  },
  "options": {
    "timeout": 60,
    "precision": 0.001
  }
}
```

**Response:**
```json
{
  "simulation_id": "sim_12345",
  "status": "completed",
  "results": {
    "result1": 3.14159,
    "result2": [1, 2, 3, 4, 5]
  },
  "metadata": {
    "duration_ms": 1245,
    "timestamp": "2025-09-01T19:10:17Z"
  }
}
```

## Data Types

### Simulation Parameters

| Field | Type | Description |
|-------|------|-------------|
| param1 | string | Description of param1 |
| param2 | number | Description of param2 |

### Simulation Results

| Field | Type | Description |
|-------|------|-------------|
| result1 | number | Description of result1 |
| result2 | number[] | Array of result values |

## Error Handling

### Error Response Format

```json
{
  "error": {
    "code": "error_code",
    "message": "Human-readable error message",
    "details": {
      "field1": "Additional error details"
    }
  }
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| invalid_request | 400 | Invalid request parameters |
| unauthorized | 401 | Missing or invalid API key |
| not_found | 404 | Resource not found |
| rate_limited | 429 | Too many requests |
| server_error | 500 | Internal server error |

## Rate Limiting

- 60 requests per minute per API key
- Exceeding the limit returns a 429 status code
- Check rate limit headers in responses:
  - `X-RateLimit-Limit`: Maximum requests allowed
  - `X-RateLimit-Remaining`: Remaining requests in window
  - `X-RateLimit-Reset`: Time when limit resets (UTC epoch seconds)

## Versioning

API version is included in the URL path:
```
/api/v1/endpoint
```

## Examples

### Python Example

```python
import requests

url = "https://api.example.com/v1/simulate"
api_key = "your_api_key_here"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "parameters": {
        "param1": "value1",
        "param2": 42
    }
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
```

### cURL Example

```bash
curl -X POST https://api.example.com/v1/simulate \
  -H "Authorization: Bearer your_api_key_here" \
  -H "Content-Type: application/json" \
  -d '{"parameters":{"param1":"value1","param2":42}}'
```
