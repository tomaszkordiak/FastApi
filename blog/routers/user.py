from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from ..hashing import Hash

from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    hashedPassword = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with {id} is not available')
    return user

