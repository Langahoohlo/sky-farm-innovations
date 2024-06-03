from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_model import Base, Detection

def initialize_db():
    engine = create_engine('sqlite:///detections.db')
    Base.metadata.create_all(engine)
    return engine

def save_to_db(engine, objects_rec):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for label, confidence in objects_rec:
        detection = Detection(label=label, confidence=confidence)
        session.add(detection)
    
    session.commit()
    session.close()
