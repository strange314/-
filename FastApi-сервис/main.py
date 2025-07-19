from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx, os
from dotenv import load_dotenv

load_dotenv()
DJANGO_BASE_URL = os.getenv("DJANGO_BASE_URL")

app = FastAPI(title="FastAPI Proxy App")
auth_scheme = HTTPBearer()

@app.get("/public-data/")
async def public_data(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    token = credentials.credentials
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{DJANGO_BASE_URL}/api/secret-data/", headers=headers)
    if res.status_code == 200:
        user_data = res.json().get("user")
        return {"data": "some public data", "user": user_data}
    raise HTTPException(status_code=401, detail="Invalid token")
