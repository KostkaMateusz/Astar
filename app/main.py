from fastapi import FastAPI
from .models import AStarParams
from astar.astar import generate_image, generate_object_list
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


@app.post("/engine")
async def root(aStarParams: AStarParams):
    """
    Generate A star heat map based on a sended parameters.
    **map_size_x** Map size X parameter
    **map_size_y** Map size Y parameter
    **start_x** Value of a start x co-ordinates
    **start_y** Value of a start y co-ordinates
    **end_x** Value of a end x co-ordinates
    **end_y** Value of a end y co-ordinates
    **weight** Value of weight for a prize algorithm
    """
    dict_of_parameters = dict([ele for ele in aStarParams])
    image = io.BytesIO()
    img = generate_image(**dict_of_parameters)
    img.savefig(image, format="png", dpi=300, transparent=True)
    image.seek(0)

    return StreamingResponse(image, media_type="image/png")


@app.post("/astar")
async def root(aStarParams: AStarParams):
    """
    Generate A star heat map based on a sended parameters.
    **map_size_x** Map size X parameter
    **map_size_y** Map size Y parameter
    **start_x** Value of a start x co-ordinates
    **start_y** Value of a start y co-ordinates
    **end_x** Value of a end x co-ordinates
    **end_y** Value of a end y co-ordinates
    **weight** Value of weight for a prize algorithm
    """
    dict_of_parameters = dict([ele for ele in aStarParams])

    objects = generate_object_list(**dict_of_parameters)

    return objects
