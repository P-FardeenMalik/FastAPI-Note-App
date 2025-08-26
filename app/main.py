from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes.notes import route as notes_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(notes_router)