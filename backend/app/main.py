from fastapi import FastAPI

app = FastAPI(title="RAG Documentation Assistant API")

@app.get("/")
def health_check():
    return {"status": "ok", "service": "backend"}