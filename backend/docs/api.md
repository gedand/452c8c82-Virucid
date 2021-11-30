# API endpoints


**Note:** Only login requires input in JSON, everything else needs to be passed as form-data.

**Note2:** `/download`, `/search`, `/comment`, and `/upload` needs to be used with valid JWT token, `/delete` with admin JWT token


- [Registration](#registration)
- [Login](#login)
- [Download](#download)
- [Search](#search)
- [Comment](#comment)
- [Upload](#upload)
- [Delete](#delete)

## Registration

POST `/registration`


The method requires both parameters:
```json
    "username": USERNAME,
    "password": PASSWORD
```

Returning value if everything is fine:
```json
    "status": "success",
    "message": "User USERNAME successfully registered"
```

In case of error, there can be different error messages:

- Username is taken
- Username or password does not meet requirements
- Username and password are required

```json
    "status": "error",
    "message": ERROR_MESSAGE
```

## Login

POST `/login`

The method requires both parameters:
```json
    "username": USERNAME,
    "password": PASSWORD
```

Returning value if the credentials are valid:
```json
    "access_token": BASE64_JWT_TOKEN
```

In case of error:

```json
    "status": "error",
    "message": "Invalid username or password!"
```


## Download

GET `/download/<string:filename>`

The method requires the filename with .jpg or .caff extension

Returning value if file exists on server is the file itself

In case of error:

```json
    "status": "error",
    "message": "Filename is not correct or file couldn't be found"
```

## Search

GET `/search?<date:start_date>&<date:end_date>`

The method without query string returns every files, and can be filtered with the query strings.

Returning value:

```json
    "files": [
        FILE1,
        FILE2,
        ...
        FILEN
    ]
```


In case of error:

```json
    "status": "error",
    "message": "Something is wrong with the dates"
```

## Comment

POST `/comment`


The method requires a filename, and optionally, a comment. If no comment given, returns every comment to the file.
```json
    "filename": FILENAME_WITHOUT_EXTENSION,
    "comment": COMMENT
```

Returning value if the filename is valid:
```json
    "comments": [
        COMMENT1,
        COMMENT2,
        ...,
        COMMENTN"
    ]
```

In case of error:

```json
    "status": "error",
    "message": "Something is wrong with the comment or the id"
```

## Upload

POST `/upload`

The method requires a CAFF file:
```json
    "file": CAFF_FILE
```

Returning value if file is valid:
```json
    "files": [
        FILENAME_WITHOUT_EXTENSION1,
        FILENAME_WITHOUT_EXTENSION2,
        ...,
        FILENAME_WITHOUT_EXTENSIONN
    ]
```

In case of error:

```json
    "status": "error",
    "message": "Something is wrong with the file""
```

## Delete

POST `/delete`

The method needs to be called by an admin, and requires a filename without extension:
```json
    "filename": FILENAME_WITHOUT_EXTENSION
```

Returning value if file is valid:
```json
    "status": "success",
    "message": ""
```

In case of error:

```json
    "status": "error",
    "message": "Something is wrong with the file or user is not admin"
```
