import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
DB_FILE = "servers.json"

# --- 1. MODÈLE DE DONNÉES ---
class Server(BaseModel):
    id: int
    name: str
    ip: str
    ram: str
    size: str

# --- 2. FONCTIONS DE GESTION DU FICHIER ---
def load_db():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- 3. LES ENDPOINTS ---

# LIRE : Récupérer tous les serveurs
@app.get("/servers", response_model=List[Server])
def get_all_servers():
    return load_db()

# CRÉER : Ajouter un serveur
@app.post("/servers")
def create_server(new_server: Server):
    db = load_db()
    if any(s["id"] == new_server.id for s in db):
        raise HTTPException(status_code=400, detail=f"L'ID {new_server.id} existe déjà.")
    
    db.append(new_server.dict())
    save_db(db)
    return {"message": "Serveur ajouté !", "server": new_server}

# MODIFIER : Mettre à jour un serveur via son ID
@app.put("/servers/{server_id}")
def update_server(server_id: int, updated_info: Server):
    db = load_db()
    for index, server in enumerate(db):
        if server["id"] == server_id:
            db[index] = updated_info.dict()
            save_db(db)
            return {"message": "Mise à jour réussie", "server": db[index]}
    raise HTTPException(status_code=404, detail="Serveur non trouvé")

# SUPPRIMER : Effacer un serveur via son ID
@app.delete("/servers/{server_id}")
def delete_server(server_id: int):
    db = load_db()
    
    # On crée une nouvelle liste qui exclut le serveur avec l'ID donné
    initial_length = len(db)
    db = [s for s in db if s["id"] != server_id]
    
    # Si la taille de la liste n'a pas changé, c'est que l'ID n'existait pas
    if len(db) == initial_length:
        raise HTTPException(status_code=404, detail="Impossible de supprimer : ID non trouvé")
    
    save_db(db)
    return {"message": f"Le serveur {server_id} a été supprimé avec succès"}