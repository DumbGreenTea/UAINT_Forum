from fastapi.middleware.cors import CORSMiddleware

def configure_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # Ajusta el puerto si tu frontend usa otro
        allow_credentials=True,
        allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
        allow_headers=["*"],  # Permite todos los headers
    )