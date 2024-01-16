## review API Spec

## findAll review

-- Endpoint : GET /api/category

Respone Body (Success)

```json
{
  "data": [
    {
      "ratting": 2,
      "comment":

    }
  ]
}
```

Respone Body (Faild)

```json
{
  "message": "review Not Found"
}
```

## find One review

-- Endpoint : GET /api/category/:productid

Respone Body (Success)

```json
{
  "id": 1,
  "ratting": 2,
  "comment": "System check identified no issues (0 silenced)."
}
```

Respone Body (Faild)

```json
{
  "message": "review Not Found"
}
```

## create-Prouduct

-- Endpoint : POST /api/category

Request Body :

```json
{
  "ratting": 2,
  "comment": "System check identified no issues (0 silenced)."
}
```

Respone Body (Success)

```json
{
  "ratting": 2,
  "comment": "System check identified no issues (0 silenced)."
}
```

Respone Body (Faild)

```json
{
  "message": "review Not Found"
}
```

## Edit review

-- Endpoint : PUT /api/category

Request Body :

```json
{
  "ratting": 2,
  "comment": "System check identified no issues (0 silenced)."
}
```

Respone Body (Success)

```json
{
  "ratting": 2,
  "comment": "System check identified no issues (0 silenced)."
}
```

Respone Body (Faild)

```json
{
  "message": "review Not Found"
}
```

## Delete-prodcut

-- Endpoint : Delete /api/category

Response Body (Success)

```json
{
  "message": "OK"
}
```
