from sqlalchemy import DateTime, create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Define the database model
Base = declarative_base()

class Detection(Base):
    __tablename__ = 'detections'
    id = Column(Integer, primary_key=True, autoincrement=True)
    label = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.now, nullable=True)

# Initialize the database
def initialize_db():
    engine = create_engine('sqlite:///detections.db')
    Base.metadata.create_all(engine)
    return engine

# Save detections to the database
def save_to_db(engine, objects_rec):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for label, confidence in objects_rec:
        detection = Detection(label=label, confidence=confidence)
        session.add(detection)
    
    session.commit()
    session.close()