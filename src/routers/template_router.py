from fastapi.responses import JSONResponse
from fastapi.param_functions import Depends
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, status, Path, HTTPException

from ..data.database import get_db
from ..crud import template_crud
from ..models import template_schema

from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError


router = APIRouter(
    prefix="/templates",
    tags=["templates"],
    responses={404: {"description" : "Not found"}}
)

@router.get("/all", response_description="Get all templates", response_model=List[template_schema.TemplateModel])
def get_templates(db: Session = Depends(get_db)) -> JSONResponse:
    templates = jsonable_encoder(template_crud.get_templates(db))

    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "message": "Template list retrieved successfully.",
        "data": templates
    })

@router.get("/id/{id}", response_description="Get template by id", response_model=template_schema.TemplateModel)
def get_template_by_id(db: Session = Depends(get_db), id: str = Path(..., title="ID of template to retrieve")) -> JSONResponse:
    template = jsonable_encoder(template_crud.get_template_by_id(db, int(id)))

    if template is None:
        raise HTTPException(status_code=404, detail="Template not found.")
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "message": "Template retrieved successfully.",
        "data": template
    })

@router.get("/name/{name}", response_description="Get template by name", response_model=template_schema.TemplateModel)
def get_template_by_name(db: Session = Depends(get_db), name: str = Path(..., title="Name of template to retrieve")) -> JSONResponse:
    template = jsonable_encoder(template_crud.get_template_by_name(db, name))

    if template is None:
        raise HTTPException(status_code=404, detail="Template not found.")
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "message": "Template retrieved successfully.",
        "data": template
    })

@router.post("/new", response_description="Create a new template in database", response_model=template_schema.TemplateModel)
def create_template(template_in: template_schema.TemplateModel, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        new_template = jsonable_encoder(template_crud.create_template(db, template_in))
    except IntegrityError:
        raise HTTPException(status_code=409, detail=f"There is already a template with provided unique name. UNIQUE constraint failed at insert operation.")

    if new_template is None:
        raise HTTPException(status_code=422, detail="Template could not be created.")

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={
        "message": "Template created successfully.",
        "data": new_template
    })

@router.post("/delete/id", response_description="Delete an existing template by id", response_model=template_schema.TemplateModel)
def delete_template_by_id(template_id: template_schema.TemplateID, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        deleted_template = jsonable_encoder(template_crud.delete_template_by_id(db, template_id))
    except UnmappedInstanceError:
        raise HTTPException(status_code=404, detail=f"Template with ID {template_id.id} could not be found, deletion aborted.")
    
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={
        "message": f"Template with ID {template_id.id} successfully deleted.",
        "data": deleted_template
    })

@router.post("/delete/name", response_description="Delete an existing template by name", response_model=template_schema.TemplateModel)
def delete_template_by_name(template_name: template_schema.TemplateName, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        deleted_template = jsonable_encoder(template_crud.delete_template_by_name(db, template_name))
    except UnmappedInstanceError:
        raise HTTPException(status_code=404, detail=f"Template with name {template_name.name} could not be found, deletion aborted.")
    
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={
        "message": f"Template with name '{template_name.name}' successfully deleted.",
        "data": deleted_template
    })

@router.post("/update/id", response_description="Update an existing template by id", response_model=template_schema.TemplateModel)
def update_template_by_id(template_update: template_schema.TemplateUpdate, db: Session = Depends(get_db)) -> JSONResponse:
    updated_template = jsonable_encoder(template_crud.update_template_by_id(db, template_update))
    
    if not updated_template:
        raise HTTPException(status_code=404, detail=f"Template with ID {template_update.id} could not be found, update aborted.")
    
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={
        "message": f"Template with ID {template_update.id} successfully updated.",
        "data": updated_template
    })
