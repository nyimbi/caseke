# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, String, Table, Text
# from sqlalchemy.orm import relationship
# from sqlalchemy.schema import FetchedValue
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


class Bail(Model):
    __tablename__ = 'bail'
    __table_args__ = (
        ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number']),
    )

    case_id = Column(Integer, primary_key=True, nullable=False)
    case_case_name = Column(String(150), primary_key=True, nullable=False)
    case_case_number = Column(String(30), primary_key=True, nullable=False)
    defendant = Column(ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
    amount = Column(Float(53), nullable=False)
    surety_count = Column(Integer, nullable=False)
    paid = Column(Boolean, nullable=False)
    paid_date = Column(Date, nullable=False)
    receipt_number = Column(Text, nullable=False)

    case = relationship(u'Case', primaryjoin='and_(Bail.case_id == Case.id, Bail.case_case_name == Case.case_name, Bail.case_case_number == Case.case_number)', backref=u'bails')
    person = relationship(u'Person', primaryjoin='Bail.defendant == Person.id', backref=u'person_bails')
    person1 = relationship(u'Person', secondary=u't_bail_surety', backref=u'person_bails_0')


t_bail_surety = Table(
    'bail_surety',
    Column('bail_case_id', Integer, primary_key=True, nullable=False),
    Column('bail_case_case_name', String(150), primary_key=True, nullable=False),
    Column('bail_case_case_number', String(30), primary_key=True, nullable=False),
    Column('bail_defendant', Integer, primary_key=True, nullable=False),
    Column('surety', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['bail_case_id', 'bail_case_case_name', 'bail_case_case_number', 'bail_defendant'], [u'bail.case_id', u'bail.case_case_name', u'bail.case_case_number', u'bail.defendant'])
)


class Case(Model):
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True, nullable=False)
    court = Column(ForeignKey(u'court.id'), nullable=False, index=True)
    case_name = Column(String(150), primary_key=True, nullable=False)
    case_number = Column(String(30), primary_key=True, nullable=False)
    is_criminal = Column(Boolean, nullable=False)
    case_category = Column(ForeignKey(u'casecategory.id'), nullable=False, index=True)
    charge_date = Column(DateTime, nullable=False)

    casecategory = relationship(u'Casecategory', primaryjoin='Case.case_category == Casecategory.id', backref=u'cases')
    court1 = relationship(u'Court', primaryjoin='Case.court == Court.id', backref=u'cases')
    person = relationship(u'Person', secondary=u't_case_plaintiff', backref=u'person_person_person_person_person_person_cases')
    person1 = relationship(u'Person', secondary=u't_case_defense_attorney', backref=u'person_person_person_person_person_person_cases_0')
    person2 = relationship(u'Person', secondary=u't_case_judge', backref=u'person_person_person_person_person_person_cases')
    offense = relationship(u'Offense', secondary=u't_case_offense', backref=u'cases')
    person3 = relationship(u'Person', secondary=u't_case_prosecutor', backref=u'person_person_person_person_person_person_cases_0')
    person4 = relationship(u'Person', secondary=u't_case_policeman', backref=u'person_person_person_person_person_person_cases')
    person5 = relationship(u'Person', secondary=u't_case_witnesses', backref=u'person_person_person_person_person_person_cases_0')
    person6 = relationship(u'Person', secondary=u't_case_defendant', backref=u'person_person_person_person_person_person_cases')


t_case_defendant = Table(
    'case_defendant',
    Column('case_id', Integer, primary_key=True, nullable=False),
    Column('case_case_name', String(150), primary_key=True, nullable=False),
    Column('case_case_number', String(30), primary_key=True, nullable=False),
    Column('defendant', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


t_case_defense_attorney = Table(
    'case_defense_attorney',
    Column('case_id', Integer, primary_key=True, nullable=False),
    Column('case_case_name', String(150), primary_key=True, nullable=False),
    Column('case_case_number', String(30), primary_key=True, nullable=False),
    Column('defense_attorney', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


class CaseHearing(Model):
    __tablename__ = 'case_hearing'
    __table_args__ = (
        ForeignKeyConstraint(['bail_case_id', 'bail_case_case_name', 'bail_case_case_number', 'bail_defendant'], [u'bail.case_id', u'bail.case_case_name', u'bail.case_case_number', u'bail.defendant']),
        ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number']),
        Index('idx_case_hearing__bail_case_id_bail_case_case_name_bail_case_ca', 'bail_case_id', 'bail_case_case_name', 'bail_case_case_number', 'bail_defendant')
    )

    case_id = Column(Integer, primary_key=True, nullable=False)
    case_case_name = Column(String(150), primary_key=True, nullable=False)
    case_case_number = Column(String(30), primary_key=True, nullable=False)
    hearingtype = Column(ForeignKey(u'hearingtype.id'), primary_key=True, nullable=False, index=True)
    hearing_date = Column(DateTime, primary_key=True, nullable=False)
    prosecutor_present = Column(Boolean, nullable=False)
    defense_attorney_present = Column(Boolean, nullable=False)
    case_outcome = Column(Text, nullable=False)
    prison = Column(ForeignKey(u'prison.id'), nullable=False, index=True)
    from_remand = Column(Boolean, nullable=False)
    to_remand = Column(Boolean, nullable=False)
    to_prison = Column(Boolean, nullable=False)
    bail_case_id = Column(Integer, nullable=False)
    bail_case_case_name = Column(String(150), nullable=False)
    bail_case_case_number = Column(String(30), nullable=False)
    bail_defendant = Column(Integer, nullable=False)
    notes = Column(Text, nullable=False)

    bail_case = relationship(u'Bail', primaryjoin='and_(CaseHearing.bail_case_id == Bail.case_id, CaseHearing.bail_case_case_name == Bail.case_case_name, CaseHearing.bail_case_case_number == Bail.case_case_number, CaseHearing.bail_defendant == Bail.defendant)', backref=u'case_hearings')
    case = relationship(u'Case', primaryjoin='and_(CaseHearing.case_id == Case.id, CaseHearing.case_case_name == Case.case_name, CaseHearing.case_case_number == Case.case_number)', backref=u'case_hearings')
    hearingtype1 = relationship(u'Hearingtype', primaryjoin='CaseHearing.hearingtype == Hearingtype.id', backref=u'case_hearings')
    prison1 = relationship(u'Prison', primaryjoin='CaseHearing.prison == Prison.id', backref=u'case_hearings')
    person = relationship(u'Person', secondary=u't_case_hearing_defense_attorney', backref=u'person_person_case_hearings')
    person1 = relationship(u'Person', secondary=u't_case_hearing_prosecutor', backref=u'person_person_case_hearings_0')
    person2 = relationship(u'Person', secondary=u't_case_hearing_judge', backref=u'person_person_case_hearings')


t_case_hearing_defense_attorney = Table(
    'case_hearing_defense_attorney',
    Column('case_hearing_case_id', Integer, primary_key=True, nullable=False),
    Column('case_hearing_case_case_name', String(150), primary_key=True, nullable=False),
    Column('case_hearing_case_case_number', String(30), primary_key=True, nullable=False),
    Column('case_hearing_hearingtype', Integer, primary_key=True, nullable=False),
    Column('case_hearing_hearing_date', DateTime, primary_key=True, nullable=False),
    Column('defense_attorney', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['case_hearing_case_id', 'case_hearing_case_case_name', 'case_hearing_case_case_number', 'case_hearing_hearingtype', 'case_hearing_hearing_date'], [u'case_hearing.case_id', u'case_hearing.case_case_name', u'case_hearing.case_case_number', u'case_hearing.hearingtype', u'case_hearing.hearing_date'])
)


t_case_hearing_judge = Table(
    'case_hearing_judge',
    Column('case_hearing_case_id', Integer, primary_key=True, nullable=False),
    Column('case_hearing_case_case_name', String(150), primary_key=True, nullable=False),
    Column('case_hearing_case_case_number', String(30), primary_key=True, nullable=False),
    Column('case_hearing_hearingtype', Integer, primary_key=True, nullable=False),
    Column('case_hearing_hearing_date', DateTime, primary_key=True, nullable=False),
    Column('judge', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['case_hearing_case_id', 'case_hearing_case_case_name', 'case_hearing_case_case_number', 'case_hearing_hearingtype', 'case_hearing_hearing_date'], [u'case_hearing.case_id', u'case_hearing.case_case_name', u'case_hearing.case_case_number', u'case_hearing.hearingtype', u'case_hearing.hearing_date'])
)


t_case_hearing_prosecutor = Table(
    'case_hearing_prosecutor',
    Column('case_hearing_case_id', Integer, primary_key=True, nullable=False),
    Column('case_hearing_case_case_name', String(150), primary_key=True, nullable=False),
    Column('case_hearing_case_case_number', String(30), primary_key=True, nullable=False),
    Column('case_hearing_hearingtype', Integer, primary_key=True, nullable=False),
    Column('case_hearing_hearing_date', DateTime, primary_key=True, nullable=False),
    Column('prosecutor', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['case_hearing_case_id', 'case_hearing_case_case_name', 'case_hearing_case_case_number', 'case_hearing_hearingtype', 'case_hearing_hearing_date'], [u'case_hearing.case_id', u'case_hearing.case_case_name', u'case_hearing.case_case_number', u'case_hearing.hearingtype', u'case_hearing.hearing_date'])
)


t_case_judge = Table(
    'case_judge',
    Column('case_id', Integer, primary_key=True, nullable=False),
    Column('case_case_name', String(150), primary_key=True, nullable=False),
    Column('case_case_number', String(30), primary_key=True, nullable=False),
    Column('judge', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


t_case_offense = Table(
    'case_offense',
    Column('case_id', Integer, primary_key=True, nullable=False),
    Column('case_case_name', String(150), primary_key=True, nullable=False),
    Column('case_case_number', String(30), primary_key=True, nullable=False),
    Column('offense', ForeignKey(u'offense.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


t_case_plaintiff = Table(
    'case_plaintiff',
    Column('case_id', Integer, primary_key=True, nullable=False),
    Column('case_case_name', String(150), primary_key=True, nullable=False),
    Column('case_case_number', String(30), primary_key=True, nullable=False),
    Column('plaintiff', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


t_case_policeman = Table(
    'case_policeman',
    Column('case_id', Integer, primary_key=True, nullable=False),
    Column('case_case_name', String(150), primary_key=True, nullable=False),
    Column('case_case_number', String(30), primary_key=True, nullable=False),
    Column('policeman', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


t_case_prosecutor = Table(
    'case_prosecutor',
    Column('case_id', Integer, primary_key=True, nullable=False),
    Column('case_case_name', String(150), primary_key=True, nullable=False),
    Column('case_case_number', String(30), primary_key=True, nullable=False),
    Column('prosecutor', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


class CaseStatusChange(Model):
    __tablename__ = 'case_status_change'
    __table_args__ = (
        ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number']),
        Index('idx_case_status_change__case_id_case_case_name_case_case_number', 'case_id', 'case_case_name', 'case_case_number')
    )

    casestatus = Column(ForeignKey(u'casestatus.id'), primary_key=True, nullable=False)
    case_id = Column(Integer, primary_key=True, nullable=False)
    case_case_name = Column(String(150), primary_key=True, nullable=False)
    case_case_number = Column(String(30), primary_key=True, nullable=False)
    csc_date = Column(DateTime, primary_key=True, nullable=False)
    notes = Column(Text, nullable=False)

    case = relationship(u'Case', primaryjoin='and_(CaseStatusChange.case_id == Case.id, CaseStatusChange.case_case_name == Case.case_name, CaseStatusChange.case_case_number == Case.case_number)', backref=u'case_status_changes')
    casestatu = relationship(u'Casestatu', primaryjoin='CaseStatusChange.casestatus == Casestatu.id', backref=u'case_status_changes')


t_case_witnesses = Table(
    'case_witnesses',
    Column('case_id', Integer, primary_key=True, nullable=False),
    Column('case_case_name', String(150), primary_key=True, nullable=False),
    Column('case_case_number', String(30), primary_key=True, nullable=False),
    Column('witnesses', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


class Casecategory(Model):
    __tablename__ = 'casecategory'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


class Casestatu(Model):
    __tablename__ = 'casestatus'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


t_complainant_complaint = Table(
    'complainant_complaint',
    Column('complainant', ForeignKey(u'person.id'), primary_key=True, nullable=False),
    Column('complaint', ForeignKey(u'complaint.id'), primary_key=True, nullable=False, index=True)
)


class Complaint(Model):
    __tablename__ = 'complaint'
    __table_args__ = (
        ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number']),
        Index('idx_complaint__case_id_case_case_name_case_case_number', 'case_id', 'case_case_name', 'case_case_number')
    )

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    complaint_date = Column(DateTime, nullable=False)
    is_case = Column(Boolean)
    case_id = Column(Integer)
    case_case_name = Column(String(150))
    case_case_number = Column(String(30))
    notes = Column(Text, nullable=False)

    case = relationship(u'Case', primaryjoin='and_(Complaint.case_id == Case.id, Complaint.case_case_name == Case.case_name, Complaint.case_case_number == Case.case_number)', backref=u'complaints')
    person = relationship(u'Person', secondary=u't_complaint_offender', backref=u'person_complaints')
    person1 = relationship(u'Person', secondary=u't_complaint_policeman', backref=u'person_complaints_0')


t_complaint_offender = Table(
    'complaint_offender',
    Column('complaint', ForeignKey(u'complaint.id'), primary_key=True, nullable=False),
    Column('offender', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


t_complaint_policeman = Table(
    'complaint_policeman',
    Column('complaint', ForeignKey(u'complaint.id'), primary_key=True, nullable=False),
    Column('policeman', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


class Contact(Model):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())

    person = relationship(u'Person', secondary=u't_contact_plaintiff', backref=u'contacts')


t_contact_plaintiff = Table(
    'contact_plaintiff',
    Column('contact', ForeignKey(u'contact.id'), primary_key=True, nullable=False),
    Column('plaintiff', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


class Court(Model):
    __tablename__ = 'court'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    town = Column(ForeignKey(u'town.id'), nullable=False, index=True)
    court_level = Column(ForeignKey(u'courtlevel.id'), nullable=False, index=True)

    courtlevel = relationship(u'Courtlevel', primaryjoin='Court.court_level == Courtlevel.id', backref=u'courts')
    town1 = relationship(u'Town', primaryjoin='Court.town == Town.id', backref=u'courts')


class Courtlevel(Model):
    __tablename__ = 'courtlevel'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


t_defendant_filing = Table(
    'defendant_filing',
    Column('defendant', ForeignKey(u'person.id'), primary_key=True, nullable=False),
    Column('filing', ForeignKey(u'filing.id'), primary_key=True, nullable=False, index=True)
)


t_defendant_prison = Table(
    'defendant_prison',
    Column('defendant', ForeignKey(u'person.id'), primary_key=True, nullable=False),
    Column('prison', ForeignKey(u'prison.id'), primary_key=True, nullable=False, index=True)
)


class District(Model):
    __tablename__ = 'district'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    region = Column(ForeignKey(u'region.id'), nullable=False, index=True)

    region1 = relationship(u'Region', primaryjoin='District.region == Region.id', backref=u'districts')


class Document(Model):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    document = Column(LargeBinary)
    doc_content = Column(Text, nullable=False)
    doc_img = Column(LargeBinary, nullable=False)
    doc_date = Column(Date, nullable=False)

    filing = relationship(u'Filing', secondary=u't_document_filing', backref=u'documents')


t_document_filing = Table(
    'document_filing',
    Column('document', ForeignKey(u'document.id'), primary_key=True, nullable=False),
    Column('filing', ForeignKey(u'filing.id'), primary_key=True, nullable=False, index=True)
)


class Filing(Model):
    __tablename__ = 'filing'
    __table_args__ = (
        ForeignKeyConstraint(['case__hearing_case_id', 'case__hearing_case_case_name', 'case__hearing_case_case_number', 'case__hearing_hearingtype', 'case__hearing_hearing_date'], [u'case_hearing.case_id', u'case_hearing.case_case_name', u'case_hearing.case_case_number', u'case_hearing.hearingtype', u'case_hearing.hearing_date']),
        ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number']),
        Index('idx_filing__case__hearing_case_id_case__hearing_case_case_name_', 'case__hearing_case_id', 'case__hearing_case_case_name', 'case__hearing_case_case_number', 'case__hearing_hearingtype', 'case__hearing_hearing_date'),
        Index('idx_filing__case_id_case_case_name_case_case_number', 'case_id', 'case_case_name', 'case_case_number')
    )

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    case_id = Column(Integer, nullable=False)
    case_case_name = Column(String(150), nullable=False)
    case_case_number = Column(String(30), nullable=False)
    filing_date = Column(DateTime, nullable=False)
    doc_name = Column(String(50), nullable=False)
    doc_content = Column(Text, nullable=False)
    case__hearing_case_id = Column(Integer, nullable=False)
    case__hearing_case_case_name = Column(String(150), nullable=False)
    case__hearing_case_case_number = Column(String(30), nullable=False)
    case__hearing_hearingtype = Column(Integer, nullable=False)
    case__hearing_hearing_date = Column(DateTime, nullable=False)
    filing_fee = Column(Float(53), nullable=False)
    receipt_number = Column(String(20), nullable=False)
    received_by = Column(String(50), nullable=False)

    case__hearing_case = relationship(u'CaseHearing', primaryjoin='and_(Filing.case__hearing_case_id == CaseHearing.case_id, Filing.case__hearing_case_case_name == CaseHearing.case_case_name, Filing.case__hearing_case_case_number == CaseHearing.case_case_number, Filing.case__hearing_hearingtype == CaseHearing.hearingtype, Filing.case__hearing_hearing_date == CaseHearing.hearing_date)', backref=u'filings')
    case = relationship(u'Case', primaryjoin='and_(Filing.case_id == Case.id, Filing.case_case_name == Case.case_name, Filing.case_case_number == Case.case_number)', backref=u'filings')
    person = relationship(u'Person', secondary=u't_filing_plaintiff', backref=u'filings')


t_filing_plaintiff = Table(
    'filing_plaintiff',
    Column('filing', ForeignKey(u'filing.id'), primary_key=True, nullable=False),
    Column('plaintiff', ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


class Gender(Model):
    __tablename__ = 'gender'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


class Hearingtype(Model):
    __tablename__ = 'hearingtype'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


t_offender_prison = Table(
    'offender_prison',
    Column('offender', ForeignKey(u'person.id'), primary_key=True, nullable=False),
    Column('prison', ForeignKey(u'prison.id'), primary_key=True, nullable=False, index=True)
)


class Offense(Model):
    __tablename__ = 'offense'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


class Person(Model):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    gender = Column(ForeignKey(u'gender.id'), nullable=False, index=True)
    date_of_birth = Column(Date, nullable=False)
    classtype = Column(Text, nullable=False)
    with_others = Column(Boolean)
    remanded = Column(Boolean)
    court = Column(ForeignKey(u'court.id'), index=True)
    court_level = Column(ForeignKey(u'courtlevel.id'), index=True)
    appelation = Column(String(100))
    is_police = Column(Boolean)
    law_firm = Column(String(100))
    bar_number = Column(String(20))
    call_to_bar_year = Column(Integer)
    special = Column(Boolean)
    role = Column(String(100))
    for_defense = Column(Boolean)
    how_many = Column(Integer)
    service_number = Column(String(50))
    rank = Column(String(40))

    court1 = relationship(u'Court', primaryjoin='Person.court == Court.id', backref=u'people')
    courtlevel = relationship(u'Courtlevel', primaryjoin='Person.court_level == Courtlevel.id', backref=u'people')
    gender1 = relationship(u'Gender', primaryjoin='Person.gender == Gender.id', backref=u'people')
    filing = relationship(u'Filing', secondary=u't_defendant_filing', backref=u'people')
    prison = relationship(u'Prison', secondary=u't_defendant_prison', backref=u'prison_people')
    prison1 = relationship(u'Prison', secondary=u't_offender_prison', backref=u'prison_people_0')
    complaint = relationship(u'Complaint', secondary=u't_complainant_complaint', backref=u'people')


class Policestation(Model):
    __tablename__ = 'policestation'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    town = Column(ForeignKey(u'town.id'), nullable=False, index=True)

    town1 = relationship(u'Town', primaryjoin='Policestation.town == Town.id', backref=u'policestations')


class Prison(Model):
    __tablename__ = 'prison'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    town = Column(ForeignKey(u'town.id'), nullable=False, index=True)

    town1 = relationship(u'Town', primaryjoin='Prison.town == Town.id', backref=u'prisons')


class Region(Model):
    __tablename__ = 'region'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())


class Town(Model):
    __tablename__ = 'town'

    id = Column(Integer, primary_key=True, server_default=FetchedValue())
    district = Column(ForeignKey(u'district.id'), nullable=False, index=True)

    district1 = relationship(u'District', primaryjoin='Town.district == District.id', backref=u'towns')
