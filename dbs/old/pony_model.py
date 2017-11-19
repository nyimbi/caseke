from datetime import date
from datetime import datetime
from pony.orm import *


db = Database()


class Court(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 100)
    cases = Set('Case')
    judges = Set('Judge')
    town = Required('Town')
    court_level = Required('CourtLevel')


class Case(db.Entity):
    court = PrimaryKey(Court)
    cs = Set('CasePlaintiff', cascade_delete=False)
    defendants = Set('Defendant')
    filings = Set('Filing', cascade_delete=False)
    judges = Set('Judge')
    prosecutors = Set('Prosecutor')
    c_def_atts = Set('CaseDefenseAttorney')
    witnessess = Set('Witnesses')
    complaints = Set('Complaint')
    case_category = Required('CaseCategory')
    cs_changes = Set('Case_status_change')
    offenses = Set('Offense')
    bail = Optional('Bail')
    policemen = Set('Policeman')
    case_hearings = Set('Case_Hearing')


class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 100)
    gender = Required('Gender')
    date_of_birth = Required(date)


class Plaintiff(Person):
    cs = Set('CasePlaintiff')
    filings = Set('Filing')
    contacts = Set('Contact')


class Defendant(Person):
    cases = Set(Case)
    filings = Set('Filing')
    prisons = Set('Prison')
    remanded = Required(bool, default=False)
    bail = Set('Bail')


class Filing(db.Entity):
    id = PrimaryKey(int, auto=True)
    defendants = Set(Defendant)
    case = Required(Case)
    plaintiffs = Set(Plaintiff)
    filing_date = Required(datetime)
    doc_name = Required(str, 50)
    doc_content = Required(LongStr)
    case__hearing = Required('Case_Hearing')
    documents = Set('Document')
    filing_fee = Required(float, default="0.00")
    receipt_number = Required(str, 20)
    received_by = Required(str, 50)


class Judge(Person):
    court = Required(Court)
    cases = Set(Case)
    court_level = Required('CourtLevel')
    appelation = Required(str, 100)
    case__hearings = Set('Case_Hearing')


class Prosecutor(Person):
    cases = Set(Case)
    ps = Set('ProsecutorHearing')
    is_police = Required(bool, default=False)
    prosecutor_team = Optional('ProsecutorTeam')


class Defense_attorney(Person):
    c_def_atts = Set('CaseDefenseAttorney')
    law_firm = Required(str, 100)
    csda = Set('AttorneyHearing')
    bar_number = Required(str, 20)
    call_to_bar_year = Required(int, default=2000)


class Witnesses(Person):
    cases = Set(Case)
    special = Required(bool, default=False)
    role = Required(str, 100)
    for_defense = Required(bool, default=False)
    how_many = Required(int)


class District(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 100)
    region = Required('Region')
    towns = Set('Town')


class Town(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 50)
    district = Required(District)
    courts = Set(Court)
    prisons = Set('Prison')
    police_stations = Set('PoliceStation')


class Prison(db.Entity):
    id = PrimaryKey(int, auto=True)
    town = Required(Town)
    inmates = Set('Offender')
    defendants = Set(Defendant)
    case__hearings = Set('Case_Hearing')
    name = Required(str, 100)


class PoliceStation(db.Entity):
    id = PrimaryKey(int, auto=True)
    town = Required(Town)


class Complaint(db.Entity):
    id = PrimaryKey(int, auto=True)
    complaint_date = Required(datetime)
    complainants = Set('Complainant')
    offenders = Set('Offender')
    is_case = Optional(bool, default=False)
    case = Optional(Case)
    policemen = Set('Policeman')
    notes = Required(LongStr)


class Complainant(Person):
    complaints = Set(Complaint)


class Offender(Person):
    complaints = Set(Complaint)
    prisons = Set(Prison)


class CaseCategory(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 40)
    cases = Set(Case)


class CaseStatus(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 40)
    cs_changes = Set('Case_status_change')


class CourtLevel(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 40)
    courts = Set(Court)
    judges = Set(Judge)


class Contact(db.Entity):
    id = PrimaryKey(int, auto=True)
    message = Required(str, 200)
    plaintiffs = Set(Plaintiff)


class Offense(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 100)
    cases = Set(Case)
    description = Required(str)


class Bail(db.Entity):
    case = Required(Case)
    defendant = Required(Defendant)
    sureties = Set('Surety')
    case_bail_hearings = Set('Case_Hearing')
    PrimaryKey(case, defendant)


class Surety(Person):
    bail = Set(Bail)


class Policeman(Person):
    service_number = Required(str, 50)
    complaints = Set(Complaint)
    cases = Set(Case)
    rank = Required(str, 40)


class Region(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 40)
    districts = Set(District)


class Gender(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 10)
    persons = Set(Person)


class HearingType(db.Entity):
    id = PrimaryKey(int, auto=True)
    case_hearings = Set('Case_Hearing')
    name = Required(str, 40)


class Case_Hearing(db.Entity):
    case = Required(Case)
    hearingtype = Required(HearingType)
    ps = Set('ProsecutorHearing')
    csda = Set('AttorneyHearing')
    judges = Set(Judge)
    filings = Set(Filing)
    prison = Required(Prison)
    bail = Required(Bail)
    PrimaryKey(case, hearingtype)


class Case_status_change(db.Entity):
    casestatus = Required(CaseStatus)
    case = Required(Case)
    PrimaryKey(casestatus, case)


class Document(db.Entity):
    id = PrimaryKey(int, auto=True)
    filings = Set(Filing)
    document = Optional(buffer)
    doc_content = Required(LongStr)
    doc_img = Required(buffer)
    doc_date = Required(date)


class ProsecutorTeam(db.Entity):
    id = PrimaryKey(int, auto=True)
    team_name = Required(str)
    prosecutors = Set(Prosecutor)


class CasePlaintiff(db.Entity):
    plaintiff = Required(Plaintiff)
    case = Required(Case)
    PrimaryKey(plaintiff, case)


class CaseDefenseAttorney(db.Entity):
    case = Required(Case)
    defense_attorney = Required(Defense_attorney)
    PrimaryKey(case, defense_attorney)


class AttorneyHearing(db.Entity):
    _table_ = 'Chda'
    defense_attorney = Required(Defense_attorney)
    case_hearing = Required(Case_Hearing)
    PrimaryKey(defense_attorney, case_hearing)


class ProsecutorHearing(db.Entity):
    prosecutor = Required(Prosecutor)
    case_hearing = Required(Case_Hearing)
    PrimaryKey(prosecutor, case_hearing)


db.bind("postgres", host="localhost", user="nyimbi", database="casetrack_tmp")
db.generate_mapping(create_tables=True)
