from sqlalchemy.orm import Session
import uuid

from . import models, schemas

def get_process(db: Session, process_uuid: str):
    return db.query(models.Process).filter(models.Process.id == process_uuid).first()

def create_process(db: Session, name: str, host_id: str, source: str, destination: str):
    db_process = models.Process(id=str(uuid.uuid1()), name=name, host=host_id, source=source, destination=destination)
    db.add(db_process)
    db.commit()
    db.refresh(db_process)
    return db_process

def get_all_process(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Process).all()

