from sqlalchemy.orm import Session
import secrets

from . import models, schemas

def get_process(db: Session, process_uuid: str):
    return db.query(models.Process).filter(models.Process.id == process_uuid).first()

def create_process(db: Session, name: str, host_id: str, source: str, destination: str):
    """
    Create a random hash, secrets is unnecessary but helpful to get something random
    """
    full_id = secrets.token_hex(nbytes=32)
    short_id = full_id[0:5]

    db_process = models.Process(id=str(short_id), full_id=full_id,  name=name, host=host_id, source=source, destination=destination)
    db.add(db_process)
    db.commit()
    db.refresh(db_process)
    return db_process

def get_process_by_name(db: Session, name: str):
    return db.query(models.Process).filter(models.Process.name == host_id).all()

def get_process_by_host_id(db: Session, host_id: str):
    return db.query(models.Process).filter(models.Process.host == host_id).all()

def get_process_by_source(db: Session, source: str):
    return db.query(models.Process).filter(models.Process.source == source).all()

def get_process_by_destination(db: Session, destination: str):
    return db.query(models.Process).filter(models.Process.source == destination).all()

def get_process_exact(db: Session, name: str, host_id: str, source: str, destination: str):
    db_obj = db.query(models.Process).filter(models.Process.name == name)
    print(db_obj)
    return db_obj

def get_all_process(db: Session):
    return db.query(models.Process).all()

