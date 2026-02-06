from fastapi import FastAPI

app = FastAPI(title="py-kojin")

@app.get("/health")
def health():
    return {"status": "ok"}
