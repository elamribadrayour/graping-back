
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import header, gallery

app = FastAPI(debug=True)
app.include_router(header.router)
app.include_router(gallery.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello Graping!"}
