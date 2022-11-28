from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import label_router, template_router

import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome!"}

app.include_router(label_router.router)
app.include_router(template_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
