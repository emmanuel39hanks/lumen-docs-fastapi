# Making Requests

This guide explains how to structure and send requests to our API.

## Base URL

All API requests should be made to:

```
https://api.example.com/v1
```

## Request Format

Our API accepts JSON-encoded request bodies. Set the following headers for your requests:

- `Content-Type: application/json`
- `Authorization: Bearer YOUR_API_KEY`

## Common HTTP Methods

- GET: Retrieve resources
- POST: Create new resources
- PUT: Update existing resources
- DELETE: Remove resources

## Example Request

Here's an example of how to make a GET request to retrieve a list of items:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" https://api.example.com/v1/items
```

## Handling Responses

Our API returns JSON-encoded responses. Always check the HTTP status code to determine the outcome of your request.

## Rate Limiting

To ensure fair usage, our API implements rate limiting. Check the `X-RateLimit-Remaining` header in the API response to monitor your current rate limit status.

## Next Steps

Explore our API Reference section for detailed information on all available endpoints and operations.