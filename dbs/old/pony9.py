from datetime import date
from datetime import datetime
from pony.orm import *


db = Database()


class Court(db.Entity):
    id = PrimaryKey(int, auto=True)
    cases = Set('Case')
    judges = Set('Judge')
    town = Required('Town')
    court_level = Required('CourtLevel')


class Case(db.Entity):
    id = PrimaryKey(int, auto=True)
    court = Required(Court)
    case_number = Required(str, 30)
    plaintiffs = Set('Plaintiff')
    defendants = Set('Defendant')
    filings = Set('Filing')
    judges = Set('Judge')
    prosecutors = Set('Prosecutor')
    attorneys = Set('Attorney')
    witnesses = Set('Witness')
    is_criminal = Required(bool, default=True)
    complaints = Set('Complaint')
    case_category = Required('CaseCategory')
    offenses = Set('Offense')
    charge_date = Required(datetime)
    bail = Optional('Bail')
    policemen = Set('Policeman')
    case_hearings = Set('CaseHearing')
    casestatuses = Set('CaseStatus')


class Plaintiff(db.Entity):
    cases = Set(Case)
    filings = Set('Filing')
    contacts = Set('Contact')
    with_others = Required(bool, default=False)
    case_hearings = Set('CaseHearing')
    complaints = Set('Complaint')
    gender = Required('Gender')


class Defendant(db.Entity):
    cases = Set(Case)
    filings = Set('Filing')
    prisons = Set('Prison')
    bail = Set('Bail')
    case_hearings = Set('CaseHearing')
    complaints = Set('Complaint')
    gender = Required('Gender')


class Filing(db.Entity):
    id = PrimaryKey(int, auto=True)
    defendants = Set(Defendant)
    case = Required(Case)
    plaintiffs = Set(Plaintiff)
    filing_date = Required(datetime)
    doc_name = Required(str, 50)
    doc_content = Required(LongStr)
    case_hearing = Required('CaseHearing')
    documents = Set('Document')
    filing_fee = Required(float, default="0.00")
    receipt_number = Required(str, 20)
    received_by = Required(str, 50)
    fee_schedules = Set('FeeSchedule')


class Judge(db.Entity):
    court = Required(Court)
    cases = Set(Case)
    court_level = Required('CourtLevel')
    appelation = Required(str, 100)
    case_hearings = Set('CaseHearing')


class Prosecutor(db.Entity):
    cases = Set(Case)
    case_hearings = Set('CaseHearing')
    is_police = Required(bool, default=False)


class Attorney(db.Entity):
    cases = Set(Case)
    case_hearings = Set('CaseHearing')
    bar_number = Required(str, 20)
    call_to_bar_year = Required(int, default=2000)
    lawfirm_member = Optional('LawFirm')


class Witness(db.Entity):
    cases = Set(Case)
    case_hearings = Set('CaseHearing')
    special = Required(bool, default=False)
    role = Required(str, 100)
    for_defense = Required(bool, default=False)


class District(db.Entity):
    id = PrimaryKey(int, auto=True)
    region = Required('Region')
    towns = Set('Town')


class Town(db.Entity):
    id = PrimaryKey(int, auto=True)
    district = Required(District)
    courts = Set(Court)
    prisons = Set('Prison')
    police_stations = Set('PoliceStation')


class Prison(db.Entity):
    id = PrimaryKey(int, auto=True)
    town = Required(Town)
    defendants = Set(Defendant)
    case_hearings = Set('CaseHearing', cascade_delete=True)
    warden = Required(str, 50)


class PoliceStation(db.Entity):
    id = PrimaryKey(int, auto=True)
    town = Required(Town)
    policemen = Set('Policeman')


class Complaint(db.Entity):
    id = PrimaryKey(int, auto=True)
    complaint_date = Required(datetime)
    is_case = Optional(bool, default=False)
    case = Optional(Case)
    policemen = Set('Policeman')
    notes = Required(LongStr)
    plaintiffs = Set(Plaintiff)
    defendants = Set(Defendant)


class CaseCategory(db.Entity):
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)


class CaseStatus(db.Entity):
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)


class CourtLevel(db.Entity):
    id = PrimaryKey(int, auto=True)
    courts = Set(Court)
    judges = Set(Judge)


class Contact(db.Entity):
    id = PrimaryKey(int, auto=True)
    plaintiffs = Set(Plaintiff)


class Offense(db.Entity):
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)


class Bail(db.Entity):
    case = PrimaryKey(Case)
    defendant = Required(Defendant)
    amount = Required(float)
    sureties = Set('Surety')
    case_bail_hearings = Set('CaseHearing', cascade_delete=True)
    surety_count = Required(int, default=0)
    paid = Required(bool, default=False)
    paid_date = Required(date)
    receipt_number = Required(str)


class Surety(db.Entity):
    bail = Set(Bail)


class Policeman(db.Entity):
    complaints = Set(Complaint)
    cases = Set(Case)
    service_number = Required(str, 50)
    rank = Required(str, 40)
    case_hearings = Set('CaseHearing')
    police_station = Required(PoliceStation)


class Region(db.Entity):
    id = PrimaryKey(int, auto=True)
    districts = Set(District)


class Gender(db.Entity):
    id = PrimaryKey(int, auto=True)
    plaintiffs = Set(Plaintiff)
    defendants = Optional(Defendant)


class HearingType(db.Entity):
    id = PrimaryKey(int, auto=True)
    case_hearings = Set('CaseHearing')


class CaseHearing(db.Entity):
    case = PrimaryKey(Case)
    hearingtype = Required(HearingType)
    hearing_date = Required(datetime)
    prosecutors = Set(Prosecutor)
    prosecutor_present = Required(bool, default=True)
    attorneys = Set(Attorney)
    defense_attorney_present = Required(bool, default=True)
    judges = Set(Judge)
    case_outcome = Required(LongStr)
    filings = Set(Filing)
    prison = Required(Prison)
    from_remand = Required(bool)
    to_remand = Required(bool, default=False)
    to_prison = Required(bool, default=False)
    bail = Required(Bail)
    notes = Required(LongStr)
    plaintiffs = Set(Plaintiff)
    defendants = Set(Defendant)
    witnesses = Set(Witness)
    policemen = Set(Policeman)


class Document(db.Entity):
    id = PrimaryKey(int, auto=True)
    filings = Set(Filing)
    document = Optional(buffer)
    doc_content = Required(LongStr)
    doc_img = Required(buffer)
    doc_date = Required(date)


class LawFirm(db.Entity):
    id = PrimaryKey(int, auto=True)
    attorneys = Set(Attorney)


class FeeSchedule(db.Entity):
    id = PrimaryKey(int, auto=True)
    amount = Required(float)
    filings = Set(Filing)


db.bind("postgres", host="localhost", user="nyimbi", database="ctmp")
db.generate_mapping(create_tables=True)
