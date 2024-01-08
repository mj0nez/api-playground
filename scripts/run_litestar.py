import uvicorn

# app_entrypoint = f"{Path(__file__).stem}:app"

if __name__ == "__main__":
    uvicorn.run(
        "playground.litestar_app.app:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        # reload=True,
    )
