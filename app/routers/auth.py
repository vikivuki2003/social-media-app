from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, utils, models, oauth2


router = APIRouter(tags=['authentication'])

@router.post("/login")
def login(user_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentianls')

    if not utils.verify(user_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials')
    access_token = oauth2.create_access_token(data={"users_id": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}