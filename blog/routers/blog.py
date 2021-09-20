from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from ..repository import blog
from .. import schemas, database, models, oath2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db),
                  current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_single_blog(id, db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(oath2.get_current_user)):
    return blog.show(id, db)
