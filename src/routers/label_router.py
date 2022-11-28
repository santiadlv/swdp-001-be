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
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError


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

@router.post("/new", response_description="Create a new label in database", response_model=label_schema.LabelModel)
def create_label(label_in: label_schema.LabelModel, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        new_label = jsonable_encoder(label_crud.create_label(db, label_in))
    except IntegrityError:
        raise HTTPException(status_code=409, detail=f"There is already a label with provided unique ID. UNIQUE constraint failed at insert operation.")

    if new_label is None:
        raise HTTPException(status_code=422, detail="Label could not be created.")

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={
        "message": "Label created successfully.",
        "data": new_label
    })

@router.post("/delete", response_description="Delete an existing label by id", response_model=label_schema.LabelModel)
def delete_label_by_id(label_id: label_schema.LabelID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        deleted_label = jsonable_encoder(label_crud.delete_label_by_id(db, label_id))
    except UnmappedInstanceError:
        raise HTTPException(status_code=404, detail=f"Label with ID {label_id.id} could not be found, deletion aborted.")
    
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={
        "message": f"Label with ID {label_id.id} successfully deleted.",
        "data": deleted_label
    })
