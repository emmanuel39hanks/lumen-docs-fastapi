# Authentication

Our API uses API keys for authentication. You must include your API key in every request to authenticate.

## Using Your API Key

Include your API key in the Authorization header of your HTTP requests:

```
Authorization: Bearer YOUR_API_KEY
```

Replace `YOUR_API_KEY` with the actual API key you obtained from our developer portal.

## Security Best Practices

- Keep your API key confidential
- Don't hardcode your API key in your source code
- Use environment variables or a secure key management system to store your API key
- Rotate your API key periodically for enhanced security

## Next Steps

Now that you understand how to authenticate your requests, move on to [Making Requests](making-requests.md) to learn how to interact with our API endpoints.