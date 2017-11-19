from sqlalchemy import func
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from flask_appbuilder.models.decorators import renders
from sqlalchemy import (Column, Integer, String, ForeignKey,
                        Sequence, Float, Text, BigInteger, Date,
                        DateTime, Time, Boolean, CheckConstraint,
                        UniqueConstraint, Table)

from sqlalchemy.orm import relationship, query, defer, deferred
from sqlalchemy_utils import aggregated
from .mixins import *
# from sqlalchemy_mixins import ActiveRecordMixin

#from ../../pjwide/mixins import *

from flask_appbuilder.filemanager import get_file_original_name, ImageManager

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
# class BaseModel(ActiveRecordMixin, Model):
#     __abstract__ = True
#     pass

class Gender(RefTypeMixin, Model):
    __tablename__ = 'gender'


class CaseStatus(RefTypeMixin, Model):
    __tablename__ = 'case_status'


class CourtLevel(RefTypeMixin, Model):
    __tablename__ = 'court_level'


class CaseType(RefTypeMixin, Model):
    __tablename__ = 'case_type'


class CaseCategory(RefTypeMixin, Model):
    __tablename__ = 'case_category'


class HearingType(RefTypeMixin, Model):
    __tablename__ = 'hearing_type'

class EventType(RefTypeMixin, Model):
    __tablename__ = 'event_type'


##### Reference Tables #####
# 10 Regions/County
class Region(RefTypeMixin, Model):
    __tablename__ = 'region'
    capital = Column(String(30))
    districts = relationship('District', backref = 'region')

# Subcounty/216 Districts in Ghana
class District(RefTypeMixin, Model):
    __tablename__ = 'district'
    region_fk = Column(Integer, ForeignKey('region.id'))
    region = relationship(Region, back_populates = 'district')
    capital = Column(String(30))
    towns = relationship('Town', backref='district')
    courts = relationship('Court', back_populates = 'district')


# class Subcounty(RefTypeMixin, PlaceMixin, AuditMixin, Model):
#     __tablename__ = 'subcounty'
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     county_fk = Column(Integer, ForeignKey('county.id'))
#     #county = relationship(County)
#     wards = relationship('Ward', backref = 'subcounty')
#
# class Ward( PlaceMixin, AuditMixin, Model): #RefTypeMixin,
#     __tablename__ = 'ward'
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     name = Column(String(30))
#     subcounty_fk = Column(Integer, ForeignKey('subcounty.id'))
#     #subcounty = relationship(Subcounty)
#     constituency_fk = Column(Integer, ForeignKey('constituency.id'))


class Town(RefTypeMixin, Model):
    __tablename__ = 'town'
    district_fk = Column(Integer, ForeignKey('district.id'))
    #district = relationship(District)
    urban_status = Column(String(30))
    local_authority = Column(String(50))
    rank = Column(Integer)


class Constituency(RefTypeMixin, Model):
    __tablename__ = 'constituency'
    region_fk = Column(Integer, ForeignKey('region.id'))
    region = relationship(Region)
    district_name = Column(String(30))
    #region = Column(String(40))

    #wards = relationship('Ward', backref='constituency')

    # @aggregated('wards', Column(Integer))
    # def ward_count(self):
    #     return func.count('1')
    #ward_count = Column(Integer)



###### Monitored Entities [Schools, Courts, Shops, Whatever] #####
# Modify These to Suit

class Court(RefTypeMixin, ContactMixin, PlaceMixin, Model):
    __tablename__ = 'court'
    id = Column(Integer, Sequence('court_id_seq'), primary_key=True)
    registrar = Column(String(30), nullable=True)
    district_fk = Column(Integer, ForeignKey('district.id'))
    district = relationship("District", back_populates="courts")


class PoliceStation(RefTypeMixin, ContactMixin, PlaceMixin, Model):
    __tablename__ = 'police_station'
    id = Column(Integer, Sequence('police_id_seq'), primary_key=True)
    district_fk = Column(Integer, ForeignKey('district.id'))
    district = relationship("District", back_populates="police_stations")
    officer_commanding = Column(String(40))
    cell_count = Column(Integer)


class Prison(RefTypeMixin, PlaceMixin, ContactMixin, Model):
    __tablename__ = 'prison'
    district_fk = Column(Integer, ForeignKey('district.id'))
    district = relationship("District", back_populates="prisons")

    holding_capacity = Column(Integer)



personcase = Table('percase', Model.metadata,
    #Column('id', Integer, ForeignKey('tag.id')),
    Column('person_id', Integer, ForeignKey('person.id')),
    Column('case_id', Integer, ForeignKey('case.id'))
)
#person case

class Person(PersonMixin, ContactMixin, ParentageMixin, AuditMixin, Model):
    __tablename__ = 'person'
    discriminator = Column('type', String(50))
    __mapper_args__ = {'polymorphic_on': discriminator}

class Plaintiff(Person):
    __mapper_args__ = {'polymorphic_identity': 'plaintiff'}

class Defendant(Person):
    __mapper_args__ = {'polymorphic_identity': 'defendant'}

class PoliceStaff(Person):
    __mapper_args__ = {'polymorphic_identity': 'policeman'}

class PrisonStaff(Person):
    __mapper_args__ = {'polymorphic_identity': 'warden'}

class Prosecutor(Person):
    __mapper_args__ = {'polymorphic_identity': 'prosecutor'}

class Registrar(Person):
    __mapper_args__ = {'polymorphic_identity': 'registrar'}

class Judge(Person):
    __mapper_args__ = {'polymorphic_identity': 'judge'}

class Magistrate(Person):
    __mapper_args__ = {'polymorphic_identity': 'magistrate'}

class Detective(Person):
    __mapper_args__ = {'polymorphic_identity': 'detective'}





# class CaseHearings(Model):
#     __tablename__ = 'case_hearings'
#
#     hearing_type_fk = Column(Integer, ForeignKey('hearing_type.id'))
#     hearing_type = relationship('Hearing')
#
#     case_fk = Column(Integer, ForeignKey('case.id'))
#     cases = relationship('Case')
#
#     reason = Column(String(200))
#     hearing_date = Column(Date, nullable=False, default=datetime.today)



# 'date_reported', 'ob_number', 'case_type', 'case_category'
class Case(AuditMixin, Model):
    __tablename__ = 'case'
    id = Column(Integer, autoincrement=True, primary_key=True)
    open_date = Column(DateTime, default=datetime.now, nullable=False)

    station_id = Column(Integer, ForeignKey('police_station.id'))
    station = relationship("PoliceStation")

    ob_number = Column(Integer, autoincrement=True, unique=True)
    report = Column(Text)

    casetype_id= Column(Integer,ForeignKey('case_type.id'), nullable=False )
    case_type = relationship("CaseType")

    case_category_id = Column(Integer,ForeignKey('case_category.id'), nullable=True )
    case_category = relationship("CaseCategory")

    status_id = Column(Integer, ForeignKey('case_status.id'))
    status = relationship(CaseStatus)
    #people  = relationship('Person', secondary=personcase, backref='case')

    # complaint_no,
    reporting_officer = Column(String(80))
    investigating_officer  = Column(String(80))
    investigation_outcomes = Column(Text)
    investigation_status  = Column(String(80))
    evidence_collected = Column(Text)
    evidence_pictures= Column(Text)
    offender_identification= Column(Text)
    offenders_arrested= Column(Text)
    arrest_location= Column(Text)
    arresting_officer= Column(Text)
    arrest_narrative= Column(Text)
    warrant_date= Column(Date)
    warrant_details= Column(Text)
    probable_cause= Column(Text)
    document_list= Column(Text)
    document_count= Column(Integer)
    documents= Column(Text)
    charge_date= Column(Date)
    charge_description= Column(Text)

    court_id = Column(Integer, ForeignKey('court.id'))
    charge_court= relationship(Court)

    first_hearing_date= Column(Date)

    # hearings = relationship('HearingType',
    #                         secondary = case_hearings,
    #                         back_populates = 'cases')
    hearing_dates= Column(Text)
    court_outcome= Column(Text)
    case_duration= Column(Integer)
    offender_picture = Column(Text)
    sentence_date= Column(Date)
    sentence= Column(Text)
    case_closed= Column(Boolean, default=False)

##### Admin Tables #####

class ContactForm(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'contact_form'
    message = Column(Text)



class Complaint(AuditMixin, Model):
    __tablename__ = 'complaint'
    id = Column(Integer, autoincrement=True, primary_key=True)
    report_date = Column(DateTime)
    report_time = Column(DateTime)
    event_date = Column(Date)
    event_place = Column(String(80))
    complainant = Column(String(80))
    comp_phone = Column(String(80))
    comp_email = Column(String(40))
    comp_address = Column(Text)
    comp_age = Column(Integer)
    comp_dob = Column(Date)
    comp_is_minor = Column(Boolean)
    comp_gender_fk = Column(Integer, ForeignKey('gender.id'))
    comp_gender = relationship(Gender)

    casetype_id = Column(Integer, ForeignKey('case_type.id'), nullable=False)
    case_type = relationship("CaseType")

    case_category_id = Column(Integer, ForeignKey('case_category.id'), nullable=True)
    case_category = relationship("CaseCategory")

    complainant_role = Column(Text)
    complaint = Column(Text, default='')
    complaint_language = Column(String(80))
    observations = Column(Text)
    injuries = Column(Text)
    loss = Column(Text)
    damage = Column(Text)
    theft = Column(Text)
    narcotics = Column(Boolean)
    fraud = Column(Text)
    domestic_abuse = Column(Boolean)
    complainant_is_victim = Column(Boolean)

    victim_name = Column(String(80))
    victim_phone = Column(String(80))
    victim_email = Column(String(80))
    victim_address = Column(String(80))
    victim_age = Column(Integer)
    victim_dob = Column(Date)
    victim_gender = Column(Boolean)
    victim_pwd = Column(Boolean)
    victim_religion = Column(String(80))
    victim_ethnicity = Column(String(80))
    offender_count = Column(Integer)
    offenders_known_to_victim = Column(Boolean)
    offender_known_to_complainant = Column(Boolean)
    offender_description = Column(Text)
    police_interpretation = Column(Text)
    is_a_crime = Column(Boolean)
    is_a_case = Column(Boolean)
    case_number = Column(String(80))
    closed = Column(Boolean, default=False)




# To Build
# Case-History
# Notifications
# Documents/ Scans/ Dockets
# Lawyer Registry
# DPP/State Counsel Registry (Teams & Team Leaders)
# User Profiles/Preferences
# Filing Fees

##### Features #####
# Contact Form
# Wizards
# Wizard Session save
