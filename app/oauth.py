from fastapi import HTTPException,  status, Depends
from fastapi.security import OAuth2PasswordBearer
from app.token import verify_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="productos")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_token(token, credentials_exception)