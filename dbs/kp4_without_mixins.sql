CREATE TABLE "Medevent" (
  "id" SERIAL CONSTRAINT "pk_medevent" PRIMARY KEY
);

CREATE TABLE "casecategory" (
  "id" SERIAL CONSTRAINT "pk_casecategory" PRIMARY KEY,
  "indictable" BOOLEAN
);

CREATE TABLE "causeofaction" (
  "id" SERIAL CONSTRAINT "pk_causeofaction" PRIMARY KEY,
  "criminal" BOOLEAN NOT NULL,
  "parent_coa" INTEGER
);

CREATE INDEX "idx_causeofaction__parent_coa" ON "causeofaction" ("parent_coa");

ALTER TABLE "causeofaction" ADD CONSTRAINT "fk_causeofaction__parent_coa" FOREIGN KEY ("parent_coa") REFERENCES "causeofaction" ("id");

CREATE TABLE "commitaltype" (
  "id" SERIAL CONSTRAINT "pk_commitaltype" PRIMARY KEY
);

CREATE TABLE "county" (
  "id" SERIAL CONSTRAINT "pk_county" PRIMARY KEY
);

CREATE TABLE "courtlevel" (
  "id" SERIAL CONSTRAINT "pk_courtlevel" PRIMARY KEY
);

CREATE TABLE "docarchive" (
  "id" SERIAL CONSTRAINT "pk_docarchive" PRIMARY KEY,
  "name" TEXT,
  "doc" TEXT,
  "scandate" TIMESTAMP,
  "archival" BOOLEAN
);

CREATE TABLE "doctemplate" (
  "id" SERIAL CONSTRAINT "pk_doctemplate" PRIMARY KEY
);

CREATE TABLE "eventlog" (
  "id" SERIAL CONSTRAINT "pk_eventlog" PRIMARY KEY,
  "temporal" TIMESTAMP,
  "event" TEXT,
  "severity" INTEGER,
  "notes" TEXT,
  "tbl" TEXT,
  "colname" TEXT,
  "colbefore" TEXT,
  "colafter" TEXT
);

CREATE TABLE "filingtype" (
  "id" SERIAL CONSTRAINT "pk_filingtype" PRIMARY KEY,
  "fees" DECIMAL(12, 2),
  "perpagecost" DECIMAL(12, 2),
  "paid_per_page" BOOLEAN
);

CREATE TABLE "gender" (
  "id" SERIAL CONSTRAINT "pk_gender" PRIMARY KEY,
  "name" VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE "hearingtype" (
  "id" SERIAL CONSTRAINT "pk_hearingtype" PRIMARY KEY
);

CREATE TABLE "jo_rank" (
  "id" SERIAL CONSTRAINT "pk_jo_rank" PRIMARY KEY,
  "appelation" TEXT NOT NULL,
  "informaladdress" TEXT NOT NULL
);

CREATE TABLE "lawfirm" (
  "id" SERIAL CONSTRAINT "pk_lawfirm" PRIMARY KEY
);

CREATE TABLE "lawyers" (
  "id" SERIAL CONSTRAINT "pk_lawyers" PRIMARY KEY,
  "gender" INTEGER,
  "barnumber" VARCHAR(20),
  "law_firm" INTEGER,
  "admissiondate" DATE
);

CREATE INDEX "idx_lawyers__gender" ON "lawyers" ("gender");

CREATE INDEX "idx_lawyers__law_firm" ON "lawyers" ("law_firm");

ALTER TABLE "lawyers" ADD CONSTRAINT "fk_lawyers__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

ALTER TABLE "lawyers" ADD CONSTRAINT "fk_lawyers__law_firm" FOREIGN KEY ("law_firm") REFERENCES "lawfirm" ("id");

CREATE TABLE "natureofsuit" (
  "id" SERIAL CONSTRAINT "pk_natureofsuit" PRIMARY KEY
);

CREATE TABLE "paymentmethod" (
  "id" SERIAL CONSTRAINT "pk_paymentmethod" PRIMARY KEY,
  "key" TEXT NOT NULL,
  "secret" TEXT NOT NULL,
  "portal" TEXT NOT NULL,
  "tillnumber" TEXT NOT NULL,
  "shortcode" TEXT NOT NULL
);

CREATE TABLE "plaintiff" (
  "id" SERIAL CONSTRAINT "pk_plaintiff" PRIMARY KEY,
  "gender" INTEGER,
  "juvenile" BOOLEAN
);

CREATE INDEX "idx_plaintiff__gender" ON "plaintiff" ("gender");

ALTER TABLE "plaintiff" ADD CONSTRAINT "fk_plaintiff__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "policerank" (
  "id" SERIAL CONSTRAINT "pk_policerank" PRIMARY KEY
);

CREATE TABLE "policerole" (
  "id" SERIAL CONSTRAINT "pk_policerole" PRIMARY KEY
);

CREATE TABLE "policestationtype" (
  "id" SERIAL CONSTRAINT "pk_policestationtype" PRIMARY KEY
);

CREATE TABLE "prosecutor" (
  "id" SERIAL CONSTRAINT "pk_prosecutor" PRIMARY KEY,
  "gender" INTEGER
);

CREATE INDEX "idx_prosecutor__gender" ON "prosecutor" ("gender");

ALTER TABLE "prosecutor" ADD CONSTRAINT "fk_prosecutor__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

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

CREATE TABLE "securityrank" (
  "id" SERIAL CONSTRAINT "pk_securityrank" PRIMARY KEY
);

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

CREATE TABLE "tag" (
  "id" SERIAL CONSTRAINT "pk_tag" PRIMARY KEY
);

CREATE TABLE "docarchive_tags" (
  "docarchive" INTEGER NOT NULL,
  "tag" INTEGER NOT NULL,
  CONSTRAINT "pk_docarchive_tags" PRIMARY KEY ("docarchive", "tag")
);

CREATE INDEX "idx_docarchive_tags" ON "docarchive_tags" ("tag");

ALTER TABLE "docarchive_tags" ADD CONSTRAINT "fk_docarchive_tags__docarchive" FOREIGN KEY ("docarchive") REFERENCES "docarchive" ("id");

ALTER TABLE "docarchive_tags" ADD CONSTRAINT "fk_docarchive_tags__tag" FOREIGN KEY ("tag") REFERENCES "tag" ("id");

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
  "residentmagistrate" VARCHAR(100),
  "registrar" VARCHAR(100) NOT NULL,
  "court_level" INTEGER NOT NULL,
  "num_of_courts" INTEGER DEFAULT 1,
  "town" INTEGER NOT NULL
);

CREATE INDEX "idx_courtstation__court_level" ON "courtstation" ("court_level");

CREATE INDEX "idx_courtstation__town" ON "courtstation" ("town");

ALTER TABLE "courtstation" ADD CONSTRAINT "fk_courtstation__court_level" FOREIGN KEY ("court_level") REFERENCES "courtlevel" ("id");

ALTER TABLE "courtstation" ADD CONSTRAINT "fk_courtstation__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "court" (
  "id" SERIAL CONSTRAINT "pk_court" PRIMARY KEY,
  "court_station" INTEGER NOT NULL
);

CREATE INDEX "idx_court__court_station" ON "court" ("court_station");

ALTER TABLE "court" ADD CONSTRAINT "fk_court__court_station" FOREIGN KEY ("court_station") REFERENCES "courtstation" ("id");

CREATE TABLE "judicialofficer" (
  "id" SERIAL CONSTRAINT "pk_judicialofficer" PRIMARY KEY,
  "j_o__rank" INTEGER NOT NULL,
  "gender" INTEGER,
  "court" INTEGER NOT NULL
);

CREATE INDEX "idx_judicialofficer__court" ON "judicialofficer" ("court");

CREATE INDEX "idx_judicialofficer__gender" ON "judicialofficer" ("gender");

CREATE INDEX "idx_judicialofficer__j_o__rank" ON "judicialofficer" ("j_o__rank");

ALTER TABLE "judicialofficer" ADD CONSTRAINT "fk_judicialofficer__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

ALTER TABLE "judicialofficer" ADD CONSTRAINT "fk_judicialofficer__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

ALTER TABLE "judicialofficer" ADD CONSTRAINT "fk_judicialofficer__j_o__rank" FOREIGN KEY ("j_o__rank") REFERENCES "jo_rank" ("id");

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

CREATE TABLE "case" (
  "id" SERIAL CONSTRAINT "pk_case" PRIMARY KEY,
  "police_station_reported" INTEGER NOT NULL,
  "report_date" TIMESTAMP NOT NULL,
  "complaint" TEXT NOT NULL,
  "priority" INTEGER NOT NULL DEFAULT 3,
  "investigationassigmentdate" TIMESTAMP,
  "investigationassignmentnote" TEXT NOT NULL,
  "investigationplan" TEXT NOT NULL,
  "investigationsummary" TEXT NOT NULL,
  "investigationreview" TEXT,
  "investigationcomplete" BOOLEAN,
  "dppadvicerequested" BOOLEAN,
  "dppadvicedate" DATE,
  "dppadvice" TEXT NOT NULL,
  "sendtotrial" BOOLEAN NOT NULL,
  "casename" VARCHAR(400) DEFAULT 'Republic Vs',
  "docketnumber" VARCHAR(100) DEFAULT 'D/000/000',
  "chargesheet" TEXT NOT NULL,
  "chargedate" TIMESTAMP,
  "judgement" TEXT NOT NULL,
  "judgementdate" TIMESTAMP,
  "sentencelengthyr" INTEGER,
  "sentencelengthmnth" INTEGER,
  "senetencelenghtdays" INTEGER,
  "sentencestartdate" DATE,
  "sentenceexpirydate" DATE,
  "fineamount" DECIMAL(12, 2),
  "caseappealed" BOOLEAN,
  "appealdate" TIMESTAMP,
  "appealexpiry" DATE,
  "caseclosed" BOOLEAN,
  "closedate" DATE
);

CREATE INDEX "idx_case__police_station_reported" ON "case" ("police_station_reported");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__police_station_reported" FOREIGN KEY ("police_station_reported") REFERENCES "policestation" ("id");

CREATE TABLE "PoliceOfficer" (
  "id" SERIAL CONSTRAINT "pk_policeofficer" PRIMARY KEY,
  "police_rank" INTEGER NOT NULL,
  "gender" INTEGER NOT NULL,
  "servicenumber" TEXT,
  "reports_to" INTEGER,
  "pol_supervisor" INTEGER NOT NULL
);

CREATE INDEX "idx_policeofficer__gender" ON "PoliceOfficer" ("gender");

CREATE INDEX "idx_policeofficer__pol_supervisor" ON "PoliceOfficer" ("pol_supervisor");

CREATE INDEX "idx_policeofficer__police_rank" ON "PoliceOfficer" ("police_rank");

CREATE INDEX "idx_policeofficer__reports_to" ON "PoliceOfficer" ("reports_to");

ALTER TABLE "PoliceOfficer" ADD CONSTRAINT "fk_policeofficer__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

ALTER TABLE "PoliceOfficer" ADD CONSTRAINT "fk_policeofficer__pol_supervisor" FOREIGN KEY ("pol_supervisor") REFERENCES "case" ("id");

ALTER TABLE "PoliceOfficer" ADD CONSTRAINT "fk_policeofficer__police_rank" FOREIGN KEY ("police_rank") REFERENCES "policerank" ("id");

ALTER TABLE "PoliceOfficer" ADD CONSTRAINT "fk_policeofficer__reports_to" FOREIGN KEY ("reports_to") REFERENCES "PoliceOfficer" ("id");

CREATE TABLE "case_advising_prosecutors" (
  "case" INTEGER NOT NULL,
  "prosecutor" INTEGER NOT NULL,
  CONSTRAINT "pk_case_advising_prosecutors" PRIMARY KEY ("case", "prosecutor")
);

CREATE INDEX "idx_case_advising_prosecutors" ON "case_advising_prosecutors" ("prosecutor");

ALTER TABLE "case_advising_prosecutors" ADD CONSTRAINT "fk_case_advising_prosecutors__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_advising_prosecutors" ADD CONSTRAINT "fk_case_advising_prosecutors__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "case_case_categories" (
  "case" INTEGER NOT NULL,
  "casecategory" INTEGER NOT NULL,
  CONSTRAINT "pk_case_case_categories" PRIMARY KEY ("case", "casecategory")
);

CREATE INDEX "idx_case_case_categories" ON "case_case_categories" ("casecategory");

ALTER TABLE "case_case_categories" ADD CONSTRAINT "fk_case_case_categories__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_case_categories" ADD CONSTRAINT "fk_case_case_categories__casecategory" FOREIGN KEY ("casecategory") REFERENCES "casecategory" ("id");

CREATE TABLE "case_causes_of_action" (
  "case" INTEGER NOT NULL,
  "causeofaction" INTEGER NOT NULL,
  CONSTRAINT "pk_case_causes_of_action" PRIMARY KEY ("case", "causeofaction")
);

CREATE INDEX "idx_case_causes_of_action" ON "case_causes_of_action" ("causeofaction");

ALTER TABLE "case_causes_of_action" ADD CONSTRAINT "fk_case_causes_of_action__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_causes_of_action" ADD CONSTRAINT "fk_case_causes_of_action__causeofaction" FOREIGN KEY ("causeofaction") REFERENCES "causeofaction" ("id");

CREATE TABLE "case_investigators" (
  "case" INTEGER NOT NULL,
  "polofficer" INTEGER NOT NULL,
  CONSTRAINT "pk_case_investigators" PRIMARY KEY ("case", "polofficer")
);

CREATE INDEX "idx_case_investigators" ON "case_investigators" ("polofficer");

ALTER TABLE "case_investigators" ADD CONSTRAINT "fk_case_investigators__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_investigators" ADD CONSTRAINT "fk_case_investigators__polofficer" FOREIGN KEY ("polofficer") REFERENCES "PoliceOfficer" ("id");

CREATE TABLE "case_nature_of_suits" (
  "case" INTEGER NOT NULL,
  "natureofsuit" INTEGER NOT NULL,
  CONSTRAINT "pk_case_nature_of_suits" PRIMARY KEY ("case", "natureofsuit")
);

CREATE INDEX "idx_case_nature_of_suits" ON "case_nature_of_suits" ("natureofsuit");

ALTER TABLE "case_nature_of_suits" ADD CONSTRAINT "fk_case_nature_of_suits__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_nature_of_suits" ADD CONSTRAINT "fk_case_nature_of_suits__natureofsuit" FOREIGN KEY ("natureofsuit") REFERENCES "natureofsuit" ("id");

CREATE TABLE "case_plaintiffs" (
  "case" INTEGER NOT NULL,
  "plaintiff" INTEGER NOT NULL,
  CONSTRAINT "pk_case_plaintiffs" PRIMARY KEY ("case", "plaintiff")
);

CREATE INDEX "idx_case_plaintiffs" ON "case_plaintiffs" ("plaintiff");

ALTER TABLE "case_plaintiffs" ADD CONSTRAINT "fk_case_plaintiffs__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_plaintiffs" ADD CONSTRAINT "fk_case_plaintiffs__plaintiff" FOREIGN KEY ("plaintiff") REFERENCES "plaintiff" ("id");

CREATE TABLE "case_pol_reported_to" (
  "case" INTEGER NOT NULL,
  "polofficer" INTEGER NOT NULL,
  CONSTRAINT "pk_case_pol_reported_to" PRIMARY KEY ("case", "polofficer")
);

CREATE INDEX "idx_case_pol_reported_to" ON "case_pol_reported_to" ("polofficer");

ALTER TABLE "case_pol_reported_to" ADD CONSTRAINT "fk_case_pol_reported_to__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_pol_reported_to" ADD CONSTRAINT "fk_case_pol_reported_to__polofficer" FOREIGN KEY ("polofficer") REFERENCES "PoliceOfficer" ("id");

CREATE TABLE "case_police_prosecutors" (
  "case" INTEGER NOT NULL,
  "polofficer" INTEGER NOT NULL,
  CONSTRAINT "pk_case_police_prosecutors" PRIMARY KEY ("case", "polofficer")
);

CREATE INDEX "idx_case_police_prosecutors" ON "case_police_prosecutors" ("polofficer");

ALTER TABLE "case_police_prosecutors" ADD CONSTRAINT "fk_case_police_prosecutors__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_police_prosecutors" ADD CONSTRAINT "fk_case_police_prosecutors__polofficer" FOREIGN KEY ("polofficer") REFERENCES "PoliceOfficer" ("id");

CREATE TABLE "case_prosecutors" (
  "case" INTEGER NOT NULL,
  "prosecutor" INTEGER NOT NULL,
  CONSTRAINT "pk_case_prosecutors" PRIMARY KEY ("case", "prosecutor")
);

CREATE INDEX "idx_case_prosecutors" ON "case_prosecutors" ("prosecutor");

ALTER TABLE "case_prosecutors" ADD CONSTRAINT "fk_case_prosecutors__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_prosecutors" ADD CONSTRAINT "fk_case_prosecutors__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "case_tags" (
  "case" INTEGER NOT NULL,
  "tag" INTEGER NOT NULL,
  CONSTRAINT "pk_case_tags" PRIMARY KEY ("case", "tag")
);

CREATE INDEX "idx_case_tags" ON "case_tags" ("tag");

ALTER TABLE "case_tags" ADD CONSTRAINT "fk_case_tags__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_tags" ADD CONSTRAINT "fk_case_tags__tag" FOREIGN KEY ("tag") REFERENCES "tag" ("id");

CREATE TABLE "filing" (
  "id" SERIAL CONSTRAINT "pk_filing" PRIMARY KEY,
  "uploaddate" TIMESTAMP,
  "pagecount" INTEGER DEFAULT 1,
  "totalfees" DECIMAL(12, 2) NOT NULL,
  "filing_attorney" INTEGER NOT NULL,
  "filing_prosecutor" INTEGER NOT NULL,
  "assessedfees" DECIMAL(12, 2),
  "receiptverified" BOOLEAN,
  "amountpaid" DECIMAL(12, 2),
  "feebalance" DECIMAL(12, 2),
  "paymenthistory" TEXT NOT NULL,
  "case" INTEGER NOT NULL,
  "urgent" BOOLEAN,
  "urgentreason" TEXT NOT NULL
);

CREATE INDEX "idx_filing__case" ON "filing" ("case");

CREATE INDEX "idx_filing__filing_attorney" ON "filing" ("filing_attorney");

CREATE INDEX "idx_filing__filing_prosecutor" ON "filing" ("filing_prosecutor");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__filing_attorney" FOREIGN KEY ("filing_attorney") REFERENCES "lawyers" ("id");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__filing_prosecutor" FOREIGN KEY ("filing_prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "causeofaction_filings" (
  "causeofaction" INTEGER NOT NULL,
  "filing" INTEGER NOT NULL,
  CONSTRAINT "pk_causeofaction_filings" PRIMARY KEY ("causeofaction", "filing")
);

CREATE INDEX "idx_causeofaction_filings" ON "causeofaction_filings" ("filing");

ALTER TABLE "causeofaction_filings" ADD CONSTRAINT "fk_causeofaction_filings__causeofaction" FOREIGN KEY ("causeofaction") REFERENCES "causeofaction" ("id");

ALTER TABLE "causeofaction_filings" ADD CONSTRAINT "fk_causeofaction_filings__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

CREATE TABLE "document" (
  "id" SERIAL CONSTRAINT "pk_document" PRIMARY KEY,
  "filing" INTEGER NOT NULL,
  "doc_template" INTEGER,
  "confidential" BOOLEAN,
  "pagecount" INTEGER,
  "locked" BOOLEAN,
  "hash" TEXT
);

CREATE INDEX "idx_document__doc_template" ON "document" ("doc_template");

CREATE INDEX "idx_document__filing" ON "document" ("filing");

ALTER TABLE "document" ADD CONSTRAINT "fk_document__doc_template" FOREIGN KEY ("doc_template") REFERENCES "doctemplate" ("id");

ALTER TABLE "document" ADD CONSTRAINT "fk_document__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

CREATE TABLE "document_tags" (
  "document" INTEGER NOT NULL,
  "tag" INTEGER NOT NULL,
  CONSTRAINT "pk_document_tags" PRIMARY KEY ("document", "tag")
);

CREATE INDEX "idx_document_tags" ON "document_tags" ("tag");

ALTER TABLE "document_tags" ADD CONSTRAINT "fk_document_tags__document" FOREIGN KEY ("document") REFERENCES "document" ("id");

ALTER TABLE "document_tags" ADD CONSTRAINT "fk_document_tags__tag" FOREIGN KEY ("tag") REFERENCES "tag" ("id");

CREATE TABLE "filing_filing_types" (
  "filing" INTEGER NOT NULL,
  "filingtype" INTEGER NOT NULL,
  CONSTRAINT "pk_filing_filing_types" PRIMARY KEY ("filing", "filingtype")
);

CREATE INDEX "idx_filing_filing_types" ON "filing_filing_types" ("filingtype");

ALTER TABLE "filing_filing_types" ADD CONSTRAINT "fk_filing_filing_types__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

ALTER TABLE "filing_filing_types" ADD CONSTRAINT "fk_filing_filing_types__filingtype" FOREIGN KEY ("filingtype") REFERENCES "filingtype" ("id");

CREATE TABLE "hearing" (
  "id" SERIAL CONSTRAINT "pk_hearing" PRIMARY KEY,
  "hearingdate" TIMESTAMP NOT NULL,
  "adjourned" BOOLEAN,
  "case" INTEGER NOT NULL,
  "court" INTEGER NOT NULL,
  "remandwarrant" TEXT,
  "hearing_type" INTEGER NOT NULL,
  "remanddays" INTEGER,
  "remanddate" DATE,
  "remandwarrantexpirydate" DATE,
  "nexthearingdate" DATE,
  "finalhearing" BOOLEAN NOT NULL,
  "transcript" TEXT,
  "audio" BYTEA,
  "video" BYTEA
);

CREATE INDEX "idx_hearing__case" ON "hearing" ("case");

CREATE INDEX "idx_hearing__court" ON "hearing" ("court");

CREATE INDEX "idx_hearing__hearing_type" ON "hearing" ("hearing_type");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__hearing_type" FOREIGN KEY ("hearing_type") REFERENCES "hearingtype" ("id");

CREATE TABLE "causeofaction_hearings" (
  "hearing" INTEGER NOT NULL,
  "causeofaction" INTEGER NOT NULL,
  CONSTRAINT "pk_causeofaction_hearings" PRIMARY KEY ("hearing", "causeofaction")
);

CREATE INDEX "idx_causeofaction_hearings" ON "causeofaction_hearings" ("causeofaction");

ALTER TABLE "causeofaction_hearings" ADD CONSTRAINT "fk_causeofaction_hearings__causeofaction" FOREIGN KEY ("causeofaction") REFERENCES "causeofaction" ("id");

ALTER TABLE "causeofaction_hearings" ADD CONSTRAINT "fk_causeofaction_hearings__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "hearing_defense_attorneys" (
  "lawyers" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_defense_attorneys" PRIMARY KEY ("lawyers", "hearing")
);

CREATE INDEX "idx_hearing_defense_attorneys" ON "hearing_defense_attorneys" ("hearing");

ALTER TABLE "hearing_defense_attorneys" ADD CONSTRAINT "fk_hearing_defense_attorneys__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_defense_attorneys" ADD CONSTRAINT "fk_hearing_defense_attorneys__lawyers" FOREIGN KEY ("lawyers") REFERENCES "lawyers" ("id");

CREATE TABLE "hearing_judicialofficers" (
  "hearing" INTEGER NOT NULL,
  "judicialofficer" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_judicialofficers" PRIMARY KEY ("hearing", "judicialofficer")
);

CREATE INDEX "idx_hearing_judicialofficers" ON "hearing_judicialofficers" ("judicialofficer");

ALTER TABLE "hearing_judicialofficers" ADD CONSTRAINT "fk_hearing_judicialofficers__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_judicialofficers" ADD CONSTRAINT "fk_hearing_judicialofficers__judicialofficer" FOREIGN KEY ("judicialofficer") REFERENCES "judicialofficer" ("id");

CREATE TABLE "hearing_police_prosecutors" (
  "polofficer" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_police_prosecutors" PRIMARY KEY ("polofficer", "hearing")
);

CREATE INDEX "idx_hearing_police_prosecutors" ON "hearing_police_prosecutors" ("hearing");

ALTER TABLE "hearing_police_prosecutors" ADD CONSTRAINT "fk_hearing_police_prosecutors__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_police_prosecutors" ADD CONSTRAINT "fk_hearing_police_prosecutors__polofficer" FOREIGN KEY ("polofficer") REFERENCES "PoliceOfficer" ("id");

CREATE TABLE "hearing_prosecutors" (
  "prosecutor" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_prosecutors" PRIMARY KEY ("prosecutor", "hearing")
);

CREATE INDEX "idx_hearing_prosecutors" ON "hearing_prosecutors" ("hearing");

ALTER TABLE "hearing_prosecutors" ADD CONSTRAINT "fk_hearing_prosecutors__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_prosecutors" ADD CONSTRAINT "fk_hearing_prosecutors__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "hearing_tags" (
  "hearing" INTEGER NOT NULL,
  "tag" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_tags" PRIMARY KEY ("hearing", "tag")
);

CREATE INDEX "idx_hearing_tags" ON "hearing_tags" ("tag");

ALTER TABLE "hearing_tags" ADD CONSTRAINT "fk_hearing_tags__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_tags" ADD CONSTRAINT "fk_hearing_tags__tag" FOREIGN KEY ("tag") REFERENCES "tag" ("id");

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
  "polofficer" INTEGER NOT NULL,
  "investigation" INTEGER NOT NULL,
  CONSTRAINT "pk_investigation_investigator" PRIMARY KEY ("polofficer", "investigation")
);

CREATE INDEX "idx_investigation_investigator" ON "investigation_investigator" ("investigation");

ALTER TABLE "investigation_investigator" ADD CONSTRAINT "fk_investigation_investigator__investigation" FOREIGN KEY ("investigation") REFERENCES "investigation" ("id");

ALTER TABLE "investigation_investigator" ADD CONSTRAINT "fk_investigation_investigator__polofficer" FOREIGN KEY ("polofficer") REFERENCES "PoliceOfficer" ("id");

CREATE TABLE "polofficer_police_roles" (
  "polofficer" INTEGER NOT NULL,
  "policerole" INTEGER NOT NULL,
  CONSTRAINT "pk_polofficer_police_roles" PRIMARY KEY ("polofficer", "policerole")
);

CREATE INDEX "idx_polofficer_police_roles" ON "polofficer_police_roles" ("policerole");

ALTER TABLE "polofficer_police_roles" ADD CONSTRAINT "fk_polofficer_police_roles__policerole" FOREIGN KEY ("policerole") REFERENCES "policerole" ("id");

ALTER TABLE "polofficer_police_roles" ADD CONSTRAINT "fk_polofficer_police_roles__polofficer" FOREIGN KEY ("polofficer") REFERENCES "PoliceOfficer" ("id");

CREATE TABLE "prison" (
  "id" SERIAL CONSTRAINT "pk_prison" PRIMARY KEY,
  "town" INTEGER NOT NULL,
  "warden" VARCHAR(100),
  "capacity" INTEGER,
  "population" INTEGER,
  "cellcount" INTEGER,
  "gatecount" INTEGER
);

CREATE INDEX "idx_prison__town" ON "prison" ("town");

ALTER TABLE "prison" ADD CONSTRAINT "fk_prison__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "gateregister" (
  "id" SERIAL CONSTRAINT "pk_gateregister" PRIMARY KEY,
  "prison" INTEGER NOT NULL,
  "opentime" TIMESTAMP,
  "closedtime" TIMESTAMP,
  "openduration" INTERVAL DAY TO SECOND,
  "movementdirection" BOOLEAN,
  "reason" TEXT,
  "staffmovement" BOOLEAN,
  "goodsmovement" TEXT NOT NULL,
  "vehicle_reg" TEXT,
  "vehicle_color" TEXT NOT NULL
);

CREATE INDEX "idx_gateregister__prison" ON "gateregister" ("prison");

ALTER TABLE "gateregister" ADD CONSTRAINT "fk_gateregister__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

CREATE TABLE "prison_security_ranks" (
  "prison" INTEGER NOT NULL,
  "securityrank" INTEGER NOT NULL,
  CONSTRAINT "pk_prison_security_ranks" PRIMARY KEY ("prison", "securityrank")
);

CREATE INDEX "idx_prison_security_ranks" ON "prison_security_ranks" ("securityrank");

ALTER TABLE "prison_security_ranks" ADD CONSTRAINT "fk_prison_security_ranks__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

ALTER TABLE "prison_security_ranks" ADD CONSTRAINT "fk_prison_security_ranks__securityrank" FOREIGN KEY ("securityrank") REFERENCES "securityrank" ("id");

CREATE TABLE "prisoncell" (
  "id" SERIAL CONSTRAINT "pk_prisoncell" PRIMARY KEY,
  "prison" INTEGER NOT NULL
);

CREATE INDEX "idx_prisoncell__prison" ON "prisoncell" ("prison");

ALTER TABLE "prisoncell" ADD CONSTRAINT "fk_prisoncell__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

CREATE TABLE "defendant" (
  "id" SERIAL CONSTRAINT "pk_defendant" PRIMARY KEY,
  "juvenile" BOOLEAN,
  "gender" INTEGER NOT NULL,
  "prisoncell" INTEGER NOT NULL,
  "casecount" INTEGER
);

CREATE INDEX "idx_defendant__gender" ON "defendant" ("gender");

CREATE INDEX "idx_defendant__prisoncell" ON "defendant" ("prisoncell");

ALTER TABLE "defendant" ADD CONSTRAINT "fk_defendant__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

ALTER TABLE "defendant" ADD CONSTRAINT "fk_defendant__prisoncell" FOREIGN KEY ("prisoncell") REFERENCES "prisoncell" ("id");

CREATE TABLE "bail" (
  "id" SERIAL CONSTRAINT "pk_bail" PRIMARY KEY,
  "hearing" INTEGER NOT NULL,
  "defendant" INTEGER NOT NULL,
  "amountgranted" DECIMAL(12, 2),
  "noofsureties" INTEGER NOT NULL,
  "paid" BOOLEAN,
  "paydate" DATE
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

CREATE TABLE "case_defendants" (
  "case" INTEGER NOT NULL,
  "defendant" INTEGER NOT NULL,
  CONSTRAINT "pk_case_defendants" PRIMARY KEY ("case", "defendant")
);

CREATE INDEX "idx_case_defendants" ON "case_defendants" ("defendant");

ALTER TABLE "case_defendants" ADD CONSTRAINT "fk_case_defendants__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_defendants" ADD CONSTRAINT "fk_case_defendants__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

CREATE TABLE "defendant_hearings" (
  "defendant" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_defendant_hearings" PRIMARY KEY ("defendant", "hearing")
);

CREATE INDEX "idx_defendant_hearings" ON "defendant_hearings" ("hearing");

ALTER TABLE "defendant_hearings" ADD CONSTRAINT "fk_defendant_hearings__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

ALTER TABLE "defendant_hearings" ADD CONSTRAINT "fk_defendant_hearings__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "defendant_medical_events" (
  "defendant" INTEGER NOT NULL,
  "medevent" INTEGER NOT NULL,
  CONSTRAINT "pk_defendant_medical_events" PRIMARY KEY ("defendant", "medevent")
);

CREATE INDEX "idx_defendant_medical_events" ON "defendant_medical_events" ("medevent");

ALTER TABLE "defendant_medical_events" ADD CONSTRAINT "fk_defendant_medical_events__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

ALTER TABLE "defendant_medical_events" ADD CONSTRAINT "fk_defendant_medical_events__medevent" FOREIGN KEY ("medevent") REFERENCES "Medevent" ("id");

CREATE TABLE "defendant_prisoner_gate_movement" (
  "defendant" INTEGER NOT NULL,
  "gateregister" INTEGER NOT NULL,
  CONSTRAINT "pk_defendant_prisoner_gate_movement" PRIMARY KEY ("defendant", "gateregister")
);

CREATE INDEX "idx_defendant_prisoner_gate_movement" ON "defendant_prisoner_gate_movement" ("gateregister");

ALTER TABLE "defendant_prisoner_gate_movement" ADD CONSTRAINT "fk_defendant_prisoner_gate_movement__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

ALTER TABLE "defendant_prisoner_gate_movement" ADD CONSTRAINT "fk_defendant_prisoner_gate_movement__gateregister" FOREIGN KEY ("gateregister") REFERENCES "gateregister" ("id");

CREATE TABLE "discipline" (
  "id" SERIAL CONSTRAINT "pk_discipline" PRIMARY KEY,
  "defendant" INTEGER NOT NULL
);

CREATE INDEX "idx_discipline__defendant" ON "discipline" ("defendant");

ALTER TABLE "discipline" ADD CONSTRAINT "fk_discipline__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

CREATE TABLE "payment" (
  "id" SERIAL CONSTRAINT "pk_payment" PRIMARY KEY,
  "datepaid" TIMESTAMP,
  "amount" DECIMAL(12, 2),
  "paymentreference" VARCHAR(80) NOT NULL,
  "paymentconfirmed" BOOLEAN DEFAULT true,
  "paidby" TEXT NOT NULL,
  "msisdn" TEXT,
  "receiptnumber" VARCHAR(100) NOT NULL,
  "ispartial" BOOLEAN,
  "bail" INTEGER NOT NULL,
  "billrefnumber" TEXT NOT NULL,
  "payment_method" INTEGER NOT NULL,
  "paymentdescription" TEXT NOT NULL,
  "case" INTEGER
);

CREATE INDEX "idx_payment__bail" ON "payment" ("bail");

CREATE INDEX "idx_payment__case" ON "payment" ("case");

CREATE INDEX "idx_payment__payment_method" ON "payment" ("payment_method");

ALTER TABLE "payment" ADD CONSTRAINT "fk_payment__bail" FOREIGN KEY ("bail") REFERENCES "bail" ("id");

ALTER TABLE "payment" ADD CONSTRAINT "fk_payment__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "payment" ADD CONSTRAINT "fk_payment__payment_method" FOREIGN KEY ("payment_method") REFERENCES "paymentmethod" ("id");

CREATE TABLE "filing_payments" (
  "filing" INTEGER NOT NULL,
  "payment" INTEGER NOT NULL,
  CONSTRAINT "pk_filing_payments" PRIMARY KEY ("filing", "payment")
);

CREATE INDEX "idx_filing_payments" ON "filing_payments" ("payment");

ALTER TABLE "filing_payments" ADD CONSTRAINT "fk_filing_payments__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

ALTER TABLE "filing_payments" ADD CONSTRAINT "fk_filing_payments__payment" FOREIGN KEY ("payment") REFERENCES "payment" ("id");

CREATE TABLE "prisoncommital" (
  "prison" INTEGER NOT NULL,
  "warrantno" VARCHAR(100) NOT NULL,
  "defendant" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  "warrantdate" TIMESTAMP,
  "hascourtdate" BOOLEAN,
  "judicial_officer_warrant" INTEGER NOT NULL,
  "warrant" TEXT NOT NULL,
  "warrantduration" INTEGER NOT NULL,
  "warrantexpiry" TIMESTAMP NOT NULL,
  "history" TEXT NOT NULL,
  "earliestrelease" DATE,
  "releasedate" TIMESTAMP,
  "property" TEXT,
  "itemcount" INTEGER,
  "releasenotes" TEXT,
  "commitalnotes" TEXT,
  "police_officer_commiting" INTEGER NOT NULL,
  "paroledate" DATE,
  "escaped" BOOLEAN,
  "escapedate" TIMESTAMP,
  "escapedetails" TEXT,
  CONSTRAINT "pk_prisoncommital" PRIMARY KEY ("prison", "warrantno")
);

CREATE INDEX "idx_prisoncommital__defendant" ON "prisoncommital" ("defendant");

CREATE INDEX "idx_prisoncommital__hearing" ON "prisoncommital" ("hearing");

CREATE INDEX "idx_prisoncommital__judicial_officer_warrant" ON "prisoncommital" ("judicial_officer_warrant");

CREATE INDEX "idx_prisoncommital__police_officer_commiting" ON "prisoncommital" ("police_officer_commiting");

ALTER TABLE "prisoncommital" ADD CONSTRAINT "fk_prisoncommital__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

ALTER TABLE "prisoncommital" ADD CONSTRAINT "fk_prisoncommital__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "prisoncommital" ADD CONSTRAINT "fk_prisoncommital__judicial_officer_warrant" FOREIGN KEY ("judicial_officer_warrant") REFERENCES "judicialofficer" ("id");

ALTER TABLE "prisoncommital" ADD CONSTRAINT "fk_prisoncommital__police_officer_commiting" FOREIGN KEY ("police_officer_commiting") REFERENCES "PoliceOfficer" ("id");

ALTER TABLE "prisoncommital" ADD CONSTRAINT "fk_prisoncommital__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

CREATE TABLE "commitaltype_prison_commitals" (
  "prisoncommital_prison" INTEGER NOT NULL,
  "prisoncommital_warrantno" VARCHAR(100) NOT NULL,
  "commitaltype" INTEGER NOT NULL,
  CONSTRAINT "pk_commitaltype_prison_commitals" PRIMARY KEY ("prisoncommital_prison", "prisoncommital_warrantno", "commitaltype")
);

CREATE INDEX "idx_commitaltype_prison_commitals" ON "commitaltype_prison_commitals" ("commitaltype");

ALTER TABLE "commitaltype_prison_commitals" ADD CONSTRAINT "fk_commitaltype_prison_commitals__commitaltype" FOREIGN KEY ("commitaltype") REFERENCES "commitaltype" ("id");

ALTER TABLE "commitaltype_prison_commitals" ADD CONSTRAINT "fk_commitaltype_prison_commitals__prisoncommital_priso_c449d31c" FOREIGN KEY ("prisoncommital_prison", "prisoncommital_warrantno") REFERENCES "prisoncommital" ("prison", "warrantno");

CREATE TABLE "prisonerproperty" (
  "id" SERIAL CONSTRAINT "pk_prisonerproperty" PRIMARY KEY,
  "prison_commital_prison" INTEGER NOT NULL,
  "prison_commital_warrantno" VARCHAR(100) NOT NULL,
  "receipted" BOOLEAN
);

CREATE INDEX "idx_prisonerproperty__prison_commital_prison_prison_co_0d67ced7" ON "prisonerproperty" ("prison_commital_prison", "prison_commital_warrantno");

ALTER TABLE "prisonerproperty" ADD CONSTRAINT "fk_prisonerproperty__prison_commital_prison__prison_co_f743afab" FOREIGN KEY ("prison_commital_prison", "prison_commital_warrantno") REFERENCES "prisoncommital" ("prison", "warrantno");

CREATE TABLE "remission" (
  "id" SERIAL CONSTRAINT "pk_remission" PRIMARY KEY,
  "prison_commital_prison" INTEGER NOT NULL,
  "prison_commital_warrantno" VARCHAR(100) NOT NULL,
  "daysearned" INTEGER,
  "dateearned" DATE,
  "amount" DECIMAL(12, 2)
);

CREATE INDEX "idx_remission__prison_commital_prison_prison_commital_warrantno" ON "remission" ("prison_commital_prison", "prison_commital_warrantno");

ALTER TABLE "remission" ADD CONSTRAINT "fk_remission__prison_commital_prison__prison_commital_warrantno" FOREIGN KEY ("prison_commital_prison", "prison_commital_warrantno") REFERENCES "prisoncommital" ("prison", "warrantno");

CREATE TABLE "visitor" (
  "id" SERIAL CONSTRAINT "pk_visitor" PRIMARY KEY,
  "gender" INTEGER NOT NULL
);

CREATE INDEX "idx_visitor__gender" ON "visitor" ("gender");

ALTER TABLE "visitor" ADD CONSTRAINT "fk_visitor__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "visit" (
  "vistors" INTEGER NOT NULL,
  "defendants" INTEGER NOT NULL,
  "visitdate" TIMESTAMP,
  "visitnotes" TEXT,
  "visitduration" INTERVAL DAY TO SECOND,
  CONSTRAINT "pk_visit" PRIMARY KEY ("vistors", "defendants")
);

CREATE INDEX "idx_visit__defendants" ON "visit" ("defendants");

ALTER TABLE "visit" ADD CONSTRAINT "fk_visit__defendants" FOREIGN KEY ("defendants") REFERENCES "defendant" ("id");

ALTER TABLE "visit" ADD CONSTRAINT "fk_visit__vistors" FOREIGN KEY ("vistors") REFERENCES "visitor" ("id");

CREATE TABLE "warderrank" (
  "id" SERIAL CONSTRAINT "pk_warderrank" PRIMARY KEY
);

CREATE TABLE "warder" (
  "id" SERIAL CONSTRAINT "pk_warder" PRIMARY KEY,
  "prison" INTEGER NOT NULL,
  "warder_rank" INTEGER NOT NULL,
  "reports_to" INTEGER
);

CREATE INDEX "idx_warder__prison" ON "warder" ("prison");

CREATE INDEX "idx_warder__reports_to" ON "warder" ("reports_to");

CREATE INDEX "idx_warder__warder_rank" ON "warder" ("warder_rank");

ALTER TABLE "warder" ADD CONSTRAINT "fk_warder__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

ALTER TABLE "warder" ADD CONSTRAINT "fk_warder__reports_to" FOREIGN KEY ("reports_to") REFERENCES "warder" ("id");

ALTER TABLE "warder" ADD CONSTRAINT "fk_warder__warder_rank" FOREIGN KEY ("warder_rank") REFERENCES "warderrank" ("id");

CREATE TABLE "gateregister_gate_warders" (
  "warder" INTEGER NOT NULL,
  "gateregister" INTEGER NOT NULL,
  CONSTRAINT "pk_gateregister_gate_warders" PRIMARY KEY ("warder", "gateregister")
);

CREATE INDEX "idx_gateregister_gate_warders" ON "gateregister_gate_warders" ("gateregister");

ALTER TABLE "gateregister_gate_warders" ADD CONSTRAINT "fk_gateregister_gate_warders__gateregister" FOREIGN KEY ("gateregister") REFERENCES "gateregister" ("id");

ALTER TABLE "gateregister_gate_warders" ADD CONSTRAINT "fk_gateregister_gate_warders__warder" FOREIGN KEY ("warder") REFERENCES "warder" ("id");

CREATE TABLE "gateregister_warders_movement" (
  "warder" INTEGER NOT NULL,
  "gateregister" INTEGER NOT NULL,
  CONSTRAINT "pk_gateregister_warders_movement" PRIMARY KEY ("warder", "gateregister")
);

CREATE INDEX "idx_gateregister_warders_movement" ON "gateregister_warders_movement" ("gateregister");

ALTER TABLE "gateregister_warders_movement" ADD CONSTRAINT "fk_gateregister_warders_movement__gateregister" FOREIGN KEY ("gateregister") REFERENCES "gateregister" ("id");

ALTER TABLE "gateregister_warders_movement" ADD CONSTRAINT "fk_gateregister_warders_movement__warder" FOREIGN KEY ("warder") REFERENCES "warder" ("id");

CREATE TABLE "prisoncommital_receiving_warders" (
  "prisoncommital_prison" INTEGER NOT NULL,
  "prisoncommital_warrantno" VARCHAR(100) NOT NULL,
  "warder" INTEGER NOT NULL,
  CONSTRAINT "pk_prisoncommital_receiving_warders" PRIMARY KEY ("prisoncommital_prison", "prisoncommital_warrantno", "warder")
);

CREATE INDEX "idx_prisoncommital_receiving_warders" ON "prisoncommital_receiving_warders" ("warder");

ALTER TABLE "prisoncommital_receiving_warders" ADD CONSTRAINT "fk_prisoncommital_receiving_warders__prisoncommital_pr_605dcd42" FOREIGN KEY ("prisoncommital_prison", "prisoncommital_warrantno") REFERENCES "prisoncommital" ("prison", "warrantno");

ALTER TABLE "prisoncommital_receiving_warders" ADD CONSTRAINT "fk_prisoncommital_receiving_warders__warder" FOREIGN KEY ("warder") REFERENCES "warder" ("id");

CREATE TABLE "witness" (
  "id" SERIAL CONSTRAINT "pk_witness" PRIMARY KEY,
  "fordefense" BOOLEAN,
  "gender" INTEGER NOT NULL
);

CREATE INDEX "idx_witness__gender" ON "witness" ("gender");

ALTER TABLE "witness" ADD CONSTRAINT "fk_witness__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "case_witnesses" (
  "case" INTEGER NOT NULL,
  "witness" INTEGER NOT NULL,
  CONSTRAINT "pk_case_witnesses" PRIMARY KEY ("case", "witness")
);

CREATE INDEX "idx_case_witnesses" ON "case_witnesses" ("witness");

ALTER TABLE "case_witnesses" ADD CONSTRAINT "fk_case_witnesses__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_witnesses" ADD CONSTRAINT "fk_case_witnesses__witness" FOREIGN KEY ("witness") REFERENCES "witness" ("id");

CREATE TABLE "hearing_witnesses" (
  "witness" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  CONSTRAINT "pk_hearing_witnesses" PRIMARY KEY ("witness", "hearing")
);

CREATE INDEX "idx_hearing_witnesses" ON "hearing_witnesses" ("hearing");

ALTER TABLE "hearing_witnesses" ADD CONSTRAINT "fk_hearing_witnesses__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_witnesses" ADD CONSTRAINT "fk_hearing_witnesses__witness" FOREIGN KEY ("witness") REFERENCES "witness" ("id");

CREATE TABLE "investigation_witnesses" (
  "investigation" INTEGER NOT NULL,
  "witness" INTEGER NOT NULL,
  CONSTRAINT "pk_investigation_witnesses" PRIMARY KEY ("investigation", "witness")
);

CREATE INDEX "idx_investigation_witnesses" ON "investigation_witnesses" ("witness");

ALTER TABLE "investigation_witnesses" ADD CONSTRAINT "fk_investigation_witnesses__investigation" FOREIGN KEY ("investigation") REFERENCES "investigation" ("id");

ALTER TABLE "investigation_witnesses" ADD CONSTRAINT "fk_investigation_witnesses__witness" FOREIGN KEY ("witness") REFERENCES "witness" ("id")
