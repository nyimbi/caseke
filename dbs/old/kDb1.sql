CREATE TABLE "ActionTYpe" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "case" (
  "id" SERIAL PRIMARY KEY,
  "investigationassigmentdate" TIMESTAMP,
  "investigationassignmentnote" TEXT NOT NULL,
  "investigationplan" TEXT NOT NULL,
  "initialreport" TEXT NOT NULL,
  "priority" INTEGER NOT NULL,
  "findings" TEXT NOT NULL,
  "agadvicerequested" BOOLEAN NOT NULL,
  "sendtotrial" BOOLEAN NOT NULL,
  "chargedate" TIMESTAMP,
  "taketotrial" BOOLEAN NOT NULL,
  "closed" BOOLEAN NOT NULL,
  "judgement" TEXT NOT NULL,
  "closeddate" DATE NOT NULL,
  "sentencelength" INTEGER NOT NULL,
  "sentencestartdate" DATE NOT NULL,
  "sentenceexpirydate" DATE NOT NULL,
  "fineamount" DOUBLE PRECISION NOT NULL
);

CREATE TABLE "causeofaction" (
  "id" SERIAL PRIMARY KEY,
  "action_type" INTEGER
);

CREATE INDEX "idx_causeofaction__action_type" ON "causeofaction" ("action_type");

ALTER TABLE "causeofaction" ADD CONSTRAINT "fk_causeofaction__action_type" FOREIGN KEY ("action_type") REFERENCES "ActionTYpe" ("id");

CREATE TABLE "county" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "courtlevel" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "defendant" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "case_defendant" (
  "case" INTEGER NOT NULL,
  "defendant" INTEGER NOT NULL,
  PRIMARY KEY ("case", "defendant")
);

CREATE INDEX "idx_case_defendant" ON "case_defendant" ("defendant");

ALTER TABLE "case_defendant" ADD CONSTRAINT "fk_case_defendant__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_defendant" ADD CONSTRAINT "fk_case_defendant__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

CREATE TABLE "doctemplate" (
  "id" SERIAL PRIMARY KEY,
  "template" TEXT NOT NULL,
  "templatejson" JSONB NOT NULL
);

CREATE TABLE "document" (
  "id" SERIAL PRIMARY KEY,
  "mimetype" VARCHAR(100) NOT NULL,
  "doctype" TEXT NOT NULL,
  "doc" TEXT NOT NULL,
  "docbin" BYTEA NOT NULL,
  "docthumbnail" BYTEA NOT NULL,
  "doc_template" INTEGER,
  "docjson" JSONB NOT NULL
);

CREATE INDEX "idx_document__doc_template" ON "document" ("doc_template");

ALTER TABLE "document" ADD CONSTRAINT "fk_document__doc_template" FOREIGN KEY ("doc_template") REFERENCES "doctemplate" ("id");

CREATE TABLE "filingtype" (
  "id" SERIAL PRIMARY KEY,
  "cost" DOUBLE PRECISION NOT NULL
);

CREATE TABLE "hearingtype" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "investigation" (
  "id" SERIAL PRIMARY KEY,
  "case" INTEGER NOT NULL,
  "actiondate" TIMESTAMP NOT NULL,
  "evidence" TEXT NOT NULL
);

CREATE INDEX "idx_investigation__case" ON "investigation" ("case");

ALTER TABLE "investigation" ADD CONSTRAINT "fk_investigation__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

CREATE TABLE "lawfirm" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "attorney" (
  "id" SERIAL PRIMARY KEY,
  "law_firm" INTEGER
);

CREATE INDEX "idx_attorney__law_firm" ON "attorney" ("law_firm");

ALTER TABLE "attorney" ADD CONSTRAINT "fk_attorney__law_firm" FOREIGN KEY ("law_firm") REFERENCES "lawfirm" ("id");

CREATE TABLE "natureofsuit" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "case_natureofsuit" (
  "case" INTEGER NOT NULL,
  "natureofsuit" INTEGER NOT NULL,
  PRIMARY KEY ("case", "natureofsuit")
);

CREATE INDEX "idx_case_natureofsuit" ON "case_natureofsuit" ("natureofsuit");

ALTER TABLE "case_natureofsuit" ADD CONSTRAINT "fk_case_natureofsuit__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_natureofsuit" ADD CONSTRAINT "fk_case_natureofsuit__natureofsuit" FOREIGN KEY ("natureofsuit") REFERENCES "natureofsuit" ("id");

CREATE TABLE "plaintiff" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "case_plaintiff" (
  "case" INTEGER NOT NULL,
  "plaintiff" INTEGER NOT NULL,
  PRIMARY KEY ("case", "plaintiff")
);

CREATE INDEX "idx_case_plaintiff" ON "case_plaintiff" ("plaintiff");

ALTER TABLE "case_plaintiff" ADD CONSTRAINT "fk_case_plaintiff__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_plaintiff" ADD CONSTRAINT "fk_case_plaintiff__plaintiff" FOREIGN KEY ("plaintiff") REFERENCES "plaintiff" ("id");

CREATE TABLE "policeman" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "case_policeman" (
  "case" INTEGER NOT NULL,
  "policeman" INTEGER NOT NULL,
  PRIMARY KEY ("case", "policeman")
);

CREATE INDEX "idx_case_policeman" ON "case_policeman" ("policeman");

ALTER TABLE "case_policeman" ADD CONSTRAINT "fk_case_policeman__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_policeman" ADD CONSTRAINT "fk_case_policeman__policeman" FOREIGN KEY ("policeman") REFERENCES "policeman" ("id");

CREATE TABLE "case_policeman_2" (
  "case" INTEGER NOT NULL,
  "policeman" INTEGER NOT NULL,
  PRIMARY KEY ("case", "policeman")
);

CREATE INDEX "idx_case_policeman_2" ON "case_policeman_2" ("policeman");

ALTER TABLE "case_policeman_2" ADD CONSTRAINT "fk_case_policeman_2__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_policeman_2" ADD CONSTRAINT "fk_case_policeman_2__policeman" FOREIGN KEY ("policeman") REFERENCES "policeman" ("id");

CREATE TABLE "investigation_policeman" (
  "investigation" INTEGER NOT NULL,
  "policeman" INTEGER NOT NULL,
  PRIMARY KEY ("investigation", "policeman")
);

CREATE INDEX "idx_investigation_policeman" ON "investigation_policeman" ("policeman");

ALTER TABLE "investigation_policeman" ADD CONSTRAINT "fk_investigation_policeman__investigation" FOREIGN KEY ("investigation") REFERENCES "investigation" ("id");

ALTER TABLE "investigation_policeman" ADD CONSTRAINT "fk_investigation_policeman__policeman" FOREIGN KEY ("policeman") REFERENCES "policeman" ("id");

CREATE TABLE "policerole" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "policerole_policeman" (
  "policerole" INTEGER NOT NULL,
  "policeman" INTEGER NOT NULL,
  PRIMARY KEY ("policerole", "policeman")
);

CREATE INDEX "idx_policerole_policeman" ON "policerole_policeman" ("policeman");

ALTER TABLE "policerole_policeman" ADD CONSTRAINT "fk_policerole_policeman__policeman" FOREIGN KEY ("policeman") REFERENCES "policeman" ("id");

ALTER TABLE "policerole_policeman" ADD CONSTRAINT "fk_policerole_policeman__policerole" FOREIGN KEY ("policerole") REFERENCES "policerole" ("id");

CREATE TABLE "prosecutor" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "case_prosecutor" (
  "case" INTEGER NOT NULL,
  "prosecutor" INTEGER NOT NULL,
  PRIMARY KEY ("case", "prosecutor")
);

CREATE INDEX "idx_case_prosecutor" ON "case_prosecutor" ("prosecutor");

ALTER TABLE "case_prosecutor" ADD CONSTRAINT "fk_case_prosecutor__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_prosecutor" ADD CONSTRAINT "fk_case_prosecutor__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "filing" (
  "id" SERIAL PRIMARY KEY,
  "filedate" TIMESTAMP NOT NULL,
  "totalfees" DOUBLE PRECISION NOT NULL,
  "filing_attorney" INTEGER NOT NULL,
  "filing_prosecutor" INTEGER NOT NULL,
  "receiptnumber" TEXT,
  "receiptverified" BOOLEAN NOT NULL,
  "amountpaid" DOUBLE PRECISION NOT NULL,
  "feebalance" DOUBLE PRECISION NOT NULL
);

CREATE INDEX "idx_filing__filing_attorney" ON "filing" ("filing_attorney");

CREATE INDEX "idx_filing__filing_prosecutor" ON "filing" ("filing_prosecutor");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__filing_attorney" FOREIGN KEY ("filing_attorney") REFERENCES "attorney" ("id");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__filing_prosecutor" FOREIGN KEY ("filing_prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "causeofaction_filing" (
  "causeofaction" INTEGER NOT NULL,
  "filing" INTEGER NOT NULL,
  PRIMARY KEY ("causeofaction", "filing")
);

CREATE INDEX "idx_causeofaction_filing" ON "causeofaction_filing" ("filing");

ALTER TABLE "causeofaction_filing" ADD CONSTRAINT "fk_causeofaction_filing__causeofaction" FOREIGN KEY ("causeofaction") REFERENCES "causeofaction" ("id");

ALTER TABLE "causeofaction_filing" ADD CONSTRAINT "fk_causeofaction_filing__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

CREATE TABLE "document_filing" (
  "document" INTEGER NOT NULL,
  "filing" INTEGER NOT NULL,
  PRIMARY KEY ("document", "filing")
);

CREATE INDEX "idx_document_filing" ON "document_filing" ("filing");

ALTER TABLE "document_filing" ADD CONSTRAINT "fk_document_filing__document" FOREIGN KEY ("document") REFERENCES "document" ("id");

ALTER TABLE "document_filing" ADD CONSTRAINT "fk_document_filing__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

CREATE TABLE "filing_filingtype" (
  "filing" INTEGER NOT NULL,
  "filingtype" INTEGER NOT NULL,
  PRIMARY KEY ("filing", "filingtype")
);

CREATE INDEX "idx_filing_filingtype" ON "filing_filingtype" ("filingtype");

ALTER TABLE "filing_filingtype" ADD CONSTRAINT "fk_filing_filingtype__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

ALTER TABLE "filing_filingtype" ADD CONSTRAINT "fk_filing_filingtype__filingtype" FOREIGN KEY ("filingtype") REFERENCES "filingtype" ("id");

CREATE TABLE "prosecutorteam" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "prosecutor_prosecutorteam" (
  "prosecutor" INTEGER NOT NULL,
  "prosecutorteam" INTEGER NOT NULL,
  PRIMARY KEY ("prosecutor", "prosecutorteam")
);

CREATE INDEX "idx_prosecutor_prosecutorteam" ON "prosecutor_prosecutorteam" ("prosecutorteam");

ALTER TABLE "prosecutor_prosecutorteam" ADD CONSTRAINT "fk_prosecutor_prosecutorteam__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

ALTER TABLE "prosecutor_prosecutorteam" ADD CONSTRAINT "fk_prosecutor_prosecutorteam__prosecutorteam" FOREIGN KEY ("prosecutorteam") REFERENCES "prosecutorteam" ("id");

CREATE TABLE "subcounty" (
  "id" SERIAL PRIMARY KEY,
  "county" INTEGER NOT NULL
);

CREATE INDEX "idx_subcounty__county" ON "subcounty" ("county");

ALTER TABLE "subcounty" ADD CONSTRAINT "fk_subcounty__county" FOREIGN KEY ("county") REFERENCES "county" ("id");

CREATE TABLE "surety" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "town" (
  "id" SERIAL PRIMARY KEY,
  "subcounty" INTEGER NOT NULL
);

CREATE INDEX "idx_town__subcounty" ON "town" ("subcounty");

ALTER TABLE "town" ADD CONSTRAINT "fk_town__subcounty" FOREIGN KEY ("subcounty") REFERENCES "subcounty" ("id");

CREATE TABLE "constituency" (
  "id" SERIAL PRIMARY KEY,
  "county" INTEGER NOT NULL,
  "town" INTEGER
);

CREATE INDEX "idx_constituency__county" ON "constituency" ("county");

CREATE INDEX "idx_constituency__town" ON "constituency" ("town");

ALTER TABLE "constituency" ADD CONSTRAINT "fk_constituency__county" FOREIGN KEY ("county") REFERENCES "county" ("id");

ALTER TABLE "constituency" ADD CONSTRAINT "fk_constituency__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "court" (
  "id" SERIAL PRIMARY KEY,
  "town" INTEGER NOT NULL,
  "residentmagistrate" VARCHAR(100),
  "registrar" VARCHAR(100) NOT NULL,
  "court_level" INTEGER NOT NULL
);

CREATE INDEX "idx_court__court_level" ON "court" ("court_level");

CREATE INDEX "idx_court__town" ON "court" ("town");

ALTER TABLE "court" ADD CONSTRAINT "fk_court__court_level" FOREIGN KEY ("court_level") REFERENCES "courtlevel" ("id");

ALTER TABLE "court" ADD CONSTRAINT "fk_court__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "hearing" (
  "id" SERIAL PRIMARY KEY,
  "hearingdate" TIMESTAMP NOT NULL,
  "case" INTEGER NOT NULL,
  "court" INTEGER NOT NULL,
  "hearing_type" INTEGER NOT NULL,
  "remandwarrant" TEXT NOT NULL,
  "remandlength" INTEGER,
  "remanddate" DATE NOT NULL,
  "remandwarrantexpirydate" DATE NOT NULL,
  "nexthearingdate" DATE,
  "finalhearing" BOOLEAN NOT NULL
);

CREATE INDEX "idx_hearing__case" ON "hearing" ("case");

CREATE INDEX "idx_hearing__court" ON "hearing" ("court");

CREATE INDEX "idx_hearing__hearing_type" ON "hearing" ("hearing_type");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__hearing_type" FOREIGN KEY ("hearing_type") REFERENCES "hearingtype" ("id");

CREATE TABLE "attorney_hearing" (
  "attorney" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  PRIMARY KEY ("attorney", "hearing")
);

CREATE INDEX "idx_attorney_hearing" ON "attorney_hearing" ("hearing");

ALTER TABLE "attorney_hearing" ADD CONSTRAINT "fk_attorney_hearing__attorney" FOREIGN KEY ("attorney") REFERENCES "attorney" ("id");

ALTER TABLE "attorney_hearing" ADD CONSTRAINT "fk_attorney_hearing__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "bail" (
  "id" SERIAL PRIMARY KEY,
  "hearing" INTEGER NOT NULL,
  "defendant" INTEGER NOT NULL,
  "amountgranted" DOUBLE PRECISION NOT NULL,
  "noofsureties" INTEGER NOT NULL,
  "paid" BOOLEAN NOT NULL,
  "paydate" DATE NOT NULL,
  "receiptno" VARCHAR(100) NOT NULL
);

CREATE INDEX "idx_bail__defendant" ON "bail" ("defendant");

CREATE INDEX "idx_bail__hearing" ON "bail" ("hearing");

ALTER TABLE "bail" ADD CONSTRAINT "fk_bail__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

ALTER TABLE "bail" ADD CONSTRAINT "fk_bail__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "bail_surety" (
  "bail" INTEGER NOT NULL,
  "surety" INTEGER NOT NULL,
  PRIMARY KEY ("bail", "surety")
);

CREATE INDEX "idx_bail_surety" ON "bail_surety" ("surety");

ALTER TABLE "bail_surety" ADD CONSTRAINT "fk_bail_surety__bail" FOREIGN KEY ("bail") REFERENCES "bail" ("id");

ALTER TABLE "bail_surety" ADD CONSTRAINT "fk_bail_surety__surety" FOREIGN KEY ("surety") REFERENCES "surety" ("id");

CREATE TABLE "causeofaction_hearing" (
  "causeofaction" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  PRIMARY KEY ("causeofaction", "hearing")
);

CREATE INDEX "idx_causeofaction_hearing" ON "causeofaction_hearing" ("hearing");

ALTER TABLE "causeofaction_hearing" ADD CONSTRAINT "fk_causeofaction_hearing__causeofaction" FOREIGN KEY ("causeofaction") REFERENCES "causeofaction" ("id");

ALTER TABLE "causeofaction_hearing" ADD CONSTRAINT "fk_causeofaction_hearing__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "defendant_hearing" (
  "defendant" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  PRIMARY KEY ("defendant", "hearing")
);

CREATE INDEX "idx_defendant_hearing" ON "defendant_hearing" ("hearing");

ALTER TABLE "defendant_hearing" ADD CONSTRAINT "fk_defendant_hearing__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

ALTER TABLE "defendant_hearing" ADD CONSTRAINT "fk_defendant_hearing__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "filing_hearing" (
  "filing" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  PRIMARY KEY ("filing", "hearing")
);

CREATE INDEX "idx_filing_hearing" ON "filing_hearing" ("hearing");

ALTER TABLE "filing_hearing" ADD CONSTRAINT "fk_filing_hearing__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

ALTER TABLE "filing_hearing" ADD CONSTRAINT "fk_filing_hearing__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "hearing_policeman" (
  "hearing" INTEGER NOT NULL,
  "policeman" INTEGER NOT NULL,
  PRIMARY KEY ("hearing", "policeman")
);

CREATE INDEX "idx_hearing_policeman" ON "hearing_policeman" ("policeman");

ALTER TABLE "hearing_policeman" ADD CONSTRAINT "fk_hearing_policeman__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_policeman" ADD CONSTRAINT "fk_hearing_policeman__policeman" FOREIGN KEY ("policeman") REFERENCES "policeman" ("id");

CREATE TABLE "hearing_prosecutor" (
  "hearing" INTEGER NOT NULL,
  "prosecutor" INTEGER NOT NULL,
  PRIMARY KEY ("hearing", "prosecutor")
);

CREATE INDEX "idx_hearing_prosecutor" ON "hearing_prosecutor" ("prosecutor");

ALTER TABLE "hearing_prosecutor" ADD CONSTRAINT "fk_hearing_prosecutor__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_prosecutor" ADD CONSTRAINT "fk_hearing_prosecutor__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "judge" (
  "id" SERIAL PRIMARY KEY,
  "court" INTEGER NOT NULL
);

CREATE INDEX "idx_judge__court" ON "judge" ("court");

ALTER TABLE "judge" ADD CONSTRAINT "fk_judge__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

CREATE TABLE "hearing_judge" (
  "hearing" INTEGER NOT NULL,
  "judge" INTEGER NOT NULL,
  PRIMARY KEY ("hearing", "judge")
);

CREATE INDEX "idx_hearing_judge" ON "hearing_judge" ("judge");

ALTER TABLE "hearing_judge" ADD CONSTRAINT "fk_hearing_judge__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_judge" ADD CONSTRAINT "fk_hearing_judge__judge" FOREIGN KEY ("judge") REFERENCES "judge" ("id");

CREATE TABLE "policestation" (
  "id" SERIAL PRIMARY KEY,
  "town" INTEGER NOT NULL,
  "officercommanding" VARCHAR(100)
);

CREATE INDEX "idx_policestation__town" ON "policestation" ("town");

ALTER TABLE "policestation" ADD CONSTRAINT "fk_policestation__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "case_policestation" (
  "case" INTEGER NOT NULL,
  "policestation" INTEGER NOT NULL,
  PRIMARY KEY ("case", "policestation")
);

CREATE INDEX "idx_case_policestation" ON "case_policestation" ("policestation");

ALTER TABLE "case_policestation" ADD CONSTRAINT "fk_case_policestation__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_policestation" ADD CONSTRAINT "fk_case_policestation__policestation" FOREIGN KEY ("policestation") REFERENCES "policestation" ("id");

CREATE TABLE "prison" (
  "id" SERIAL PRIMARY KEY,
  "town" INTEGER NOT NULL,
  "warden" VARCHAR(100)
);

CREATE INDEX "idx_prison__town" ON "prison" ("town");

ALTER TABLE "prison" ADD CONSTRAINT "fk_prison__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "hearing_prison" (
  "hearing" INTEGER NOT NULL,
  "prison" INTEGER NOT NULL,
  PRIMARY KEY ("hearing", "prison")
);

CREATE INDEX "idx_hearing_prison" ON "hearing_prison" ("prison");

ALTER TABLE "hearing_prison" ADD CONSTRAINT "fk_hearing_prison__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_prison" ADD CONSTRAINT "fk_hearing_prison__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

CREATE TABLE "witness" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "case_witness" (
  "case" INTEGER NOT NULL,
  "witness" INTEGER NOT NULL,
  PRIMARY KEY ("case", "witness")
);

CREATE INDEX "idx_case_witness" ON "case_witness" ("witness");

ALTER TABLE "case_witness" ADD CONSTRAINT "fk_case_witness__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_witness" ADD CONSTRAINT "fk_case_witness__witness" FOREIGN KEY ("witness") REFERENCES "witness" ("id");

CREATE TABLE "hearing_witness" (
  "hearing" INTEGER NOT NULL,
  "witness" INTEGER NOT NULL,
  PRIMARY KEY ("hearing", "witness")
);

CREATE INDEX "idx_hearing_witness" ON "hearing_witness" ("witness");

ALTER TABLE "hearing_witness" ADD CONSTRAINT "fk_hearing_witness__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_witness" ADD CONSTRAINT "fk_hearing_witness__witness" FOREIGN KEY ("witness") REFERENCES "witness" ("id");

CREATE TABLE "investigation_witness" (
  "investigation" INTEGER NOT NULL,
  "witness" INTEGER NOT NULL,
  PRIMARY KEY ("investigation", "witness")
);

CREATE INDEX "idx_investigation_witness" ON "investigation_witness" ("witness");

ALTER TABLE "investigation_witness" ADD CONSTRAINT "fk_investigation_witness__investigation" FOREIGN KEY ("investigation") REFERENCES "investigation" ("id");

ALTER TABLE "investigation_witness" ADD CONSTRAINT "fk_investigation_witness__witness" FOREIGN KEY ("witness") REFERENCES "witness" ("id")
