from typing import Optional, List
from sqlalchemy.orm import Session
from ..models import label_schema, label_model


def get_labels(db: Session) -> Optional[List[label_schema.LabelModel]]:
    return db.query(label_model.Label).all()
     

def get_label_by_id(db: Session, label_id: int) -> Optional[label_schema.LabelModel]:
    return db.query(label_model.Label).filter(label_model.Label.id == label_id).first()
