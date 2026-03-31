from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import httpx
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI(title="Voter Registration Gateway")
app.mount("/static", StaticFiles(directory="static"), name="static")

VOTER_SERVICE_URL = "http://127.0.0.1:4001"
STATS_SERVICE_URL = "http://127.0.0.1:4002"

class Voter(BaseModel):
    name: str
    email: EmailStr
    age: int
    phone: str
    address: str
    password: str

@app.get("/")
def read_root():
    return FileResponse('static/index.html')

@app.post("/voters")
async def register_voter(voter: Voter):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{VOTER_SERVICE_URL}/register", json=voter.dict())
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json()["detail"])
        return response.json()

@app.get("/voters")
async def get_all_voters(
    search: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = Query("name")
):
    params = {"page": page, "limit": limit, "sort_by": sort_by}
    if search:
        params["search"] = search
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{VOTER_SERVICE_URL}/voters", params=params)
        return response.json()

@app.get("/voters/{voter_id}")
async def get_voter_by_id(voter_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{VOTER_SERVICE_URL}/voters/{voter_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json()["detail"])
        return response.json()

@app.put("/voters/{voter_id}")
async def update_voter(voter_id: int, voter: Voter):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{VOTER_SERVICE_URL}/voters/{voter_id}", json=voter.dict())
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json()["detail"])
        return response.json()

@app.delete("/voters/{voter_id}")
async def delete_voter(voter_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{VOTER_SERVICE_URL}/voters/{voter_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json()["detail"])
        return response.json()

@app.get("/stats")
async def get_stats():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{STATS_SERVICE_URL}/stats")
        return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=4000)