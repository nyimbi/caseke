# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class CaeType(db.Model):
    __tablename__ = 'CaeType'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Bail(db.Model):
    __tablename__ = 'bail'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    hearing = db.Column(db.ForeignKey(u'hearing.id'), nullable=False, index=True)
    amount = db.Column(db.Float(53), nullable=False)

    hearing1 = db.relationship(u'Hearing', primaryjoin='Bail.hearing == Hearing.id', backref=u'bails')


class Case(db.Model):
    __tablename__ = 'case'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    complaint = db.Column(db.ForeignKey(u'complaint.id'), nullable=False, index=True)
    prosecutor_team = db.Column(db.ForeignKey(u'prosecutorteam.id'), nullable=False, index=True)
    complainant = db.Column(db.ForeignKey(u'person.id'), index=True)
    offender = db.Column(db.ForeignKey(u'person.id'), nullable=False, index=True)
    defense_att = db.Column(db.ForeignKey(u'person.id'), nullable=False, index=True)
    court = db.Column(db.ForeignKey(u'court.id'), nullable=False, index=True)
    judge = db.Column(db.ForeignKey(u'person.id'), nullable=False, index=True)
    prison = db.Column(db.ForeignKey(u'prison.id'), nullable=False, index=True)
    case_type = db.Column(db.ForeignKey(u'CaeType.id'), nullable=False, index=True)
    case_status = db.Column(db.ForeignKey(u'casestatus.id'), nullable=False, index=True)

    casestatu = db.relationship(u'Casestatu', primaryjoin='Case.case_status == Casestatu.id', backref=u'cases')
    CaeType = db.relationship(u'CaeType', primaryjoin='Case.case_type == CaeType.id', backref=u'cases')
    person = db.relationship(u'Person', primaryjoin='Case.complainant == Person.id', backref=u'person_person_person_cases')
    complaint1 = db.relationship(u'Complaint', primaryjoin='Case.complaint == Complaint.id', backref=u'cases')
    court1 = db.relationship(u'Court', primaryjoin='Case.court == Court.id', backref=u'cases')
    person1 = db.relationship(u'Person', primaryjoin='Case.defense_att == Person.id', backref=u'person_person_person_cases_0')
    person2 = db.relationship(u'Person', primaryjoin='Case.judge == Person.id', backref=u'person_person_person_cases')
    person3 = db.relationship(u'Person', primaryjoin='Case.offender == Person.id', backref=u'person_person_person_cases_0')
    prison1 = db.relationship(u'Prison', primaryjoin='Case.prison == Prison.id', backref=u'cases')
    prosecutorteam = db.relationship(u'Prosecutorteam', primaryjoin='Case.prosecutor_team == Prosecutorteam.id', backref=u'cases')


class Casestatu(db.Model):
    __tablename__ = 'casestatus'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Complaint(db.Model):
    __tablename__ = 'complaint'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    complainant = db.Column(db.ForeignKey(u'person.id'), nullable=False, index=True)
    police = db.Column(db.ForeignKey(u'person.id'), nullable=False, index=True)
    police_station = db.Column(db.ForeignKey(u'policestation.id'), nullable=False, index=True)
    statement = db.Column(db.Text, nullable=False)

    person = db.relationship(u'Person', primaryjoin='Complaint.complainant == Person.id', backref=u'person_complaints')
    person1 = db.relationship(u'Person', primaryjoin='Complaint.police == Person.id', backref=u'person_complaints_0')
    policestation = db.relationship(u'Policestation', primaryjoin='Complaint.police_station == Policestation.id', backref=u'complaints')


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
    name = db.Column(db.String(40), nullable=False)


class District(db.Model):
    __tablename__ = 'district'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    region = db.Column(db.ForeignKey(u'region.id'), nullable=False, index=True)

    region1 = db.relationship(u'Region', primaryjoin='District.region == Region.id', backref=u'districts')


class Document(db.Model):
    __tablename__ = 'document'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    filing = db.Column(db.ForeignKey(u'filing.id'), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)

    filing1 = db.relationship(u'Filing', primaryjoin='Document.filing == Filing.id', backref=u'documents')


class Filing(db.Model):
    __tablename__ = 'filing'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    hearing = db.Column(db.ForeignKey(u'hearing.id'), index=True)
    file_date = db.Column(db.Date, nullable=False)

    hearing1 = db.relationship(u'Hearing', primaryjoin='Filing.hearing == Hearing.id', backref=u'filings')


class Gender(db.Model):
    __tablename__ = 'gender'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Hearing(db.Model):
    __tablename__ = 'hearing'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    case = db.Column(db.ForeignKey(u'case.id'), nullable=False, index=True)
    defense_att = db.Column(db.ForeignKey(u'person.id'), index=True)
    prosecutor = db.Column(db.ForeignKey(u'person.id'), index=True)
    hearing_date = db.Column(db.Date, nullable=False)
    judge = db.Column(db.ForeignKey(u'person.id'), index=True)
    hearing_type = db.Column(db.ForeignKey(u'hearingtype.id'), nullable=False, index=True)
    notification = db.Column(db.ForeignKey(u'notification.id'), index=True)

    case1 = db.relationship(u'Case', primaryjoin='Hearing.case == Case.id', backref=u'hearings')
    person = db.relationship(u'Person', primaryjoin='Hearing.defense_att == Person.id', backref=u'person_person_hearings')
    hearingtype = db.relationship(u'Hearingtype', primaryjoin='Hearing.hearing_type == Hearingtype.id', backref=u'hearings')
    person1 = db.relationship(u'Person', primaryjoin='Hearing.judge == Person.id', backref=u'person_person_hearings_0')
    notification1 = db.relationship(u'Notification', primaryjoin='Hearing.notification == Notification.id', backref=u'hearings')
    person2 = db.relationship(u'Person', primaryjoin='Hearing.prosecutor == Person.id', backref=u'person_person_hearings')


class Hearingtype(db.Model):
    __tablename__ = 'hearingtype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(40), nullable=False)


class Lawfirm(db.Model):
    __tablename__ = 'lawfirm'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Notification(db.Model):
    __tablename__ = 'notification'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    xname = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50))
    gender = db.Column(db.ForeignKey(u'gender.id'), nullable=False, index=True)
    classtype = db.Column(db.Text, nullable=False)
    service_number = db.Column(db.String(50))
    reg_date = db.Column(db.Date)
    bar_number = db.Column(db.String(20))
    prosecutor_team = db.Column(db.ForeignKey(u'prosecutorteam.id'), index=True)
    law_firm = db.Column(db.ForeignKey(u'lawfirm.id'), index=True)
    phone = db.Column(db.Text)
    complaint = db.Column(db.ForeignKey(u'complaint.id'), index=True)
    prison = db.Column(db.ForeignKey(u'prison.id'), index=True)
    court = db.Column(db.ForeignKey(u'court.id'), index=True)
    bail = db.Column(db.ForeignKey(u'bail.id'), index=True)

    bail1 = db.relationship(u'Bail', primaryjoin='Person.bail == Bail.id', backref=u'people')
    complaint1 = db.relationship(u'Complaint', primaryjoin='Person.complaint == Complaint.id', backref=u'people')
    court1 = db.relationship(u'Court', primaryjoin='Person.court == Court.id', backref=u'people')
    gender1 = db.relationship(u'Gender', primaryjoin='Person.gender == Gender.id', backref=u'people')
    lawfirm = db.relationship(u'Lawfirm', primaryjoin='Person.law_firm == Lawfirm.id', backref=u'people')
    prison1 = db.relationship(u'Prison', primaryjoin='Person.prison == Prison.id', backref=u'people')
    prosecutorteam = db.relationship(u'Prosecutorteam', primaryjoin='Person.prosecutor_team == Prosecutorteam.id', backref=u'people')


class Policestation(db.Model):
    __tablename__ = 'policestation'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    town = db.Column(db.ForeignKey(u'town.id'), nullable=False, index=True)

    town1 = db.relationship(u'Town', primaryjoin='Policestation.town == Town.id', backref=u'policestations')


class Prison(db.Model):
    __tablename__ = 'prison'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Prosecutorteam(db.Model):
    __tablename__ = 'prosecutorteam'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Region(db.Model):
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Town(db.Model):
    __tablename__ = 'town'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    district = db.Column(db.ForeignKey(u'district.id'), nullable=False, index=True)

    district1 = db.relationship(u'District', primaryjoin='Town.district == District.id', backref=u'towns')
