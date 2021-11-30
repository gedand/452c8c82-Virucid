# A brief implementation documentation

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
