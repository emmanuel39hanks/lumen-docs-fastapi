# `POST /books/`

### Summary:
This endpoint is used to create a new book in the database. The book details are sent in the request body in JSON format.

### Endpoint:
- **Method**: `POST`
- **URL**: `https://api.example.com/books/`

### Headers:
- **Content-Type**: `application/json`

### Query Parameters:
This endpoint does not require any query parameters.

### Request Body:
The request body must be in JSON format and follow the schema defined in `#/components/schemas/BookCreate`. An example of a valid request body might look like this:

```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "publishedYear": 1925
}
```

### Expected Response:

#### Status Codes:
- `200`: The book was successfully created and the details of the new book are returned in the response body.
- `422`: There was a validation error with the request. The details of the error are returned in the response body.

#### Response Body (example):
If the request is successful, the response body will follow the schema defined in `#/components/schemas/BookRead`. An example of a successful response body might look like this:

```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "publishedYear": 1925
}
```

If there is a validation error, the response body will follow the schema defined in `#/components/schemas/HTTPValidationError`. An example of an error response body might look like this:

```json
{
  "detail": [
    {
      "loc": [
        "body",
        "publishedYear"
      ],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

### Example Request:
Here is an example of how to make a request to this endpoint using curl:

```bash
curl -X POST https://api.example.com/books/ \
-H 'Content-Type: application/json' \
-d '{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "publishedYear": 1925
}'
```

### Notes:
The `publishedYear` field in the request body must be an integer. If it is not, a validation error will be returned.