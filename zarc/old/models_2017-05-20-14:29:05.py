# coding: utf-8
# AUTOGENERATED BY gen_script.sh from kpony3.py
# Copyright (C) Nyimbi Odero, Sat May 20 14:27:05 EAT 2017
 
from sqlalchemy import func
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn, UserExtensionMixin 
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.filemanager import ImageManager
from sqlalchemy_utils import aggregated
from sqlalchemy.orm import relationship, query, defer, deferred

from sqlalchemy import (Column, Integer, String, ForeignKey,
	Sequence, Float, Text, BigInteger, Date,
	DateTime, Time, Boolean, CheckConstraint,
	UniqueConstraint, LargeBinary , Table)
from datetime import timedelta, datetime, date
from sqlalchemy.dialects.postgresql import *
from .mixins import *

# Here is how to extend the User model
#class UserExtended(Model, UserExtensionMixin):
#    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=True)
#    contact_group = relationship('ContactGroup')




class Attorney(PersonMixin, ContactMixin,  AuditMixin, Model):
    __tablename__ = 'attorney'

    id = Column(Integer, primary_key=True, autoincrement=True)
    law_firm = Column(ForeignKey(u'lawfirm.id'), index=True)
    barnumber = Column(String(20), nullable=False)

    lawfirm = relationship(u'Lawfirm', primaryjoin='Attorney.law_firm == Lawfirm.id', backref=u'attorneys')
    hearing = relationship(u'Hearing', secondary='attorney_hearing', backref=u'attorneys')


attorney_hearing = Table(
    'attorney_hearing', Model.metadata, 
    Column('attorney', ForeignKey(u'attorney.id'), primary_key=True, nullable=False),
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False, index=True)
)


class Bail(AuditMixin, Model):
    __tablename__ = 'bail'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hearing = Column(ForeignKey(u'hearing.id'), nullable=False, index=True)
    defendant = Column(ForeignKey(u'defendant.id'), nullable=False, index=True)
    amountgranted = Column(Float(53), nullable=False)
    noofsureties = Column(Integer, nullable=False)
    paid = Column(Boolean, nullable=False)
    paydate = Column(Date, nullable=False)
    receiptno = Column(String(100), nullable=False)

    defendant1 = relationship(u'Defendant', primaryjoin='Bail.defendant == Defendant.id', backref=u'bails')
    hearing1 = relationship(u'Hearing', primaryjoin='Bail.hearing == Hearing.id', backref=u'bails')
    surety = relationship(u'Surety', secondary='bail_surety', backref=u'bails')


bail_surety = Table(
    'bail_surety', Model.metadata, 
    Column('bail', ForeignKey(u'bail.id'), primary_key=True, nullable=False),
    Column('surety', ForeignKey(u'surety.id'), primary_key=True, nullable=False, index=True)
)


class Case(AuditMixin, Model):
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True, autoincrement=True)
    casename = Column(String(200), nullable=False)
    investigationassigmentdate = Column(DateTime)
    investigationassignmentnote = Column(Text, nullable=False)
    investigationplan = Column(Text, nullable=False)
    initialreport = Column(Text, nullable=False)
    priority = Column(Integer, nullable=False)
    investigationsummary = Column(Text, nullable=False)
    agadvicerequested = Column(Boolean, nullable=False)
    sendtotrial = Column(Boolean, nullable=False)
    chargedate = Column(DateTime)
    agadvice = Column(Text, nullable=False)
    taketotrial = Column(Boolean, nullable=False)
    caseclosed = Column(Boolean, nullable=False)
    judgement = Column(Text, nullable=False)
    closeddate = Column(Date, nullable=False)
    sentencelength = Column(Integer, nullable=False)
    sentencestartdate = Column(Date, nullable=False)
    sentenceexpirydate = Column(Date, nullable=False)
    fineamount = Column(Float(53), nullable=False)
    caseappealed = Column(Boolean, nullable=False)
    appealdate = Column(DateTime, nullable=False)

    natureofsuit = relationship(u'Natureofsuit', secondary='case_natureofsuit', backref=u'cases')
    plaintiff = relationship(u'Plaintiff', secondary='case_plaintiff', backref=u'cases')
    policeman = relationship(u'Policeman', secondary='case_policeman_2', backref=u'policeman_cases')
    prosecutor = relationship(u'Prosecutor', secondary='case_prosecutor', backref=u'cases')
    policeman1 = relationship(u'Policeman', secondary='case_policeman', backref=u'policeman_cases_0')
    policestation = relationship(u'Policestation', secondary='case_policestation', backref=u'cases')
    observer = relationship(u'Observer', secondary='case_observer', backref=u'cases')
    defendant = relationship(u'Defendant', secondary='case_defendant', backref=u'cases')
    causeofaction = relationship(u'Causeofaction', secondary='case_causeofaction', backref=u'cases')


case_causeofaction = Table(
    'case_causeofaction', Model.metadata, 
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('causeofaction', ForeignKey(u'causeofaction.id'), primary_key=True, nullable=False, index=True)
)


case_defendant = Table(
    'case_defendant', Model.metadata, 
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('defendant', ForeignKey(u'defendant.id'), primary_key=True, nullable=False, index=True)
)


case_natureofsuit = Table(
    'case_natureofsuit', Model.metadata, 
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('natureofsuit', ForeignKey(u'natureofsuit.id'), primary_key=True, nullable=False, index=True)
)


case_observer = Table(
    'case_observer', Model.metadata, 
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('observer', ForeignKey(u'observer.id'), primary_key=True, nullable=False, index=True)
)


case_plaintiff = Table(
    'case_plaintiff', Model.metadata, 
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('plaintiff', ForeignKey(u'plaintiff.id'), primary_key=True, nullable=False, index=True)
)


case_policeman = Table(
    'case_policeman', Model.metadata, 
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('policeman', ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


case_policeman_2 = Table(
    'case_policeman_2', Model.metadata, 
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('policeman', ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


case_policestation = Table(
    'case_policestation', Model.metadata, 
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('policestation', ForeignKey(u'policestation.id'), primary_key=True, nullable=False, index=True)
)


case_prosecutor = Table(
    'case_prosecutor', Model.metadata, 
    Column('case', ForeignKey(u'case.id'), primary_key=True, nullable=False),
    Column('prosecutor', ForeignKey(u'prosecutor.id'), primary_key=True, nullable=False, index=True)
)


class Causeofaction(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'causeofaction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    criminal = Column(Boolean, nullable=False)
    parent_coa = Column(ForeignKey(u'causeofaction.id'), index=True)

    parent = relationship(u'Causeofaction', remote_side=[id], primaryjoin='Causeofaction.parent_coa == Causeofaction.id', backref=u'causeofactions')
    filing = relationship(u'Filing', secondary='causeofaction_filing', backref=u'causeofactions')
    hearing = relationship(u'Hearing', secondary='causeofaction_hearing', backref=u'causeofactions')


causeofaction_filing = Table(
    'causeofaction_filing', Model.metadata, 
    Column('causeofaction', ForeignKey(u'causeofaction.id'), primary_key=True, nullable=False),
    Column('filing', ForeignKey(u'filing.id'), primary_key=True, nullable=False, index=True)
)


causeofaction_hearing = Table(
    'causeofaction_hearing', Model.metadata, 
    Column('causeofaction', ForeignKey(u'causeofaction.id'), primary_key=True, nullable=False),
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False, index=True)
)


class Constituency(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'constituency'

    id = Column(Integer, primary_key=True, autoincrement=True)
    county = Column(ForeignKey(u'county.id'), nullable=False, index=True)
    town = Column(ForeignKey(u'town.id'), index=True)

    county1 = relationship(u'County', primaryjoin='Constituency.county == County.id', backref=u'constituencies')
    town1 = relationship(u'Town', primaryjoin='Constituency.town == Town.id', backref=u'constituencies')


class County(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'county'

    id = Column(Integer, primary_key=True, autoincrement=True)


class Court(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'court'

    id = Column(Integer, primary_key=True, autoincrement=True)
    town = Column(ForeignKey(u'town.id'), nullable=False, index=True)
    residentmagistrate = Column(String(100))
    registrar = Column(String(100), nullable=False)
    court_level = Column(ForeignKey(u'courtlevel.id'), nullable=False, index=True)

    courtlevel = relationship(u'Courtlevel', primaryjoin='Court.court_level == Courtlevel.id', backref=u'courts')
    town1 = relationship(u'Town', primaryjoin='Court.town == Town.id', backref=u'courts')


class Courtlevel(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'courtlevel'

    id = Column(Integer, primary_key=True, autoincrement=True)


class Defendant(BiometricMixin, EmploymentMixin, PersonMixin, ContactMixin,  AuditMixin, Model):
    __tablename__ = 'defendant'

    id = Column(Integer, primary_key=True, autoincrement=True)

    hearing = relationship(u'Hearing', secondary='defendant_hearing', backref=u'defendants')


defendant_hearing = Table(
    'defendant_hearing', Model.metadata, 
    Column('defendant', ForeignKey(u'defendant.id'), primary_key=True, nullable=False),
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False, index=True)
)


class Doctemplate(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'doctemplate'

    id = Column(Integer, primary_key=True, autoincrement=True)
    template = Column(Text, nullable=False)
    templatejson = Column(JSON, nullable=False)

    filing = relationship(u'Filing', secondary='doctemplate_filing', backref=u'doctemplates')


doctemplate_filing = Table(
    'doctemplate_filing', Model.metadata, 
    Column('doctemplate', ForeignKey(u'doctemplate.id'), primary_key=True, nullable=False),
    Column('filing', ForeignKey(u'filing.id'), primary_key=True, nullable=False, index=True)
)


class Filing(AuditMixin, Model):
    __tablename__ = 'filing'

    id = Column(Integer, primary_key=True, autoincrement=True)
    filedate = Column(DateTime, nullable=False)
    totalfees = Column(Float(53), nullable=False)
    filing_attorney = Column(ForeignKey(u'attorney.id'), nullable=False, index=True)
    filing_prosecutor = Column(ForeignKey(u'prosecutor.id'), nullable=False, index=True)
    receiptnumber = Column(Text)
    receiptverified = Column(Boolean, nullable=False)
    amountpaid = Column(Float(53), nullable=False)
    feebalance = Column(Float(53), nullable=False)
    paymenthistory = Column(Text, nullable=False)
    doctype = Column(String(100), nullable=False)
    doc = Column(Text, nullable=False)
    docbin = Column(Text, nullable=False)
    docthumbnail = Column(ImageColumn, nullable=False)
    docjson = Column(JSON, nullable=False)
    pagecount = Column(Integer, nullable=False)
    binhash = Column(String(100), nullable=False)
    texthash = Column(String(100), nullable=False)

    attorney = relationship(u'Attorney', primaryjoin='Filing.filing_attorney == Attorney.id', backref=u'filings')
    prosecutor = relationship(u'Prosecutor', primaryjoin='Filing.filing_prosecutor == Prosecutor.id', backref=u'filings')
    filingtype = relationship(u'Filingtype', secondary='filing_filingtype', backref=u'filings')
    hearing = relationship(u'Hearing', secondary='filing_hearing', backref=u'filings')


filing_filingtype = Table(
    'filing_filingtype', Model.metadata, 
    Column('filing', ForeignKey(u'filing.id'), primary_key=True, nullable=False),
    Column('filingtype', ForeignKey(u'filingtype.id'), primary_key=True, nullable=False, index=True)
)


filing_hearing = Table(
    'filing_hearing', Model.metadata, 
    Column('filing', ForeignKey(u'filing.id'), primary_key=True, nullable=False),
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False, index=True)
)


class Filingtype(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'filingtype'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cost = Column(Float(53), nullable=False)
    perpagecost = Column(Float(53), nullable=False)


class Hearing(ActivityMixin, AuditMixin, Model):
    __tablename__ = 'hearing'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hearingdate = Column(DateTime, nullable=False)
    adjourned = Column(Boolean, nullable=False)
    case = Column(ForeignKey(u'case.id'), nullable=False, index=True)
    court = Column(ForeignKey(u'court.id'), nullable=False, index=True)
    hearing_type = Column(ForeignKey(u'hearingtype.id'), nullable=False, index=True)
    remandwarrant = Column(Text, nullable=False)
    remandlength = Column(Integer)
    remanddate = Column(Date, nullable=False)
    remandwarrantexpirydate = Column(Date, nullable=False)
    nexthearingdate = Column(Date)
    finalhearing = Column(Boolean, nullable=False)
    transcript = Column(Text, nullable=False)
    audio = Column(ImageColumn, nullable=False)
    video = Column(ImageColumn, nullable=False)

    case1 = relationship(u'Case', primaryjoin='Hearing.case == Case.id', backref=u'hearings')
    court1 = relationship(u'Court', primaryjoin='Hearing.court == Court.id', backref=u'hearings')
    hearingtype = relationship(u'Hearingtype', primaryjoin='Hearing.hearing_type == Hearingtype.id', backref=u'hearings')
    prosecutor = relationship(u'Prosecutor', secondary='hearing_prosecutor', backref=u'hearings')
    judge = relationship(u'Judge', secondary='hearing_judge', backref=u'hearings')
    policeman = relationship(u'Policeman', secondary='hearing_policeman', backref=u'hearings')
    observer = relationship(u'Observer', secondary='hearing_observer', backref=u'hearings')


hearing_judge = Table(
    'hearing_judge', Model.metadata, 
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    Column('judge', ForeignKey(u'judge.id'), primary_key=True, nullable=False, index=True)
)


hearing_observer = Table(
    'hearing_observer', Model.metadata, 
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    Column('observer', ForeignKey(u'observer.id'), primary_key=True, nullable=False, index=True)
)


hearing_policeman = Table(
    'hearing_policeman', Model.metadata, 
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    Column('policeman', ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


hearing_prosecutor = Table(
    'hearing_prosecutor', Model.metadata, 
    Column('hearing', ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    Column('prosecutor', ForeignKey(u'prosecutor.id'), primary_key=True, nullable=False, index=True)
)


class Hearingtype(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'hearingtype'

    id = Column(Integer, primary_key=True, autoincrement=True)


class Investigation(AuditMixin, Model):
    __tablename__ = 'investigation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    case = Column(ForeignKey(u'case.id'), nullable=False, index=True)
    actiondate = Column(DateTime, nullable=False)
    evidence = Column(Text, nullable=False)
    narrative = Column(Text, nullable=False)
    weather = Column(Text, nullable=False)
    location = Column(Text, nullable=False)

    case1 = relationship(u'Case', primaryjoin='Investigation.case == Case.id', backref=u'investigations')
    observer = relationship(u'Observer', secondary='investigation_observer', backref=u'investigations')
    policeman = relationship(u'Policeman', secondary='investigation_policeman', backref=u'investigations')


investigation_observer = Table(
    'investigation_observer', Model.metadata, 
    Column('investigation', ForeignKey(u'investigation.id'), primary_key=True, nullable=False),
    Column('observer', ForeignKey(u'observer.id'), primary_key=True, nullable=False, index=True)
)


investigation_policeman = Table(
    'investigation_policeman', Model.metadata, 
    Column('investigation', ForeignKey(u'investigation.id'), primary_key=True, nullable=False),
    Column('policeman', ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


class Judge(PersonMixin, ContactMixin,  AuditMixin, Model):
    __tablename__ = 'judge'

    id = Column(Integer, primary_key=True, autoincrement=True)
    court = Column(ForeignKey(u'court.id'), nullable=False, index=True)

    court1 = relationship(u'Court', primaryjoin='Judge.court == Court.id', backref=u'judges')


class Lawfirm(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'lawfirm'

    id = Column(Integer, primary_key=True, autoincrement=True)


class Natureofsuit(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'natureofsuit'

    id = Column(Integer, primary_key=True, autoincrement=True)


class Observer(PersonMixin, ContactMixin,  AuditMixin, Model):
    __tablename__ = 'observer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fordefense = Column(Boolean, nullable=False)


class Plaintiff(PersonMixin, ContactMixin,  AuditMixin, Model):
    __tablename__ = 'plaintiff'

    id = Column(Integer, primary_key=True, autoincrement=True)


class Policeman(PersonMixin, ContactMixin,  AuditMixin, Model):
    __tablename__ = 'policeman'

    id = Column(Integer, primary_key=True, autoincrement=True)

    policerole = relationship(u'Policerole', secondary='policerole_policeman', backref=u'policemen')


class Policerole(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'policerole'

    id = Column(Integer, primary_key=True, autoincrement=True)


policerole_policeman = Table(
    'policerole_policeman', Model.metadata, 
    Column('policerole', ForeignKey(u'policerole.id'), primary_key=True, nullable=False),
    Column('policeman', ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


class Policestation(AuditMixin, Model):
    __tablename__ = 'policestation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    town = Column(ForeignKey(u'town.id'), nullable=False, index=True)
    officercommanding = Column(String(100))

    town1 = relationship(u'Town', primaryjoin='Policestation.town == Town.id', backref=u'policestations')


class Prison(AuditMixin, Model):
    __tablename__ = 'prison'

    id = Column(Integer, primary_key=True, autoincrement=True)
    town = Column(ForeignKey(u'town.id'), nullable=False, index=True)
    warden = Column(String(100))
    capacity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)

    town1 = relationship(u'Town', primaryjoin='Prison.town == Town.id', backref=u'prisons')


class Prisonremand(AuditMixin, Model):
    __tablename__ = 'prisonremand'

    prison = Column(ForeignKey(u'prison.id'), primary_key=True, nullable=False)
    warrantno = Column(String(100), primary_key=True, nullable=False)
    hearing = Column(ForeignKey(u'hearing.id'), nullable=False, index=True)
    defendant = Column(ForeignKey(u'defendant.id'), nullable=False, index=True)
    warrantduration = Column(Integer, nullable=False)
    warrantdate = Column(DateTime, nullable=False)
    warrant = Column(Text, nullable=False)
    warrantexpiry = Column(DateTime, nullable=False)
    history = Column(Text, nullable=False)

    defendant1 = relationship(u'Defendant', primaryjoin='Prisonremand.defendant == Defendant.id', backref=u'prisonremands')
    hearing1 = relationship(u'Hearing', primaryjoin='Prisonremand.hearing == Hearing.id', backref=u'prisonremands')
    prison1 = relationship(u'Prison', primaryjoin='Prisonremand.prison == Prison.id', backref=u'prisonremands')


class Prosecutor(PersonMixin, ContactMixin,  AuditMixin, Model):
    __tablename__ = 'prosecutor'

    id = Column(Integer, primary_key=True, autoincrement=True)

    prosecutorteam = relationship(u'Prosecutorteam', secondary='prosecutor_prosecutorteam', backref=u'prosecutors')


prosecutor_prosecutorteam = Table(
    'prosecutor_prosecutorteam', Model.metadata, 
    Column('prosecutor', ForeignKey(u'prosecutor.id'), primary_key=True, nullable=False),
    Column('prosecutorteam', ForeignKey(u'prosecutorteam.id'), primary_key=True, nullable=False, index=True)
)


class Prosecutorteam(AuditMixin, Model):
    __tablename__ = 'prosecutorteam'

    id = Column(Integer, primary_key=True, autoincrement=True)


class Subcounty(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'subcounty'

    id = Column(Integer, primary_key=True, autoincrement=True)
    county = Column(ForeignKey(u'county.id'), nullable=False, index=True)

    county1 = relationship(u'County', primaryjoin='Subcounty.county == County.id', backref=u'subcounties')


class Surety(PersonMixin, ContactMixin,  AuditMixin, Model):
    __tablename__ = 'surety'

    id = Column(Integer, primary_key=True, autoincrement=True)


class Town(RefTypeMixin, AuditMixin, Model):
    __tablename__ = 'town'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subcounty = Column(ForeignKey(u'subcounty.id'), nullable=False, index=True)

    subcounty1 = relationship(u'Subcounty', primaryjoin='Town.subcounty == Subcounty.id', backref=u'towns')
