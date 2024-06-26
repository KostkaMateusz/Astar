import sys
import time
import asyncio
from .models import InputMap
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.responses import StreamingResponse
from starlette.status import HTTP_504_GATEWAY_TIMEOUT
from astar.astar import generate_object_list

sys.setrecursionlimit(9000)

REQUEST_TIMEOUT_ERROR = 10  # Time out Threshold

app = FastAPI()


@app.middleware("http")
async def timeout_middleware(request: Request, call_next):
    try:
        start_time = time.time()
        return await asyncio.wait_for(call_next(request), timeout=REQUEST_TIMEOUT_ERROR)

    except asyncio.TimeoutError:
        process_time = time.time() - start_time
        return JSONResponse({'detail': 'Request processing time excedeed limit',
                             'processing_time': process_time},
                            status_code=HTTP_504_GATEWAY_TIMEOUT)


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get(
    "/", summary="Send a simple JS client", description="This api call send JS client that connecct with api", response_description="HTML,CSS,JS static files"
)
async def root():
    return RedirectResponse("/static/index.html")


@app.post("/astar")
async def root(input:InputMap):

    path = generate_object_list(input.input_map)
    output_map = {"Path": path[0], "Values":path[1]}

    return output_map
