# from fastapi import FastAPI
# from fastapi.openapi.utils import get_openapi
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
# import os
# from models.database import Base, engine
# from controllers.auth_controller import auth_router
# from controllers.user_controller import user_router
# from controllers.stream_controller import stream_router

# # Initialize FastAPI app
# app = FastAPI(title="PPE Kit Detection API", version="1.0")

# # Enable CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # use ["http://127.0.0.1:5500"] in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
# # Create database tables
# Base.metadata.create_all(bind=engine)

# # Include routers
# app.include_router(auth_router)
# app.include_router(user_router)
# app.include_router(stream_router)

# # Serve Static Files (CSS, JS, Images)
# FRONTEND_PATH = os.path.abspath("../frontend")

# @app.get("/")
# def root():
#     return FileResponse(os.path.join(FRONTEND_PATH, "index.html"))

# # Serve /index.html (optional duplicate of root)
# @app.get("/index.html")
# def index_page():
#     return FileResponse(os.path.join(FRONTEND_PATH, "index.html"))

# # Serve login.html
# @app.get("/login")
# def serve_login():
#     return FileResponse(os.path.join(FRONTEND_PATH, "login.html"))

# # Serve dashboard.html after login
# @app.get("/dashboard")
# def serve_dashboard():
#     return FileResponse(os.path.join(FRONTEND_PATH, "dashboard.html"))


# # Custom OpenAPI Schema to display "BearerAuth" in Swagger
# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title=app.title,
#         version=app.version,
#         description="API with simple Bearer token authentication",
#         routes=app.routes,
#     )
#     openapi_schema["components"]["securitySchemes"] = {
#         "BearerAuth": {
#             "type": "http",
#             "scheme": "bearer",
#             "bearerFormat": "JWT"
#         }
#     }
#     for path in openapi_schema["paths"].values():
#         for operation in path.values():
#             operation.setdefault("security", []).append({"BearerAuth": []})
#     app.openapi_schema = openapi_schema
#     return openapi_schema

# app.openapi = custom_openapi


from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from models.database import Base, engine
from controllers.auth_controller import auth_router
from controllers.user_controller import user_router
from controllers.stream_controller import stream_router
from controllers.detection_controller import router as detection_router  # New Import

# Initialize FastAPI app
app = FastAPI(title="PPE Kit Detection API", version="1.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # use ["http://127.0.0.1:5500"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(stream_router)
app.include_router(detection_router, prefix="/api")  # New router included

# Serve Static Files (CSS, JS, Images)
FRONTEND_PATH = os.path.abspath("../frontend")

@app.get("/")
def root():
    return FileResponse(os.path.join(FRONTEND_PATH, "index.html"))

# Serve /index.html (optional duplicate of root)
@app.get("/index.html")
def index_page():
    return FileResponse(os.path.join(FRONTEND_PATH, "index.html"))

# Serve login.html
@app.get("/login")
def serve_login():
    return FileResponse(os.path.join(FRONTEND_PATH, "login.html"))

# Serve dashboard.html after login
@app.get("/dashboard")
def serve_dashboard():
    return FileResponse(os.path.join(FRONTEND_PATH, "dashboard.html"))

# Custom OpenAPI Schema to display "BearerAuth" in Swagger
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description="API with simple Bearer token authentication",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for operation in path.values():
            operation.setdefault("security", []).append({"BearerAuth": []})
    app.openapi_schema = openapi_schema
    return openapi_schema

app.openapi = custom_openapi
