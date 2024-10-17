from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Bah tche"}

@app.get("/S")
async def read_root():
    return {"message": "essa url é do Samuel"}

@app.get("/mutiplicacao")
async def root(V1: int = 10, V2: int = 10):
    res = V1 * V2
    return {"resultado": res}

@app.get("/nomes")
async def root(N1: str = "Anna", N2: str = "Samuel"):
    nome = N1 , N2
    return {"Nomes": nome }