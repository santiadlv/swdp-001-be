import copy
from typing import Optional, List
from sqlalchemy.orm import Session
from ..models import label_schema, label_model


def get_labels(db: Session) -> Optional[List[label_schema.LabelModel]]:
    return db.query(label_model.Label).all()

def get_label_by_id(db: Session, label_id: int) -> Optional[label_schema.LabelModel]:
    return db.query(label_model.Label).filter(label_model.Label.id == label_id).first()

def create_label(db: Session, obj_in: label_schema.LabelModel) -> Optional[label_schema.LabelModel]:
    new_label = label_model.Label(
        id=obj_in.id,
        purchase_order=obj_in.purchase_order,
        date=obj_in.date,
        description=obj_in.description,
        client=obj_in.client,
        quantity=obj_in.quantity,
        supplier=obj_in.supplier
    )

    db.add(new_label)
    db.commit()
    db.refresh(new_label)

    return new_label

def delete_label_by_id(db: Session, label_id: label_schema.LabelID) -> Optional[label_schema.LabelModel]:
    label_to_delete = db.query(label_model.Label).filter(label_model.Label.id == label_id.id).first()
    result = copy.copy(label_to_delete)
    db.delete(label_to_delete)
    db.commit()

    return result
