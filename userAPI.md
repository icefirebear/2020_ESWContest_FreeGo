# user table 관련 API 명세

## 기기 등록

```
    POST /register
```

- Request

```
{
    "id" : "내 냉장고1",
    "pwd" : "password"
}
```

- Response

```
{
    SUCCESS { "code" : 200, "message": "register success" }
    FAIL { "code" : 400, "message" : "fail" }
}
```

## 기기 존재 확인

```
    GET /finduser/{id}
```

- Request

```

```

- Response

```
{
    SUCCESS already existed { "code" : 200, "message": "existed" }
    SUCCESS not exist {"code" : 404, "message": "not exist"}
    FAIL { "code" : 400, "message" : "fail" }
}
```