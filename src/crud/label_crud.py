from sqlalchemy.orm import Session
from ..models import label_model


def get_labels(db: Session, skip: int = 0, limit: int = 0):
    return db.query(label_model.Label).offset(skip).limit(limit).all()

def get_label_by_id(db: Session, label_id: int):
    return db.query(label_model.Label).filter(label_model.Label.id == label_id).first()
