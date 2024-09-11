from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.api import health, joke
from app.core.config import settings

from langserve import add_routes
from app.agents.search_agent.graph import graph

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0",
    description="FastAPI LangGraph Streaming Service API 🚀",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #origins when origins is set
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include pre-built route

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(joke.router, prefix="/api/v1", tags=["joke"])

add_routes(
    app,
    graph,
    path="/websearch",
)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)