from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from image_extension.core import start_process

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Img2imgRequestBody(BaseModel):
    base_image: str
    roop_image: str
    face_index: int


class Img2ImgResponse(BaseModel):
    image: str


@app.post("/api/v1/img2img")
async def img2img_api(req: Img2imgRequestBody) -> Img2ImgResponse:
    image = await start_process(
        req.base_image,
        req.roop_image,
        req.face_index
    )

    return Img2ImgResponse(image=image)
