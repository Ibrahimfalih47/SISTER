## items API Spec

## findAll items

-- Endpoint : GET /api/products

Respone Body (Success)

```json
{
  "data": [
    {
      "title": "product",
      "description": "product stroong"
    }
  ]
}
```

Respone Body (Faild)

```json
{
  "message": "items Not Found"
}
```

## find One items

-- Endpoint : GET /api/products/:productid

Respone Body (Success)

```json
{
  "title": "product",
  "description": "product stroong"
}
```

Respone Body (Faild)

```json
{
  "message": "items Not Found"
}
```

## create-Prouduct

-- Endpoint : POST /api/products

Request Body :

```json
{
  "title": "product",
  "description": "product stroong"
}
```

Respone Body (Success)

```json
{
  "title": "product",
  "description": "product stroong"
}
```

Respone Body (Faild)

```json
{
  "message": "items Not Found"
}
```

## Edit items

-- Endpoint : PUT /api/products

Request Body :

```json
{
  "title": "product",
  "description": "product stroong"
}
```

Respone Body (Success)

```json
{
  "title": "product",
  "description": "product stroong"
}
```

Respone Body (Faild)

```json
{
  "message": "items Not Found"
}
```

## Delete-prodcut

-- Endpoint : Delete /api/products

Response Body (Success)

```json
{
  "message": "OK"
}
```
