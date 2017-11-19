CREATE TABLE "case" (
  "id" SERIAL CONSTRAINT "pk_case" PRIMARY KEY,
  "casename" VARCHAR(200) NOT NULL,
  "docketnumber" VARCHAR(100),
  "investigationassigmentdate" TIMESTAMP,
  "investigationassignmentnote" TEXT NOT NULL,
  "investigationplan" TEXT NOT NULL,
  "initialreport" TEXT NOT NULL,
  "priority" INTEGER NOT NULL DEFAULT 3,
  "investigationsummary" TEXT NOT NULL,
  "agadvicerequested" BOOLEAN,
  "sendtotrial" BOOLEAN NOT NULL,
  "chargedate" TIMESTAMP,
  "agadvice" TEXT NOT NULL,
  "taketotrial" BOOLEAN NOT NULL,
  "caseclosed" BOOLEAN,
  "judgement" TEXT NOT NULL,
  "closeddate" DATE,
  "sentencelength" INTEGER,
  "sentencestartdate" DATE,
  "sentenceexpirydate" DATE,
  "fineamount" DOUBLE PRECISION,
  "caseappealed" BOOLEAN,
  "appealdate" TIMESTAMP
);

CREATE TABLE "causeofaction" (
  "id" SERIAL CONSTRAINT "pk_causeofaction" PRIMARY KEY,
  "criminal" BOOLEAN NOT NULL,
  "parent_coa" INTEGER
);

CREATE INDEX "idx_causeofaction__parent_coa" ON "causeofaction" ("parent_coa");

ALTER TABLE "causeofaction" ADD CONSTRAINT "fk_causeofaction__parent_coa" FOREIGN KEY ("parent_coa") REFERENCES "causeofaction" ("id");

CREATE TABLE "case_causes_of_action" (
  "case" INTEGER NOT NULL,
  "causeofaction" INTEGER NOT NULL,
  CONSTRAINT "pk_case_causes_of_action" PRIMARY KEY ("case", "causeofaction")
);

CREATE INDEX "idx_case_causes_of_action" ON "case_causes_of_action" ("causeofaction");

ALTER TABLE "case_causes_of_action" ADD CONSTRAINT "fk_case_causes_of_action__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_causes_of_action" ADD CONSTRAINT "fk_case_causes_of_action__causeofaction" FOREIGN KEY ("causeofaction") REFERENCES "causeofaction" ("id");

CREATE TABLE "commitaltype" (
  "id" SERIAL CONSTRAINT "pk_commitaltype" PRIMARY KEY
);

CREATE TABLE "county" (
  "id" SERIAL CONSTRAINT "pk_county" PRIMARY KEY
);

CREATE TABLE "courtlevel" (
  "id" SERIAL CONSTRAINT "pk_courtlevel" PRIMARY KEY
);

CREATE TABLE "doctemplate" (
  "id" SERIAL CONSTRAINT "pk_doctemplate" PRIMARY KEY
);

CREATE TABLE "document" (
  "id" SERIAL CONSTRAINT "pk_document" PRIMARY KEY,
  "doc_template" INTEGER
);

CREATE INDEX "idx_document__doc_template" ON "document" ("doc_template");

ALTER TABLE "document" ADD CONSTRAINT "fk_document__doc_template" FOREIGN KEY ("doc_template") REFERENCES "doctemplate" ("id");

CREATE TABLE "filingtype" (
  "id" SERIAL CONSTRAINT "pk_filingtype" PRIMARY KEY,
  "cost" DECIMAL(12, 2) NOT NULL,
  "perpagecost" DECIMAL(12, 2),
  "paid_per_page" BOOLEAN DEFAULT true
);

CREATE TABLE "gender" (
  "id" SERIAL CONSTRAINT "pk_gender" PRIMARY KEY,
  "name" VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE "Policeman" (
  "id" SERIAL CONSTRAINT "pk_policeman" PRIMARY KEY,
  "gender" INTEGER NOT NULL
);

CREATE INDEX "idx_policeman__gender" ON "Policeman" ("gender");

ALTER TABLE "Policeman" ADD CONSTRAINT "fk_policeman__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "case_police_prosecutors" (
  "case" INTEGER NOT NULL,
  "policeofficer" INTEGER NOT NULL,
  CONSTRAINT "pk_case_police_prosecutors" PRIMARY KEY ("case", "policeofficer")
);

CREATE INDEX "idx_case_police_prosecutors" ON "case_police_prosecutors" ("policeofficer");

ALTER TABLE "case_police_prosecutors" ADD CONSTRAINT "fk_case_police_prosecutors__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_police_prosecutors" ADD CONSTRAINT "fk_case_police_prosecutors__policeofficer" FOREIGN KEY ("policeofficer") REFERENCES "Policeman" ("id");

CREATE TABLE "case_reported_to_policeman" (
  "case" INTEGER NOT NULL,
  "policeofficer" INTEGER NOT NULL,
  CONSTRAINT "pk_case_reported_to_policeman" PRIMARY KEY ("case", "policeofficer")
);

CREATE INDEX "idx_case_reported_to_policeman" ON "case_reported_to_policeman" ("policeofficer");

ALTER TABLE "case_reported_to_policeman" ADD CONSTRAINT "fk_case_reported_to_policeman__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_reported_to_policeman" ADD CONSTRAINT "fk_case_reported_to_policeman__policeofficer" FOREIGN KEY ("policeofficer") REFERENCES "Policeman" ("id");

CREATE TABLE "defendant" (
  "id" SERIAL CONSTRAINT "pk_defendant" PRIMARY KEY,
  "gender" INTEGER NOT NULL
);

CREATE INDEX "idx_defendant__gender" ON "defendant" ("gender");

ALTER TABLE "defendant" ADD CONSTRAINT "fk_defendant__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "case_defendants" (
  "case" INTEGER NOT NULL,
  "defendant" INTEGER NOT NULL,
  CONSTRAINT "pk_case_defendants" PRIMARY KEY ("case", "defendant")
);

CREATE INDEX "idx_case_defendants" ON "case_defendants" ("defendant");

ALTER TABLE "case_defendants" ADD CONSTRAINT "fk_case_defendants__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_defendants" ADD CONSTRAINT "fk_case_defendants__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

CREATE TABLE "hearingtype" (
  "id" SERIAL CONSTRAINT "pk_hearingtype" PRIMARY KEY
);

CREATE TABLE "investigation" (
  "id" SERIAL CONSTRAINT "pk_investigation" PRIMARY KEY,
  "case" INTEGER NOT NULL,
  "actiondate" TIMESTAMP NOT NULL,
  "evidence" TEXT NOT NULL,
  "narrative" TEXT NOT NULL,
  "weather" TEXT NOT NULL,
  "location" TEXT NOT NULL
);

CREATE INDEX "idx_investigation__case" ON "investigation" ("case");

ALTER TABLE "investigation" ADD CONSTRAINT "fk_investigation__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

CREATE TABLE "investigation_investigator" (
  "policeofficer" INTEGER NOT NULL,
  "investigation" INTEGER NOT NULL,
  CONSTRAINT "pk_investigation_investigator" PRIMARY KEY ("policeofficer", "investigation")
);

CREATE INDEX "idx_investigation_investigator" ON "investigation_investigator" ("investigation");

ALTER TABLE "investigation_investigator" ADD CONSTRAINT "fk_investigation_investigator__investigation" FOREIGN KEY ("investigation") REFERENCES "investigation" ("id");

ALTER TABLE "investigation_investigator" ADD CONSTRAINT "fk_investigation_investigator__policeofficer" FOREIGN KEY ("policeofficer") REFERENCES "Policeman" ("id");

CREATE TABLE "lawfirm" (
  "id" SERIAL CONSTRAINT "pk_lawfirm" PRIMARY KEY
);

CREATE TABLE "attorney" (
  "id" SERIAL CONSTRAINT "pk_attorney" PRIMARY KEY,
  "law_firm" INTEGER,
  "barnumber" VARCHAR(20),
  "gender" INTEGER
);

CREATE INDEX "idx_attorney__gender" ON "attorney" ("gender");

CREATE INDEX "idx_attorney__law_firm" ON "attorney" ("law_firm");

ALTER TABLE "attorney" ADD CONSTRAINT "fk_attorney__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

ALTER TABLE "attorney" ADD CONSTRAINT "fk_attorney__law_firm" FOREIGN KEY ("law_firm") REFERENCES "lawfirm" ("id");

CREATE TABLE "natureofsuit" (
  "id" SERIAL CONSTRAINT "pk_natureofsuit" PRIMARY KEY
);

CREATE TABLE "case_nature_of_suits" (
  "case" INTEGER NOT NULL,
  "natureofsuit" INTEGER NOT NULL,
  CONSTRAINT "pk_case_nature_of_suits" PRIMARY KEY ("case", "natureofsuit")
);

CREATE INDEX "idx_case_nature_of_suits" ON "case_nature_of_suits" ("natureofsuit");

ALTER TABLE "case_nature_of_suits" ADD CONSTRAINT "fk_case_nature_of_suits__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_nature_of_suits" ADD CONSTRAINT "fk_case_nature_of_suits__natureofsuit" FOREIGN KEY ("natureofsuit") REFERENCES "natureofsuit" ("id");

CREATE TABLE "observer" (
  "id" SERIAL CONSTRAINT "pk_observer" PRIMARY KEY,
  "fordefense" BOOLEAN,
  "gender" INTEGER NOT NULL
);

CREATE INDEX "idx_observer__gender" ON "observer" ("gender");

ALTER TABLE "observer" ADD CONSTRAINT "fk_observer__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "case_observers" (
  "case" INTEGER NOT NULL,
  "observer" INTEGER NOT NULL,
  CONSTRAINT "pk_case_observers" PRIMARY KEY ("case", "observer")
);

CREATE INDEX "idx_case_observers" ON "case_observers" ("observer");

ALTER TABLE "case_observers" ADD CONSTRAINT "fk_case_observers__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_observers" ADD CONSTRAINT "fk_case_observers__observer" FOREIGN KEY ("observer") REFERENCES "observer" ("id");

CREATE TABLE "investigation_observers" (
  "investigation" INTEGER NOT NULL,
  "observer" INTEGER NOT NULL,
  CONSTRAINT "pk_investigation_observers" PRIMARY KEY ("investigation", "observer")
);

CREATE INDEX "idx_investigation_observers" ON "investigation_observers" ("observer");

ALTER TABLE "investigation_observers" ADD CONSTRAINT "fk_investigation_observers__investigation" FOREIGN KEY ("investigation") REFERENCES "investigation" ("id");

ALTER TABLE "investigation_observers" ADD CONSTRAINT "fk_investigation_observers__observer" FOREIGN KEY ("observer") REFERENCES "observer" ("id");

CREATE TABLE "plaintiff" (
  "id" SERIAL CONSTRAINT "pk_plaintiff" PRIMARY KEY,
  "gender" INTEGER
);

CREATE INDEX "idx_plaintiff__gender" ON "plaintiff" ("gender");

ALTER TABLE "plaintiff" ADD CONSTRAINT "fk_plaintiff__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "case_plaintiffs" (
  "case" INTEGER NOT NULL,
  "plaintiff" INTEGER NOT NULL,
  CONSTRAINT "pk_case_plaintiffs" PRIMARY KEY ("case", "plaintiff")
);

CREATE INDEX "idx_case_plaintiffs" ON "case_plaintiffs" ("plaintiff");

ALTER TABLE "case_plaintiffs" ADD CONSTRAINT "fk_case_plaintiffs__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_plaintiffs" ADD CONSTRAINT "fk_case_plaintiffs__plaintiff" FOREIGN KEY ("plaintiff") REFERENCES "plaintiff" ("id");

CREATE TABLE "policerole" (
  "id" SERIAL CONSTRAINT "pk_policerole" PRIMARY KEY
);

CREATE TABLE "policeofficer_police_roles" (
  "policeofficer" INTEGER NOT NULL,
  "policerole" INTEGER NOT NULL,
  CONSTRAINT "pk_policeofficer_police_roles" PRIMARY KEY ("policeofficer", "policerole")
);

CREATE INDEX "idx_policeofficer_police_roles" ON "policeofficer_police_roles" ("policerole");

ALTER TABLE "policeofficer_police_roles" ADD CONSTRAINT "fk_policeofficer_police_roles__policeofficer" FOREIGN KEY ("policeofficer") REFERENCES "Policeman" ("id");

ALTER TABLE "policeofficer_police_roles" ADD CONSTRAINT "fk_policeofficer_police_roles__policerole" FOREIGN KEY ("policerole") REFERENCES "policerole" ("id");

CREATE TABLE "policestationtype" (
  "id" SERIAL CONSTRAINT "pk_policestationtype" PRIMARY KEY
);

CREATE TABLE "prosecutor" (
  "id" SERIAL CONSTRAINT "pk_prosecutor" PRIMARY KEY,
  "gender" INTEGER
);

CREATE INDEX "idx_prosecutor__gender" ON "prosecutor" ("gender");

ALTER TABLE "prosecutor" ADD CONSTRAINT "fk_prosecutor__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "case_advising_prosecutors" (
  "case" INTEGER NOT NULL,
  "prosecutor" INTEGER NOT NULL,
  CONSTRAINT "pk_case_advising_prosecutors" PRIMARY KEY ("case", "prosecutor")
);

CREATE INDEX "idx_case_advising_prosecutors" ON "case_advising_prosecutors" ("prosecutor");

ALTER TABLE "case_advising_prosecutors" ADD CONSTRAINT "fk_case_advising_prosecutors__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_advising_prosecutors" ADD CONSTRAINT "fk_case_advising_prosecutors__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "filing" (
  "id" SERIAL CONSTRAINT "pk_filing" PRIMARY KEY,
  "filedate" TIMESTAMP,
  "totalfees" DECIMAL(12, 2) NOT NULL,
  "filing_attorney" INTEGER NOT NULL,
  "filing_prosecutor" INTEGER NOT NULL,
  "receiptnumber" TEXT,
  "receiptverified" BOOLEAN,
  "amountpaid" DECIMAL(12, 2),
  "feebalance" DECIMAL(12, 2),
  "paymenthistory" TEXT NOT NULL
);

CREATE INDEX "idx_filing__filing_attorney" ON "filing" ("filing_attorney");

CREATE INDEX "idx_filing__filing_prosecutor" ON "filing" ("filing_prosecutor");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__filing_attorney" FOREIGN KEY ("filing_attorney") REFERENCES "attorney" ("id");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__filing_prosecutor" FOREIGN KEY ("filing_prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "causeofaction_filings" (
  "causeofaction" INTEGER NOT NULL,
  "filing" INTEGER NOT NULL,
  CONSTRAINT "pk_causeofaction_filings" PRIMARY KEY ("causeofaction", "filing")
);

CREATE INDEX "idx_causeofaction_filings" ON "causeofaction_filings" ("filing");

ALTER TABLE "causeofaction_filings" ADD CONSTRAINT "fk_causeofaction_filings__causeofaction" FOREIGN KEY ("causeofaction") REFERENCES "causeofaction" ("id");

ALTER TABLE "causeofaction_filings" ADD CONSTRAINT "fk_causeofaction_filings__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

CREATE TABLE "document_filings" (
  "filing" INTEGER NOT NULL,
  "document" INTEGER NOT NULL,
  CONSTRAINT "pk_document_filings" PRIMARY KEY ("filing", "document")
);

CREATE INDEX "idx_document_filings" ON "document_filings" ("document");

ALTER TABLE "document_filings" ADD CONSTRAINT "fk_document_filings__document" FOREIGN KEY ("document") REFERENCES "document" ("id");

ALTER TABLE "document_filings" ADD CONSTRAINT "fk_document_filings__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

CREATE TABLE "filing_filing_types" (
  "filing" INTEGER NOT NULL,
  "filingtype" INTEGER NOT NULL,
  CONSTRAINT "pk_filing_filing_types" PRIMARY KEY ("filing", "filingtype")
);

CREATE INDEX "idx_filing_filing_types" ON "filing_filing_types" ("filingtype");

ALTER TABLE "filing_filing_types" ADD CONSTRAINT "fk_filing_filing_types__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

ALTER TABLE "filing_filing_types" ADD CONSTRAINT "fk_filing_filing_types__filingtype" FOREIGN KEY ("filingtype") REFERENCES "filingtype" ("id");

CREATE TABLE "prosecutorteam" (
  "id" SERIAL CONSTRAINT "pk_prosecutorteam" PRIMARY KEY
);

CREATE TABLE "prosecutor_prosecutor_teams" (
  "prosecutor" INTEGER NOT NULL,
  "prosecutorteam" INTEGER NOT NULL,
  CONSTRAINT "pk_prosecutor_prosecutor_teams" PRIMARY KEY ("prosecutor", "prosecutorteam")
);

CREATE INDEX "idx_prosecutor_prosecutor_teams" ON "prosecutor_prosecutor_teams" ("prosecutorteam");

ALTER TABLE "prosecutor_prosecutor_teams" ADD CONSTRAINT "fk_prosecutor_prosecutor_teams__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

ALTER TABLE "prosecutor_prosecutor_teams" ADD CONSTRAINT "fk_prosecutor_prosecutor_teams__prosecutorteam" FOREIGN KEY ("prosecutorteam") REFERENCES "prosecutorteam" ("id");

CREATE TABLE "subcounty" (
  "id" SERIAL CONSTRAINT "pk_subcounty" PRIMARY KEY,
  "county" INTEGER NOT NULL
);

CREATE INDEX "idx_subcounty__county" ON "subcounty" ("county");

ALTER TABLE "subcounty" ADD CONSTRAINT "fk_subcounty__county" FOREIGN KEY ("county") REFERENCES "county" ("id");

CREATE TABLE "surety" (
  "id" SERIAL CONSTRAINT "pk_surety" PRIMARY KEY,
  "gender" INTEGER
);

CREATE INDEX "idx_surety__gender" ON "surety" ("gender");

ALTER TABLE "surety" ADD CONSTRAINT "fk_surety__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "town" (
  "id" SERIAL CONSTRAINT "pk_town" PRIMARY KEY,
  "subcounty" INTEGER NOT NULL
);

CREATE INDEX "idx_town__subcounty" ON "town" ("subcounty");

ALTER TABLE "town" ADD CONSTRAINT "fk_town__subcounty" FOREIGN KEY ("subcounty") REFERENCES "subcounty" ("id");

CREATE TABLE "constituency" (
  "id" SERIAL CONSTRAINT "pk_constituency" PRIMARY KEY,
  "county" INTEGER NOT NULL,
  "town" INTEGER
);

CREATE INDEX "idx_constituency__county" ON "constituency" ("county");

CREATE INDEX "idx_constituency__town" ON "constituency" ("town");

ALTER TABLE "constituency" ADD CONSTRAINT "fk_constituency__county" FOREIGN KEY ("county") REFERENCES "county" ("id");

ALTER TABLE "constituency" ADD CONSTRAINT "fk_constituency__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "courtstation" (
  "id" SERIAL CONSTRAINT "pk_courtstation" PRIMARY KEY,
  "town" INTEGER NOT NULL,
  "residentmagistrate" VARCHAR(100),
  "registrar" VARCHAR(100) NOT NULL,
  "court_level" INTEGER NOT NULL
);

CREATE INDEX "idx_courtstation__court_level" ON "courtstation" ("court_level");

CREATE INDEX "idx_courtstation__town" ON "courtstation" ("town");

ALTER TABLE "courtstation" ADD CONSTRAINT "fk_courtstation__court_level" FOREIGN KEY ("court_level") REFERENCES "courtlevel" ("id");

ALTER TABLE "courtstation" ADD CONSTRAINT "fk_courtstation__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "hearing" (
  "id" SERIAL CONSTRAINT "pk_hearing" PRIMARY KEY,
  "hearingdate" TIMESTAMP NOT NULL,
  "adjourned" BOOLEAN,
  "case" INTEGER NOT NULL,
  "courtstation" INTEGER NOT NULL,
  "hearing_type" INTEGER NOT NULL,
  "remandwarrant" TEXT NOT NULL,
  "remandlength" INTEGER,
  "remanddate" DATE,
  "remandwarrantexpirydate" DATE,
  "nexthearingdate" DATE,
  "finalhearing" BOOLEAN NOT NULL,
  "transcript" TEXT NOT NULL,
  "audio" BYTEA,
  "video" BYTEA
);

CREATE INDEX "idx_hearing__case" ON "hearing" ("case");

CREATE INDEX "idx_hearing__courtstation" ON "hearing" ("courtstation");

CREATE INDEX "idx_hearing__hearing_type" ON "hearing" ("hearing_type");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__courtstation" FOREIGN KEY ("courtstation") REFERENCES "courtstation" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__hearing_type" FOREIGN KEY ("hearing_type") REFERENCES "hearingtype" ("id");

CREATE TABLE "attorney_hearings" (
  "attorney" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_attorney_hearings" PRIMARY KEY ("attorney", "hearing")
);

CREATE INDEX "idx_attorney_hearings" ON "attorney_hearings" ("hearing");

ALTER TABLE "attorney_hearings" ADD CONSTRAINT "fk_attorney_hearings__attorney" FOREIGN KEY ("attorney") REFERENCES "attorney" ("id");

ALTER TABLE "attorney_hearings" ADD CONSTRAINT "fk_attorney_hearings__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "bail" (
  "id" SERIAL CONSTRAINT "pk_bail" PRIMARY KEY,
  "hearing" INTEGER NOT NULL,
  "defendant" INTEGER NOT NULL,
  "amountgranted" DECIMAL(12, 2),
  "noofsureties" INTEGER NOT NULL,
  "paid" BOOLEAN,
  "paydate" DATE,
  "receiptno" VARCHAR(100) NOT NULL
);

CREATE INDEX "idx_bail__defendant" ON "bail" ("defendant");

CREATE INDEX "idx_bail__hearing" ON "bail" ("hearing");

ALTER TABLE "bail" ADD CONSTRAINT "fk_bail__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

ALTER TABLE "bail" ADD CONSTRAINT "fk_bail__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "bail_sureties" (
  "bail" INTEGER NOT NULL,
  "surety" INTEGER NOT NULL,
  CONSTRAINT "pk_bail_sureties" PRIMARY KEY ("bail", "surety")
);

CREATE INDEX "idx_bail_sureties" ON "bail_sureties" ("surety");

ALTER TABLE "bail_sureties" ADD CONSTRAINT "fk_bail_sureties__bail" FOREIGN KEY ("bail") REFERENCES "bail" ("id");

ALTER TABLE "bail_sureties" ADD CONSTRAINT "fk_bail_sureties__surety" FOREIGN KEY ("surety") REFERENCES "surety" ("id");

CREATE TABLE "causeofaction_hearings" (
  "hearing" INTEGER NOT NULL,
  "causeofaction" INTEGER NOT NULL,
  CONSTRAINT "pk_causeofaction_hearings" PRIMARY KEY ("hearing", "causeofaction")
);

CREATE INDEX "idx_causeofaction_hearings" ON "causeofaction_hearings" ("causeofaction");

ALTER TABLE "causeofaction_hearings" ADD CONSTRAINT "fk_causeofaction_hearings__causeofaction" FOREIGN KEY ("causeofaction") REFERENCES "causeofaction" ("id");

ALTER TABLE "causeofaction_hearings" ADD CONSTRAINT "fk_causeofaction_hearings__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "defendant_hearings" (
  "defendant" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_defendant_hearings" PRIMARY KEY ("defendant", "hearing")
);

CREATE INDEX "idx_defendant_hearings" ON "defendant_hearings" ("hearing");

ALTER TABLE "defendant_hearings" ADD CONSTRAINT "fk_defendant_hearings__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

ALTER TABLE "defendant_hearings" ADD CONSTRAINT "fk_defendant_hearings__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "filing_hearings" (
  "hearing" INTEGER NOT NULL,
  "filing" INTEGER NOT NULL,
  CONSTRAINT "pk_filing_hearings" PRIMARY KEY ("hearing", "filing")
);

CREATE INDEX "idx_filing_hearings" ON "filing_hearings" ("filing");

ALTER TABLE "filing_hearings" ADD CONSTRAINT "fk_filing_hearings__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

ALTER TABLE "filing_hearings" ADD CONSTRAINT "fk_filing_hearings__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "hearing_observers" (
  "observer" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_observers" PRIMARY KEY ("observer", "hearing")
);

CREATE INDEX "idx_hearing_observers" ON "hearing_observers" ("hearing");

ALTER TABLE "hearing_observers" ADD CONSTRAINT "fk_hearing_observers__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_observers" ADD CONSTRAINT "fk_hearing_observers__observer" FOREIGN KEY ("observer") REFERENCES "observer" ("id");

CREATE TABLE "hearing_police_prosecutors" (
  "policeofficer" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_police_prosecutors" PRIMARY KEY ("policeofficer", "hearing")
);

CREATE INDEX "idx_hearing_police_prosecutors" ON "hearing_police_prosecutors" ("hearing");

ALTER TABLE "hearing_police_prosecutors" ADD CONSTRAINT "fk_hearing_police_prosecutors__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_police_prosecutors" ADD CONSTRAINT "fk_hearing_police_prosecutors__policeofficer" FOREIGN KEY ("policeofficer") REFERENCES "Policeman" ("id");

CREATE TABLE "hearing_prosecutors" (
  "prosecutor" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_prosecutors" PRIMARY KEY ("prosecutor", "hearing")
);

CREATE INDEX "idx_hearing_prosecutors" ON "hearing_prosecutors" ("hearing");

ALTER TABLE "hearing_prosecutors" ADD CONSTRAINT "fk_hearing_prosecutors__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_prosecutors" ADD CONSTRAINT "fk_hearing_prosecutors__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "judge" (
  "id" SERIAL CONSTRAINT "pk_judge" PRIMARY KEY,
  "courtstation" INTEGER NOT NULL,
  "gender" INTEGER
);

CREATE INDEX "idx_judge__courtstation" ON "judge" ("courtstation");

CREATE INDEX "idx_judge__gender" ON "judge" ("gender");

ALTER TABLE "judge" ADD CONSTRAINT "fk_judge__courtstation" FOREIGN KEY ("courtstation") REFERENCES "courtstation" ("id");

ALTER TABLE "judge" ADD CONSTRAINT "fk_judge__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "hearing_judges" (
  "hearing" INTEGER NOT NULL,
  "judge" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_judges" PRIMARY KEY ("hearing", "judge")
);

CREATE INDEX "idx_hearing_judges" ON "hearing_judges" ("judge");

ALTER TABLE "hearing_judges" ADD CONSTRAINT "fk_hearing_judges__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_judges" ADD CONSTRAINT "fk_hearing_judges__judge" FOREIGN KEY ("judge") REFERENCES "judge" ("id");

CREATE TABLE "policestation" (
  "id" SERIAL CONSTRAINT "pk_policestation" PRIMARY KEY,
  "town" INTEGER NOT NULL,
  "officercommanding" VARCHAR(100),
  "police_station_type" INTEGER NOT NULL
);

CREATE INDEX "idx_policestation__police_station_type" ON "policestation" ("police_station_type");

CREATE INDEX "idx_policestation__town" ON "policestation" ("town");

ALTER TABLE "policestation" ADD CONSTRAINT "fk_policestation__police_station_type" FOREIGN KEY ("police_station_type") REFERENCES "policestationtype" ("id");

ALTER TABLE "policestation" ADD CONSTRAINT "fk_policestation__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "case_reported_to_police_stations" (
  "case" INTEGER NOT NULL,
  "policestation" INTEGER NOT NULL,
  CONSTRAINT "pk_case_reported_to_police_stations" PRIMARY KEY ("case", "policestation")
);

CREATE INDEX "idx_case_reported_to_police_stations" ON "case_reported_to_police_stations" ("policestation");

ALTER TABLE "case_reported_to_police_stations" ADD CONSTRAINT "fk_case_reported_to_police_stations__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_reported_to_police_stations" ADD CONSTRAINT "fk_case_reported_to_police_stations__policestation" FOREIGN KEY ("policestation") REFERENCES "policestation" ("id");

CREATE TABLE "prison" (
  "id" SERIAL CONSTRAINT "pk_prison" PRIMARY KEY,
  "town" INTEGER NOT NULL,
  "warden" VARCHAR(100),
  "capacity" INTEGER,
  "population" INTEGER
);

CREATE INDEX "idx_prison__town" ON "prison" ("town");

ALTER TABLE "prison" ADD CONSTRAINT "fk_prison__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "prisoncommital" (
  "prison" INTEGER NOT NULL,
  "warrantno" VARCHAR(100) NOT NULL,
  "hearing" INTEGER NOT NULL,
  "defendant" INTEGER NOT NULL,
  "warrantduration" INTEGER NOT NULL,
  "warrantdate" TIMESTAMP,
  "warrant" TEXT NOT NULL,
  "warrantexpiry" TIMESTAMP NOT NULL,
  "history" TEXT NOT NULL,
  "earliestrelease" DATE,
  CONSTRAINT "pk_prisoncommital" PRIMARY KEY ("prison", "warrantno")
);

CREATE INDEX "idx_prisoncommital__defendant" ON "prisoncommital" ("defendant");

CREATE INDEX "idx_prisoncommital__hearing" ON "prisoncommital" ("hearing");

ALTER TABLE "prisoncommital" ADD CONSTRAINT "fk_prisoncommital__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

ALTER TABLE "prisoncommital" ADD CONSTRAINT "fk_prisoncommital__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "prisoncommital" ADD CONSTRAINT "fk_prisoncommital__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

CREATE TABLE "commitaltype_prison_commitals" (
  "prisoncommital_prison" INTEGER NOT NULL,
  "prisoncommital_warrantno" VARCHAR(100) NOT NULL,
  "commitaltype" INTEGER NOT NULL,
  CONSTRAINT "pk_commitaltype_prison_commitals" PRIMARY KEY ("prisoncommital_prison", "prisoncommital_warrantno", "commitaltype")
);

CREATE INDEX "idx_commitaltype_prison_commitals" ON "commitaltype_prison_commitals" ("commitaltype");

ALTER TABLE "commitaltype_prison_commitals" ADD CONSTRAINT "fk_commitaltype_prison_commitals__commitaltype" FOREIGN KEY ("commitaltype") REFERENCES "commitaltype" ("id");

ALTER TABLE "commitaltype_prison_commitals" ADD CONSTRAINT "fk_commitaltype_prison_commitals__prisoncommital_priso_c449d31c" FOREIGN KEY ("prisoncommital_prison", "prisoncommital_warrantno") REFERENCES "prisoncommital" ("prison", "warrantno")



