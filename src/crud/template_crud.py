import copy
from typing import Optional, List
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from ..models import template_model, template_schema


def get_templates(db: Session) -> Optional[List[template_schema.TemplateModel]]:
    return db.query(template_model.Template).all()
     
def get_template_by_id(db: Session, template_id: int) -> Optional[template_schema.TemplateModel]:
    return db.query(template_model.Template).filter(template_model.Template.id == template_id).first()

def get_template_by_name(db: Session, template_name: str) -> Optional[template_schema.TemplateModel]:
    return db.query(template_model.Template).filter(template_model.Template.name == template_name).first()

def create_template(db: Session, obj_in: template_schema.TemplateModel) -> Optional[template_schema.TemplateModel]:
    new_template = template_model.Template(
        name=obj_in.name,
        description=obj_in.description,
        date=obj_in.date,
        purchase_order=obj_in.purchase_order,
        supplier=obj_in.supplier,
        barcode=obj_in.barcode,
        client=obj_in.client,
        quantity=obj_in.quantity,
        internal_code=obj_in.internal_code,
        t_height=obj_in.t_height,
        t_width=obj_in.t_width
    )

    db.add(new_template)
    db.commit()
    db.refresh(new_template)

    return new_template

def delete_template_by_id(db: Session, template_id: template_schema.TemplateID) -> Optional[template_schema.TemplateModel]:
    template_to_delete = db.query(template_model.Template).filter(template_model.Template.id == template_id.id).first()
    result = copy.copy(template_to_delete)
    db.delete(template_to_delete)
    db.commit()

    return result

def delete_template_by_name(db: Session, template_name: template_schema.TemplateName) -> Optional[template_schema.TemplateModel]:
    template_to_delete = db.query(template_model.Template).filter(template_model.Template.name == template_name.name).first()
    result = copy.copy(template_to_delete)
    db.delete(template_to_delete)
    db.commit()

    return result

def update_template_by_id(db: Session, template_update: template_schema.TemplateUpdate) -> Optional[template_schema.TemplateModel]:
    update_attr = dict(jsonable_encoder(template_update))
    template_id = update_attr.pop("id")

    updated_rows = db.query(template_model.Template).filter(template_model.Template.id == template_id).update(update_attr)

    if not updated_rows:
        return None

    db.commit()
    updated_template = db.query(template_model.Template).filter(template_model.Template.id == template_update.id).first()

    return updated_template
