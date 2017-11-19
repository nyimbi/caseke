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

CREATE TABLE "hearingtype" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "lawfirm" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "offense" (
  "id" SERIAL PRIMARY KEY
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
  "id" INTEGER NOT NULL,
  "court" INTEGER NOT NULL,
  "case_name" VARCHAR(150) NOT NULL,
  "case_number" VARCHAR(30) NOT NULL,
  "is_criminal" BOOLEAN NOT NULL,
  "case_category" INTEGER NOT NULL,
  "charge_date" TIMESTAMP NOT NULL,
  PRIMARY KEY ("id", "case_name", "case_number")
);

CREATE INDEX "idx_case__case_category" ON "case" ("case_category");

CREATE INDEX "idx_case__court" ON "case" ("court");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__case_category" FOREIGN KEY ("case_category") REFERENCES "casecategory" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

CREATE TABLE "case_offense" (
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  "offense" INTEGER NOT NULL,
  PRIMARY KEY ("case_id", "case_case_name", "case_case_number", "offense")
);

CREATE INDEX "idx_case_offense" ON "case_offense" ("offense");

ALTER TABLE "case_offense" ADD CONSTRAINT "fk_case_offense__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

ALTER TABLE "case_offense" ADD CONSTRAINT "fk_case_offense__offense" FOREIGN KEY ("offense") REFERENCES "offense" ("id");

CREATE TABLE "case_status_change" (
  "casestatus" INTEGER NOT NULL,
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  "csc_date" TIMESTAMP NOT NULL,
  "notes" TEXT NOT NULL,
  PRIMARY KEY ("casestatus", "case_id", "case_case_name", "case_case_number", "csc_date")
);

CREATE INDEX "idx_case_status_change__case_id_case_case_name_case_case_number" ON "case_status_change" ("case_id", "case_case_name", "case_case_number");

ALTER TABLE "case_status_change" ADD CONSTRAINT "fk_case_status_change__case_id__case_case_name__case_case_numbe" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

ALTER TABLE "case_status_change" ADD CONSTRAINT "fk_case_status_change__casestatus" FOREIGN KEY ("casestatus") REFERENCES "casestatus" ("id");

CREATE TABLE "complaint" (
  "id" SERIAL PRIMARY KEY,
  "complaint_date" TIMESTAMP NOT NULL,
  "is_case" BOOLEAN,
  "case_id" INTEGER,
  "case_case_name" VARCHAR(150),
  "case_case_number" VARCHAR(30),
  "notes" TEXT NOT NULL
);

CREATE INDEX "idx_complaint__case_id_case_case_name_case_case_number" ON "complaint" ("case_id", "case_case_name", "case_case_number");

ALTER TABLE "complaint" ADD CONSTRAINT "fk_complaint__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

CREATE TABLE "person" (
  "id" SERIAL PRIMARY KEY,
  "gender" INTEGER NOT NULL,
  "date_of_birth" DATE NOT NULL,
  "identity" TEXT NOT NULL,
  "address" TEXT NOT NULL,
  "biometrics" TEXT NOT NULL,
  "classtype" TEXT NOT NULL,
  "with_others" BOOLEAN,
  "remanded" BOOLEAN,
  "court" INTEGER,
  "court_level" INTEGER,
  "appelation" VARCHAR(100),
  "is_police" BOOLEAN,
  "law_firm" VARCHAR(100),
  "bar_number" VARCHAR(20),
  "call_to_bar_year" INTEGER,
  "member_law_firm" INTEGER,
  "special" BOOLEAN,
  "role" VARCHAR(100),
  "for_defense" BOOLEAN,
  "how_many" INTEGER,
  "arrested" BOOLEAN,
  "arrest_date" DATE,
  "service_number" VARCHAR(50),
  "rank" VARCHAR(40)
);

CREATE INDEX "idx_person__court" ON "person" ("court");

CREATE INDEX "idx_person__court_level" ON "person" ("court_level");

CREATE INDEX "idx_person__gender" ON "person" ("gender");

CREATE INDEX "idx_person__member_law_firm" ON "person" ("member_law_firm");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__court_level" FOREIGN KEY ("court_level") REFERENCES "courtlevel" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__member_law_firm" FOREIGN KEY ("member_law_firm") REFERENCES "lawfirm" ("id");

CREATE TABLE "attorney_case" (
  "attorney" INTEGER NOT NULL,
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  PRIMARY KEY ("attorney", "case_id", "case_case_name", "case_case_number")
);

CREATE INDEX "idx_attorney_case" ON "attorney_case" ("case_id", "case_case_name", "case_case_number");

ALTER TABLE "attorney_case" ADD CONSTRAINT "fk_attorney_case__attorney" FOREIGN KEY ("attorney") REFERENCES "person" ("id");

ALTER TABLE "attorney_case" ADD CONSTRAINT "fk_attorney_case__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

CREATE TABLE "bail" (
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  "defendant" INTEGER NOT NULL,
  "amount" DOUBLE PRECISION NOT NULL,
  "surety_count" INTEGER NOT NULL,
  "paid" BOOLEAN NOT NULL,
  "paid_date" DATE NOT NULL,
  "receipt_number" TEXT NOT NULL,
  PRIMARY KEY ("case_id", "case_case_name", "case_case_number", "defendant")
);

CREATE INDEX "idx_bail__defendant" ON "bail" ("defendant");

ALTER TABLE "bail" ADD CONSTRAINT "fk_bail__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

ALTER TABLE "bail" ADD CONSTRAINT "fk_bail__defendant" FOREIGN KEY ("defendant") REFERENCES "person" ("id");

CREATE TABLE "bail_surety" (
  "bail_case_id" INTEGER NOT NULL,
  "bail_case_case_name" VARCHAR(150) NOT NULL,
  "bail_case_case_number" VARCHAR(30) NOT NULL,
  "bail_defendant" INTEGER NOT NULL,
  "surety" INTEGER NOT NULL,
  PRIMARY KEY ("bail_case_id", "bail_case_case_name", "bail_case_case_number", "bail_defendant", "surety")
);

CREATE INDEX "idx_bail_surety" ON "bail_surety" ("surety");

ALTER TABLE "bail_surety" ADD CONSTRAINT "fk_bail_surety__bail_case_id__bail_case_case_name__bail_case_ca" FOREIGN KEY ("bail_case_id", "bail_case_case_name", "bail_case_case_number", "bail_defendant") REFERENCES "bail" ("case_id", "case_case_name", "case_case_number", "defendant");

ALTER TABLE "bail_surety" ADD CONSTRAINT "fk_bail_surety__surety" FOREIGN KEY ("surety") REFERENCES "person" ("id");

CREATE TABLE "case_defendant" (
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  "defendant" INTEGER NOT NULL,
  PRIMARY KEY ("case_id", "case_case_name", "case_case_number", "defendant")
);

CREATE INDEX "idx_case_defendant" ON "case_defendant" ("defendant");

ALTER TABLE "case_defendant" ADD CONSTRAINT "fk_case_defendant__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

ALTER TABLE "case_defendant" ADD CONSTRAINT "fk_case_defendant__defendant" FOREIGN KEY ("defendant") REFERENCES "person" ("id");

CREATE TABLE "case_judge" (
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  "judge" INTEGER NOT NULL,
  PRIMARY KEY ("case_id", "case_case_name", "case_case_number", "judge")
);

CREATE INDEX "idx_case_judge" ON "case_judge" ("judge");

ALTER TABLE "case_judge" ADD CONSTRAINT "fk_case_judge__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

ALTER TABLE "case_judge" ADD CONSTRAINT "fk_case_judge__judge" FOREIGN KEY ("judge") REFERENCES "person" ("id");

CREATE TABLE "case_plaintiff" (
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  "plaintiff" INTEGER NOT NULL,
  PRIMARY KEY ("case_id", "case_case_name", "case_case_number", "plaintiff")
);

CREATE INDEX "idx_case_plaintiff" ON "case_plaintiff" ("plaintiff");

ALTER TABLE "case_plaintiff" ADD CONSTRAINT "fk_case_plaintiff__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

ALTER TABLE "case_plaintiff" ADD CONSTRAINT "fk_case_plaintiff__plaintiff" FOREIGN KEY ("plaintiff") REFERENCES "person" ("id");

CREATE TABLE "case_policeman" (
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  "policeman" INTEGER NOT NULL,
  PRIMARY KEY ("case_id", "case_case_name", "case_case_number", "policeman")
);

CREATE INDEX "idx_case_policeman" ON "case_policeman" ("policeman");

ALTER TABLE "case_policeman" ADD CONSTRAINT "fk_case_policeman__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

ALTER TABLE "case_policeman" ADD CONSTRAINT "fk_case_policeman__policeman" FOREIGN KEY ("policeman") REFERENCES "person" ("id");

CREATE TABLE "case_prosecutor" (
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  "prosecutor" INTEGER NOT NULL,
  PRIMARY KEY ("case_id", "case_case_name", "case_case_number", "prosecutor")
);

CREATE INDEX "idx_case_prosecutor" ON "case_prosecutor" ("prosecutor");

ALTER TABLE "case_prosecutor" ADD CONSTRAINT "fk_case_prosecutor__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

ALTER TABLE "case_prosecutor" ADD CONSTRAINT "fk_case_prosecutor__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "person" ("id");

CREATE TABLE "case_witness" (
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  "witness" INTEGER NOT NULL,
  PRIMARY KEY ("case_id", "case_case_name", "case_case_number", "witness")
);

CREATE INDEX "idx_case_witness" ON "case_witness" ("witness");

ALTER TABLE "case_witness" ADD CONSTRAINT "fk_case_witness__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

ALTER TABLE "case_witness" ADD CONSTRAINT "fk_case_witness__witness" FOREIGN KEY ("witness") REFERENCES "person" ("id");

CREATE TABLE "complainant_complaint" (
  "complainant" INTEGER NOT NULL,
  "complaint" INTEGER NOT NULL,
  PRIMARY KEY ("complainant", "complaint")
);

CREATE INDEX "idx_complainant_complaint" ON "complainant_complaint" ("complaint");

ALTER TABLE "complainant_complaint" ADD CONSTRAINT "fk_complainant_complaint__complainant" FOREIGN KEY ("complainant") REFERENCES "person" ("id");

ALTER TABLE "complainant_complaint" ADD CONSTRAINT "fk_complainant_complaint__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

CREATE TABLE "complaint_offender" (
  "complaint" INTEGER NOT NULL,
  "offender" INTEGER NOT NULL,
  PRIMARY KEY ("complaint", "offender")
);

CREATE INDEX "idx_complaint_offender" ON "complaint_offender" ("offender");

ALTER TABLE "complaint_offender" ADD CONSTRAINT "fk_complaint_offender__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

ALTER TABLE "complaint_offender" ADD CONSTRAINT "fk_complaint_offender__offender" FOREIGN KEY ("offender") REFERENCES "person" ("id");

CREATE TABLE "complaint_policeman" (
  "complaint" INTEGER NOT NULL,
  "policeman" INTEGER NOT NULL,
  PRIMARY KEY ("complaint", "policeman")
);

CREATE INDEX "idx_complaint_policeman" ON "complaint_policeman" ("policeman");

ALTER TABLE "complaint_policeman" ADD CONSTRAINT "fk_complaint_policeman__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

ALTER TABLE "complaint_policeman" ADD CONSTRAINT "fk_complaint_policeman__policeman" FOREIGN KEY ("policeman") REFERENCES "person" ("id");

CREATE TABLE "contact_plaintiff" (
  "contact" INTEGER NOT NULL,
  "plaintiff" INTEGER NOT NULL,
  PRIMARY KEY ("contact", "plaintiff")
);

CREATE INDEX "idx_contact_plaintiff" ON "contact_plaintiff" ("plaintiff");

ALTER TABLE "contact_plaintiff" ADD CONSTRAINT "fk_contact_plaintiff__contact" FOREIGN KEY ("contact") REFERENCES "contact" ("id");

ALTER TABLE "contact_plaintiff" ADD CONSTRAINT "fk_contact_plaintiff__plaintiff" FOREIGN KEY ("plaintiff") REFERENCES "person" ("id");

CREATE TABLE "policestation" (
  "id" SERIAL PRIMARY KEY,
  "town" INTEGER NOT NULL
);

CREATE INDEX "idx_policestation__town" ON "policestation" ("town");

ALTER TABLE "policestation" ADD CONSTRAINT "fk_policestation__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "prison" (
  "id" SERIAL PRIMARY KEY,
  "town" INTEGER NOT NULL,
  "warden" VARCHAR(50) NOT NULL
);

CREATE INDEX "idx_prison__town" ON "prison" ("town");

ALTER TABLE "prison" ADD CONSTRAINT "fk_prison__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "case_hearing" (
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  "hearingtype" INTEGER NOT NULL,
  "hearing_date" TIMESTAMP NOT NULL,
  "prosecutor_present" BOOLEAN NOT NULL,
  "defense_attorney_present" BOOLEAN NOT NULL,
  "case_outcome" TEXT NOT NULL,
  "prison" INTEGER NOT NULL,
  "from_remand" BOOLEAN NOT NULL,
  "to_remand" BOOLEAN NOT NULL,
  "to_prison" BOOLEAN NOT NULL,
  "bail_case_id" INTEGER NOT NULL,
  "bail_case_case_name" VARCHAR(150) NOT NULL,
  "bail_case_case_number" VARCHAR(30) NOT NULL,
  "bail_defendant" INTEGER NOT NULL,
  "notes" TEXT NOT NULL,
  PRIMARY KEY ("case_id", "case_case_name", "case_case_number", "hearingtype", "hearing_date")
);

CREATE INDEX "idx_case_hearing__bail_case_id_bail_case_case_name_bail_case_ca" ON "case_hearing" ("bail_case_id", "bail_case_case_name", "bail_case_case_number", "bail_defendant");

CREATE INDEX "idx_case_hearing__hearingtype" ON "case_hearing" ("hearingtype");

CREATE INDEX "idx_case_hearing__prison" ON "case_hearing" ("prison");

ALTER TABLE "case_hearing" ADD CONSTRAINT "fk_case_hearing__bail_case_id__bail_case_case_name__bail_case_c" FOREIGN KEY ("bail_case_id", "bail_case_case_name", "bail_case_case_number", "bail_defendant") REFERENCES "bail" ("case_id", "case_case_name", "case_case_number", "defendant");

ALTER TABLE "case_hearing" ADD CONSTRAINT "fk_case_hearing__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

ALTER TABLE "case_hearing" ADD CONSTRAINT "fk_case_hearing__hearingtype" FOREIGN KEY ("hearingtype") REFERENCES "hearingtype" ("id");

ALTER TABLE "case_hearing" ADD CONSTRAINT "fk_case_hearing__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

CREATE TABLE "attorney_case_hearing" (
  "attorney" INTEGER NOT NULL,
  "case_hearing_case_id" INTEGER NOT NULL,
  "case_hearing_case_case_name" VARCHAR(150) NOT NULL,
  "case_hearing_case_case_number" VARCHAR(30) NOT NULL,
  "case_hearing_hearingtype" INTEGER NOT NULL,
  "case_hearing_hearing_date" TIMESTAMP NOT NULL,
  PRIMARY KEY ("attorney", "case_hearing_case_id", "case_hearing_case_case_name", "case_hearing_case_case_number", "case_hearing_hearingtype", "case_hearing_hearing_date")
);

CREATE INDEX "idx_attorney_case_hearing" ON "attorney_case_hearing" ("case_hearing_case_id", "case_hearing_case_case_name", "case_hearing_case_case_number", "case_hearing_hearingtype", "case_hearing_hearing_date");

ALTER TABLE "attorney_case_hearing" ADD CONSTRAINT "fk_attorney_case_hearing__attorney" FOREIGN KEY ("attorney") REFERENCES "person" ("id");

ALTER TABLE "attorney_case_hearing" ADD CONSTRAINT "fk_attorney_case_hearing__case_hearing_case_id__case_hearing_ca" FOREIGN KEY ("case_hearing_case_id", "case_hearing_case_case_name", "case_hearing_case_case_number", "case_hearing_hearingtype", "case_hearing_hearing_date") REFERENCES "case_hearing" ("case_id", "case_case_name", "case_case_number", "hearingtype", "hearing_date");

CREATE TABLE "case_hearing_judge" (
  "case_hearing_case_id" INTEGER NOT NULL,
  "case_hearing_case_case_name" VARCHAR(150) NOT NULL,
  "case_hearing_case_case_number" VARCHAR(30) NOT NULL,
  "case_hearing_hearingtype" INTEGER NOT NULL,
  "case_hearing_hearing_date" TIMESTAMP NOT NULL,
  "judge" INTEGER NOT NULL,
  PRIMARY KEY ("case_hearing_case_id", "case_hearing_case_case_name", "case_hearing_case_case_number", "case_hearing_hearingtype", "case_hearing_hearing_date", "judge")
);

CREATE INDEX "idx_case_hearing_judge" ON "case_hearing_judge" ("judge");

ALTER TABLE "case_hearing_judge" ADD CONSTRAINT "fk_case_hearing_judge__case_hearing_case_id__case_hearing_case_" FOREIGN KEY ("case_hearing_case_id", "case_hearing_case_case_name", "case_hearing_case_case_number", "case_hearing_hearingtype", "case_hearing_hearing_date") REFERENCES "case_hearing" ("case_id", "case_case_name", "case_case_number", "hearingtype", "hearing_date");

ALTER TABLE "case_hearing_judge" ADD CONSTRAINT "fk_case_hearing_judge__judge" FOREIGN KEY ("judge") REFERENCES "person" ("id");

CREATE TABLE "case_hearing_prosecutor" (
  "case_hearing_case_id" INTEGER NOT NULL,
  "case_hearing_case_case_name" VARCHAR(150) NOT NULL,
  "case_hearing_case_case_number" VARCHAR(30) NOT NULL,
  "case_hearing_hearingtype" INTEGER NOT NULL,
  "case_hearing_hearing_date" TIMESTAMP NOT NULL,
  "prosecutor" INTEGER NOT NULL,
  PRIMARY KEY ("case_hearing_case_id", "case_hearing_case_case_name", "case_hearing_case_case_number", "case_hearing_hearingtype", "case_hearing_hearing_date", "prosecutor")
);

CREATE INDEX "idx_case_hearing_prosecutor" ON "case_hearing_prosecutor" ("prosecutor");

ALTER TABLE "case_hearing_prosecutor" ADD CONSTRAINT "fk_case_hearing_prosecutor__case_hearing_case_id__case_hearing_" FOREIGN KEY ("case_hearing_case_id", "case_hearing_case_case_name", "case_hearing_case_case_number", "case_hearing_hearingtype", "case_hearing_hearing_date") REFERENCES "case_hearing" ("case_id", "case_case_name", "case_case_number", "hearingtype", "hearing_date");

ALTER TABLE "case_hearing_prosecutor" ADD CONSTRAINT "fk_case_hearing_prosecutor__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "person" ("id");

CREATE TABLE "defendant_prison" (
  "defendant" INTEGER NOT NULL,
  "prison" INTEGER NOT NULL,
  PRIMARY KEY ("defendant", "prison")
);

CREATE INDEX "idx_defendant_prison" ON "defendant_prison" ("prison");

ALTER TABLE "defendant_prison" ADD CONSTRAINT "fk_defendant_prison__defendant" FOREIGN KEY ("defendant") REFERENCES "person" ("id");

ALTER TABLE "defendant_prison" ADD CONSTRAINT "fk_defendant_prison__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

CREATE TABLE "filing" (
  "id" SERIAL PRIMARY KEY,
  "case_id" INTEGER NOT NULL,
  "case_case_name" VARCHAR(150) NOT NULL,
  "case_case_number" VARCHAR(30) NOT NULL,
  "filing_date" TIMESTAMP NOT NULL,
  "doc_name" VARCHAR(50) NOT NULL,
  "doc_content" TEXT NOT NULL,
  "case__hearing_case_id" INTEGER NOT NULL,
  "case__hearing_case_case_name" VARCHAR(150) NOT NULL,
  "case__hearing_case_case_number" VARCHAR(30) NOT NULL,
  "case__hearing_hearingtype" INTEGER NOT NULL,
  "case__hearing_hearing_date" TIMESTAMP NOT NULL,
  "filing_fee" DOUBLE PRECISION NOT NULL,
  "receipt_number" VARCHAR(20) NOT NULL,
  "received_by" VARCHAR(50) NOT NULL
);

CREATE INDEX "idx_filing__case__hearing_case_id_case__hearing_case_case_name_" ON "filing" ("case__hearing_case_id", "case__hearing_case_case_name", "case__hearing_case_case_number", "case__hearing_hearingtype", "case__hearing_hearing_date");

CREATE INDEX "idx_filing__case_id_case_case_name_case_case_number" ON "filing" ("case_id", "case_case_name", "case_case_number");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__case__hearing_case_id__case__hearing_case_case_name_" FOREIGN KEY ("case__hearing_case_id", "case__hearing_case_case_name", "case__hearing_case_case_number", "case__hearing_hearingtype", "case__hearing_hearing_date") REFERENCES "case_hearing" ("case_id", "case_case_name", "case_case_number", "hearingtype", "hearing_date");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__case_id__case_case_name__case_case_number" FOREIGN KEY ("case_id", "case_case_name", "case_case_number") REFERENCES "case" ("id", "case_name", "case_number");

CREATE TABLE "defendant_filing" (
  "defendant" INTEGER NOT NULL,
  "filing" INTEGER NOT NULL,
  PRIMARY KEY ("defendant", "filing")
);

CREATE INDEX "idx_defendant_filing" ON "defendant_filing" ("filing");

ALTER TABLE "defendant_filing" ADD CONSTRAINT "fk_defendant_filing__defendant" FOREIGN KEY ("defendant") REFERENCES "person" ("id");

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

ALTER TABLE "filing_plaintiff" ADD CONSTRAINT "fk_filing_plaintiff__plaintiff" FOREIGN KEY ("plaintiff") REFERENCES "person" ("id");

CREATE TABLE "offender_prison" (
  "offender" INTEGER NOT NULL,
  "prison" INTEGER NOT NULL,
  PRIMARY KEY ("offender", "prison")
);

CREATE INDEX "idx_offender_prison" ON "offender_prison" ("prison");

ALTER TABLE "offender_prison" ADD CONSTRAINT "fk_offender_prison__offender" FOREIGN KEY ("offender") REFERENCES "person" ("id");

ALTER TABLE "offender_prison" ADD CONSTRAINT "fk_offender_prison__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id")

