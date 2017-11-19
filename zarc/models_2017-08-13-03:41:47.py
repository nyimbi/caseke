# coding: utf-8
# AUTOGENERATED BY gen_script.sh from kp3.py
# Copyright (C) Nyimbi Odero, Sun Aug 13 03:35:34 EAT 2017
 
from sqlalchemy import func
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn, UserExtensionMixin 
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.filemanager import ImageManager
from sqlalchemy_utils import aggregated, force_auto_coercion
from sqlalchemy.orm import relationship, query, defer, deferred
# IMPORT Postgresql Specific Types 
from sqlalchemy.dialects.postgresql import ( 
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE,  
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER,  
    INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT,  
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE,  
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR )
from sqlalchemy.dialects.postgresql import aggregate_order_by

from sqlalchemy import (Column, Integer, String, ForeignKey,
    Sequence, Float, Text, BigInteger, Date,
    DateTime, Time, Boolean, Index, CheckConstraint,
    UniqueConstraint,ForeignKeyConstraint, Numeric, LargeBinary , Table)
from datetime import timedelta, datetime, date
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.sql import func
from .mixins import *

# Here is how to extend the User model
#class UserExtended(Model, UserExtensionMixin):
#    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=True)
#    contact_group = relationship('ContactGroup')

# UTILITY CLASSES

import arrow, enum
import enum
# Initialize sqlalchemy_utils 
#force_auto_coercion()


