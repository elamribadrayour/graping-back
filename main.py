
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import duckdb

from routers import header, gallery, ml

app = FastAPI(debug=True)
app.include_router(ml.router)
app.include_router(header.router)
app.include_router(gallery.router)

con = duckdb.connect()

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
