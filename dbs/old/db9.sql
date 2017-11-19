CREATE TABLE "casecategory" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "casestatus" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "contact" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "courtlevel" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "document" (
  "id" SERIAL PRIMARY KEY,
  "document" BYTEA,
  "doc_content" TEXT NOT NULL,
  "doc_img" BYTEA NOT NULL,
  "doc_date" DATE NOT NULL
);

CREATE TABLE "feeschedule" (
  "id" SERIAL PRIMARY KEY,
  "amount" DOUBLE PRECISION NOT NULL
);

CREATE TABLE "gender" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "defendant" (
  "id" SERIAL PRIMARY KEY,
  "gender" INTEGER NOT NULL
);

CREATE INDEX "idx_defendant__gender" ON "defendant" ("gender");

ALTER TABLE "defendant" ADD CONSTRAINT "fk_defendant__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "hearingtype" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "lawfirm" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "attorney" (
  "id" SERIAL PRIMARY KEY,
  "bar_number" VARCHAR(20) NOT NULL,
  "call_to_bar_year" INTEGER NOT NULL,
  "lawfirm_member" INTEGER
);

CREATE INDEX "idx_attorney__lawfirm_member" ON "attorney" ("lawfirm_member");

ALTER TABLE "attorney" ADD CONSTRAINT "fk_attorney__lawfirm_member" FOREIGN KEY ("lawfirm_member") REFERENCES "lawfirm" ("id");

CREATE TABLE "offense" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "plaintiff" (
  "id" SERIAL PRIMARY KEY,
  "with_others" BOOLEAN NOT NULL,
  "gender" INTEGER NOT NULL
);

CREATE INDEX "idx_plaintiff__gender" ON "plaintiff" ("gender");

ALTER TABLE "plaintiff" ADD CONSTRAINT "fk_plaintiff__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

CREATE TABLE "contact_plaintiff" (
  "contact" INTEGER NOT NULL,
  "plaintiff" INTEGER NOT NULL,
  PRIMARY KEY ("contact", "plaintiff")
);

CREATE INDEX "idx_contact_plaintiff" ON "contact_plaintiff" ("plaintiff");

ALTER TABLE "contact_plaintiff" ADD CONSTRAINT "fk_contact_plaintiff__contact" FOREIGN KEY ("contact") REFERENCES "contact" ("id");

ALTER TABLE "contact_plaintiff" ADD CONSTRAINT "fk_contact_plaintiff__plaintiff" FOREIGN KEY ("plaintiff") REFERENCES "plaintiff" ("id");

CREATE TABLE "prosecutor" (
  "id" SERIAL PRIMARY KEY,
  "is_police" BOOLEAN NOT NULL
);

CREATE TABLE "region" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "district" (
  "id" SERIAL PRIMARY KEY,
  "region" INTEGER NOT NULL
);

CREATE INDEX "idx_district__region" ON "district" ("region");

ALTER TABLE "district" ADD CONSTRAINT "fk_district__region" FOREIGN KEY ("region") REFERENCES "region" ("id");

CREATE TABLE "surety" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "town" (
  "id" SERIAL PRIMARY KEY,
  "district" INTEGER NOT NULL
);

CREATE INDEX "idx_town__district" ON "town" ("district");

ALTER TABLE "town" ADD CONSTRAINT "fk_town__district" FOREIGN KEY ("district") REFERENCES "district" ("id");

CREATE TABLE "court" (
  "id" SERIAL PRIMARY KEY,
  "town" INTEGER NOT NULL,
  "court_level" INTEGER NOT NULL
);

CREATE INDEX "idx_court__court_level" ON "court" ("court_level");

CREATE INDEX "idx_court__town" ON "court" ("town");

ALTER TABLE "court" ADD CONSTRAINT "fk_court__court_level" FOREIGN KEY ("court_level") REFERENCES "courtlevel" ("id");

ALTER TABLE "court" ADD CONSTRAINT "fk_court__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "case" (
  "id" SERIAL PRIMARY KEY,
  "court" INTEGER NOT NULL,
  "case_number" VARCHAR(30) NOT NULL,
  "is_criminal" BOOLEAN NOT NULL,
  "case_category" INTEGER NOT NULL,
  "charge_date" TIMESTAMP NOT NULL
);

CREATE INDEX "idx_case__case_category" ON "case" ("case_category");

CREATE INDEX "idx_case__court" ON "case" ("court");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__case_category" FOREIGN KEY ("case_category") REFERENCES "casecategory" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

CREATE TABLE "attorney_case" (
  "attorney" INTEGER NOT NULL,
  "case" INTEGER NOT NULL,
  PRIMARY KEY ("attorney", "case")
);

CREATE INDEX "idx_attorney_case" ON "attorney_case" ("case");

ALTER TABLE "attorney_case" ADD CONSTRAINT "fk_attorney_case__attorney" FOREIGN KEY ("attorney") REFERENCES "attorney" ("id");

ALTER TABLE "attorney_case" ADD CONSTRAINT "fk_attorney_case__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

CREATE TABLE "bail" (
  "case" INTEGER PRIMARY KEY,
  "defendant" INTEGER NOT NULL,
  "amount" DOUBLE PRECISION NOT NULL,
  "surety_count" INTEGER NOT NULL,
  "paid" BOOLEAN NOT NULL,
  "paid_date" DATE NOT NULL,
  "receipt_number" TEXT NOT NULL
);

CREATE INDEX "idx_bail__defendant" ON "bail" ("defendant");

ALTER TABLE "bail" ADD CONSTRAINT "fk_bail__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "bail" ADD CONSTRAINT "fk_bail__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

CREATE TABLE "bail_surety" (
  "bail" INTEGER NOT NULL,
  "surety" INTEGER NOT NULL,
  PRIMARY KEY ("bail", "surety")
);

CREATE INDEX "idx_bail_surety" ON "bail_surety" ("surety");

ALTER TABLE "bail_surety" ADD CONSTRAINT "fk_bail_surety__bail" FOREIGN KEY ("bail") REFERENCES "bail" ("case");

ALTER TABLE "bail_surety" ADD CONSTRAINT "fk_bail_surety__surety" FOREIGN KEY ("surety") REFERENCES "surety" ("id");

CREATE TABLE "case_casestatus" (
  "case" INTEGER NOT NULL,
  "casestatus" INTEGER NOT NULL,
  PRIMARY KEY ("case", "casestatus")
);

CREATE INDEX "idx_case_casestatus" ON "case_casestatus" ("casestatus");

ALTER TABLE "case_casestatus" ADD CONSTRAINT "fk_case_casestatus__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_casestatus" ADD CONSTRAINT "fk_case_casestatus__casestatus" FOREIGN KEY ("casestatus") REFERENCES "casestatus" ("id");

CREATE TABLE "case_defendant" (
  "case" INTEGER NOT NULL,
  "defendant" INTEGER NOT NULL,
  PRIMARY KEY ("case", "defendant")
);

CREATE INDEX "idx_case_defendant" ON "case_defendant" ("defendant");

ALTER TABLE "case_defendant" ADD CONSTRAINT "fk_case_defendant__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_defendant" ADD CONSTRAINT "fk_case_defendant__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

CREATE TABLE "case_offense" (
  "case" INTEGER NOT NULL,
  "offense" INTEGER NOT NULL,
  PRIMARY KEY ("case", "offense")
);

CREATE INDEX "idx_case_offense" ON "case_offense" ("offense");

ALTER TABLE "case_offense" ADD CONSTRAINT "fk_case_offense__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_offense" ADD CONSTRAINT "fk_case_offense__offense" FOREIGN KEY ("offense") REFERENCES "offense" ("id");

CREATE TABLE "case_plaintiff" (
  "case" INTEGER NOT NULL,
  "plaintiff" INTEGER NOT NULL,
  PRIMARY KEY ("case", "plaintiff")
);

CREATE INDEX "idx_case_plaintiff" ON "case_plaintiff" ("plaintiff");

ALTER TABLE "case_plaintiff" ADD CONSTRAINT "fk_case_plaintiff__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_plaintiff" ADD CONSTRAINT "fk_case_plaintiff__plaintiff" FOREIGN KEY ("plaintiff") REFERENCES "plaintiff" ("id");

CREATE TABLE "case_prosecutor" (
  "case" INTEGER NOT NULL,
  "prosecutor" INTEGER NOT NULL,
  PRIMARY KEY ("case", "prosecutor")
);

CREATE INDEX "idx_case_prosecutor" ON "case_prosecutor" ("prosecutor");

ALTER TABLE "case_prosecutor" ADD CONSTRAINT "fk_case_prosecutor__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_prosecutor" ADD CONSTRAINT "fk_case_prosecutor__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "complaint" (
  "id" SERIAL PRIMARY KEY,
  "complaint_date" TIMESTAMP NOT NULL,
  "is_case" BOOLEAN,
  "case" INTEGER,
  "notes" TEXT NOT NULL
);

CREATE INDEX "idx_complaint__case" ON "complaint" ("case");

ALTER TABLE "complaint" ADD CONSTRAINT "fk_complaint__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

CREATE TABLE "complaint_defendant" (
  "complaint" INTEGER NOT NULL,
  "defendant" INTEGER NOT NULL,
  PRIMARY KEY ("complaint", "defendant")
);

CREATE INDEX "idx_complaint_defendant" ON "complaint_defendant" ("defendant");

ALTER TABLE "complaint_defendant" ADD CONSTRAINT "fk_complaint_defendant__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

ALTER TABLE "complaint_defendant" ADD CONSTRAINT "fk_complaint_defendant__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

CREATE TABLE "complaint_plaintiff" (
  "complaint" INTEGER NOT NULL,
  "plaintiff" INTEGER NOT NULL,
  PRIMARY KEY ("complaint", "plaintiff")
);

CREATE INDEX "idx_complaint_plaintiff" ON "complaint_plaintiff" ("plaintiff");

ALTER TABLE "complaint_plaintiff" ADD CONSTRAINT "fk_complaint_plaintiff__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

ALTER TABLE "complaint_plaintiff" ADD CONSTRAINT "fk_complaint_plaintiff__plaintiff" FOREIGN KEY ("plaintiff") REFERENCES "plaintiff" ("id");

CREATE TABLE "judge" (
  "id" SERIAL PRIMARY KEY,
  "court" INTEGER NOT NULL,
  "court_level" INTEGER NOT NULL,
  "appelation" VARCHAR(100) NOT NULL
);

CREATE INDEX "idx_judge__court" ON "judge" ("court");

CREATE INDEX "idx_judge__court_level" ON "judge" ("court_level");

ALTER TABLE "judge" ADD CONSTRAINT "fk_judge__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

ALTER TABLE "judge" ADD CONSTRAINT "fk_judge__court_level" FOREIGN KEY ("court_level") REFERENCES "courtlevel" ("id");

CREATE TABLE "case_judge" (
  "case" INTEGER NOT NULL,
  "judge" INTEGER NOT NULL,
  PRIMARY KEY ("case", "judge")
);

CREATE INDEX "idx_case_judge" ON "case_judge" ("judge");

ALTER TABLE "case_judge" ADD CONSTRAINT "fk_case_judge__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_judge" ADD CONSTRAINT "fk_case_judge__judge" FOREIGN KEY ("judge") REFERENCES "judge" ("id");

CREATE TABLE "policestation" (
  "id" SERIAL PRIMARY KEY,
  "town" INTEGER NOT NULL
);

CREATE INDEX "idx_policestation__town" ON "policestation" ("town");

ALTER TABLE "policestation" ADD CONSTRAINT "fk_policestation__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "policeman" (
  "id" SERIAL PRIMARY KEY,
  "service_number" VARCHAR(50) NOT NULL,
  "rank" VARCHAR(40) NOT NULL,
  "police_station" INTEGER NOT NULL
);

CREATE INDEX "idx_policeman__police_station" ON "policeman" ("police_station");

ALTER TABLE "policeman" ADD CONSTRAINT "fk_policeman__police_station" FOREIGN KEY ("police_station") REFERENCES "policestation" ("id");

CREATE TABLE "case_policeman" (
  "case" INTEGER NOT NULL,
  "policeman" INTEGER NOT NULL,
  PRIMARY KEY ("case", "policeman")
);

CREATE INDEX "idx_case_policeman" ON "case_policeman" ("policeman");

ALTER TABLE "case_policeman" ADD CONSTRAINT "fk_case_policeman__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_policeman" ADD CONSTRAINT "fk_case_policeman__policeman" FOREIGN KEY ("policeman") REFERENCES "policeman" ("id");

CREATE TABLE "complaint_policeman" (
  "complaint" INTEGER NOT NULL,
  "policeman" INTEGER NOT NULL,
  PRIMARY KEY ("complaint", "policeman")
);

CREATE INDEX "idx_complaint_policeman" ON "complaint_policeman" ("policeman");

ALTER TABLE "complaint_policeman" ADD CONSTRAINT "fk_complaint_policeman__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

ALTER TABLE "complaint_policeman" ADD CONSTRAINT "fk_complaint_policeman__policeman" FOREIGN KEY ("policeman") REFERENCES "policeman" ("id");

CREATE TABLE "prison" (
  "id" SERIAL PRIMARY KEY,
  "town" INTEGER NOT NULL,
  "warden" VARCHAR(50) NOT NULL
);

CREATE INDEX "idx_prison__town" ON "prison" ("town");

ALTER TABLE "prison" ADD CONSTRAINT "fk_prison__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "casehearing" (
  "case" INTEGER PRIMARY KEY,
  "hearingtype" INTEGER NOT NULL,
  "hearing_date" TIMESTAMP NOT NULL,
  "prosecutor_present" BOOLEAN NOT NULL,
  "defense_attorney_present" BOOLEAN NOT NULL,
  "case_outcome" TEXT NOT NULL,
  "prison" INTEGER NOT NULL,
  "from_remand" BOOLEAN NOT NULL,
  "to_remand" BOOLEAN NOT NULL,
  "to_prison" BOOLEAN NOT NULL,
  "bail" INTEGER NOT NULL,
  "notes" TEXT NOT NULL
);

CREATE INDEX "idx_casehearing__bail" ON "casehearing" ("bail");

CREATE INDEX "idx_casehearing__hearingtype" ON "casehearing" ("hearingtype");

CREATE INDEX "idx_casehearing__prison" ON "casehearing" ("prison");

ALTER TABLE "casehearing" ADD CONSTRAINT "fk_casehearing__bail" FOREIGN KEY ("bail") REFERENCES "bail" ("case");

ALTER TABLE "casehearing" ADD CONSTRAINT "fk_casehearing__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "casehearing" ADD CONSTRAINT "fk_casehearing__hearingtype" FOREIGN KEY ("hearingtype") REFERENCES "hearingtype" ("id");

ALTER TABLE "casehearing" ADD CONSTRAINT "fk_casehearing__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

CREATE TABLE "attorney_casehearing" (
  "attorney" INTEGER NOT NULL,
  "casehearing" INTEGER NOT NULL,
  PRIMARY KEY ("attorney", "casehearing")
);

CREATE INDEX "idx_attorney_casehearing" ON "attorney_casehearing" ("casehearing");

ALTER TABLE "attorney_casehearing" ADD CONSTRAINT "fk_attorney_casehearing__attorney" FOREIGN KEY ("attorney") REFERENCES "attorney" ("id");

ALTER TABLE "attorney_casehearing" ADD CONSTRAINT "fk_attorney_casehearing__casehearing" FOREIGN KEY ("casehearing") REFERENCES "casehearing" ("case");

CREATE TABLE "casehearing_defendant" (
  "casehearing" INTEGER NOT NULL,
  "defendant" INTEGER NOT NULL,
  PRIMARY KEY ("casehearing", "defendant")
);

CREATE INDEX "idx_casehearing_defendant" ON "casehearing_defendant" ("defendant");

ALTER TABLE "casehearing_defendant" ADD CONSTRAINT "fk_casehearing_defendant__casehearing" FOREIGN KEY ("casehearing") REFERENCES "casehearing" ("case");

ALTER TABLE "casehearing_defendant" ADD CONSTRAINT "fk_casehearing_defendant__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

CREATE TABLE "casehearing_judge" (
  "casehearing" INTEGER NOT NULL,
  "judge" INTEGER NOT NULL,
  PRIMARY KEY ("casehearing", "judge")
);

CREATE INDEX "idx_casehearing_judge" ON "casehearing_judge" ("judge");

ALTER TABLE "casehearing_judge" ADD CONSTRAINT "fk_casehearing_judge__casehearing" FOREIGN KEY ("casehearing") REFERENCES "casehearing" ("case");

ALTER TABLE "casehearing_judge" ADD CONSTRAINT "fk_casehearing_judge__judge" FOREIGN KEY ("judge") REFERENCES "judge" ("id");

CREATE TABLE "casehearing_plaintiff" (
  "casehearing" INTEGER NOT NULL,
  "plaintiff" INTEGER NOT NULL,
  PRIMARY KEY ("casehearing", "plaintiff")
);

CREATE INDEX "idx_casehearing_plaintiff" ON "casehearing_plaintiff" ("plaintiff");

ALTER TABLE "casehearing_plaintiff" ADD CONSTRAINT "fk_casehearing_plaintiff__casehearing" FOREIGN KEY ("casehearing") REFERENCES "casehearing" ("case");

ALTER TABLE "casehearing_plaintiff" ADD CONSTRAINT "fk_casehearing_plaintiff__plaintiff" FOREIGN KEY ("plaintiff") REFERENCES "plaintiff" ("id");

CREATE TABLE "casehearing_policeman" (
  "casehearing" INTEGER NOT NULL,
  "policeman" INTEGER NOT NULL,
  PRIMARY KEY ("casehearing", "policeman")
);

CREATE INDEX "idx_casehearing_policeman" ON "casehearing_policeman" ("policeman");

ALTER TABLE "casehearing_policeman" ADD CONSTRAINT "fk_casehearing_policeman__casehearing" FOREIGN KEY ("casehearing") REFERENCES "casehearing" ("case");

ALTER TABLE "casehearing_policeman" ADD CONSTRAINT "fk_casehearing_policeman__policeman" FOREIGN KEY ("policeman") REFERENCES "policeman" ("id");

CREATE TABLE "casehearing_prosecutor" (
  "casehearing" INTEGER NOT NULL,
  "prosecutor" INTEGER NOT NULL,
  PRIMARY KEY ("casehearing", "prosecutor")
);

CREATE INDEX "idx_casehearing_prosecutor" ON "casehearing_prosecutor" ("prosecutor");

ALTER TABLE "casehearing_prosecutor" ADD CONSTRAINT "fk_casehearing_prosecutor__casehearing" FOREIGN KEY ("casehearing") REFERENCES "casehearing" ("case");

ALTER TABLE "casehearing_prosecutor" ADD CONSTRAINT "fk_casehearing_prosecutor__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "prosecutor" ("id");

CREATE TABLE "defendant_prison" (
  "defendant" INTEGER NOT NULL,
  "prison" INTEGER NOT NULL,
  PRIMARY KEY ("defendant", "prison")
);

CREATE INDEX "idx_defendant_prison" ON "defendant_prison" ("prison");

ALTER TABLE "defendant_prison" ADD CONSTRAINT "fk_defendant_prison__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

ALTER TABLE "defendant_prison" ADD CONSTRAINT "fk_defendant_prison__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

CREATE TABLE "filing" (
  "id" SERIAL PRIMARY KEY,
  "case" INTEGER NOT NULL,
  "filing_date" TIMESTAMP NOT NULL,
  "doc_name" VARCHAR(50) NOT NULL,
  "doc_content" TEXT NOT NULL,
  "case_hearing" INTEGER NOT NULL,
  "filing_fee" DOUBLE PRECISION NOT NULL,
  "receipt_number" VARCHAR(20) NOT NULL,
  "received_by" VARCHAR(50) NOT NULL
);

CREATE INDEX "idx_filing__case" ON "filing" ("case");

CREATE INDEX "idx_filing__case_hearing" ON "filing" ("case_hearing");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__case_hearing" FOREIGN KEY ("case_hearing") REFERENCES "casehearing" ("case");

CREATE TABLE "defendant_filing" (
  "defendant" INTEGER NOT NULL,
  "filing" INTEGER NOT NULL,
  PRIMARY KEY ("defendant", "filing")
);

CREATE INDEX "idx_defendant_filing" ON "defendant_filing" ("filing");

ALTER TABLE "defendant_filing" ADD CONSTRAINT "fk_defendant_filing__defendant" FOREIGN KEY ("defendant") REFERENCES "defendant" ("id");

ALTER TABLE "defendant_filing" ADD CONSTRAINT "fk_defendant_filing__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

CREATE TABLE "document_filing" (
  "document" INTEGER NOT NULL,
  "filing" INTEGER NOT NULL,
  PRIMARY KEY ("document", "filing")
);

CREATE INDEX "idx_document_filing" ON "document_filing" ("filing");

ALTER TABLE "document_filing" ADD CONSTRAINT "fk_document_filing__document" FOREIGN KEY ("document") REFERENCES "document" ("id");

ALTER TABLE "document_filing" ADD CONSTRAINT "fk_document_filing__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

CREATE TABLE "feeschedule_filing" (
  "feeschedule" INTEGER NOT NULL,
  "filing" INTEGER NOT NULL,
  PRIMARY KEY ("feeschedule", "filing")
);

CREATE INDEX "idx_feeschedule_filing" ON "feeschedule_filing" ("filing");

ALTER TABLE "feeschedule_filing" ADD CONSTRAINT "fk_feeschedule_filing__feeschedule" FOREIGN KEY ("feeschedule") REFERENCES "feeschedule" ("id");

ALTER TABLE "feeschedule_filing" ADD CONSTRAINT "fk_feeschedule_filing__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

CREATE TABLE "filing_plaintiff" (
  "filing" INTEGER NOT NULL,
  "plaintiff" INTEGER NOT NULL,
  PRIMARY KEY ("filing", "plaintiff")
);

CREATE INDEX "idx_filing_plaintiff" ON "filing_plaintiff" ("plaintiff");

ALTER TABLE "filing_plaintiff" ADD CONSTRAINT "fk_filing_plaintiff__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

ALTER TABLE "filing_plaintiff" ADD CONSTRAINT "fk_filing_plaintiff__plaintiff" FOREIGN KEY ("plaintiff") REFERENCES "plaintiff" ("id");

CREATE TABLE "witness" (
  "id" SERIAL PRIMARY KEY,
  "special" BOOLEAN NOT NULL,
  "role" VARCHAR(100) NOT NULL,
  "for_defense" BOOLEAN NOT NULL
);

CREATE TABLE "case_witness" (
  "case" INTEGER NOT NULL,
  "witness" INTEGER NOT NULL,
  PRIMARY KEY ("case", "witness")
);

CREATE INDEX "idx_case_witness" ON "case_witness" ("witness");

ALTER TABLE "case_witness" ADD CONSTRAINT "fk_case_witness__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_witness" ADD CONSTRAINT "fk_case_witness__witness" FOREIGN KEY ("witness") REFERENCES "witness" ("id");

CREATE TABLE "casehearing_witness" (
  "casehearing" INTEGER NOT NULL,
  "witness" INTEGER NOT NULL,
  PRIMARY KEY ("casehearing", "witness")
);

CREATE INDEX "idx_casehearing_witness" ON "casehearing_witness" ("witness");

ALTER TABLE "casehearing_witness" ADD CONSTRAINT "fk_casehearing_witness__casehearing" FOREIGN KEY ("casehearing") REFERENCES "casehearing" ("case");

ALTER TABLE "casehearing_witness" ADD CONSTRAINT "fk_casehearing_witness__witness" FOREIGN KEY ("witness") REFERENCES "witness" ("id")
