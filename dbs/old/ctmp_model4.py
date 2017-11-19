# coding: utf-8
# from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Table, Text
from sqlalchemy.schema import FetchedValue
# from sqlalchemy.orm import relationship
# from flask_sqlalchemy import SQLAlchemy
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

# = SQLAlchemy()


class Bail(AuditMixin, Model):
    __tablename__ = 'bail'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    amount = Column(Float(53), nullable=False)

    hearing = relationship(u'Hearing', secondary=u't_bail_hearing', backref=u'bails')
    person = relationship(u'Person', secondary=u't_bail_surety', backref=u'bails')


t_bail_hearing = Table(
    'bail_hearing',
    Column('bail', ForeignKey(u'bail.id'), primary_key=True, nullable=False),
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False, index=True)
)


t_bail_surety = Table(
    'bail_surety',
    Column('bail', ForeignKey(u'bail.id'), primary_key=True, nullable=False),
    Column('surety', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


class Case(Model):
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    prosecutor_team = Column(ForeignKey(u'prosecutorteam.id'), nullable=False, index=True)
    complainant = Column(ForeignKey(u'person.id'), index=True)
    defense_att = Column(ForeignKey(u'person.id'), nullable=False, index=True)
    court = Column(ForeignKey(u'court.id'), nullable=False, index=True)
    judge = Column(ForeignKey(u'person.id'), nullable=False, index=True)
    case_type = Column(ForeignKey(u'casetype.id'), nullable=False, index=True)
    case_status = Column(ForeignKey(u'casestatus.id'), nullable=False, index=True)

    casestatu = relationship(u'Casestatu', primaryjoin='Case.case_status == Casestatu.id', backref=u'cases')
    casetype = relationship(u'Casetype', primaryjoin='Case.case_type == Casetype.id', backref=u'cases')
    person = relationship(u'Person', primaryjoin='Case.complainant == Person.id', backref=u'person_person_person_person_cases')
    court1 = relationship(u'Court', primaryjoin='Case.court == Court.id', backref=u'cases')
    person1 = relationship(u'Person', primaryjoin='Case.defense_att == Person.id', backref=u'person_person_person_person_cases_0')
    person2 = relationship(u'Person', primaryjoin='Case.judge == Person.id', backref=u'person_person_person_person_cases')
    prosecutorteam = relationship(u'Prosecutorteam', primaryjoin='Case.prosecutor_team == Prosecutorteam.id', backref=u'cases')
    person3 = relationship(u'Person', secondary=u't_case_witness', backref=u'person_person_person_person_cases_0')
    person4 = relationship(u'Person', secondary=u't_case_offender', backref=u'person_person_person_person_cases')
    complaint = relationship(u'Complaint', secondary=u't_case_complaint', backref=u'cases')
    policestation = relationship(u'Policestation', secondary=u't_case_policestation', backref=u'cases')
    prison = relationship(u'Prison', secondary=u't_case_prison', backref=u'cases')


t_case_complaint = Table(
    'case_complaint',
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('complaint', ForeignKey(u'complaint.id'), primary_key=True, nullable=False, index=True)
)


t_case_offender = Table(
    'case_offender',
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('offender', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


t_case_policestation = Table(
    'case_policestation',
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('policestation', ForeignKey(u'policestation.id'), primary_key=True, nullable=False, index=True)
)


t_case_prison = Table(
    'case_prison',
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('prison', ForeignKey(u'prison.id'), primary_key=True, nullable=False, index=True)
)


t_case_witness = Table(
    'case_witness',
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('witness', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


class Casestatu(Model):
    __tablename__ = 'casestatus'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


class Casetype(Model):
    __tablename__ = 'casetype'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


class Complaint(Model):
    __tablename__ = 'complaint'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    complainant_fk = Column(ForeignKey(u'person.id'), nullable=False, index=True)
    policeman_fk = Column(ForeignKey(u'person.id'), nullable=False, index=True)
    police_station = Column(ForeignKey(u'policestation.id'), nullable=False, index=True)
    statement = Column(Text, nullable=False)

    complainant = relationship(u'Person', primaryjoin='Complaint.complainant == Person.id', backref=u'person_complaints')
    policestation = relationship(u'Policestation', primaryjoin='Complaint.police_station == Policestation.id', backref=u'complaints')
    policeman = relationship(u'Person', primaryjoin='Complaint.policeman == Person.id', backref=u'person_complaints_0')


class Court(Model):
    __tablename__ = 'court'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    town = Column(ForeignKey(u'town.id'), nullable=False, index=True)
    court_level = Column(ForeignKey(u'courtlevel.id'), nullable=False, index=True)

    courtlevel = relationship(u'Courtlevel', primaryjoin='Court.court_level == Courtlevel.id', backref=u'courts')
    town1 = relationship(u'Town', primaryjoin='Court.town == Town.id', backref=u'courts')
    person = relationship(u'Person', secondary=u't_court_judge', backref=u'courts')


t_court_judge = Table(
    'court_judge',
    Column('court', ForeignKey(u'court.id'), primary_key=True, nullable=False),
    Column('judge', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


class Courtlevel(Model):
    __tablename__ = 'courtlevel'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    name = Column(String(40), nullable=False)


t_defenseatt_hearing = Table(
    'defenseatt_hearing',
    Column('defenseatt', ForeignKey(u'person.id'), primary_key=True, nullable=False),
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False, index=True)
)


class District(Model):
    __tablename__ = 'district'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    region = Column(ForeignKey(u'region.id'), nullable=False, index=True)

    region1 = relationship(u'Region', primaryjoin='District.region == Region.id', backref=u'districts')


class Document(Model):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    filing = Column(ForeignKey(u'filing.id'), nullable=False, index=True)
    content = Column(Text, nullable=False)

    filing1 = relationship(u'Filing', primaryjoin='Document.filing == Filing.id', backref=u'documents')


class Filing(Model):
    __tablename__ = 'filing'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    hearing = Column(ForeignKey(u'hearing.id'), index=True)
    file_date = Column(Date, nullable=False)

    hearing1 = relationship(u'Hearing', primaryjoin='Filing.hearing == Hearing.id', backref=u'filings')


class Gender(Model):
    __tablename__ = 'gender'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


class Hearing(Model):
    __tablename__ = 'hearing'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    case = Column(ForeignKey(u'case.id'), nullable=False, index=True)
    hearing_date = Column(Date, nullable=False)
    judge = Column(ForeignKey(u'person.id'), index=True)
    hearing_type = Column(ForeignKey(u'hearingtype.id'), nullable=False, index=True)

    case1 = relationship(u'Case', primaryjoin='Hearing.case == Case.id', backref=u'hearings')
    hearingtype = relationship(u'Hearingtype', primaryjoin='Hearing.hearing_type == Hearingtype.id', backref=u'hearings')
    person = relationship(u'Person', primaryjoin='Hearing.judge == Person.id', backref=u'person_person_hearings')
    person1 = relationship(u'Person', secondary=u't_hearing_prosecutor', backref=u'person_person_hearings_0')
    person2 = relationship(u'Person', secondary=u't_hearing_witness', backref=u'person_person_hearings')
    notification = relationship(u'Notification', secondary=u't_hearing_notification', backref=u'hearings')


t_hearing_notification = Table(
    'hearing_notification',
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    Column('notification', ForeignKey(u'notification.id'), primary_key=True, nullable=False, index=True)
)


t_hearing_prosecutor = Table(
    'hearing_prosecutor',
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    Column('prosecutor', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


t_hearing_witness = Table(
    'hearing_witness',
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    Column('witness', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


class Hearingtype(Model):
    __tablename__ = 'hearingtype'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    name = Column(String(40), nullable=False)


class Lawfirm(Model):
    __tablename__ = 'lawfirm'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


class Notification(Model):
    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


t_offender_prison = Table(
    'offender_prison',
    Column('offender', ForeignKey(u'person.id'), primary_key=True, nullable=False),
    Column('prison', ForeignKey(u'prison.id'), primary_key=True, nullable=False, index=True)
)




class Policestation(Model):
    __tablename__ = 'policestation'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    town = Column(ForeignKey(u'town.id'), nullable=False, index=True)

    town1 = relationship(u'Town', primaryjoin='Policestation.town == Town.id', backref=u'policestations')


class Prison(Model):
    __tablename__ = 'prison'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


class Prosecutorteam(Model):
    __tablename__ = 'prosecutorteam'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


class Region(Model):
    __tablename__ = 'region'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


class Town(Model):
    __tablename__ = 'town'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    district = Column(ForeignKey(u'district.id'), nullable=False, index=True)

    district1 = relationship(u'District', primaryjoin='Town.district == District.id', backref=u'towns')


class Person(PersonMixin, ContactMixin, ParentageMixin, AuditMixin, Model):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    # xname = Column(String(50), nullable=False)
    # address = Column(String(50))
    gender = Column(ForeignKey(u'gender.id'), nullable=False, index=True)

    discriminator = Column('type', String(50))
    __mapper_args__ = {'polymorphic_on': discriminator}

    #classtype = Column(Text, nullable=False)
    service_number = Column(String(50))
    reg_date = Column(Date)
    bar_number = Column(String(20))
    prosecutor_team = Column(ForeignKey(u'prosecutorteam.id'), index=True)
    law_firm = Column(ForeignKey(u'lawfirm.id'), index=True)
    phone = Column(Text)
    complaint = Column(ForeignKey(u'complaint.id'), index=True)

    complaint1 = relationship(u'Complaint', primaryjoin='Person.complaint == Complaint.id', backref=u'people')
    gender1 = relationship(u'Gender', primaryjoin='Person.gender == Gender.id', backref=u'people')
    lawfirm = relationship(u'Lawfirm', primaryjoin='Person.law_firm == Lawfirm.id', backref=u'people')
    prosecutorteam = relationship(u'Prosecutorteam', primaryjoin='Person.prosecutor_team == Prosecutorteam.id', backref=u'people')
    hearing = relationship(u'Hearing', secondary=u't_defenseatt_hearing', backref=u'people')
    prison = relationship(u'Prison', secondary=u't_offender_prison', backref=u'people')


class Policeman(Person):
    __mapper_args__ = {'polymorphic_identity': 'policeman'}
    service_number = Required(str, 50)
    complaints = Set('Complaint')


class Lawyer(Person):
    __mapper_args__ = {'polymorphic_identity': 'lawyer'}
    Reg_date = Required(date)
    bar_number = Required(str, 20)


class Prosecutor(Lawyer):
    __mapper_args__ = {'polymorphic_identity': 'prosecutor'}
    prosecutor_team = Required('ProsecutorTeam')
    hearings = Set('Hearing')


class DefenseAtt(Lawyer):
    __mapper_args__ = {'polymorphic_identity': 'defense_attorney'}
    law_firm = Optional('LawFirm')
    cases = Set('Case')
    hearings = Set('Hearing')



class Complainant(Person):
    __mapper_args__ = {'polymorphic_identity': 'complainant'}
    phone = Required(str)
    complaints = Set('Complaint')
    cases = Set('Case')


class Offender(Person):
    __mapper_args__ = {'polymorphic_identity': 'offender'}
    complaint = Required('Complaint')
    cases = Set('Case')
    prisons = Set('Prison')


class Witness(Person):
    __mapper_args__ = {'polymorphic_identity': 'witness'}
    cases = Set('Case')
    hearings = Set('Hearing')
