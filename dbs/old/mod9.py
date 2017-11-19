# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, LargeBinary, String, Table, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Attorney(db.Model):
    __tablename__ = 'attorney'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    bar_number = db.Column(db.String(20), nullable=False)
    call_to_bar_year = db.Column(db.Integer, nullable=False)
    lawfirm_member = db.Column(db.ForeignKey(u'lawfirm.id'), index=True)

    lawfirm = db.relationship(u'Lawfirm', primaryjoin='Attorney.lawfirm_member == Lawfirm.id', backref=u'attorneys')
    casehearing = db.relationship(u'Casehearing', secondary=u't_attorney_casehearing', backref=u'casehearing_attorneys')
    case = db.relationship(u'Case', secondary=u't_attorney_case', backref=u'attorneys')


t_attorney_case = db.Table(
    'attorney_case',
    db.Column('attorney', db.ForeignKey(u'attorney.id'), primary_key=True, nullable=False),
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False, index=True)
)


t_attorney_casehearing = db.Table(
    'attorney_casehearing',
    db.Column('attorney', db.ForeignKey(u'attorney.id'), primary_key=True, nullable=False),
    db.Column('casehearing', db.ForeignKey(u'casehearing.case'), primary_key=True, nullable=False, index=True)
)


t_bail_surety = db.Table(
    'bail_surety',
    db.Column('bail', db.ForeignKey(u'bail.case'), primary_key=True, nullable=False),
    db.Column('surety', db.ForeignKey(u'surety.id'), primary_key=True, nullable=False, index=True)
)


class Case(db.Model):
    __tablename__ = 'case'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    court = db.Column(db.ForeignKey(u'court.id'), nullable=False, index=True)
    case_number = db.Column(db.String(30), nullable=False)
    is_criminal = db.Column(db.Boolean, nullable=False)
    case_category = db.Column(db.ForeignKey(u'casecategory.id'), nullable=False, index=True)
    charge_date = db.Column(db.DateTime, nullable=False)

    casecategory = db.relationship(u'Casecategory', primaryjoin='Case.case_category == Casecategory.id', backref=u'cases')
    court1 = db.relationship(u'Court', primaryjoin='Case.court == Court.id', backref=u'cases')
    plaintiff = db.relationship(u'Plaintiff', secondary=u't_case_plaintiff', backref=u'cases')
    casestatus = db.relationship(u'Casestatu', secondary=u't_case_casestatus', backref=u'cases')
    prosecutor = db.relationship(u'Prosecutor', secondary=u't_case_prosecutor', backref=u'cases')
    witness = db.relationship(u'Witnes', secondary=u't_case_witness', backref=u'cases')
    judge = db.relationship(u'Judge', secondary=u't_case_judge', backref=u'cases')
    offense = db.relationship(u'Offense', secondary=u't_case_offense', backref=u'cases')
    policeman = db.relationship(u'Policeman', secondary=u't_case_policeman', backref=u'cases')
    defendant = db.relationship(u'Defendant', secondary=u't_case_defendant', backref=u'cases')


class Casehearing(Case):
    __tablename__ = 'casehearing'

    case = db.Column(db.ForeignKey(u'case.id'), primary_key=True)
    hearingtype = db.Column(db.ForeignKey(u'hearingtype.id'), nullable=False, index=True)
    hearing_date = db.Column(db.DateTime, nullable=False)
    prosecutor_present = db.Column(db.Boolean, nullable=False)
    defense_attorney_present = db.Column(db.Boolean, nullable=False)
    case_outcome = db.Column(db.Text, nullable=False)
    prison = db.Column(db.ForeignKey(u'prison.id'), nullable=False, index=True)
    from_remand = db.Column(db.Boolean, nullable=False)
    to_remand = db.Column(db.Boolean, nullable=False)
    to_prison = db.Column(db.Boolean, nullable=False)
    bail = db.Column(db.ForeignKey(u'bail.case'), nullable=False, index=True)
    notes = db.Column(db.Text, nullable=False)

    bail1 = db.relationship(u'Bail', primaryjoin='Casehearing.bail == Bail.case', backref=u'casehearings')
    hearingtype1 = db.relationship(u'Hearingtype', primaryjoin='Casehearing.hearingtype == Hearingtype.id', backref=u'casehearings')
    prison1 = db.relationship(u'Prison', primaryjoin='Casehearing.prison == Prison.id', backref=u'casehearings')
    witness = db.relationship(u'Witnes', secondary=u't_casehearing_witness', backref=u'casehearings')
    judge = db.relationship(u'Judge', secondary=u't_casehearing_judge', backref=u'casehearings')
    prosecutor = db.relationship(u'Prosecutor', secondary=u't_casehearing_prosecutor', backref=u'casehearings')
    plaintiff = db.relationship(u'Plaintiff', secondary=u't_casehearing_plaintiff', backref=u'casehearings')
    policeman = db.relationship(u'Policeman', secondary=u't_casehearing_policeman', backref=u'casehearings')
    defendant = db.relationship(u'Defendant', secondary=u't_casehearing_defendant', backref=u'casehearings')


class Bail(Case):
    __tablename__ = 'bail'

    case = db.Column(db.ForeignKey(u'case.id'), primary_key=True)
    defendant = db.Column(db.ForeignKey(u'defendant.id'), nullable=False, index=True)
    amount = db.Column(db.Float(53), nullable=False)
    surety_count = db.Column(db.Integer, nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
    paid_date = db.Column(db.Date, nullable=False)
    receipt_number = db.Column(db.Text, nullable=False)

    defendant1 = db.relationship(u'Defendant', primaryjoin='Bail.defendant == Defendant.id', backref=u'bails')
    surety = db.relationship(u'Surety', secondary=u't_bail_surety', backref=u'bails')


t_case_casestatus = db.Table(
    'case_casestatus',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('casestatus', db.ForeignKey(u'casestatus.id'), primary_key=True, nullable=False, index=True)
)


t_case_defendant = db.Table(
    'case_defendant',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('defendant', db.ForeignKey(u'defendant.id'), primary_key=True, nullable=False, index=True)
)


t_case_judge = db.Table(
    'case_judge',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('judge', db.ForeignKey(u'judge.id'), primary_key=True, nullable=False, index=True)
)


t_case_offense = db.Table(
    'case_offense',
    db.Column('case', db.ForeignKey(u'case.id'), primary_key=True, nullable=False),
    db.Column('offense', db.ForeignKey(u'offense.id'), primary_key=True, nullable=False, index=True)
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


class Casecategory(db.Model):
    __tablename__ = 'casecategory'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


t_casehearing_defendant = db.Table(
    'casehearing_defendant',
    db.Column('casehearing', db.ForeignKey(u'casehearing.case'), primary_key=True, nullable=False),
    db.Column('defendant', db.ForeignKey(u'defendant.id'), primary_key=True, nullable=False, index=True)
)


t_casehearing_judge = db.Table(
    'casehearing_judge',
    db.Column('casehearing', db.ForeignKey(u'casehearing.case'), primary_key=True, nullable=False),
    db.Column('judge', db.ForeignKey(u'judge.id'), primary_key=True, nullable=False, index=True)
)


t_casehearing_plaintiff = db.Table(
    'casehearing_plaintiff',
    db.Column('casehearing', db.ForeignKey(u'casehearing.case'), primary_key=True, nullable=False),
    db.Column('plaintiff', db.ForeignKey(u'plaintiff.id'), primary_key=True, nullable=False, index=True)
)


t_casehearing_policeman = db.Table(
    'casehearing_policeman',
    db.Column('casehearing', db.ForeignKey(u'casehearing.case'), primary_key=True, nullable=False),
    db.Column('policeman', db.ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


t_casehearing_prosecutor = db.Table(
    'casehearing_prosecutor',
    db.Column('casehearing', db.ForeignKey(u'casehearing.case'), primary_key=True, nullable=False),
    db.Column('prosecutor', db.ForeignKey(u'prosecutor.id'), primary_key=True, nullable=False, index=True)
)


t_casehearing_witness = db.Table(
    'casehearing_witness',
    db.Column('casehearing', db.ForeignKey(u'casehearing.case'), primary_key=True, nullable=False),
    db.Column('witness', db.ForeignKey(u'witness.id'), primary_key=True, nullable=False, index=True)
)


class Casestatu(db.Model):
    __tablename__ = 'casestatus'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Complaint(db.Model):
    __tablename__ = 'complaint'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    complaint_date = db.Column(db.DateTime, nullable=False)
    is_case = db.Column(db.Boolean)
    case = db.Column(db.ForeignKey(u'case.id'), index=True)
    notes = db.Column(db.Text, nullable=False)

    case1 = db.relationship(u'Case', primaryjoin='Complaint.case == Case.id', backref=u'complaints')
    defendant = db.relationship(u'Defendant', secondary=u't_complaint_defendant', backref=u'complaints')
    policeman = db.relationship(u'Policeman', secondary=u't_complaint_policeman', backref=u'complaints')
    plaintiff = db.relationship(u'Plaintiff', secondary=u't_complaint_plaintiff', backref=u'complaints')


t_complaint_defendant = db.Table(
    'complaint_defendant',
    db.Column('complaint', db.ForeignKey(u'complaint.id'), primary_key=True, nullable=False),
    db.Column('defendant', db.ForeignKey(u'defendant.id'), primary_key=True, nullable=False, index=True)
)


t_complaint_plaintiff = db.Table(
    'complaint_plaintiff',
    db.Column('complaint', db.ForeignKey(u'complaint.id'), primary_key=True, nullable=False),
    db.Column('plaintiff', db.ForeignKey(u'plaintiff.id'), primary_key=True, nullable=False, index=True)
)


t_complaint_policeman = db.Table(
    'complaint_policeman',
    db.Column('complaint', db.ForeignKey(u'complaint.id'), primary_key=True, nullable=False),
    db.Column('policeman', db.ForeignKey(u'policeman.id'), primary_key=True, nullable=False, index=True)
)


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())

    plaintiff = db.relationship(u'Plaintiff', secondary=u't_contact_plaintiff', backref=u'contacts')


t_contact_plaintiff = db.Table(
    'contact_plaintiff',
    db.Column('contact', db.ForeignKey(u'contact.id'), primary_key=True, nullable=False),
    db.Column('plaintiff', db.ForeignKey(u'plaintiff.id'), primary_key=True, nullable=False, index=True)
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


class Defendant(db.Model):
    __tablename__ = 'defendant'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    gender = db.Column(db.ForeignKey(u'gender.id'), nullable=False, index=True)

    gender1 = db.relationship(u'Gender', primaryjoin='Defendant.gender == Gender.id', backref=u'defendants')
    filing = db.relationship(u'Filing', secondary=u't_defendant_filing', backref=u'defendants')
    prison = db.relationship(u'Prison', secondary=u't_defendant_prison', backref=u'defendants')


t_defendant_filing = db.Table(
    'defendant_filing',
    db.Column('defendant', db.ForeignKey(u'defendant.id'), primary_key=True, nullable=False),
    db.Column('filing', db.ForeignKey(u'filing.id'), primary_key=True, nullable=False, index=True)
)


t_defendant_prison = db.Table(
    'defendant_prison',
    db.Column('defendant', db.ForeignKey(u'defendant.id'), primary_key=True, nullable=False),
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


class Feeschedule(db.Model):
    __tablename__ = 'feeschedule'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    amount = db.Column(db.Float(53), nullable=False)

    filing = db.relationship(u'Filing', secondary=u't_feeschedule_filing', backref=u'feeschedules')


t_feeschedule_filing = db.Table(
    'feeschedule_filing',
    db.Column('feeschedule', db.ForeignKey(u'feeschedule.id'), primary_key=True, nullable=False),
    db.Column('filing', db.ForeignKey(u'filing.id'), primary_key=True, nullable=False, index=True)
)


class Filing(db.Model):
    __tablename__ = 'filing'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    case = db.Column(db.ForeignKey(u'case.id'), nullable=False, index=True)
    filing_date = db.Column(db.DateTime, nullable=False)
    doc_name = db.Column(db.String(50), nullable=False)
    doc_content = db.Column(db.Text, nullable=False)
    case_hearing = db.Column(db.ForeignKey(u'casehearing.case'), nullable=False, index=True)
    filing_fee = db.Column(db.Float(53), nullable=False)
    receipt_number = db.Column(db.String(20), nullable=False)
    received_by = db.Column(db.String(50), nullable=False)

    case1 = db.relationship(u'Case', primaryjoin='Filing.case == Case.id', backref=u'filings')
    casehearing = db.relationship(u'Casehearing', primaryjoin='Filing.case_hearing == Casehearing.case', backref=u'casehearing_filings')
    plaintiff = db.relationship(u'Plaintiff', secondary=u't_filing_plaintiff', backref=u'filings')


t_filing_plaintiff = db.Table(
    'filing_plaintiff',
    db.Column('filing', db.ForeignKey(u'filing.id'), primary_key=True, nullable=False),
    db.Column('plaintiff', db.ForeignKey(u'plaintiff.id'), primary_key=True, nullable=False, index=True)
)


class Gender(db.Model):
    __tablename__ = 'gender'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Hearingtype(db.Model):
    __tablename__ = 'hearingtype'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Judge(db.Model):
    __tablename__ = 'judge'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    court = db.Column(db.ForeignKey(u'court.id'), nullable=False, index=True)
    court_level = db.Column(db.ForeignKey(u'courtlevel.id'), nullable=False, index=True)
    appelation = db.Column(db.String(100), nullable=False)

    court1 = db.relationship(u'Court', primaryjoin='Judge.court == Court.id', backref=u'judges')
    courtlevel = db.relationship(u'Courtlevel', primaryjoin='Judge.court_level == Courtlevel.id', backref=u'judges')


class Lawfirm(db.Model):
    __tablename__ = 'lawfirm'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Offense(db.Model):
    __tablename__ = 'offense'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Plaintiff(db.Model):
    __tablename__ = 'plaintiff'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    with_others = db.Column(db.Boolean, nullable=False)
    gender = db.Column(db.ForeignKey(u'gender.id'), nullable=False, index=True)

    gender1 = db.relationship(u'Gender', primaryjoin='Plaintiff.gender == Gender.id', backref=u'plaintiffs')


class Policeman(db.Model):
    __tablename__ = 'policeman'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    service_number = db.Column(db.String(50), nullable=False)
    rank = db.Column(db.String(40), nullable=False)
    police_station = db.Column(db.ForeignKey(u'policestation.id'), nullable=False, index=True)

    policestation = db.relationship(u'Policestation', primaryjoin='Policeman.police_station == Policestation.id', backref=u'policemen')


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


class Prosecutor(db.Model):
    __tablename__ = 'prosecutor'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    is_police = db.Column(db.Boolean, nullable=False)


class Region(db.Model):
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Surety(db.Model):
    __tablename__ = 'surety'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())


class Town(db.Model):
    __tablename__ = 'town'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    district = db.Column(db.ForeignKey(u'district.id'), nullable=False, index=True)

    district1 = db.relationship(u'District', primaryjoin='Town.district == District.id', backref=u'towns')


class Witnes(db.Model):
    __tablename__ = 'witness'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    special = db.Column(db.Boolean, nullable=False)
    role = db.Column(db.String(100), nullable=False)
    for_defense = db.Column(db.Boolean, nullable=False)
