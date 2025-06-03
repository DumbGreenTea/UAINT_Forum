from fastapi.middleware.cors import CORSMiddleware

def configure_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",    # Tu frontend en Vite
            "http://127.0.0.1:5173",    # Alternativa del frontend para Safari
            "http://localhost:8000",    # Acceso directo al backend
            "http://127.0.0.1:8000",    # Alternativa del backend para Safari
            "*"                         # Fallback para cualquier otro origen
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )