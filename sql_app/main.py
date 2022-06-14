from typing import List, Union

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/process/", response_model=schemas.Process)
def create_process(name: str, db: Session = Depends(get_db), host_id: str = "generic", source: str = "generic" , destination: str = "generic"):
    return crud.create_process(db=db, name=name, host_id=host_id, source=source, destination=destination)

@app.get("/processes/{process}", response_model=schemas.Process)
def read_process(process: str, db: Session = Depends(get_db)):
    db_process = crud.get_process(db, process_uuid=process)
    if db_process is None:
        raise HTTPException(status_code=404, detail="process not found")
    return db_process

@app.get("/host/{host}", response_model=List[schemas.HostOut])
def get_host_processes(host: str, db: Session = Depends(get_db)):
    db_process = crud.get_process_by_host_id(db, host_id=host)
    if db_process is None:
        raise HTTPException(status_code=404, detail="process not found")
    return db_process

@app.get("/all_processes/", response_model=List[schemas.ProcessOut])
def get_all_processes(db: Session = Depends(get_db)):
    db_process = crud.get_all_process(db)
    if db_process is None:
        raise HTTPException(status_code=404, detail="Nothing found")
    return db_process

