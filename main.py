from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import Config
import json



config = Config()
r = config.get_redis_config()

app = FastAPI()

class Player(BaseModel):
    id: int
    name: str
    team: str

@app.post("/player", status_code=201)
def save_player(player: Player) -> Player:
    tmp = player.model_dump_json()
    r.set(player.id, tmp)
    return player

@app.get("/player/{id}") 
def read_player(id) -> Player:
    body = r.get(id)
    if(body):
        return json.loads(body)
    else:
        raise HTTPException(status_code=404, detail="Item not found")

    
@app.delete("/player/{id}")
def delete_player(id):
    body = r.get(id)
    if(body):
        return r.delete(id)
    else:
        raise HTTPException(status_code=404, detail="Item not found")