# from fastapi import FastAPI
# from models.database import Base, engine
# from controllers.auth_controller import auth_router  # Fix import here
# from controllers.user_controller import user_router  # Import user routes


# # Initialize FastAPI app
# app = FastAPI(title="PPE Kit Detection API", version="1.0")

# # Create database tables
# Base.metadata.create_all(bind=engine)

# # Include routers
# app.include_router(auth_router)  # Include auth routes
# app.include_router(user_router)  # Include user routes

# # Root endpoint
# @app.get("/")
# def home():
#     return {"message": "Welcome to the PPE Kit Detection API"}


# second code snippet
# from fastapi import FastAPI
# from fastapi.openapi.utils import get_openapi
# from models.database import Base, engine
# from controllers.auth_controller import auth_router
# from controllers.user_controller import user_router
# from controllers.stream_controller import stream_router


# # Initialize FastAPI app
# app = FastAPI(title="PPE Kit Detection API", version="1.0")

# # Create database tables
# Base.metadata.create_all(bind=engine)

# # Include routers
# app.include_router(auth_router)
# app.include_router(user_router)
# # Include the live stream router
# app.include_router(stream_router)

# # Root endpoint
# @app.get("/")
# def home():
#     return {"message": "Welcome to the PPE Kit Detection API"}

# # Custom OpenAPI Schema to display "BearerAuth" in Swagger
# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     # Use get_openapi to generate the schema without recursion
#     openapi_schema = get_openapi(
#         title=app.title,
#         version=app.version,
#         description="API with simple Bearer token authentication",
#         routes=app.routes,
#     )
#     # Add BearerAuth to components
#     openapi_schema["components"]["securitySchemes"] = {
#         "BearerAuth": {
#             "type": "http",
#             "scheme": "bearer",
#             "bearerFormat": "JWT"
#         }
#     }
#     # Apply BearerAuth globally (optional)
#     for path in openapi_schema["paths"].values():
#         for operation in path.values():
#             operation.setdefault("security", []).append({"BearerAuth": []})
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema

# app.openapi = custom_openapi


# from fastapi import FastAPI
# from fastapi.openapi.utils import get_openapi
# from models.database import Base, engine
# from controllers.auth_controller import auth_router
# from controllers.user_controller import user_router
# from controllers.stream_controller import stream_router


# # Initialize FastAPI app
# app = FastAPI(title="PPE Kit Detection API", version="1.0")

# # Create database tables
# Base.metadata.create_all(bind=engine)

# # Include routers
# app.include_router(auth_router)
# app.include_router(user_router)
# # Include the live stream router
# app.include_router(stream_router)

# # Root endpoint
# @app.get("/")
# def home():
#     return {"message": "Welcome to the PPE Kit Detection API"}

# # Custom OpenAPI Schema to display "BearerAuth" in Swagger
# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     # Use get_openapi to generate the schema without recursion
#     openapi_schema = get_openapi(
#         title=app.title,
#         version=app.version,
#         description="API with simple Bearer token authentication",
#         routes=app.routes,
#     )
#     # Add BearerAuth to components
#     openapi_schema["components"]["securitySchemes"] = {
#         "BearerAuth": {
#             "type": "http",
#             "scheme": "bearer",
#             "bearerFormat": "JWT"
#         }
#     }
#     # Apply BearerAuth globally (optional)
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

# Initialize FastAPI app
app = FastAPI(title="PPE Kit Detection API", version="1.0")

# Enable CORS
origins = ["*"]  # Allow all origins; restrict in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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

# Serve Static Files (CSS, JS, Images)
FRONTEND_PATH = os.path.abspath("../frontend")  # Adjust if needed
app.mount("/static", StaticFiles(directory=os.path.join(FRONTEND_PATH, "static")), name="static")

# Serve Login Page
@app.get("/login")
def serve_login():
    return FileResponse(os.path.join(FRONTEND_PATH, "login.html"))

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the PPE Kit Detection API"}

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