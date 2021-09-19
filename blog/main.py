import uvicorn
from fastapi import FastAPI

from . import database
from . import models
from .routers import blog, user

app = FastAPI()

models.Base.metadata.create_all(database.engine)
app.include_router(blog.router)
app.include_router(user.router)

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)
