from fastapi import FastAPI

app = FastAPI(title="Kiro Challenges API")


@app.get("/")
async def root():
    return {"message": "Welcome to Kiro Challenges API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
