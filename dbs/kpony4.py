from datetime import date
from datetime import datetime
from decimal import Decimal
from pony.orm import *


db = Database()


class Case(db.Entity):
    """PlaceMixin, RefTypeMixin"""
    _table_ = 'case'
    id = PrimaryKey(int, auto=True)
    CaseName = Required(str, 200)  # parties X vs Y
    DocketNumber = Required(str, 100, nullable=True)
    nature_of_suits = Set('NatureOfSuit')
    plaintiffs = Set('Plaintiff')
    defendants = Set('Defendant')
    reported_to_police_stations = Set('PoliceStation')
    reported_to_policeman = Set('Policeman', reverse='report_cases')
    police_prosecutors = Set('Policeman', reverse='prosecute_cases')
    InvestigationAssigmentDate = Optional(datetime, default=datetime.now)
    InvestigationAssignmentNote = Required(LongStr)
    InvestigationPlan = Required(LongStr)
    investigationDiary = Set('Investigation')
    InitialReport = Optional(LongStr)
    Priority = Required(int, default=3)
    InvestigationSummary = Optional(LongStr)
    AgAdviceRequested = Required(bool, default=False)
    SendToTrial = Required(bool, default=False)
    ChargeDate = Optional(datetime, default=datetime.now)
    advising_prosecutors = Set('Prosecutor')
    AgAdvice = Required(LongStr)
    TakeToTrial = Required(bool, default=False)
    observers = Set('Observer')
    hearings = Set('Hearing')
    CaseClosed = Required(bool, default=False)
    Judgement = Required(LongStr)
    ClosedDate = Required(date)
    SentenceLength = Required(int)
    SentenceStartDate = Required(date)
    SentenceExpiryDate = Required(date)
    FineAmount = Required(float)
    CaseAppealed = Required(bool, default=False)
    AppealDate = Required(datetime, default=datetime.now)
    causes_of_action = Set('CauseOfAction')


class County(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    subcounties = Set('Subcounty')
    constituencies = Set('Constituency')


class Subcounty(db.Entity):
    """RefTypeMixin"""
    id = PrimaryKey(int, auto=True)
    county = Required(County)
    towns = Set('Town')


class Town(db.Entity):
    """RefTypeMixin, PlaceMixin"""
    id = PrimaryKey(int, auto=True)
    subcounty = Required(Subcounty)
    constituencies = Set('Constituency')
    police_stations = Set('PoliceStation')
    prisons = Set('Prison')
    courts = Set('Court')


class Constituency(db.Entity):
    id = PrimaryKey(int, auto=True)
    county = Required(County)
    town = Optional(Town)


class PoliceStation(db.Entity):
    """RefTypeMixin, PlaceMixin, ContactMixin"""
    id = PrimaryKey(int, auto=True)
    town = Required(Town)
    OfficerCommanding = Optional(str, 100, nullable=True)
    reported_cases = Set(Case)


class Prison(db.Entity):
    """RefTypeMixin, PlaceMixin, ContactMixin"""
    id = PrimaryKey(int, auto=True)
    town = Required(Town)
    Warden = Optional(str, 100, nullable=True)
    prisonremands = Set('PrisonRemand')
    Capacity = Required(int)
    Population = Required(int)


class Court(db.Entity):
    """RefTypeMixin, PlaceMixin, ContactMixin"""
    id = PrimaryKey(int, auto=True)
    town = Required(Town)
    ResidentMagistrate = Optional(str, 100, nullable=True)
    Registrar = Optional(str, 100)
    hearings = Set('Hearing')
    judges = Set('Judge')
    court_level = Required('CourtLevel')


class Plaintiff(db.Entity):
    """PersonMixin, ContactMixin"""
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)


class Defendant(db.Entity):
    """PersonMixin, ContactMixn, BiometricMixin"""
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)
    hearings = Set('Hearing')
    bails = Set('Bail')
    prison_remands = Set('PrisonRemand')


class Policeman(db.Entity):
    """PersonMixin
Rank, ServiceNumber, Specialization, Notes"""
    id = PrimaryKey(int, auto=True)
    police_roles = Set('PoliceRole')
    report_cases = Set(Case, reverse='reported_to_policeman')
    prosecute_cases = Set(Case, reverse='police_prosecutors')
    investigations = Set('Investigation')
    hearings = Set('Hearing')


class PoliceRole(db.Entity):
    """RefTypeMixin
Investigator, Prosecutor, ReportingOfficer, ArrestingOfficer, DetainingOfficer, Supervisor"""
    id = PrimaryKey(int, auto=True)
    policemen = Set(Policeman)


class Prosecutor(db.Entity):
    id = PrimaryKey(int, auto=True)
    prosecutor_teams = Set('ProsecutorTeam')
    advise_cases = Set(Case)
    hearings = Set('Hearing')
    filings = Set('Filing')


class Attorney(db.Entity):
    id = PrimaryKey(int, auto=True)
    hearings = Set('Hearing')
    law_firm = Optional('LawFirm')
    filings = Set('Filing')
    BarNumber = Required(str, 20, nullable=True)


class ProsecutorTeam(db.Entity):
    id = PrimaryKey(int, auto=True)
    prosecutors = Set(Prosecutor)


class LawFirm(db.Entity):
    id = PrimaryKey(int, auto=True)
    attorneys = Set(Attorney)


class Investigation(db.Entity):
    """PlaceMixin, ActivityMixin
Actions, Finding, InterviewNotes, Interviewees, Forensics"""
    id = PrimaryKey(int, auto=True)
    investigator = Set(Policeman)
    case = Required(Case)
    ActionDate = Required(datetime, default=datetime.now)
    observers = Set('Observer')
    Evidence = Required(LongStr)
    Narrative = Required(LongStr)
    Weather = Required(LongStr)
    Location = Required(LongStr)


class Observer(db.Entity):
    _table_ = 'observer'
    id = PrimaryKey(int, auto=True)
    ForDefense = Required(bool, default=False)
    investigations = Set(Investigation)
    cases = Set(Case)
    hearings = Set('Hearing')


class Hearing(db.Entity):
    id = PrimaryKey(int, auto=True)
    HearingDate = Required(datetime)
    Adjourned = Required(bool, default=False)
    case = Required(Case)
    court = Required(Court)
    prosecutors = Set(Prosecutor)
    police_prosecutors = Set(Policeman)
    defendants = Set(Defendant)
    hearing_type = Required('HearingType')
    defense_attorneys = Set(Attorney)
    judges = Set('Judge')
    observers = Set(Observer)
    filings = Set('Filing')
    RemandedToPrison = Set('PrisonRemand')
    RemandWarrant = Required(LongStr)
    RemandLength = Optional(int)
    RemandDate = Required(date, default=datetime.now)
    RemandWarrantExpiryDate = Required(date)
    NextHearingDate = Optional(date)
    FinalHearing = Required(bool, default=False)
    bail = Set('Bail')
    Transcript = Required(LongStr)
    Audio = Required(buffer)
    Video = Required(buffer)
    causes_of_action = Set('CauseOfAction')


class HearingType(db.Entity):
    id = PrimaryKey(int, auto=True)
    hearings = Set(Hearing)


class Judge(db.Entity):
    id = PrimaryKey(int, auto=True)
    court = Required(Court)
    hearings = Set(Hearing)


class NatureOfSuit(db.Entity):
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)


class CauseOfAction(db.Entity):
    """Heirarchy of causes of action"""
    id = PrimaryKey(int, auto=True)
    Criminal = Required(bool, default=False)
    parent_coa = Optional('CauseOfAction', reverse='causes_of_action')
    filings = Set('Filing')
    causes_of_action = Set('CauseOfAction', reverse='parent_coa')
    cases = Set(Case)
    hearings = Set(Hearing)


class Filing(db.Entity):
    id = PrimaryKey(int, auto=True)
    FileDate = Required(datetime, default=datetime.now)
    hearings = Set(Hearing)
    filing_types = Set('FilingType')
    TotalFees = Required(Decimal, default="0.00")
    documents = Set('Document')
    causes_of_action = Set(CauseOfAction)
    filing_attorney = Required(Attorney)
    filing_prosecutor = Required(Prosecutor)
    ReceiptNumber = Required(str, nullable=True)
    ReceiptVerified = Required(bool, default=False)
    AmountPaid = Required(Decimal, default="0.00")
    FeeBalance = Required(Decimal, default="0.00")
    PaymentHistory = Required(LongStr)


class FilingType(db.Entity):
    id = PrimaryKey(int, auto=True)
    Cost = Required(Decimal, default="0.00")
    filings = Set(Filing)
    PerPageCost = Required(Decimal)
    paid_per_page = Required(bool, default=True)


class Document(db.Entity):
    id = PrimaryKey(int, auto=True)
    filings = Set(Filing)
    doc_template = Optional('DocTemplate')


class DocTemplate(db.Entity):
    id = PrimaryKey(int, auto=True)
    documents = Set(Document)


class Bail(db.Entity):
    id = PrimaryKey(int, auto=True)
    hearing = Required(Hearing)
    defendant = Required(Defendant)
    AmountGranted = Required(Decimal)
    NoOfSureties = Required(int, default=0)
    sureties = Set('Surety')
    Paid = Required(bool)
    PayDate = Required(date)
    ReceiptNo = Required(str, 100)


class Surety(db.Entity):
    id = PrimaryKey(int, auto=True)
    bails = Set(Bail)


class CourtLevel(db.Entity):
    id = PrimaryKey(int, auto=True)
    courts = Set(Court)


class PrisonRemand(db.Entity):
    prison = Required(Prison)
    WarrantNo = Required(str, 100)
    hearing = Required(Hearing)
    defendant = Required(Defendant)
    WarrantDuration = Required(int)
    WarrantDate = Required(datetime, default=datetime.now)
    Warrant = Required(LongStr)
    WarrantExpiry = Required(datetime, default=datetime.now)
    History = Required(LongStr)
    PrimaryKey(prison, WarrantNo)


db.bind("postgres", host="localhost", user="nyimbi", database="ctmp")
db.generate_mapping(create_tables=True)
