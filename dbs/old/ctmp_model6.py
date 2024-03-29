# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, ForeignKeyConstraint, Index, Integer, LargeBinary, String, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy





class Bail(db.Model):
    __tablename__ = 'bail'
    __table_args__ = (
        db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number']),
    )

    case_id = db.Column(db.Integer, primary_key=True, nullable=False)
    case_case_name = db.Column(db.String(150), primary_key=True, nullable=False)
    case_case_number = db.Column(db.String(30), primary_key=True, nullable=False)
    defendant = db.Column(db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
    amount = db.Column(db.Float(53), nullable=False)
    surety_count = db.Column(db.Integer, nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
    paid_date = db.Column(db.Date, nullable=False)
    receipt_number = db.Column(db.Text, nullable=False)

    case = db.relationship(u'Case', primaryjoin='and_(Bail.case_id == Case.id, Bail.case_case_name == Case.case_name, Bail.case_case_number == Case.case_number)', backref=u'bails')
    person = db.relationship(u'Person', primaryjoin='Bail.defendant == Person.id', backref=u'person_bails')
    person1 = db.relationship(u'Person', secondary=u't_bail_surety', backref=u'person_bails_0')


t_bail_surety = db.Table(
    'bail_surety',
    db.Column('bail_case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('bail_case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('bail_case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('bail_defendant', db.Integer, primary_key=True, nullable=False),
    db.Column('surety', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['bail_case_id', 'bail_case_case_name', 'bail_case_case_number', 'bail_defendant'], [u'bail.case_id', u'bail.case_case_name', u'bail.case_case_number', u'bail.defendant'])
)


class Case(db.Model):
    __tablename__ = 'case'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    court = db.Column(db.ForeignKey(u'court.id'), nullable=False, index=True)
    case_name = db.Column(db.String(150), primary_key=True, nullable=False)
    case_number = db.Column(db.String(30), primary_key=True, nullable=False)
    is_criminal = db.Column(db.Boolean, nullable=False)
    case_category = db.Column(db.ForeignKey(u'casecategory.id'), nullable=False, index=True)
    charge_date = db.Column(db.DateTime, nullable=False)

    casecategory = db.relationship(u'Casecategory', primaryjoin='Case.case_category == Casecategory.id', backref=u'cases')
    court1 = db.relationship(u'Court', primaryjoin='Case.court == Court.id', backref=u'cases')
    person = db.relationship(u'Person', secondary=u't_case_plaintiff', backref=u'person_person_person_person_person_person_cases')
    person1 = db.relationship(u'Person', secondary=u't_case_defense_attorney', backref=u'person_person_person_person_person_person_cases_0')
    person2 = db.relationship(u'Person', secondary=u't_case_witness', backref=u'person_person_person_person_person_person_cases')
    person3 = db.relationship(u'Person', secondary=u't_case_judge', backref=u'person_person_person_person_person_person_cases_0')
    offense = db.relationship(u'Offense', secondary=u't_case_offense', backref=u'cases')
    person4 = db.relationship(u'Person', secondary=u't_case_prosecutor', backref=u'person_person_person_person_person_person_cases')
    person5 = db.relationship(u'Person', secondary=u't_case_policeman', backref=u'person_person_person_person_person_person_cases_0')
    person6 = db.relationship(u'Person', secondary=u't_case_defendant', backref=u'person_person_person_person_person_person_cases')


t_case_defendant = db.Table(
    'case_defendant',
    db.Column('case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('defendant', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


t_case_defense_attorney = db.Table(
    'case_defense_attorney',
    db.Column('case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('defense_attorney', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


class CaseHearing(db.Model):
    __tablename__ = 'case_hearing'
    __table_args__ = (
        db.ForeignKeyConstraint(['bail_case_id', 'bail_case_case_name', 'bail_case_case_number', 'bail_defendant'], [u'bail.case_id', u'bail.case_case_name', u'bail.case_case_number', u'bail.defendant']),
        db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number']),
        db.Index('idx_case_hearing__bail_case_id_bail_case_case_name_bail_case_ca', 'bail_case_id', 'bail_case_case_name', 'bail_case_case_number', 'bail_defendant')
    )

    case_id = db.Column(db.Integer, primary_key=True, nullable=False)
    case_case_name = db.Column(db.String(150), primary_key=True, nullable=False)
    case_case_number = db.Column(db.String(30), primary_key=True, nullable=False)
    hearingtype = db.Column(db.ForeignKey(u'hearingtype.id'), primary_key=True, nullable=False, index=True)
    hearing_date = db.Column(db.DateTime, primary_key=True, nullable=False)
    prosecutor_present = db.Column(db.Boolean, nullable=False)
    defense_attorney_present = db.Column(db.Boolean, nullable=False)
    case_outcome = db.Column(db.Text, nullable=False)
    prison = db.Column(db.ForeignKey(u'prison.id'), nullable=False, index=True)
    from_remand = db.Column(db.Boolean, nullable=False)
    to_remand = db.Column(db.Boolean, nullable=False)
    to_prison = db.Column(db.Boolean, nullable=False)
    bail_case_id = db.Column(db.Integer, nullable=False)
    bail_case_case_name = db.Column(db.String(150), nullable=False)
    bail_case_case_number = db.Column(db.String(30), nullable=False)
    bail_defendant = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=False)

    bail_case = db.relationship(u'Bail', primaryjoin='and_(CaseHearing.bail_case_id == Bail.case_id, CaseHearing.bail_case_case_name == Bail.case_case_name, CaseHearing.bail_case_case_number == Bail.case_case_number, CaseHearing.bail_defendant == Bail.defendant)', backref=u'case_hearings')
    case = db.relationship(u'Case', primaryjoin='and_(CaseHearing.case_id == Case.id, CaseHearing.case_case_name == Case.case_name, CaseHearing.case_case_number == Case.case_number)', backref=u'case_hearings')
    hearingtype1 = db.relationship(u'Hearingtype', primaryjoin='CaseHearing.hearingtype == Hearingtype.id', backref=u'case_hearings')
    prison1 = db.relationship(u'Prison', primaryjoin='CaseHearing.prison == Prison.id', backref=u'case_hearings')
    person = db.relationship(u'Person', secondary=u't_case_hearing_defense_attorney', backref=u'person_person_case_hearings')
    person1 = db.relationship(u'Person', secondary=u't_case_hearing_prosecutor', backref=u'person_person_case_hearings_0')
    person2 = db.relationship(u'Person', secondary=u't_case_hearing_judge', backref=u'person_person_case_hearings')


t_case_hearing_defense_attorney = db.Table(
    'case_hearing_defense_attorney',
    db.Column('case_hearing_case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('case_hearing_case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('case_hearing_case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('case_hearing_hearingtype', db.Integer, primary_key=True, nullable=False),
    db.Column('case_hearing_hearing_date', db.DateTime, primary_key=True, nullable=False),
    db.Column('defense_attorney', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['case_hearing_case_id', 'case_hearing_case_case_name', 'case_hearing_case_case_number', 'case_hearing_hearingtype', 'case_hearing_hearing_date'], [u'case_hearing.case_id', u'case_hearing.case_case_name', u'case_hearing.case_case_number', u'case_hearing.hearingtype', u'case_hearing.hearing_date'])
)


t_case_hearing_judge = db.Table(
    'case_hearing_judge',
    db.Column('case_hearing_case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('case_hearing_case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('case_hearing_case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('case_hearing_hearingtype', db.Integer, primary_key=True, nullable=False),
    db.Column('case_hearing_hearing_date', db.DateTime, primary_key=True, nullable=False),
    db.Column('judge', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['case_hearing_case_id', 'case_hearing_case_case_name', 'case_hearing_case_case_number', 'case_hearing_hearingtype', 'case_hearing_hearing_date'], [u'case_hearing.case_id', u'case_hearing.case_case_name', u'case_hearing.case_case_number', u'case_hearing.hearingtype', u'case_hearing.hearing_date'])
)


t_case_hearing_prosecutor = db.Table(
    'case_hearing_prosecutor',
    db.Column('case_hearing_case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('case_hearing_case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('case_hearing_case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('case_hearing_hearingtype', db.Integer, primary_key=True, nullable=False),
    db.Column('case_hearing_hearing_date', db.DateTime, primary_key=True, nullable=False),
    db.Column('prosecutor', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['case_hearing_case_id', 'case_hearing_case_case_name', 'case_hearing_case_case_number', 'case_hearing_hearingtype', 'case_hearing_hearing_date'], [u'case_hearing.case_id', u'case_hearing.case_case_name', u'case_hearing.case_case_number', u'case_hearing.hearingtype', u'case_hearing.hearing_date'])
)


t_case_judge = db.Table(
    'case_judge',
    db.Column('case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('judge', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


t_case_offense = db.Table(
    'case_offense',
    db.Column('case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('offense', db.ForeignKey(u'offense.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


t_case_plaintiff = db.Table(
    'case_plaintiff',
    db.Column('case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('plaintiff', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


t_case_policeman = db.Table(
    'case_policeman',
    db.Column('case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('policeman', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


t_case_prosecutor = db.Table(
    'case_prosecutor',
    db.Column('case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('prosecutor', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


class CaseStatusChange(db.Model):
    __tablename__ = 'case_status_change'
    __table_args__ = (
        db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number']),
        db.Index('idx_case_status_change__case_id_case_case_name_case_case_number', 'case_id', 'case_case_name', 'case_case_number')
    )

    casestatus = db.Column(db.ForeignKey(u'casestatus.id'), primary_key=True, nullable=False)
    case_id = db.Column(db.Integer, primary_key=True, nullable=False)
    case_case_name = db.Column(db.String(150), primary_key=True, nullable=False)
    case_case_number = db.Column(db.String(30), primary_key=True, nullable=False)
    csc_date = db.Column(db.DateTime, primary_key=True, nullable=False)
    notes = db.Column(db.Text, nullable=False)

    case = db.relationship(u'Case', primaryjoin='and_(CaseStatusChange.case_id == Case.id, CaseStatusChange.case_case_name == Case.case_name, CaseStatusChange.case_case_number == Case.case_number)', backref=u'case_status_changes')
    casestatu = db.relationship(u'Casestatu', primaryjoin='CaseStatusChange.casestatus == Casestatu.id', backref=u'case_status_changes')


t_case_witness = db.Table(
    'case_witness',
    db.Column('case_id', db.Integer, primary_key=True, nullable=False),
    db.Column('case_case_name', db.String(150), primary_key=True, nullable=False),
    db.Column('case_case_number', db.String(30), primary_key=True, nullable=False),
    db.Column('witness', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True),
    db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number'])
)


class Casecategory(db.Model):
    __tablename__ = 'casecategory'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Casestatu(db.Model):
    __tablename__ = 'casestatus'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


t_complainant_complaint = db.Table(
    'complainant_complaint',
    db.Column('complainant', db.ForeignKey(u'person.id'), primary_key=True, nullable=False),
    db.Column('complaint', db.ForeignKey(u'complaint.id'), primary_key=True, nullable=False, index=True)
)


class Complaint(db.Model):
    __tablename__ = 'complaint'
    __table_args__ = (
        db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number']),
        db.Index('idx_complaint__case_id_case_case_name_case_case_number', 'case_id', 'case_case_name', 'case_case_number')
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    complaint_date = db.Column(db.DateTime, nullable=False)
    is_case = db.Column(db.Boolean)
    case_id = db.Column(db.Integer)
    case_case_name = db.Column(db.String(150))
    case_case_number = db.Column(db.String(30))
    notes = db.Column(db.Text, nullable=False)

    case = db.relationship(u'Case', primaryjoin='and_(Complaint.case_id == Case.id, Complaint.case_case_name == Case.case_name, Complaint.case_case_number == Case.case_number)', backref=u'complaints')
    person = db.relationship(u'Person', secondary=u't_complaint_offender', backref=u'person_complaints')
    person1 = db.relationship(u'Person', secondary=u't_complaint_policeman', backref=u'person_complaints_0')


t_complaint_offender = db.Table(
    'complaint_offender',
    db.Column('complaint', db.ForeignKey(u'complaint.id'), primary_key=True, nullable=False),
    db.Column('offender', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


t_complaint_policeman = db.Table(
    'complaint_policeman',
    db.Column('complaint', db.ForeignKey(u'complaint.id'), primary_key=True, nullable=False),
    db.Column('policeman', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())

    person = db.relationship(u'Person', secondary=u't_contact_plaintiff', backref=u'contacts')


t_contact_plaintiff = db.Table(
    'contact_plaintiff',
    db.Column('contact', db.ForeignKey(u'contact.id'), primary_key=True, nullable=False),
    db.Column('plaintiff', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


class Court(db.Model):
    __tablename__ = 'court'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    town = db.Column(db.ForeignKey(u'town.id'), nullable=False, index=True)
    court_level = db.Column(db.ForeignKey(u'courtlevel.id'), nullable=False, index=True)

    courtlevel = db.relationship(u'Courtlevel', primaryjoin='Court.court_level == Courtlevel.id', backref=u'courts')
    town1 = db.relationship(u'Town', primaryjoin='Court.town == Town.id', backref=u'courts')


class Courtlevel(db.Model):
    __tablename__ = 'courtlevel'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


t_defendant_filing = db.Table(
    'defendant_filing',
    db.Column('defendant', db.ForeignKey(u'person.id'), primary_key=True, nullable=False),
    db.Column('filing', db.ForeignKey(u'filing.id'), primary_key=True, nullable=False, index=True)
)


t_defendant_prison = db.Table(
    'defendant_prison',
    db.Column('defendant', db.ForeignKey(u'person.id'), primary_key=True, nullable=False),
    db.Column('prison', db.ForeignKey(u'prison.id'), primary_key=True, nullable=False, index=True)
)


class District(db.Model):
    __tablename__ = 'district'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    region = db.Column(db.ForeignKey(u'region.id'), nullable=False, index=True)

    region1 = db.relationship(u'Region', primaryjoin='District.region == Region.id', backref=u'districts')


class Document(db.Model):
    __tablename__ = 'document'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    document = db.Column(db.LargeBinary)
    doc_content = db.Column(db.Text, nullable=False)
    doc_img = db.Column(db.LargeBinary, nullable=False)
    doc_date = db.Column(db.Date, nullable=False)

    filing = db.relationship(u'Filing', secondary=u't_document_filing', backref=u'documents')


t_document_filing = db.Table(
    'document_filing',
    db.Column('document', db.ForeignKey(u'document.id'), primary_key=True, nullable=False),
    db.Column('filing', db.ForeignKey(u'filing.id'), primary_key=True, nullable=False, index=True)
)


class Filing(db.Model):
    __tablename__ = 'filing'
    __table_args__ = (
        db.ForeignKeyConstraint(['case__hearing_case_id', 'case__hearing_case_case_name', 'case__hearing_case_case_number', 'case__hearing_hearingtype', 'case__hearing_hearing_date'], [u'case_hearing.case_id', u'case_hearing.case_case_name', u'case_hearing.case_case_number', u'case_hearing.hearingtype', u'case_hearing.hearing_date']),
        db.ForeignKeyConstraint(['case_id', 'case_case_name', 'case_case_number'], [u'case.id', u'case.case_name', u'case.case_number']),
        db.Index('idx_filing__case__hearing_case_id_case__hearing_case_case_name_', 'case__hearing_case_id', 'case__hearing_case_case_name', 'case__hearing_case_case_number', 'case__hearing_hearingtype', 'case__hearing_hearing_date'),
        db.Index('idx_filing__case_id_case_case_name_case_case_number', 'case_id', 'case_case_name', 'case_case_number')
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    case_id = db.Column(db.Integer, nullable=False)
    case_case_name = db.Column(db.String(150), nullable=False)
    case_case_number = db.Column(db.String(30), nullable=False)
    filing_date = db.Column(db.DateTime, nullable=False)
    doc_name = db.Column(db.String(50), nullable=False)
    doc_content = db.Column(db.Text, nullable=False)
    case__hearing_case_id = db.Column(db.Integer, nullable=False)
    case__hearing_case_case_name = db.Column(db.String(150), nullable=False)
    case__hearing_case_case_number = db.Column(db.String(30), nullable=False)
    case__hearing_hearingtype = db.Column(db.Integer, nullable=False)
    case__hearing_hearing_date = db.Column(db.DateTime, nullable=False)
    filing_fee = db.Column(db.Float(53), nullable=False)
    receipt_number = db.Column(db.String(20), nullable=False)
    received_by = db.Column(db.String(50), nullable=False)

    case__hearing_case = db.relationship(u'CaseHearing', primaryjoin='and_(Filing.case__hearing_case_id == CaseHearing.case_id, Filing.case__hearing_case_case_name == CaseHearing.case_case_name, Filing.case__hearing_case_case_number == CaseHearing.case_case_number, Filing.case__hearing_hearingtype == CaseHearing.hearingtype, Filing.case__hearing_hearing_date == CaseHearing.hearing_date)', backref=u'filings')
    case = db.relationship(u'Case', primaryjoin='and_(Filing.case_id == Case.id, Filing.case_case_name == Case.case_name, Filing.case_case_number == Case.case_number)', backref=u'filings')
    person = db.relationship(u'Person', secondary=u't_filing_plaintiff', backref=u'filings')


t_filing_plaintiff = db.Table(
    'filing_plaintiff',
    db.Column('filing', db.ForeignKey(u'filing.id'), primary_key=True, nullable=False),
    db.Column('plaintiff', db.ForeignKey(u'person.id'), primary_key=True, nullable=False, index=True)
)


class Gender(db.Model):
    __tablename__ = 'gender'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Hearingtype(db.Model):
    __tablename__ = 'hearingtype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


t_offender_prison = db.Table(
    'offender_prison',
    db.Column('offender', db.ForeignKey(u'person.id'), primary_key=True, nullable=False),
    db.Column('prison', db.ForeignKey(u'prison.id'), primary_key=True, nullable=False, index=True)
)


class Offense(db.Model):
    __tablename__ = 'offense'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    gender = db.Column(db.ForeignKey(u'gender.id'), nullable=False, index=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    classtype = db.Column(db.Text, nullable=False)
    with_others = db.Column(db.Boolean)
    remanded = db.Column(db.Boolean)
    court = db.Column(db.ForeignKey(u'court.id'), index=True)
    court_level = db.Column(db.ForeignKey(u'courtlevel.id'), index=True)
    appelation = db.Column(db.String(100))
    is_police = db.Column(db.Boolean)
    law_firm = db.Column(db.String(100))
    bar_number = db.Column(db.String(20))
    call_to_bar_year = db.Column(db.Integer)
    special = db.Column(db.Boolean)
    role = db.Column(db.String(100))
    for_defense = db.Column(db.Boolean)
    how_many = db.Column(db.Integer)
    service_number = db.Column(db.String(50))
    rank = db.Column(db.String(40))

    court1 = db.relationship(u'Court', primaryjoin='Person.court == Court.id', backref=u'people')
    courtlevel = db.relationship(u'Courtlevel', primaryjoin='Person.court_level == Courtlevel.id', backref=u'people')
    gender1 = db.relationship(u'Gender', primaryjoin='Person.gender == Gender.id', backref=u'people')
    filing = db.relationship(u'Filing', secondary=u't_defendant_filing', backref=u'people')
    prison = db.relationship(u'Prison', secondary=u't_defendant_prison', backref=u'prison_people')
    prison1 = db.relationship(u'Prison', secondary=u't_offender_prison', backref=u'prison_people_0')
    complaint = db.relationship(u'Complaint', secondary=u't_complainant_complaint', backref=u'people')


class Policestation(db.Model):
    __tablename__ = 'policestation'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    town = db.Column(db.ForeignKey(u'town.id'), nullable=False, index=True)

    town1 = db.relationship(u'Town', primaryjoin='Policestation.town == Town.id', backref=u'policestations')


class Prison(db.Model):
    __tablename__ = 'prison'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    town = db.Column(db.ForeignKey(u'town.id'), nullable=False, index=True)
    warden = db.Column(db.String(50), nullable=False)

    town1 = db.relationship(u'Town', primaryjoin='Prison.town == Town.id', backref=u'prisons')


class Region(db.Model):
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Town(db.Model):
    __tablename__ = 'town'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    district = db.Column(db.ForeignKey(u'district.id'), nullable=False, index=True)

    district1 = db.relationship(u'District', primaryjoin='Town.district == District.id', backref=u'towns')
