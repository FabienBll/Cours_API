import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
DB_FILE = "servers.json"

# Modèle de données
class Server(BaseModel):
    id: int
    name: str
    ip: str
    ram: str
    size: str

# Utilitaires JSON
def load_db():
    if not os.path.exists(DB_FILE): return []
    try:
        with open(DB_FILE, "r") as f: return json.load(f)
    except: return []

def save_db(data):
    with open(DB_FILE, "w") as f: json.dump(data, f, indent=4)

# --- ENDPOINTS VERSIONNÉS (v1) ---

@app.get("/api_v1/servers", response_model=List[Server])
def get_all_servers():
    return load_db()

@app.post("/api_v1/servers")
def create_server(new_server: Server):
    db = load_db()
    if any(s["id"] == new_server.id for s in db):
        raise HTTPException(status_code=400, detail="ID déjà utilisé")
    db.append(new_server.dict())
    save_db(db)
    return {"status": "success", "server": new_server}

@app.put("/api_v1/servers/{server_id}")
def update_server(server_id: int, updated_info: Server):
    db = load_db()
    for i, s in enumerate(db):
        if s["id"] == server_id:
            db[i] = updated_info.dict()
            save_db(db)
            return {"status": "updated", "server": db[i]}
    raise HTTPException(status_code=404, detail="Serveur non trouvé")

@app.delete("/api_v1/servers/{server_id}")
def delete_server(server_id: int):
    db = load_db()
    new_db = [s for s in db if s["id"] != server_id]
    if len(new_db) == len(db):
        raise HTTPException(status_code=404, detail="ID non trouvé")
    save_db(new_db)
    return {"status": "deleted", "id": server_id}
