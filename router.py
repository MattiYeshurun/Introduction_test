from fastapi import FastAPI

from models.houses import Room


app = FastAPI()

app.get("/space{room}")
def info_rooms(room: Room):
    

