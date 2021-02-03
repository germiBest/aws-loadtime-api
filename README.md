# aws-loadtime-api

# API

- [POST]
body in type `application\json`
Example:
```json
{
  "links": [
    "https://google.com",
    "https://github.com"
  ]
}
```

Response:

```json
{
  "statusCode": 200,
  "body": {
    "https://google.com": 0.26179373264312744,
    "https://github.com": 0.10623228549957275
  }
}
```
