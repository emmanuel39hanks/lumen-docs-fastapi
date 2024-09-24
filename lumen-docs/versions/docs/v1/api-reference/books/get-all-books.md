# `GET /books/`

### Summary:
This endpoint is used to retrieve a list of books from the server. The list can be manipulated by using the 'skip' and 'limit' parameters to control the number of books returned and the starting point in the list.

### Endpoint:
- **Method**: `GET`
- **URL**: `https://api.example.com/books/`

### Headers:
- **Content-Type**: `application/json`

### Query Parameters:
- **skip**: This optional parameter is an integer that determines the number of books to skip before starting to return entries. The default value is 0.
- **limit**: This optional parameter is an integer that limits the number of books to be returned. The default value is 10.

### Request Body:
This endpoint does not require a request body.

### Expected Response:

#### Status Codes:
- **200**: Successful Response. The server successfully processed the request and returned the requested list of books.
- **422**: Validation Error. The server was unable to process the request due to a validation error, such as an invalid value for the 'skip' or 'limit' parameter.

#### Response Body (example):
The response body will be a JSON array of books, with each book represented as a JSON object. The exact structure of these objects is defined in the `BookRead` schema.

```json
[
  {
    "title": "Book Title 1",
    "author": "Author Name 1",
    "publicationYear": 2001
  },
  {
    "title": "Book Title 2",
    "author": "Author Name 2",
    "publicationYear": 2002
  }
]
```

### Example Request:
Here is an example of how to make a request to this endpoint using curl:

```bash
curl -X GET "https://api.example.com/books/?skip=10&limit=5" -H "Content-Type: application/json"
```

### Notes:
The 'skip' and 'limit' parameters are useful for implementing pagination in your application. By adjusting these parameters, you can control which segment of the book list is returned by the server.