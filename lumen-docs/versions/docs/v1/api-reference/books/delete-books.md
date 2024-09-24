# `DELETE /books/{book_id}`

### Summary:
This endpoint is used to delete a book from the database. The book is identified by its unique ID, which is passed as a parameter in the URL.

### Endpoint:
- **Method**: `DELETE`
- **URL**: `https://api.example.com/books/{book_id}`

### Headers:
- **Content-Type**: `application/json`

### Query Parameters:
No query parameters are required for this endpoint.

### Request Body:
This endpoint does not require a request body.

### Expected Response:

#### Status Codes:
- `200`: The book was successfully deleted. The response body will contain a reference to the deleted book's schema.
- `422`: There was a validation error. This could occur if the book_id provided does not exist in the database. The response body will contain details about the validation error.

#### Response Body (example):
For a successful deletion:
```json
{
  "message": "Book successfully deleted",
  "book_id": 123
}
```
For a validation error:
```json
{
  "detail": [
    {
      "loc": [
        "path",
        "book_id"
      ],
      "msg": "Book with this ID does not exist",
      "type": "value_error"
    }
  ]
}
```

### Example Request:
Here is an example of how to make a request to this endpoint using curl:
```bash
curl -X DELETE https://api.example.com/books/123 -H 'Content-Type: application/json'
```

### Notes:
Please ensure that the book_id provided in the URL is valid and exists in the database. If the book_id does not exist, a validation error will be returned.