from fastapi import FastAPI
from .models import AStarParams
from astar.astar import generate_image
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import io
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return RedirectResponse("/static/index.html")


@app.post("/engine")
async def root(aStarParams: AStarParams):

    dict_of_parameters = dict([ele for ele in aStarParams])

    image = io.BytesIO()
    img = generate_image(**dict_of_parameters)
    img.savefig(image, format="png", dpi=600, transparent=True)
    image.seek(0)

    return StreamingResponse(image, media_type="image/png")
