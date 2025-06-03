# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.config import configure_cors
from app.routes.health import router as health_router # Importa el router de health

app = FastAPI(title="UAINT Forum API")

# Configura CORS
configure_cors(app)

# Incluye las rutas
app.include_router(health_router, prefix="/health", tags=["health"])

@app.get("/")
async def root():
    return JSONResponse(
        content={"message": "API activa!"}, 
        media_type="application/json; charset=utf-8"
    )