from fastapi.responses import JSONResponse
from fastapi.param_functions import Depends
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, status, Path, HTTPException

from ..data.database import get_db
from ..crud import label_crud
from ..models import label_schema
from ..utils import encoder

from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/labels",
    tags=["labels"],
    responses={404: {"description" : "Not found"}}
)

@router.get("/all", response_model=List[label_schema.LabelModel])
def get_labels(db: Session = Depends(get_db)) -> JSONResponse:
    labels = jsonable_encoder(label_crud.get_labels(db))

    for label in labels:
        label["svg"] = encoder.create_label_image(label["id"])

    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "message": "Label list retrieved successfully",
        "data": labels
    })

@router.get("/{id}", response_model=label_schema.LabelModel)
def get_label(db: Session = Depends(get_db), id: str = Path(..., title="ID of label to retrieve")) -> JSONResponse:
    label = jsonable_encoder(label_crud.get_label_by_id(db, int(id)))
    if label is None:
        raise HTTPException(status_code=404, detail="Label not found")
    label["svg"] = encoder.create_label_image(label["id"])
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "message": "Label retrieved successfully",
        "data": label
    })
