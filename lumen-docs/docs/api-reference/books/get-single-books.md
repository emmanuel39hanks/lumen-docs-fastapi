# `GET /books/{book_id}`

### Summary:
This endpoint is used to retrieve the details of a specific book from the database. The book is identified by its unique `book_id` which is passed as a path parameter in the URL.

### Endpoint:
- **Method**: `GET`
- **URL**: `https://api.example.com/books/{book_id}`

### Headers:
- **Content-Type**: `application/json`

### Path Parameters:
- **book_id**: This is a required parameter. It is an integer that uniquely identifies a book in the database.

### Request Body:
This endpoint does not require a request body.

### Expected Response:

#### Status Codes:
- **200**: Successful Response. This means that the book details were successfully retrieved from the database.
- **422**: Validation Error. This means that the provided `book_id` was not valid or did not match any book in the database.

#### Response Body (example):
The response body will be in JSON format and will contain the details of the book. The exact structure of this JSON will be defined by the `BookRead` schema.

### Example Request:
Here is an example of how to make a request to this endpoint using curl:

```bash
curl -X GET "https://api.example.com/books/123" -H "Content-Type: application/json"
```

In this example, `123` is the `book_id` of the book we want to retrieve.

### Notes:
Please ensure that the `book_id` provided in the URL is valid and corresponds to an existing book in the database. If the `book_id` is not valid, a `422` status code will be returned along with an error message detailing the validation error.