from fastapi import FastAPI
#from db import init_db
from endpoints import users, auth, jobs
import uvicorn

#init_db()

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])

#@app.on_event("startup")
#async def startup():
#    await database.connect()
#
#@app.on_event("shutdown")
#async def shutdown():
#    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)