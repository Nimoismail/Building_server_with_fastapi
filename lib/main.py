from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

# Creating the database engine
engine = create_engine("sqlite:///./my_database.db")

# Creating a session factory
Session = sessionmaker(bind=engine)

# creating the base declaration models
Base = declarative_base()

# Defining the item model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Creating the database tables
Base.metadata.create_all(bind=engine)

# Creating the FastAPI instance
app = FastAPI()

# Pydantic model for POST and PUT requests
class ItemCreate(BaseModel):

    name: str
    description: str

# Pydantic model for GET responses
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

# Functioning to get a database session
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# GET all item
@app.get("/get_all_endpoint/")
def get_all_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items

# GET single item
@app.get("/get_one_endpoint/{id}")
def get_single_item(id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# POST of new item
@app.post("/post_endpoint/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    data = Item(name=item.name, description=item.description)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

# PUT full update of  the item
@app.put("/put_endpoint/{id}")
def update_item(id: int, item: ItemCreate, db: Session = Depends(get_db)):
    data = db.query(Item).filter(Item.id == id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Item not found")
    data.name = item.name
    data.description = item.description
    db.commit()
    db.refresh(data)
    return data

# PATCH partial update of the  item
@app.patch("/patch_endpoint/{id}")
def partial_update_item(id: int, item: ItemCreate, db: Session = Depends(get_db)):
    data = db.query(Item).filter(Item.id == id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.name:
        data.name = item.name
    if item.description:
        data.description = item.description
    db.commit()
    db.refresh(data)
    return data

# DELETE a single of item
@app.delete("/delete_endpoint/{id}")
def delete_item(id: int, db: Session = Depends(get_db)):
    data = db.query(Item).filter(Item.id == id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(data)
    db.commit()
    return {"message": "Data deleted"}