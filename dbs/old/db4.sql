CREATE TABLE "bail" (
  "id" SERIAL PRIMARY KEY,
  "amount" DOUBLE PRECISION NOT NULL
);

CREATE TABLE "casestatus" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "casetype" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "courtlevel" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(40) NOT NULL
);

CREATE TABLE "gender" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "hearingtype" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(40) NOT NULL
);

CREATE TABLE "lawfirm" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "notification" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "prison" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "prosecutorteam" (
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

CREATE TABLE "policestation" (
  "id" SERIAL PRIMARY KEY,
  "town" INTEGER NOT NULL
);

CREATE INDEX "idx_policestation__town" ON "policestation" ("town");

ALTER TABLE "policestation" ADD CONSTRAINT "fk_policestation__town" FOREIGN KEY ("town") REFERENCES "town" ("id");

CREATE TABLE "person" (
  "id" SERIAL PRIMARY KEY,
  "xname" VARCHAR(50) NOT NULL,
  "address" VARCHAR(50),
  "gender" INTEGER NOT NULL,
  "classtype" TEXT NOT NULL,
  "service_number" VARCHAR(50),
  "reg_date" DATE,
  "bar_number" VARCHAR(20),
  "prosecutor_team" INTEGER,
  "law_firm" INTEGER,
  "phone" TEXT,
  "complaint" INTEGER
);

CREATE INDEX "idx_person__complaint" ON "person" ("complaint");

CREATE INDEX "idx_person__gender" ON "person" ("gender");

CREATE INDEX "idx_person__law_firm" ON "person" ("law_firm");

CREATE INDEX "idx_person__prosecutor_team" ON "person" ("prosecutor_team");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__law_firm" FOREIGN KEY ("law_firm") REFERENCES "lawfirm" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__prosecutor_team" FOREIGN KEY ("prosecutor_team") REFERENCES "prosecutorteam" ("id");

CREATE TABLE "offender_prison" (
  "offender" INTEGER NOT NULL,
  "prison" INTEGER NOT NULL,
  PRIMARY KEY ("offender", "prison")
);

CREATE INDEX "idx_offender_prison" ON "offender_prison" ("prison");

ALTER TABLE "offender_prison" ADD CONSTRAINT "fk_offender_prison__offender" FOREIGN KEY ("offender") REFERENCES "person" ("id");

ALTER TABLE "offender_prison" ADD CONSTRAINT "fk_offender_prison__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

CREATE TABLE "hearing_witness" (
  "hearing" INTEGER NOT NULL,
  "witness" INTEGER NOT NULL,
  PRIMARY KEY ("hearing", "witness")
);

CREATE INDEX "idx_hearing_witness" ON "hearing_witness" ("witness");

ALTER TABLE "hearing_witness" ADD CONSTRAINT "fk_hearing_witness__witness" FOREIGN KEY ("witness") REFERENCES "person" ("id");

CREATE TABLE "hearing_prosecutor" (
  "hearing" INTEGER NOT NULL,
  "prosecutor" INTEGER NOT NULL,
  PRIMARY KEY ("hearing", "prosecutor")
);

CREATE INDEX "idx_hearing_prosecutor" ON "hearing_prosecutor" ("prosecutor");

ALTER TABLE "hearing_prosecutor" ADD CONSTRAINT "fk_hearing_prosecutor__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "person" ("id");

CREATE TABLE "hearing_notification" (
  "hearing" INTEGER NOT NULL,
  "notification" INTEGER NOT NULL,
  PRIMARY KEY ("hearing", "notification")
);

CREATE INDEX "idx_hearing_notification" ON "hearing_notification" ("notification");

ALTER TABLE "hearing_notification" ADD CONSTRAINT "fk_hearing_notification__notification" FOREIGN KEY ("notification") REFERENCES "notification" ("id");

CREATE TABLE "hearing" (
  "id" SERIAL PRIMARY KEY,
  "case" INTEGER NOT NULL,
  "hearing_date" DATE NOT NULL,
  "judge" INTEGER,
  "hearing_type" INTEGER NOT NULL
);

CREATE INDEX "idx_hearing__case" ON "hearing" ("case");

CREATE INDEX "idx_hearing__hearing_type" ON "hearing" ("hearing_type");

CREATE INDEX "idx_hearing__judge" ON "hearing" ("judge");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__hearing_type" FOREIGN KEY ("hearing_type") REFERENCES "hearingtype" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__judge" FOREIGN KEY ("judge") REFERENCES "person" ("id");

ALTER TABLE "hearing_witness" ADD CONSTRAINT "fk_hearing_witness__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_prosecutor" ADD CONSTRAINT "fk_hearing_prosecutor__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "hearing_notification" ADD CONSTRAINT "fk_hearing_notification__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "filing" (
  "id" SERIAL PRIMARY KEY,
  "hearing" INTEGER,
  "file_date" DATE NOT NULL
);

CREATE INDEX "idx_filing__hearing" ON "filing" ("hearing");

ALTER TABLE "filing" ADD CONSTRAINT "fk_filing__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "document" (
  "id" SERIAL PRIMARY KEY,
  "filing" INTEGER NOT NULL,
  "content" TEXT NOT NULL
);

CREATE INDEX "idx_document__filing" ON "document" ("filing");

ALTER TABLE "document" ADD CONSTRAINT "fk_document__filing" FOREIGN KEY ("filing") REFERENCES "filing" ("id");

CREATE TABLE "defenseatt_hearing" (
  "defenseatt" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  PRIMARY KEY ("defenseatt", "hearing")
);

CREATE INDEX "idx_defenseatt_hearing" ON "defenseatt_hearing" ("hearing");

ALTER TABLE "defenseatt_hearing" ADD CONSTRAINT "fk_defenseatt_hearing__defenseatt" FOREIGN KEY ("defenseatt") REFERENCES "person" ("id");

ALTER TABLE "defenseatt_hearing" ADD CONSTRAINT "fk_defenseatt_hearing__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

CREATE TABLE "court_judge" (
  "court" INTEGER NOT NULL,
  "judge" INTEGER NOT NULL,
  PRIMARY KEY ("court", "judge")
);

CREATE INDEX "idx_court_judge" ON "court_judge" ("judge");

ALTER TABLE "court_judge" ADD CONSTRAINT "fk_court_judge__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

ALTER TABLE "court_judge" ADD CONSTRAINT "fk_court_judge__judge" FOREIGN KEY ("judge") REFERENCES "person" ("id");

CREATE TABLE "complaint" (
  "id" SERIAL PRIMARY KEY,
  "complainant" INTEGER NOT NULL,
  "policeman" INTEGER NOT NULL,
  "police_station" INTEGER NOT NULL,
  "statement" TEXT NOT NULL
);

CREATE INDEX "idx_complaint__complainant" ON "complaint" ("complainant");

CREATE INDEX "idx_complaint__police_station" ON "complaint" ("police_station");

CREATE INDEX "idx_complaint__policeman" ON "complaint" ("policeman");

ALTER TABLE "complaint" ADD CONSTRAINT "fk_complaint__complainant" FOREIGN KEY ("complainant") REFERENCES "person" ("id");

ALTER TABLE "complaint" ADD CONSTRAINT "fk_complaint__police_station" FOREIGN KEY ("police_station") REFERENCES "policestation" ("id");

ALTER TABLE "complaint" ADD CONSTRAINT "fk_complaint__policeman" FOREIGN KEY ("policeman") REFERENCES "person" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

CREATE TABLE "case_witness" (
  "case" INTEGER NOT NULL,
  "witness" INTEGER NOT NULL,
  PRIMARY KEY ("case", "witness")
);

CREATE INDEX "idx_case_witness" ON "case_witness" ("witness");

ALTER TABLE "case_witness" ADD CONSTRAINT "fk_case_witness__witness" FOREIGN KEY ("witness") REFERENCES "person" ("id");

CREATE TABLE "case_prison" (
  "case" INTEGER NOT NULL,
  "prison" INTEGER NOT NULL,
  PRIMARY KEY ("case", "prison")
);

CREATE INDEX "idx_case_prison" ON "case_prison" ("prison");

ALTER TABLE "case_prison" ADD CONSTRAINT "fk_case_prison__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

CREATE TABLE "case_policestation" (
  "case" INTEGER NOT NULL,
  "policestation" INTEGER NOT NULL,
  PRIMARY KEY ("case", "policestation")
);

CREATE INDEX "idx_case_policestation" ON "case_policestation" ("policestation");

ALTER TABLE "case_policestation" ADD CONSTRAINT "fk_case_policestation__policestation" FOREIGN KEY ("policestation") REFERENCES "policestation" ("id");

CREATE TABLE "case_offender" (
  "case" INTEGER NOT NULL,
  "offender" INTEGER NOT NULL,
  PRIMARY KEY ("case", "offender")
);

CREATE INDEX "idx_case_offender" ON "case_offender" ("offender");

ALTER TABLE "case_offender" ADD CONSTRAINT "fk_case_offender__offender" FOREIGN KEY ("offender") REFERENCES "person" ("id");

CREATE TABLE "case_complaint" (
  "case" INTEGER NOT NULL,
  "complaint" INTEGER NOT NULL,
  PRIMARY KEY ("case", "complaint")
);

CREATE INDEX "idx_case_complaint" ON "case_complaint" ("complaint");

ALTER TABLE "case_complaint" ADD CONSTRAINT "fk_case_complaint__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

CREATE TABLE "case" (
  "id" SERIAL PRIMARY KEY,
  "prosecutor_team" INTEGER NOT NULL,
  "complainant" INTEGER,
  "defense_att" INTEGER NOT NULL,
  "court" INTEGER NOT NULL,
  "judge" INTEGER NOT NULL,
  "case_type" INTEGER NOT NULL,
  "case_status" INTEGER NOT NULL
);

CREATE INDEX "idx_case__case_status" ON "case" ("case_status");

CREATE INDEX "idx_case__case_type" ON "case" ("case_type");

CREATE INDEX "idx_case__complainant" ON "case" ("complainant");

CREATE INDEX "idx_case__court" ON "case" ("court");

CREATE INDEX "idx_case__defense_att" ON "case" ("defense_att");

CREATE INDEX "idx_case__judge" ON "case" ("judge");

CREATE INDEX "idx_case__prosecutor_team" ON "case" ("prosecutor_team");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__case_status" FOREIGN KEY ("case_status") REFERENCES "casestatus" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__case_type" FOREIGN KEY ("case_type") REFERENCES "casetype" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__complainant" FOREIGN KEY ("complainant") REFERENCES "person" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__defense_att" FOREIGN KEY ("defense_att") REFERENCES "person" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__judge" FOREIGN KEY ("judge") REFERENCES "person" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__prosecutor_team" FOREIGN KEY ("prosecutor_team") REFERENCES "prosecutorteam" ("id");

ALTER TABLE "case_complaint" ADD CONSTRAINT "fk_case_complaint__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_offender" ADD CONSTRAINT "fk_case_offender__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_policestation" ADD CONSTRAINT "fk_case_policestation__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_prison" ADD CONSTRAINT "fk_case_prison__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

ALTER TABLE "case_witness" ADD CONSTRAINT "fk_case_witness__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

CREATE TABLE "bail_surety" (
  "bail" INTEGER NOT NULL,
  "surety" INTEGER NOT NULL,
  PRIMARY KEY ("bail", "surety")
);

CREATE INDEX "idx_bail_surety" ON "bail_surety" ("surety");

ALTER TABLE "bail_surety" ADD CONSTRAINT "fk_bail_surety__bail" FOREIGN KEY ("bail") REFERENCES "bail" ("id");

ALTER TABLE "bail_surety" ADD CONSTRAINT "fk_bail_surety__surety" FOREIGN KEY ("surety") REFERENCES "person" ("id");

CREATE TABLE "bail_hearing" (
  "bail" INTEGER NOT NULL,
  "hearing" INTEGER NOT NULL,
  PRIMARY KEY ("bail", "hearing")
);

CREATE INDEX "idx_bail_hearing" ON "bail_hearing" ("hearing");

ALTER TABLE "bail_hearing" ADD CONSTRAINT "fk_bail_hearing__bail" FOREIGN KEY ("bail") REFERENCES "bail" ("id");

ALTER TABLE "bail_hearing" ADD CONSTRAINT "fk_bail_hearing__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id")
