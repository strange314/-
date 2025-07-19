from fastapi import FastAPI, Request, HTTPException
import httpx

app = FastAPI()

@app.get("/public-data/")
async def public_data(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/api/secret-data/", headers={"Authorization": auth_header})
        if response.status_code == 200:
            data = response.json()
            return {"data": "some public data", "user": data["user"]}
        else:
            raise HTTPException(status_code=401, detail="Invalid token")
