# A brief implementation documentation

## Overview
Our application was implemented using Python3 and Flask web framework. We used a lot of Python libraries, but we would like to mention some more important here:
- **Flask-JWT-Extended:** used for JWT tokens
- **Marshmallow**: used for input validation
- **pycryptodome**: used for password hashing
- **SQLAlchemy**: used for communicating with the database

## Folder structure

- **config**: stores admin's password (`admin_pass`) that is being set up after the server started
- **datab:** stores files for using DBs with SQLAlchemy
- **docs/postman:** screenshots of every endpoint in its working form
- **files:** uploaded files saved as .caff (/caff) and .jpg (/img) file
- **helper:** helper functions that needs to be used typically by multiple endpoints
- **log:** stores logs (`api.log`)
- **resources:** stores the logic of endpoint functions
- **tmp_caff:** stores executable for CAFF parser, and temporary files that being stored only during parsing phase
- **validators:** function for input validation of parameters
- **`app.py`:** main Flask component of our app
- **`requirements.txt`:** Python needed dependencies


## Error handling

In our application, every endpoint is protected by a try-except block. We log every exception or unnormal activity to `api.log` file but for the user, we return only general information as a response.

## Validation

In the application, we validate every input on the server-side. For that, we used the customizable Marshmallow library. The most important goal was not to allow any kind of data that is not in an appropriate format, avoiding any kind of malicious attempt. We have to mention here that the usage of SQLAlchemy itself protects the app against some kind of attacks, for example SQL injection.
