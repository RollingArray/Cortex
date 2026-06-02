from fastapi import FastAPI

app = FastAPI(
    title="Cortex",
    description="AI-powered knowledge and reasoning platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "application": "cortex",
        "version": "0.1.0",
        "status": "running",
    }