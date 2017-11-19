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
    cs_changes = Set('Case_status_change')
    offenses = Set('Offense')
    charge_date = Required(datetime)
    bail = Optional('Bail')
    policemen = Set('Policeman')
    case_hearings = Set('Case_Hearing')


class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    gender = Required('Gender')
    date_of_birth = Required(date)
    identity = Required(LongStr)
    address = Required(LongStr)
    biometrics = Required(LongStr)


class Plaintiff(Person):
    _discriminator_ = 'plaintiff'
    cases = Set(Case)
    filings = Set('Filing')
    contacts = Set('Contact')
    with_others = Required(bool, default=False)


class Defendant(Person):
    _discriminator_ = 'defendant'
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
    fee_schedules = Set('FeeSchedule')


class Judge(Person):
    _discriminator_ = 'judge'
    court = Required(Court)
    cases = Set(Case)
    court_level = Required('CourtLevel')
    appelation = Required(str, 100)
    case__hearings = Set('Case_Hearing')


class Prosecutor(Person):
    _discriminator_ = 'prosecutor'
    cases = Set(Case)
    case__hearings = Set('Case_Hearing')
    is_police = Required(bool, default=False)


class Attorney(Person):
    _discriminator_ = 'attorney'
    cases = Set(Case)
    law_firm = Required(str, 100)
    case__hearings = Set('Case_Hearing')
    bar_number = Required(str, 20)
    call_to_bar_year = Required(int, default=2000)
    lawfirm_member = Optional('LawFirm')


class Witness(Person):
    _discriminator_ = 'witness'
    cases = Set(Case)
    special = Required(bool, default=False)
    role = Required(str, 100)
    for_defense = Required(bool, default=False)
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
    inmates = Set('Offender')
    defendants = Set(Defendant)
    case__hearings = Set('Case_Hearing', cascade_delete=True)
    warden = Required(str, 50)


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
    arrested = Required(bool, default=False)
    arrest_date = Optional(date)


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
    case = Required(Case)
    defendant = Required(Defendant)
    amount = Required(float)
    sureties = Set('Surety')
    case_bail_hearings = Set('Case_Hearing', cascade_delete=True)
    surety_count = Required(int, default=0)
    paid = Required(bool, default=False)
    paid_date = Required(date)
    receipt_number = Required(str)
    PrimaryKey(case, defendant)


class Surety(Person):
    _discriminator_ = 'surety'
    bail = Set(Bail)


class Policeman(Person):
    service_number = Required(str, 50)
    complaints = Set(Complaint)
    cases = Set(Case)
    rank = Required(str, 40)


class Region(db.Entity):
    id = PrimaryKey(int, auto=True)
    districts = Set(District)


class Gender(db.Entity):
    id = PrimaryKey(int, auto=True)
    persons = Set(Person)


class HearingType(db.Entity):
    id = PrimaryKey(int, auto=True)
    case_hearings = Set('Case_Hearing')


class Case_Hearing(db.Entity):
    case = Required(Case)
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
    PrimaryKey(case, hearingtype, hearing_date)


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


db.bind("postgres", host="localhost", user="nyimbi", database="ctmp")
db.generate_mapping(create_tables=True)
