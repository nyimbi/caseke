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
    accused = Set('Accused')
    filings = Set('Filing')
    judges = Set('Judge')
    prosecutors = Set('Prosecutor')
    defense_attorneys = Set('Attorney', reverse='defending_case')
    witnesses = Set('Witness')
    is_criminal = Required(bool, default=True)
    complaints = Set('Complaint')
    case_category = Required('CaseCategory')
    cs_changes = Set('Case_status_change')
    offenses = Set('Offense')
    charge_date = Required(datetime)
    policemen = Set('Policeman')
    case_hearings = Set('Case_Hearing')
    suing_attorneys = Set('Attorney', reverse='suing_case')
    case_type = Required('CaseType')


class Litigant(db.Entity):
    _table_ = 'Person'
    _discriminator_ = 'litigant'
    discriminator = Discriminator(str)
    id = PrimaryKey(int, auto=True)
    gender = Required('Gender')
    date_of_birth = Required(date)
    identity = Required(LongStr)
    address = Required(LongStr)
    biometrics = Required(LongStr)


class Plaintiff(Litigant):
    _discriminator_ = 'plaintiff'
    cases = Set(Case)
    filings = Set('Filing')
    contacts = Set('Contact')
    complaints = Set('Complaint')
    with_others = Optional(bool, default=False)


class Accused(Litigant):
    _discriminator_ = 'accused'
    cases = Set(Case)
    filings = Set('Filing')
    prisons = Set('Prison')
    bail = Set('Bail')
    case_hearings = Set('Case_Hearing')
    complaints = Set('Complaint')
    remanded = Required(bool, default=False)


class Filing(db.Entity):
    id = PrimaryKey(int, auto=True)
    accussed = Set(Accused)
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
    fee_schedules = Set('FeeSchedule')


class Judge(db.Entity):
    court = Required(Court)
    cases = Set(Case)
    court_level = Required('CourtLevel')
    appelation = Required(str, 100)
    case__hearings = Set('Case_Hearing')


class Prosecutor(db.Entity):
    cases = Set(Case)
    case__hearings = Set('Case_Hearing')
    is_police = Required(bool, default=False)


class Attorney(db.Entity):
    hearings_attend = Set('Case_Hearing')
    defending_case = Set(Case, reverse='defense_attorneys')
    suing_case = Set(Case, reverse='suing_attorneys')
    bar_number = Required(str, 20)
    call_to_bar_year = Required(int, default=2000)
    law_firm = Optional('LawFirm')


class Witness(db.Entity):
    witness_cases = Set(Case)
    special = Required(bool, default=False)
    role = Required(str, 100)
    for_defense = Optional(bool, default=False)
    how_many = Required(int)


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
    accused = Set(Accused)
    case__hearings = Set('Case_Hearing')
    warden = Required(str, 50)


class PoliceStation(db.Entity):
    id = PrimaryKey(int, auto=True)
    town = Required(Town)


class Complaint(db.Entity):
    id = PrimaryKey(int, auto=True)
    complainants = Set(Plaintiff)
    accused = Set(Accused)
    policemen = Set('Policeman')
    complaint_date = Required(datetime)
    is_case = Optional(bool, default=False)
    case = Optional(Case)
    notes = Required(LongStr)


class CaseCategory(db.Entity):
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)


class CaseStatus(db.Entity):
    id = PrimaryKey(int, auto=True)
    cs_changes = Set('Case_status_change')


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
    accused = PrimaryKey(Accused)
    amount = Required(float)
    sureties = Set('Surety')
    case_bail_hearings = Set('Case_Hearing', cascade_delete=True)
    surety_count = Required(int, default=0)
    paid = Required(bool, default=False)
    paid_date = Required(date)
    receipt_number = Required(str)


class Surety(Litigant):
    _discriminator_ = 'surety'
    bail = Set(Bail)


class Policeman(db.Entity):
    service_number = Required(str, 50)
    complaints = Set(Complaint)
    cases = Set(Case)
    rank = Required(str, 40)


class Region(db.Entity):
    id = PrimaryKey(int, auto=True)
    districts = Set(District)


class Gender(db.Entity):
    id = PrimaryKey(int, auto=True)
    litigants = Set(Litigant)


class HearingType(db.Entity):
    id = PrimaryKey(int, auto=True)
    case_hearings = Set('Case_Hearing')


class Case_Hearing(db.Entity):
    case = PrimaryKey(Case)
    hearingtype = Required(HearingType)
    hearing_date = Required(datetime)
    prosecutors = Set(Prosecutor)
    attorneys = Set(Attorney)
    judges = Set(Judge)
    filings = Set(Filing)
    accused = Set(Accused)
    prisons = Set(Prison)
    prosecutor_present = Required(bool, default=True)
    defense_attorney_present = Required(bool, default=True)
    case_outcome = Required(LongStr)
    from_remand = Required(bool)
    to_remand = Optional(bool, default=False)
    to_prison = Required(bool, default=False)
    bail = Optional(Bail)
    notes = Required(LongStr)
    transcript = Required(LongStr)


class Case_status_change(db.Entity):
    casestatus = Required(CaseStatus)
    case = Required(Case)
    csc_date = Required(datetime)
    notes = Required(LongStr)
    PrimaryKey(casestatus, case, csc_date)


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


class CaseType(db.Entity):
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)


db.bind("postgres", host="localhost", user="nyimbi", database="ctmp")
db.generate_mapping(create_tables=True)
