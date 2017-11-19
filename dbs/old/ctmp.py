from datetime import date
from pony.orm import *


db = Database()


class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    xname = Required(str, 50)
    address = Optional(str, 50, nullable=True)
    gender = Required('Gender')


class Police(Person):
    service_number = Required(str, 50)
    complaints = Set('Complaint')


class Lawyer(Person):
    Reg_date = Required(date)
    bar_number = Required(str, 20)


class Prosecutor(Lawyer):
    prosecutor_team = Required('ProsecutorTeam')
    hearings = Set('Hearing')


class ProsecutorTeam(db.Entity):
    id = PrimaryKey(int, auto=True)
    prosecutors = Set(Prosecutor)
    cases = Set('Case')


class DefenseAtt(Lawyer):
    law_firm = Optional('LawFirm')
    cases = Set('Case')
    hearings = Set('Hearing')


class LawFirm(db.Entity):
    id = PrimaryKey(int, auto=True)
    defense_atts = Set(DefenseAtt)


class Complainant(Person):
    phone = Required(str)
    complaints = Set('Complaint')
    cases = Set('Case')


class Offender(Person):
    complaint = Required('Complaint')
    cases = Set('Case')
    prison = Required('Prison')


class Witness(Person):
    pass


class Complaint(db.Entity):
    id = PrimaryKey(int, auto=True)
    complainant = Required(Complainant)
    offenders = Set(Offender)
    police = Required(Police)
    police_station = Required('PoliceStation')
    cases = Set('Case')
    statement = Required(LongStr)


class PoliceStation(db.Entity):
    id = PrimaryKey(int, auto=True)
    complaints = Set(Complaint)
    town = Required('Town')


class District(db.Entity):
    id = PrimaryKey(int, auto=True)
    region = Required('Region')
    towns = Set('Town')


class Region(db.Entity):
    id = PrimaryKey(int, auto=True)
    districts = Set(District)


class Town(db.Entity):
    id = PrimaryKey(int, auto=True)
    district = Required(District)
    police_stations = Set(PoliceStation)
    courts = Set('Court')


class Case(db.Entity):
    id = PrimaryKey(int, auto=True)
    complaint = Required(Complaint)
    prosecutor_team = Required(ProsecutorTeam)
    complainant = Optional(Complainant)
    offender = Required(Offender)
    defense_att = Required(DefenseAtt)
    court = Required('Court')
    judge = Required('Judge')
    prison = Required('Prison')
    hearings = Set('Hearing')
    case_type = Required('CaseType')
    case_status = Required('CaseStatus')


class Judge(Lawyer):
    court = Required('Court')
    cases = Set(Case)
    hearings = Set('Hearing')


class Court(db.Entity):
    id = PrimaryKey(int, auto=True)
    town = Required(Town)
    judges = Set(Judge)
    cases = Set(Case)
    court_level = Required('CourtLevel')


class Prison(db.Entity):
    id = PrimaryKey(int, auto=True)
    offenders = Set(Offender)
    cases = Set(Case)


class Hearing(db.Entity):
    id = PrimaryKey(int, auto=True)
    case = Required(Case)
    bails = Set('Bail')
    filings = Set('Filing')
    defense_att = Optional(DefenseAtt)
    prosecutor = Optional(Prosecutor)
    hearing_date = Required(date)
    judge = Optional(Judge)
    hearing_type = Required('HearingType')
    notification = Optional('Notification')


class Bail(db.Entity):
    id = PrimaryKey(int, auto=True)
    hearing = Required(Hearing)
    Amount = Required(float)
    suretys = Set('Surety')


class Surety(Person):
    bail = Required(Bail)


class CourtLevel(db.Entity):
    id = PrimaryKey(int, auto=True)
    courts = Set(Court)
    name = Required(str, 40)


class CaseType(db.Entity):
    _table_ = 'CaeType'
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)


class CaseStatus(db.Entity):
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)


class Filing(db.Entity):
    id = PrimaryKey(int, auto=True)
    hearing = Optional(Hearing)
    documents = Set('Document')
    File_date = Required(date)


class Document(db.Entity):
    id = PrimaryKey(int, auto=True)
    filing = Required(Filing)
    Content = Required(LongStr)


class HearingType(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, 40)
    hearings = Set(Hearing)


class Gender(db.Entity):
    id = PrimaryKey(int, auto=True)
    people = Set(Person)


class Notification(db.Entity):
    id = PrimaryKey(int, auto=True)
    hearings = Set(Hearing)


db.bind("postgres", host="localhost", user="nyimbi", database="ctmp")
db.generate_mapping(create_tables=True)
