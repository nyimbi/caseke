from datetime import date
from datetime import datetime
from datetime import timedelta
from decimal import Decimal
from pony.orm import *


db = Database()


class Case(db.Entity):
    """PlaceMixin, RefTypeMixin"""
    _table_ = 'case'
    id = PrimaryKey(int, auto=True)
    CaseName = Optional(str, 200)  # parties X vs Y
    InitialReport = Optional(LongStr)
    nature_of_suits = Set('NatureOfSuit')
    plaintiffs = Set('Plaintiff')
    defendants = Set('Defendant')
    reported_to_police_stations = Set('PoliceStation')
    reported_to_police_officer = Set('PoliceOfficer', reverse='report_cases')
    police_prosecutors = Set('PoliceOfficer', reverse='prosecute_cases')
    Priority = Required(int, default=3)
    InvestigationAssigmentDate = Optional(datetime)
    InvestigationAssignmentNote = Optional(LongStr)
    InvestigationPlan = Optional(LongStr)
    investigationDiary = Set('Investigation')
    InvestigationSummary = Optional(LongStr)
    InvestigationReview = Optional(LongStr, nullable=True)
    AgAdviceRequested = Optional(bool, default=False)
    AgAdviceDate = Optional(date, default=lambda: date.today())
    AgAdvice = Optional(LongStr)
    ChargeSheet = Optional(LongStr)
    SendToTrial = Required(bool, default=False)
    DocketNumber = Optional(str, 100, nullable=True, default="D/000/000")
    NameofCase = Optional(str, 400, nullable=True, default="Republic Vs ")
    ChargeDate = Optional(datetime)
    advising_prosecutors = Set('Prosecutor', reverse='advise_cases')
    prosecutors = Set('Prosecutor', reverse='case_prosecutor')
    witnesses = Set('Witness')
    hearings = Set('Hearing')
    Judgement = Optional(LongStr)
    JudgementDate = Optional(datetime, nullable=True, default=lambda: datetime.now())
    SentenceLengthYr = Optional(int)
    SentenceLengthMnth = Optional(int)
    SenetenceLenghtDays = Optional(int)
    SentenceStartDate = Optional(date, nullable=True, default=lambda: date.today())
    SentenceExpiryDate = Optional(date, nullable=True, default=lambda: date.today())
    FineAmount = Optional(Decimal, nullable=True, default="0.00")
    fines_paid = Set('Payment')
    CaseAppealed = Optional(bool, default=False)
    AppealDate = Optional(datetime)
    AppealExpiry = Optional(date, nullable=True, default=lambda: date.today())
    causes_of_action = Set('CauseOfAction')
    filings = Set('Filing')
    case_categories = Set('CaseCategory')
    CaseClosed = Optional(bool, default=False)
    CloseDate = Optional(date, nullable=True, default=lambda: date.today())


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
    court_stations = Set('CourtStation')


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
    police_station_type = Required('PoliceStationType')


class Prison(db.Entity):
    """RefTypeMixin, PlaceMixin, ContactMixin"""
    id = PrimaryKey(int, auto=True)
    town = Required(Town)
    Warden = Optional(str, 100, nullable=True)
    prisoncommitals = Set('PrisonCommital')
    Capacity = Optional(int)
    Population = Optional(int)
    warders = Set('Warder')
    CellCount = Optional(int)
    security_ranks = Set('SecurityRank')
    cells = Set('Cell')


class CourtStation(db.Entity):
    """RefTypeMixin, PlaceMixin, ContactMixin"""
    id = PrimaryKey(int, auto=True)
    ResidentMagistrate = Optional(str, 100, nullable=True)
    Registrar = Optional(str, 100)
    court_level = Required('CourtLevel')
    num_of_courts = Optional(int, nullable=True, default=1)
    courts = Set('Court')
    town = Required(Town)


class Plaintiff(db.Entity):
    """PersonMixin, ContactMixin"""
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)
    gender = Optional('Gender')
    Juvenile = Optional(bool, nullable=True, default=False)


class Defendant(db.Entity):
    """PersonMixin, ContactMixn, BiometricMixin"""
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)
    hearings = Set('Hearing')
    bails = Set('Bail')
    Juvenile = Optional(bool, default=False)
    prison_remands = Set('PrisonCommital')
    gender = Required('Gender')
    disciplinary = Set('Discipline')
    medical_events = Set('MedEvent')
    visits = Set('Visit')
    cell = Required('Cell')


class PoliceOfficer(db.Entity):
    """PersonMixin
Rank, ServiceNumber, Specialization, Notes"""
    id = PrimaryKey(int, auto=True)
    police_roles = Set('PoliceRole')
    police_rank = Required('PoliceRank')
    report_cases = Set(Case, reverse='reported_to_police_officer')
    prosecute_cases = Set(Case, reverse='police_prosecutors')
    investigations = Set('Investigation')
    hearings = Set('Hearing')
    gender = Required('Gender')
    ServiceNumber = Optional(str, nullable=True)
    prison_commitals = Set('PrisonCommital')


class PoliceRole(db.Entity):
    """RefTypeMixin
Investigator, Prosecutor, ReportingOfficer, ArrestingOfficer, DetainingOfficer, Supervisor"""
    id = PrimaryKey(int, auto=True)
    policeofficers = Set(PoliceOfficer)


class Prosecutor(db.Entity):
    id = PrimaryKey(int, auto=True)
    prosecutor_teams = Set('ProsecutorTeam')
    advise_cases = Set(Case, reverse='advising_prosecutors')
    hearings = Set('Hearing')
    filings = Set('Filing')
    gender = Optional('Gender')
    case_prosecutor = Set(Case, reverse='prosecutors')


class Lawyer(db.Entity):
    _table_ = 'Lawyers'
    id = PrimaryKey(int, auto=True)
    hearings = Set('Hearing')
    law_firm = Optional('LawFirm')
    gender = Optional('Gender')
    filings = Set('Filing')
    BarNumber = Optional(str, 20, nullable=True)
    AdmissionDate = Optional(date, default=lambda: date.today())


class ProsecutorTeam(db.Entity):
    id = PrimaryKey(int, auto=True)
    prosecutors = Set(Prosecutor)


class LawFirm(db.Entity):
    id = PrimaryKey(int, auto=True)
    lawyers = Set(Lawyer)


class Investigation(db.Entity):
    """PlaceMixin, ActivityMixin
Actions, Finding, InterviewNotes, Interviewees, Forensics"""
    id = PrimaryKey(int, auto=True)
    investigator = Set(PoliceOfficer)
    case = Required(Case)
    ActionDate = Required(datetime)
    witnesses = Set('Witness')
    Evidence = Optional(LongStr)
    Narrative = Optional(LongStr)
    Weather = Optional(LongStr)
    Location = Optional(LongStr)


class Witness(db.Entity):
    id = PrimaryKey(int, auto=True)
    ForDefense = Optional(bool, default=False)
    investigations = Set(Investigation)
    cases = Set(Case)
    hearings = Set('Hearing')
    gender = Required('Gender')


class Hearing(db.Entity):
    id = PrimaryKey(int, auto=True)
    HearingDate = Required(datetime, default=lambda: datetime.now())
    Adjourned = Optional(bool, default=False)
    case = Required(Case)
    prosecutors = Set(Prosecutor)
    police_prosecutors = Set(PoliceOfficer)
    court = Required('Court')
    defendants = Set(Defendant)
    defense_attorneys = Set(Lawyer)
    judicialofficers = Set('JudicialOfficer')
    witnesses = Set(Witness)
    RemandedToPrison = Set('PrisonCommital', nullable=True)
    RemandWarrant = Optional(LongStr, nullable=True)
    hearing_type = Required('HearingType')
    RemandDays = Optional(int)
    RemandDate = Optional(date)
    RemandWarrantExpiryDate = Optional(date)
    NextHearingDate = Optional(date, default=lambda: date.today())
    FinalHearing = Required(bool, default=False)
    bail = Set('Bail')
    Transcript = Optional(LongStr, nullable=True)
    Audio = Optional(buffer, nullable=True)
    Video = Optional(buffer, nullable=True)
    causes_of_action = Set('CauseOfAction')


class HearingType(db.Entity):
    id = PrimaryKey(int, auto=True)
    hearings = Set(Hearing)


class JudicialOfficer(db.Entity):
    id = PrimaryKey(int, auto=True)
    j_o__rank = Required('JO_Rank')
    hearings = Set(Hearing)
    gender = Optional('Gender')
    court = Required('Court')


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
    UploadDate = Optional(datetime, nullable=True, default=lambda: datetime.now())
    filing_types = Set('FilingType')
    PageCount = Optional(int, nullable=True, default=1)
    TotalFees = Required(Decimal, default="0.00")
    causes_of_action = Set(CauseOfAction)
    filing_attorney = Required(Lawyer)
    filing_prosecutor = Required(Prosecutor)
    AssessedFees = Optional(Decimal, default="0.00")
    ReceiptVerified = Optional(bool, default=False)
    AmountPaid = Optional(Decimal, default="0.00")
    FeeBalance = Optional(Decimal, nullable=True, default="0.00")
    PaymentHistory = Optional(LongStr)
    case = Required(Case)
    payments = Set('Payment')
    documents = Set('Document')
    Urgent = Optional(bool, nullable=True, default=False)
    UrgentReason = Optional(LongStr)


class FilingType(db.Entity):
    id = PrimaryKey(int, auto=True)
    Fees = Required(Decimal, nullable=True, default="0.00")
    filings = Set(Filing)
    PerPageCost = Optional(Decimal, nullable=True, default="0.00")
    paid_per_page = Optional(bool, default=False)


class Document(db.Entity):
    id = PrimaryKey(int, auto=True)
    doc_template = Optional('DocTemplate')
    Confidential = Optional(bool, nullable=True, default=False)
    PageCount = Optional(int)
    filing = Required(Filing)
    Locked = Optional(bool, nullable=True, default=False)


class DocTemplate(db.Entity):
    id = PrimaryKey(int, auto=True)
    documents = Set(Document)


class Bail(db.Entity):
    id = PrimaryKey(int, auto=True)
    hearing = Required(Hearing)
    defendant = Required(Defendant)
    AmountGranted = Optional(Decimal)
    NoOfSureties = Required(int, default=0)
    sureties = Set('Surety')
    Paid = Optional(bool, default=False)
    PayDate = Optional(date, default=lambda: date.today())
    payments = Set('Payment', nullable=True)


class Surety(db.Entity):
    id = PrimaryKey(int, auto=True)
    bails = Set(Bail)
    gender = Optional('Gender')


class CourtLevel(db.Entity):
    id = PrimaryKey(int, auto=True)
    courtstations = Set(CourtStation)


class PrisonCommital(db.Entity):
    prison = Required(Prison)
    prison_commital_types = Set('CommitalType')
    WarrantNo = Required(str, 100)
    defendant = Required(Defendant)
    hearing = Required(Hearing)
    WarrantDuration = Required(int)
    WarrantDate = Optional(datetime)
    Warrant = Optional(LongStr)
    WarrantExpiry = Required(datetime)
    History = Optional(LongStr)
    EarliestRelease = Optional(date, nullable=True)
    ReleaseDate = Optional(datetime, nullable=True, default=lambda: datetime.now())
    Property = Optional(LongStr, nullable=True)
    ItemCount = Optional(int, nullable=True, default=0)
    ReleaseNotes = Optional(LongStr, nullable=True)
    CommitalNotes = Optional(LongStr, nullable=True)
    police_officer_commiting = Required(PoliceOfficer)
    receiving_warders = Set('Warder')
    PrimaryKey(prison, WarrantNo)


class Gender(db.Entity):
    id = PrimaryKey(int, auto=True)
    Name = Required(str, 20, unique=True)
    lawyers = Set(Lawyer)
    defendants = Set(Defendant)
    judicialofficers = Set(JudicialOfficer)
    witnesses = Set(Witness)
    plaintiffs = Set(Plaintiff)
    policeofficers = Set(PoliceOfficer)
    prosecutors = Set(Prosecutor)
    sureties = Set(Surety)
    visitors = Set('Visitor')


class PoliceStationType(db.Entity):
    id = PrimaryKey(int, auto=True)
    police_stations = Set(PoliceStation)


class CommitalType(db.Entity):
    id = PrimaryKey(int, auto=True)
    prison_commitals = Set(PrisonCommital)


class Court(db.Entity):
    id = PrimaryKey(int, auto=True)
    court_station = Required(CourtStation)
    judicialofficers = Set(JudicialOfficer)
    hearings = Set(Hearing)


class Payment(db.Entity):
    id = PrimaryKey(int, auto=True)
    AmountPaid = Optional(Decimal, nullable=True, default="0.00")
    DatePaid = Optional(datetime, default=lambda: datetime.now())
    PaymentReference = Optional(str, 80)
    PaymentConfirmed = Optional(bool, default=True)
    PaidBy = Optional(str)
    MSISDN = Optional(str, nullable=True)
    ReceiptNumber = Optional(str, 100)
    IsPartial = Optional(bool, nullable=True, default=False)
    bail = Required(Bail, nullable=True)
    filings = Set(Filing)
    BillRefNumber = Optional(str)
    payment_method = Required('PaymentMethod')
    PaymentDescription = Optional(str)
    case = Required(Case)


class PaymentMethod(db.Entity):
    id = PrimaryKey(int, auto=True)
    payments = Set(Payment)
    Key = Optional(str)
    Secret = Optional(str)
    Portal = Optional(str)
    TillNumber = Optional(str)
    ShortCode = Optional(str)


class JO_Rank(db.Entity):
    id = PrimaryKey(int, auto=True)
    judicial_officers = Set(JudicialOfficer)
    Appelation = Optional(str)
    InformalAddress = Optional(str)


class PoliceRank(db.Entity):
    id = PrimaryKey(int, auto=True)
    police_officers = Set(PoliceOfficer)


class CaseCategory(db.Entity):
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)
    Indictable = Optional(bool)


class Discipline(db.Entity):
    id = PrimaryKey(int, auto=True)
    defendant = Required(Defendant)


class MedEvent(db.Entity):
    _table_ = 'Medevent'
    id = PrimaryKey(int, auto=True)
    defendants = Set(Defendant)


class Warder(db.Entity):
    id = PrimaryKey(int, auto=True)
    prison = Required(Prison)
    prison_commitals = Set(PrisonCommital, nullable=True)
    warder_rank = Required('WarderRank')


class Visitor(db.Entity):
    id = PrimaryKey(int, auto=True)
    gender = Required(Gender)
    visits = Set('Visit')


class Visit(db.Entity):
    vistors = Required(Visitor)
    defendants = Required(Defendant)
    VisitDate = Optional(datetime, default=lambda: datetime.now())
    VisitNotes = Optional(LongStr, nullable=True)
    VisitDuration = Optional(timedelta, nullable=True)
    PrimaryKey(vistors, defendants)


class WarderRank(db.Entity):
    id = PrimaryKey(int, auto=True)
    warders = Set(Warder)


class SecurityRank(db.Entity):
    id = PrimaryKey(int, auto=True)
    prisons = Set(Prison)


class Cell(db.Entity):
    id = PrimaryKey(int, auto=True)
    prison = Required(Prison)
    defendants = Set(Defendant)


db.bind("postgres", host="localhost", user="nyimbi", database="gtmp")
db.generate_mapping(create_tables=True)
