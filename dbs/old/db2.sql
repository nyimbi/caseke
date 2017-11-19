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
  "complaint" INTEGER,
  "prison" INTEGER,
  "court" INTEGER,
  "bail" INTEGER
);

CREATE INDEX "idx_person__bail" ON "person" ("bail");

CREATE INDEX "idx_person__complaint" ON "person" ("complaint");

CREATE INDEX "idx_person__court" ON "person" ("court");

CREATE INDEX "idx_person__gender" ON "person" ("gender");

CREATE INDEX "idx_person__law_firm" ON "person" ("law_firm");

CREATE INDEX "idx_person__prison" ON "person" ("prison");

CREATE INDEX "idx_person__prosecutor_team" ON "person" ("prosecutor_team");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__gender" FOREIGN KEY ("gender") REFERENCES "gender" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__law_firm" FOREIGN KEY ("law_firm") REFERENCES "lawfirm" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__prosecutor_team" FOREIGN KEY ("prosecutor_team") REFERENCES "prosecutorteam" ("id");

CREATE TABLE "hearing" (
  "id" SERIAL PRIMARY KEY,
  "case" INTEGER NOT NULL,
  "defense_att" INTEGER,
  "prosecutor" INTEGER,
  "hearing_date" DATE NOT NULL,
  "judge" INTEGER,
  "hearing_type" INTEGER NOT NULL,
  "notification" INTEGER
);

CREATE INDEX "idx_hearing__case" ON "hearing" ("case");

CREATE INDEX "idx_hearing__defense_att" ON "hearing" ("defense_att");

CREATE INDEX "idx_hearing__hearing_type" ON "hearing" ("hearing_type");

CREATE INDEX "idx_hearing__judge" ON "hearing" ("judge");

CREATE INDEX "idx_hearing__notification" ON "hearing" ("notification");

CREATE INDEX "idx_hearing__prosecutor" ON "hearing" ("prosecutor");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__defense_att" FOREIGN KEY ("defense_att") REFERENCES "person" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__hearing_type" FOREIGN KEY ("hearing_type") REFERENCES "hearingtype" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__judge" FOREIGN KEY ("judge") REFERENCES "person" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__notification" FOREIGN KEY ("notification") REFERENCES "notification" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__prosecutor" FOREIGN KEY ("prosecutor") REFERENCES "person" ("id");

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

CREATE TABLE "complaint" (
  "id" SERIAL PRIMARY KEY,
  "complainant" INTEGER NOT NULL,
  "police" INTEGER NOT NULL,
  "police_station" INTEGER NOT NULL,
  "statement" TEXT NOT NULL
);

CREATE INDEX "idx_complaint__complainant" ON "complaint" ("complainant");

CREATE INDEX "idx_complaint__police" ON "complaint" ("police");

CREATE INDEX "idx_complaint__police_station" ON "complaint" ("police_station");

ALTER TABLE "complaint" ADD CONSTRAINT "fk_complaint__complainant" FOREIGN KEY ("complainant") REFERENCES "person" ("id");

ALTER TABLE "complaint" ADD CONSTRAINT "fk_complaint__police" FOREIGN KEY ("police") REFERENCES "person" ("id");

ALTER TABLE "complaint" ADD CONSTRAINT "fk_complaint__police_station" FOREIGN KEY ("police_station") REFERENCES "policestation" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

CREATE TABLE "case" (
  "id" SERIAL PRIMARY KEY,
  "complaint" INTEGER NOT NULL,
  "prosecutor_team" INTEGER NOT NULL,
  "complainant" INTEGER,
  "offender" INTEGER NOT NULL,
  "defense_att" INTEGER NOT NULL,
  "court" INTEGER NOT NULL,
  "judge" INTEGER NOT NULL,
  "prison" INTEGER NOT NULL,
  "case_type" INTEGER NOT NULL,
  "case_status" INTEGER NOT NULL
);

CREATE INDEX "idx_case__case_status" ON "case" ("case_status");

CREATE INDEX "idx_case__case_type" ON "case" ("case_type");

CREATE INDEX "idx_case__complainant" ON "case" ("complainant");

CREATE INDEX "idx_case__complaint" ON "case" ("complaint");

CREATE INDEX "idx_case__court" ON "case" ("court");

CREATE INDEX "idx_case__defense_att" ON "case" ("defense_att");

CREATE INDEX "idx_case__judge" ON "case" ("judge");

CREATE INDEX "idx_case__offender" ON "case" ("offender");

CREATE INDEX "idx_case__prison" ON "case" ("prison");

CREATE INDEX "idx_case__prosecutor_team" ON "case" ("prosecutor_team");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__case_status" FOREIGN KEY ("case_status") REFERENCES "casestatus" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__case_type" FOREIGN KEY ("case_type") REFERENCES "casetype" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__complainant" FOREIGN KEY ("complainant") REFERENCES "person" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__complaint" FOREIGN KEY ("complaint") REFERENCES "complaint" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__court" FOREIGN KEY ("court") REFERENCES "court" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__defense_att" FOREIGN KEY ("defense_att") REFERENCES "person" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__judge" FOREIGN KEY ("judge") REFERENCES "person" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__offender" FOREIGN KEY ("offender") REFERENCES "person" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__prison" FOREIGN KEY ("prison") REFERENCES "prison" ("id");

ALTER TABLE "case" ADD CONSTRAINT "fk_case__prosecutor_team" FOREIGN KEY ("prosecutor_team") REFERENCES "prosecutorteam" ("id");

ALTER TABLE "hearing" ADD CONSTRAINT "fk_hearing__case" FOREIGN KEY ("case") REFERENCES "case" ("id");

CREATE TABLE "bail" (
  "id" SERIAL PRIMARY KEY,
  "hearing" INTEGER NOT NULL,
  "amount" DOUBLE PRECISION NOT NULL
);

CREATE INDEX "idx_bail__hearing" ON "bail" ("hearing");

ALTER TABLE "bail" ADD CONSTRAINT "fk_bail__hearing" FOREIGN KEY ("hearing") REFERENCES "hearing" ("id");

ALTER TABLE "person" ADD CONSTRAINT "fk_person__bail" FOREIGN KEY ("bail") REFERENCES "bail" ("id")
