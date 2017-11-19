# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, LargeBinary, String, Table, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.json import JSON
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Actiontype(db.Model):
    __tablename__ = 'actiontype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Attorney(db.Model):
    __tablename__ = 'attorney'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    law_firm = db.Column(db.ForeignKey(u'lawfirm.id'), index=True)

    lawfirm = db.relationship(u'Lawfirm', primaryjoin='Attorney.law_firm == Lawfirm.id', backref=u'attorneys')
    hearing = db.relationship(u'Hearing', secondary=u't_attorney_hearing', backref=u'attorneys')


t_attorney_hearing = db.Table(
    'attorney_hearing',
    db.Column('attorney', db.ForeignKey(u'attorney.id'), primary_key=True, nullable=False),
    db.Column('hearing', db.ForeignKey(u'hearing.id'), primary_key=True, nullable=False, index=True)
)


class Bail(db.Model):
    __tablename__ = 'bail'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    hearing = db.Column(db.ForeignKey(u'hearing.id'), nullable=False, index=True)
    defendant = db.Column(db.ForeignKey(u'defendant.id'), nullable=False, index=True)
    amountgranted = db.Column(db.Float(53), nullable=False)
    noofsureties = db.Column(db.Integer, nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
    paydate = db.Column(db.Date, nullable=False)
    receiptno = db.Column(db.String(100), nullable=False)

    defendant1 = db.relationship(u'Defendant', primaryjoin='Bail.defendant == Defendant.id', backref=u'bails')
    hearing1 = db.relationship(u'Hearing', primaryjoin='Bail.hearing == Hearing.id', backref=u'bails')
    surety = db.relationship(u'Surety', secondary=u't_bail_surety', backref=u'bails')


t_bail_surety = db.Table(
    'bail_surety',
    db.Column('bail', db.ForeignKey(u'bail.id'), primary_key=True, nullable=False),
    db.Column('surety', db.ForeignKey(u'surety.id'), primary_key=True, nullable=False, index=True)
)


class Case(db.Model):
    __tablename__ = 'case'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    investigationassigmentdate = db.Column(db.DateTime)
    investigationassignmentnote = db.Column(db.Text, nullable=False)
    investigationplan = db.Column(db.Text, nullable=False)
    initialreport = db.Column(db.Text, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    findings = db.Column(db.Text, nullable=False)
    agadvicerequested = db.Column(db.Boolean, nullable=False)
    sendtotrial = db.Column(db.Boolean, nullable=False)
    chargedate = db.Column(db.DateTime)
    taketotrial = db.Column(db.Boolean, nullable=False)
    closed = db.Column(db.Boolean, nullable=False)
    judgement = db.Column(db.Text, nullable=False)
    closeddate = db.Column(db.Date, nullable=False)
    sentencelength = db.Column(db.Integer, nullable=False)
    sentencestartdate = db.Column(db.Date, nullable=False)
    sentenceexpirydate = db.Column(db.Date, nullable=False)
    fineamount = db.Column(db.Float(53), nullable=False)

    natureofsuit = db.relationship(u'Natureofsuit', secondary=u't_case_natureofsuit', backref=u'cases')
    plaintiff = db.relationship(u'Plaintiff', secondary=u't_case_plaintiff', backref=u'cases')
    policeman = db.relationship(u'Policeman', secondary=u't_case_policeman_2', backref=u'policeman_cases')
    prosecutor = db.relationship(u'Prosecutor', secondary=u't_case_prosecutor', backref=u'cases')
    witness = db.relationship(u'Witnes', secondary=u't_case_witness', backref=u'cases')
    policeman1 = db.relationship(u'Policeman', secondary=u't_case_policeman', backref=u'policeman_cases_0')
    policestation = db.relationship(u'Policestation', secondary=u't_case_policestation', backref=u'cases')
    defendant = db.relationship(u'Defendant', secondary=u't_case_defendant', backref=u'cases')


t_case_defendant = db.Table(
    'case_defendant',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('defendant', db.ForeignKey(u'defendant.id'), primary_key=True, nullable=False, index=True)
)


t_case_natureofsuit = db.Table(
    'case_natureofsuit',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('natureofsuit', db.ForeignKey(u'natureofsuit.id'), primary_key=True, nullable=False, index=True)
)


t_case_plaintiff = db.Table(
    'case_plaintiff',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('plaintiff', db.ForeignKey(u'plaintiff.id'), primary_key=True, nullable=False, index=True)
)


t_case_policeman = db.Table(
    'case_policeman',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('policeman', db.ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


t_case_policeman_2 = db.Table(
    'case_policeman_2',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('policeman', db.ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


t_case_policestation = db.Table(
    'case_policestation',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('policestation', db.ForeignKey(u'policestation.id'), primary_key=True, nullable=False, index=True)
)


t_case_prosecutor = db.Table(
    'case_prosecutor',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('prosecutor', db.ForeignKey(u'prosecutor.id'), primary_key=True, nullable=False, index=True)
)


t_case_witness = db.Table(
    'case_witness',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('witness', db.ForeignKey(u'witness.id'), primary_key=True, nullable=False, index=True)
)


class Causeofaction(db.Model):
    __tablename__ = 'causeofaction'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    action_type = db.Column(db.ForeignKey(u'actiontype.id'), index=True)

    actiontype = db.relationship(u'Actiontype', primaryjoin='Causeofaction.action_type == Actiontype.id', backref=u'causeofactions')
    filing = db.relationship(u'Filing', secondary=u't_causeofaction_filing', backref=u'causeofactions')
    hearing = db.relationship(u'Hearing', secondary=u't_causeofaction_hearing', backref=u'causeofactions')


t_causeofaction_filing = db.Table(
    'causeofaction_filing',
    db.Column('causeofaction', db.ForeignKey(u'causeofaction.id'), primary_key=True, nullable=False),
    db.Column('filing', db.ForeignKey(u'filing.id'), primary_key=True, nullable=False, index=True)
)


t_causeofaction_hearing = db.Table(
    'causeofaction_hearing',
    db.Column('causeofaction', db.ForeignKey(u'causeofaction.id'), primary_key=True, nullable=False),
    db.Column('hearing', db.ForeignKey(u'hearing.id'), primary_key=True, nullable=False, index=True)
)


class Constituency(db.Model):
    __tablename__ = 'constituency'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    county = db.Column(db.ForeignKey(u'county.id'), nullable=False, index=True)
    town = db.Column(db.ForeignKey(u'town.id'), index=True)

    county1 = db.relationship(u'County', primaryjoin='Constituency.county == County.id', backref=u'constituencies')
    town1 = db.relationship(u'Town', primaryjoin='Constituency.town == Town.id', backref=u'constituencies')


class County(db.Model):
    __tablename__ = 'county'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Court(db.Model):
    __tablename__ = 'court'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    town = db.Column(db.ForeignKey(u'town.id'), nullable=False, index=True)
    residentmagistrate = db.Column(db.String(100))
    registrar = db.Column(db.String(100), nullable=False)
    court_level = db.Column(db.ForeignKey(u'courtlevel.id'), nullable=False, index=True)

    courtlevel = db.relationship(u'Courtlevel', primaryjoin='Court.court_level == Courtlevel.id', backref=u'courts')
    town1 = db.relationship(u'Town', primaryjoin='Court.town == Town.id', backref=u'courts')


class Courtlevel(db.Model):
    __tablename__ = 'courtlevel'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Defendant(db.Model):
    __tablename__ = 'defendant'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())

    hearing = db.relationship(u'Hearing', secondary=u't_defendant_hearing', backref=u'defendants')


t_defendant_hearing = db.Table(
    'defendant_hearing',
    db.Column('defendant', db.ForeignKey(u'defendant.id'), primary_key=True, nullable=False),
    db.Column('hearing', db.ForeignKey(u'hearing.id'), primary_key=True, nullable=False, index=True)
)


class Doctemplate(db.Model):
    __tablename__ = 'doctemplate'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    template = db.Column(db.Text, nullable=False)
    templatejson = db.Column(db.JSON, nullable=False)


class Document(db.Model):
    __tablename__ = 'document'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    mimetype = db.Column(db.String(100), nullable=False)
    doctype = db.Column(db.Text, nullable=False)
    doc = db.Column(db.Text, nullable=False)
    docbin = db.Column(db.LargeBinary, nullable=False)
    docthumbnail = db.Column(db.LargeBinary, nullable=False)
    doc_template = db.Column(db.ForeignKey(u'doctemplate.id'), index=True)
    docjson = db.Column(db.JSON, nullable=False)

    doctemplate = db.relationship(u'Doctemplate', primaryjoin='Document.doc_template == Doctemplate.id', backref=u'documents')
    filing = db.relationship(u'Filing', secondary=u't_document_filing', backref=u'documents')


t_document_filing = db.Table(
    'document_filing',
    db.Column('document', db.ForeignKey(u'document.id'), primary_key=True, nullable=False),
    db.Column('filing', db.ForeignKey(u'filing.id'), primary_key=True, nullable=False, index=True)
)


class Filing(db.Model):
    __tablename__ = 'filing'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    filedate = db.Column(db.DateTime, nullable=False)
    totalfees = db.Column(db.Float(53), nullable=False)
    filing_attorney = db.Column(db.ForeignKey(u'attorney.id'), nullable=False, index=True)
    filing_prosecutor = db.Column(db.ForeignKey(u'prosecutor.id'), nullable=False, index=True)
    receiptnumber = db.Column(db.Text)
    receiptverified = db.Column(db.Boolean, nullable=False)
    amountpaid = db.Column(db.Float(53), nullable=False)
    feebalance = db.Column(db.Float(53), nullable=False)

    attorney = db.relationship(u'Attorney', primaryjoin='Filing.filing_attorney == Attorney.id', backref=u'filings')
    prosecutor = db.relationship(u'Prosecutor', primaryjoin='Filing.filing_prosecutor == Prosecutor.id', backref=u'filings')
    filingtype = db.relationship(u'Filingtype', secondary=u't_filing_filingtype', backref=u'filings')
    hearing = db.relationship(u'Hearing', secondary=u't_filing_hearing', backref=u'filings')


t_filing_filingtype = db.Table(
    'filing_filingtype',
    db.Column('filing', db.ForeignKey(u'filing.id'), primary_key=True, nullable=False),
    db.Column('filingtype', db.ForeignKey(u'filingtype.id'), primary_key=True, nullable=False, index=True)
)


t_filing_hearing = db.Table(
    'filing_hearing',
    db.Column('filing', db.ForeignKey(u'filing.id'), primary_key=True, nullable=False),
    db.Column('hearing', db.ForeignKey(u'hearing.id'), primary_key=True, nullable=False, index=True)
)


class Filingtype(db.Model):
    __tablename__ = 'filingtype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    cost = db.Column(db.Float(53), nullable=False)


class Hearing(db.Model):
    __tablename__ = 'hearing'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    hearingdate = db.Column(db.DateTime, nullable=False)
    case = db.Column(db.ForeignKey(u'case.id'), nullable=False, index=True)
    court = db.Column(db.ForeignKey(u'court.id'), nullable=False, index=True)
    hearing_type = db.Column(db.ForeignKey(u'hearingtype.id'), nullable=False, index=True)
    remandwarrant = db.Column(db.Text, nullable=False)
    remandlength = db.Column(db.Integer)
    remanddate = db.Column(db.Date, nullable=False)
    remandwarrantexpirydate = db.Column(db.Date, nullable=False)
    nexthearingdate = db.Column(db.Date)
    finalhearing = db.Column(db.Boolean, nullable=False)

    case1 = db.relationship(u'Case', primaryjoin='Hearing.case == Case.id', backref=u'hearings')
    court1 = db.relationship(u'Court', primaryjoin='Hearing.court == Court.id', backref=u'hearings')
    hearingtype = db.relationship(u'Hearingtype', primaryjoin='Hearing.hearing_type == Hearingtype.id', backref=u'hearings')
    witness = db.relationship(u'Witnes', secondary=u't_hearing_witness', backref=u'hearings')
    prosecutor = db.relationship(u'Prosecutor', secondary=u't_hearing_prosecutor', backref=u'hearings')
    judge = db.relationship(u'Judge', secondary=u't_hearing_judge', backref=u'hearings')
    prison = db.relationship(u'Prison', secondary=u't_hearing_prison', backref=u'hearings')
    policeman = db.relationship(u'Policeman', secondary=u't_hearing_policeman', backref=u'hearings')


t_hearing_judge = db.Table(
    'hearing_judge',
    db.Column('hearing', db.ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    db.Column('judge', db.ForeignKey(u'judge.id'), primary_key=True, nullable=False, index=True)
)


t_hearing_policeman = db.Table(
    'hearing_policeman',
    db.Column('hearing', db.ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    db.Column('policeman', db.ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


t_hearing_prison = db.Table(
    'hearing_prison',
    db.Column('hearing', db.ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    db.Column('prison', db.ForeignKey(u'prison.id'), primary_key=True, nullable=False, index=True)
)


t_hearing_prosecutor = db.Table(
    'hearing_prosecutor',
    db.Column('hearing', db.ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    db.Column('prosecutor', db.ForeignKey(u'prosecutor.id'), primary_key=True, nullable=False, index=True)
)


t_hearing_witness = db.Table(
    'hearing_witness',
    db.Column('hearing', db.ForeignKey(u'hearing.id'), primary_key=True, nullable=False),
    db.Column('witness', db.ForeignKey(u'witness.id'), primary_key=True, nullable=False, index=True)
)


class Hearingtype(db.Model):
    __tablename__ = 'hearingtype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Investigation(db.Model):
    __tablename__ = 'investigation'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    case = db.Column(db.ForeignKey(u'case.id'), nullable=False, index=True)
    actiondate = db.Column(db.DateTime, nullable=False)
    evidence = db.Column(db.Text, nullable=False)

    case1 = db.relationship(u'Case', primaryjoin='Investigation.case == Case.id', backref=u'investigations')
    policeman = db.relationship(u'Policeman', secondary=u't_investigation_policeman', backref=u'investigations')
    witness = db.relationship(u'Witnes', secondary=u't_investigation_witness', backref=u'investigations')


t_investigation_policeman = db.Table(
    'investigation_policeman',
    db.Column('investigation', db.ForeignKey(u'investigation.id'), primary_key=True, nullable=False),
    db.Column('policeman', db.ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


t_investigation_witness = db.Table(
    'investigation_witness',
    db.Column('investigation', db.ForeignKey(u'investigation.id'), primary_key=True, nullable=False),
    db.Column('witness', db.ForeignKey(u'witness.id'), primary_key=True, nullable=False, index=True)
)


class Judge(db.Model):
    __tablename__ = 'judge'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    court = db.Column(db.ForeignKey(u'court.id'), nullable=False, index=True)

    court1 = db.relationship(u'Court', primaryjoin='Judge.court == Court.id', backref=u'judges')


class Lawfirm(db.Model):
    __tablename__ = 'lawfirm'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Natureofsuit(db.Model):
    __tablename__ = 'natureofsuit'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Plaintiff(db.Model):
    __tablename__ = 'plaintiff'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Policeman(db.Model):
    __tablename__ = 'policeman'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())

    policerole = db.relationship(u'Policerole', secondary=u't_policerole_policeman', backref=u'policemen')


class Policerole(db.Model):
    __tablename__ = 'policerole'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


t_policerole_policeman = db.Table(
    'policerole_policeman',
    db.Column('policerole', db.ForeignKey(u'policerole.id'), primary_key=True, nullable=False),
    db.Column('policeman', db.ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


class Policestation(db.Model):
    __tablename__ = 'policestation'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    town = db.Column(db.ForeignKey(u'town.id'), nullable=False, index=True)
    officercommanding = db.Column(db.String(100))

    town1 = db.relationship(u'Town', primaryjoin='Policestation.town == Town.id', backref=u'policestations')


class Prison(db.Model):
    __tablename__ = 'prison'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    town = db.Column(db.ForeignKey(u'town.id'), nullable=False, index=True)
    warden = db.Column(db.String(100))

    town1 = db.relationship(u'Town', primaryjoin='Prison.town == Town.id', backref=u'prisons')


class Prosecutor(db.Model):
    __tablename__ = 'prosecutor'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())

    prosecutorteam = db.relationship(u'Prosecutorteam', secondary=u't_prosecutor_prosecutorteam', backref=u'prosecutors')


t_prosecutor_prosecutorteam = db.Table(
    'prosecutor_prosecutorteam',
    db.Column('prosecutor', db.ForeignKey(u'prosecutor.id'), primary_key=True, nullable=False),
    db.Column('prosecutorteam', db.ForeignKey(u'prosecutorteam.id'), primary_key=True, nullable=False, index=True)
)


class Prosecutorteam(db.Model):
    __tablename__ = 'prosecutorteam'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Subcounty(db.Model):
    __tablename__ = 'subcounty'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    county = db.Column(db.ForeignKey(u'county.id'), nullable=False, index=True)

    county1 = db.relationship(u'County', primaryjoin='Subcounty.county == County.id', backref=u'subcounties')


class Surety(db.Model):
    __tablename__ = 'surety'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Town(db.Model):
    __tablename__ = 'town'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subcounty = db.Column(db.ForeignKey(u'subcounty.id'), nullable=False, index=True)

    subcounty1 = db.relationship(u'Subcounty', primaryjoin='Town.subcounty == Subcounty.id', backref=u'towns')


class Witnes(db.Model):
    __tablename__ = 'witness'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
