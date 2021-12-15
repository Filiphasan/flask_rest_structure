from db import db
import datetime

class BaseModel(object):
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    created_by = db.Column(db.String(128), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow())
    updated_by = db.Column(db.String(128), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False, nullable=False)