# Import the custom module
class PostBase(BaseModel):
    title: str
    content: str
    user_id: int
    
class UserBase(BaseModel):
    username: str
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/user")


