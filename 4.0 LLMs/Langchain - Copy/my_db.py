

#1. Engne. Connect our db to python program
# 2. eclarative base that help create our dbmodel
#3 session maker helps us to talk to our database helps us manipulate our db, maps our python objects to our db, just like prisma for for js

from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
#connect our db
engine=create_engine("sqlite:///deepseeds.db",echo=True) 
#3 slash means it is local
#in your create_enguine , we pass a connetion string
print(f"My Engine is Engine{engine}")

Base =declarative_base()
# print(Base)
sessionlocal=sessionmaker() 

#before creating a table, we create a class using python, no sql language, thanks to sql alchemy

class ModelInfo(Base):
   __tablename__='modelInfo'

    #we just inherited from the base class
#Each model/table needs an ID
   id=Column(Integer, primary_key=True, index= True)
   model_name=Column(String(50), nullable=False)
   prompt=Column(String(300), nullable=False)
   email=Column(String(30), nullable=False, unique=True)

class User(Base):
   __tablename__='user'
   id=Column(Integer, primary_key=True, index=True)
   name=Column(String(40), nullable=False)
   email=Column(String(30), nullable=False, unique=True)
   created_at=Column(DateTime,default=datetime.utcnow )

# print(f'Model info{ModelInfo}')
# print(f'Model info{User}')

 #Now we have to be able to migrate our database uing the Base class
Base.metadata.create_all(bind=engine)
#creating a db with the engine above

# Add data to our database
session = sessionlocal()

try: 
   #When the code is ok, the try block ends
   user1=User(name='JJ',email='jj@gmsil.com')
   user2=User(name='JJ2',email='jj2@gmsil.com')
   #use session to add data to our db
   
except Exception as e:
   #when there is a problem
   

finally: