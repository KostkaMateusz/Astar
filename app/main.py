from fastapi import FastAPI
from .models import InputMap
#from astar.astar import generate_image, generate_object_list
from astar.astar import generate_object_list
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


@app.get(
    "/", summary="Send a simple JS client", description="This api call send JS client that connecct with api", response_description="HTML,CSS,JS static files"
)
async def root():
    return RedirectResponse("/static/index.html")


@app.post("/astar")
async def root(input:InputMap):

    path = generate_object_list(input.input_map)

    output_map = {"Path": path}

    return output_map
