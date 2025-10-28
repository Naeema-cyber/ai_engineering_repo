from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker 
from pymysql.constants import CLIENT
from dotenv import load_dotenv
import os

load_dotenv()

db_url =f"mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}"

#engine = create_engine(db_url)
engine = create_engine(
    db_url,
    connect_args={"client_flag": CLIENT.MULTI_STATEMENTS}
)

session = sessionmaker(bind=engine)

db = session()

query = text("SELECT * FROM user")

users = db.execute(query).fetchall()
print(users)


create_users_table = text("""
CREATE TABLE IF NOT EXISTS users(
    id int AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) NOT NULL,
    email varchar(100) NOT NULL,
    password VARCHAR(100) NOT NULL                        
);
""")
create_courses_table = text("""
CREATE TABLE IF NOT EXISTS courses(
    id int AUTO_INCREMENT PRIMARY KEY,
    title varchar(100) NOT NULL,
    level VARCHAR(100) NOT NULL
);
""")                       

create_enrollment_table = text("""
CREATE TABLE IF NOT EXISTS enrollment(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_Id INT,
    courses_Id INT,
    FOREIGN KEY (user_Id) REFERENCES users(id),
    FOREIGN KEY (courses_Id) REFERENCES courses(id)
);
""")

db.execute(create_users_table)
db.execute(create_courses_table)
db.execute(create_enrollment_table)
print("Tables created successfully.")
