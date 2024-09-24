# `PUT /books/{book_id}`

### Summary:
This endpoint is used to update the details of a specific book in the database. The book is identified by its unique `book_id`. The updated details of the book are provided in the request body in JSON format.

### Endpoint:
- **Method**: `PUT`
- **URL**: `https://api.example.com/books/{book_id}`

### Headers:
- **Content-Type**: `application/json`

### Path Parameters:
- **book_id** (required): The unique identifier of the book to be updated. This is an integer value.

### Request Body:
The request body must be in JSON format and follow the schema defined in `#/components/schemas/BookUpdate`. An example of the request body might look like this:

```json
{
  "title": "Updated Book Title",
  "author": "Updated Author Name",
  "published_date": "2022-01-01",
  "isbn": "123-4567890123"
}
```

### Expected Response:

#### Status Codes:
- **200**: The book was successfully updated. The response body will contain the updated details of the book.
- **422**: There was a validation error with the request. The response body will contain details about the validation errors.

#### Response Body (example):
On a successful update (200 status code), the response might look like this:

```json
{
  "id": 1,
  "title": "Updated Book Title",
  "author": "Updated Author Name",
  "published_date": "2022-01-01",
  "isbn": "123-4567890123"
}
```

On a validation error (422 status code), the response might look like this:

```json
{
  "detail": [
    {
      "loc": [
        "body",
        "isbn"
      ],
      "msg": "value is not a valid isbn",
      "type": "type_error.isbn"
    }
  ]
}
```

### Example Request:
Here is an example of how to make a request to this endpoint using curl:

```bash
curl -X PUT 'https://api.example.com/books/1' \
-H 'Content-Type: application/json' \
-d '{
  "title": "Updated Book Title",
  "author": "Updated Author Name",
  "published_date": "2022-01-01",
  "isbn": "123-4567890123"
}'
```

### Notes:
Ensure that the `book_id` in the URL and the details in the request body are correct. If the `book_id` does not exist in the database, or if the request body does not match the `BookUpdate` schema, the request will fail with a 422 status code.