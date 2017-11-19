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
    nature_of_suits = Set('NatureOfSuit')
    plaintiffs = Set('Plaintiff')
    defendants = Set('Defendant')
    police_station_reported = Required('PoliceStation')
    pol_reported_to = Set('PolOfficer', reverse='reports')
    report_date = Required(datetime, default=lambda: datetime.now())
    Complaint = Optional(LongStr)
    case_categories = Set('CaseCategory')
    Priority = Required(int, default=3)
    inv_supervisor = Optional('PolOfficer', reverse='pol_supervisor')
    investigators = Set('PolOfficer', reverse='investigators')
    InvestigationAssigmentDate = Optional(datetime)
    InvestigationAssignmentNote = Optional(LongStr)
    InvestigationPlan = Optional(LongStr)
    investigationDiary = Set('Investigation')
    InvestigationSummary = Optional(LongStr)
    InvestigationReview = Optional(LongStr, nullable=True)
    InvestigationComplete = Optional(bool)
    DPPAdviceRequested = Optional(bool, default=False)
    DPPAdviceDate = Optional(date, default=lambda: date.today())
    advising_prosecutors = Set('Prosecutor', reverse='case_advisors')
    DPPAdvice = Optional(LongStr)
    SendToTrial = Required(bool, default=False)
    CaseName = Optional(str, 400, nullable=True, default="Republic Vs ")
    DocketNumber = Optional(str, 100, nullable=True, default="D/000/000")
    ChargeSheet = Optional(LongStr)
    police_prosecutors = Set('PolOfficer', reverse='prosecutes')
    ChargeDate = Optional(datetime)
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
    CaseClosed = Optional(bool, default=False)
    CloseDate = Optional(date, nullable=True, default=lambda: date.today())
    tags = Set('Tag')


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
    police_station_type = Required('PoliceStationType')
    cases = Set(Case)


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
    prisoncells = Set('PrisonCell')
    GateCount = Optional(int)
    gate_openings = Set('GateRegister')


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
    remandments = Set('PrisonCommital')
    gender = Required('Gender')
    disciplinary = Set('Discipline')
    medical_events = Set('MedEvent')
    visits = Set('Visit')
    prisoncell = Required('PrisonCell')
    CaseCount = Optional(int)
    prisoner_gate_movement = Set('GateRegister')

class MedEvent(db.Entity):
    _table_ = 'Medevent'
    id = PrimaryKey(int, auto=True)
    defendants = Set(Defendant)
    
class PolOfficer(db.Entity):
    """PersonMixin
Rank, ServiceNumber, Specialization, Notes"""
    _table_ = 'PoliceOfficer'
    id = PrimaryKey(int, auto=True)
    police_roles = Set('PoliceRole')
    police_rank = Required('PoliceRank')
    reports = Set(Case, reverse='pol_reported_to')
    prosecutes = Set(Case, reverse='police_prosecutors')
    investigations = Set('Investigation')
    hearings = Set('Hearing')
    gender = Required('Gender')
    ServiceNumber = Optional(str, nullable=True)
    prison_commitals = Set('PrisonCommital')
    supervises = Set('PolOfficer', reverse='reports_to')
    reports_to = Optional('PolOfficer', reverse='supervises')
    pol_supervisor = Required(Case, reverse='inv_supervisor')
    investigators = Set(Case, reverse='investigators')


class PoliceRole(db.Entity):
    """RefTypeMixin
Investigator, Prosecutor, ReportingOfficer, ArrestingOfficer, DetainingOfficer, Supervisor"""
    id = PrimaryKey(int, auto=True)
    polofficers = Set(PolOfficer)


class Prosecutor(db.Entity):
    id = PrimaryKey(int, auto=True)
    prosecutor_teams = Set('ProsecutorTeam')
    case_advisors = Set(Case, reverse='advising_prosecutors')
    hearings = Set('Hearing')
    filings = Set('Filing')
    gender = Optional('Gender')
    case_prosecutor = Set(Case, reverse='prosecutors')


class Lawyers(db.Entity):
    """List of all Laywers"""
    id = PrimaryKey(int, auto=True)
    hearings = Set('Hearing')
    gender = Optional('Gender', nullable=True)
    filings = Set('Filing')
    BarNumber = Optional(str, 20, nullable=True)
    law_firm = Optional('LawFirm')
    AdmissionDate = Optional(date, default=lambda: date.today())


class ProsecutorTeam(db.Entity):
    id = PrimaryKey(int, auto=True)
    prosecutors = Set(Prosecutor)


class LawFirm(db.Entity):
    id = PrimaryKey(int, auto=True)
    lawyer_lawfirm = Set(Lawyers)


class Investigation(db.Entity):
    """PlaceMixin, ActivityMixin
Actions, Finding, InterviewNotes, Interviewees, Forensics"""
    id = PrimaryKey(int, auto=True)
    investigator = Set(PolOfficer)
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
    police_prosecutors = Set(PolOfficer)
    court = Required('Court')
    defendants = Set(Defendant)
    defense_attorneys = Set(Lawyers)
    judicialofficers = Set('JudicialOfficer')
    witnesses = Set(Witness)
    RemandedToPrison = Set('PrisonCommital')
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
    tags = Set('Tag')


class HearingType(db.Entity):
    id = PrimaryKey(int, auto=True)
    hearings = Set(Hearing)


class JudicialOfficer(db.Entity):
    id = PrimaryKey(int, auto=True)
    j_o__rank = Required('JO_Rank')
    hearings = Set(Hearing)
    gender = Optional('Gender')
    court = Required('Court')
    prison_commitals_warrants = Set('PrisonCommital')


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
    filing_attorney = Required(Lawyers)
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
    filing = Required(Filing)
    doc_template = Optional('DocTemplate')
    Confidential = Optional(bool, nullable=True, default=False)
    PageCount = Optional(int)
    Locked = Optional(bool, nullable=True, default=False)
    tags = Set('Tag')
    Hash = Optional(str, nullable=True)


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
    payments = Set('Payment')


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
    WarrantDate = Optional(datetime)
    HasCourtDate = Optional(bool)
    judicial_officer_warrant = Required(JudicialOfficer)
    Warrant = Optional(LongStr)
    WarrantDuration = Required(int)
    WarrantExpiry = Required(datetime)
    History = Optional(LongStr)
    EarliestRelease = Optional(date, nullable=True)
    ReleaseDate = Optional(datetime, nullable=True, default=lambda: datetime.now())
    Property = Optional(LongStr, nullable=True)
    ItemCount = Optional(int, nullable=True, default=0)
    ReleaseNotes = Optional(LongStr, nullable=True)
    CommitalNotes = Optional(LongStr, nullable=True)
    police_officer_commiting = Required(PolOfficer)
    receiving_warders = Set('Warder')
    ParoleDate = Optional(date, nullable=True)
    prisonerproperties = Set('PrisonerProperty')
    remissions = Set('Remission')
    Escaped = Optional(bool, nullable=True)
    EscapeDate = Optional(datetime, nullable=True, default=lambda: datetime.now())
    EscapeDetails = Optional(LongStr, nullable=True)
    PrimaryKey(prison, WarrantNo)


class Gender(db.Entity):
    id = PrimaryKey(int, auto=True)
    Name = Required(str, 20, unique=True)
    lawyer = Set(Lawyers)
    defendants = Set(Defendant)
    judicialofficers = Set(JudicialOfficer)
    witnesses = Set(Witness)
    plaintiffs = Set(Plaintiff)
    polofficers = Set(PolOfficer)
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
    DatePaid = Optional(datetime, default=lambda: datetime.now())
    Amount = Optional(Decimal, nullable=True, default="0.00")
    PaymentReference = Optional(str, 80)
    PaymentConfirmed = Optional(bool, default=True)
    PaidBy = Optional(str)
    MSISDN = Optional(str, nullable=True)
    ReceiptNumber = Optional(str, 100)
    IsPartial = Optional(bool, nullable=True, default=False)
    bail = Required(Bail)
    filings = Set(Filing)
    BillRefNumber = Optional(str)
    payment_method = Required('PaymentMethod')
    PaymentDescription = Optional(str)
    case = Optional(Case)


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
    police_officers = Set(PolOfficer)


class CaseCategory(db.Entity):
    id = PrimaryKey(int, auto=True)
    cases = Set(Case)
    Indictable = Optional(bool)


class Discipline(db.Entity):
    id = PrimaryKey(int, auto=True)
    defendant = Required(Defendant)





class Warder(db.Entity):
    id = PrimaryKey(int, auto=True)
    prison = Required(Prison)
    prison_commitals = Set(PrisonCommital)
    warder_rank = Required('WarderRank')
    supervises = Set('Warder', reverse='reports_to')
    reports_to = Optional('Warder', reverse='supervises')
    gate_registers = Set('GateRegister', reverse='gate_warders')
    warder_gate_access = Set('GateRegister', reverse='warders_movement')


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


class PrisonCell(db.Entity):
    id = PrimaryKey(int, auto=True)
    prison = Required(Prison)
    defendants = Set(Defendant)


class EventLog(db.Entity):
    id = PrimaryKey(int, auto=True)
    Temporal = Required(datetime, nullable=True, default=lambda: datetime.now())
    Event = Optional(LongStr, nullable=True)
    Severity = Optional(int, nullable=True)
    Notes = Optional(LongStr, nullable=True)
    Tbl = Optional(str, nullable=True)
    ColName = Optional(str, nullable=True)
    ColBefore = Optional(str, nullable=True)
    ColAfter = Optional(str, nullable=True)


class DocArchive(db.Entity):
    """For scanned documents"""
    id = PrimaryKey(int, auto=True)
    Name = Optional(str, nullable=True)
    Doc = Optional(LongStr, nullable=True)
    ScanDate = Optional(datetime, nullable=True, default=lambda: datetime.now())
    Archival = Optional(bool, nullable=True)
    tags = Set('Tag')


class Tag(db.Entity):
    id = PrimaryKey(int, auto=True)
    doc_archives = Set(DocArchive)
    documents = Set(Document)
    cases = Set(Case)
    hearings = Set(Hearing)


class PrisonerProperty(db.Entity):
    id = PrimaryKey(int, auto=True)
    prison_commital = Required(PrisonCommital)
    Receipted = Optional(bool)


class Remission(db.Entity):
    id = PrimaryKey(int, auto=True)
    prison_commital = Required(PrisonCommital)
    DaysEarned = Optional(int, nullable=True)
    DateEarned = Optional(date)
    Amount = Optional(Decimal, nullable=True)


class GateRegister(db.Entity):
    id = PrimaryKey(int, auto=True)
    prison = Required(Prison)
    OpenTime = Optional(datetime, default=lambda: datetime.now())
    ClosedTime = Optional(datetime, default=lambda: datetime.now())
    OpenDuration = Optional(timedelta, nullable=True)
    MovementDirection = Optional(bool)
    Reason = Optional(LongStr, nullable=True)
    StaffMovement = Optional(bool)
    GoodsMovement = Optional(LongStr)
    gate_warders = Set(Warder, reverse='gate_registers')
    warders_movement = Set(Warder, reverse='warder_gate_access')
    prisoner_movement = Set(Defendant)
    Vehicle_Reg = Optional(str, nullable=True)
    Vehicle_color = Optional(str)



db.bind("postgres", host="localhost", user="nyimbi", database="gtmp")

db.generate_mapping()
