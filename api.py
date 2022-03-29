from fastapi import FastAPI
from models import AStarParams


app = FastAPI()


# then generate one image
# then send plot


@app.post("/")
async def root(aStarParams: AStarParams):
    return {"message": f"{aStarParams}"}
