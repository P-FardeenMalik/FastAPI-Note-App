from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes.notes import route as notes_router
from app.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(notes_router)
app.include_router(auth_router)