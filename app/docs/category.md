Category API Specification

Find All Categories

Endpoint: GET /api/categories
Response Body (Success):

```json
{
  "data": [
    {
      "name": "elektronik"
    }
  ]
}
```

Response Body (Failed):

```json
{
  "message": "Categories Not Found"
}
```

Find One Category

Endpoint: GET /api/categories/:categoryid
Response Body (Success):

```json
{
  "name": "elektronik"
}
```

Response Body (Failed):

```json
{
  "message": "Category Not Found"
}
```

Create Category
Endpoint: POST /api/categories
Request Body:

```json
{
  "title": "elektronik"
}
```

Response Body (Success):

```json
{
  "title": "elektronik"
}
```

Response Body (Failed):

```json
{
  "message": "Category Not Found"
}
```

Edit Category
Endpoint: PUT /api/categories
Request Body:

```json
{
  "title": "elektronik"
}
```

Response Body (Success):

```json
{
  "title": "elektronik"
}
```

Response Body (Failed):

```json
{
  "message": "Category Not Found"
}
```

Delete Category
Endpoint: DELETE /api/categories
Response Body (Success):

```json
{
  "message": "OK"
}
```
