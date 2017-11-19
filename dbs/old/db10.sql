
CREATE SEQUENCE public.surety_id_seq;

CREATE TABLE public.surety (
                id INTEGER DEFAULT nextval('surety_id_seq'::regclass) NOT NULL DEFAULT nextval('public.surety_id_seq'),
                firstname VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL,
                othernames VARCHAR(100),
                dob DATE,
                age INTEGER,
                gender BOOLEAN,
                marital_status VARCHAR(10),
                picture TEXT,
                bc_id VARCHAR(20),
                bc_number VARCHAR(20),
                bc_serial VARCHAR(20),
                bc_place VARCHAR(20),
                bc_scan TEXT,
                citizenship VARCHAR(20),
                nat_id_num VARCHAR(15),
                nat_id_serial VARCHAR(30),
                nat_id_scan TEXT,
                pp_no VARCHAR(20),
                pp_issue_date DATE,
                pp_issue_place VARCHAR(40),
                pp_scan TEXT,
                pp_expiry_date DATE,
                allergies TEXT,
                chronic_conditions TEXT,
                chronic_medications TEXT,
                hbp BOOLEAN,
                diabetes BOOLEAN,
                hiv BOOLEAN,
                current_health_status TEXT,
                kin1_name VARCHAR(40),
                kin1_phone VARCHAR(50),
                kin1_email VARCHAR(125),
                kin1_addr TEXT,
                kin2_name VARCHAR(40),
                kin2_phone VARCHAR(50),
                kin2_email VARCHAR(125),
                kin2_addr TEXT,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                town VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                CONSTRAINT surety_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.surety_id_seq OWNED BY public.surety.id;

CREATE UNIQUE INDEX ix_surety_bc_id
 ON public.surety USING BTREE
 ( bc_id );

CREATE UNIQUE INDEX ix_surety_nat_id_num
 ON public.surety USING BTREE
 ( nat_id_num );

CREATE INDEX ix_surety_bc_number
 ON public.surety USING BTREE
 ( bc_number );

CREATE INDEX ix_surety_bc_place
 ON public.surety USING BTREE
 ( bc_place );

CREATE INDEX ix_surety_bc_serial
 ON public.surety USING BTREE
 ( bc_serial );

CREATE INDEX ix_surety_dob
 ON public.surety USING BTREE
 ( dob );

CREATE INDEX ix_surety_firstname
 ON public.surety USING BTREE
 ( firstname );

CREATE INDEX ix_surety_mobile
 ON public.surety USING BTREE
 ( mobile );

CREATE INDEX ix_surety_nat_id_serial
 ON public.surety USING BTREE
 ( nat_id_serial );

CREATE INDEX ix_surety_pp_no
 ON public.surety USING BTREE
 ( pp_no );

CREATE INDEX ix_surety_surname
 ON public.surety USING BTREE
 ( surname );

CREATE SEQUENCE public.region_id_seq;

CREATE TABLE public.region (
                id INTEGER DEFAULT nextval('region_id_seq'::regclass) NOT NULL DEFAULT nextval('public.region_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                capital VARCHAR(30),
                CONSTRAINT region_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.region_id_seq OWNED BY public.region.id;

CREATE UNIQUE INDEX ix_region_name
 ON public.region USING BTREE
 ( name );

CREATE SEQUENCE public.prosecutor_team_id_seq;

CREATE TABLE public.prosecutor_team (
                id INTEGER DEFAULT nextval('prosecutor_team_id_seq'::regclass) NOT NULL DEFAULT nextval('public.prosecutor_team_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                taem_lead VARCHAR(60),
                CONSTRAINT prosecutor_team_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.prosecutor_team_id_seq OWNED BY public.prosecutor_team.id;

CREATE UNIQUE INDEX ix_prosecutor_team_name
 ON public.prosecutor_team USING BTREE
 ( name );

CREATE SEQUENCE public.police_role_id_seq;

CREATE TABLE public.police_role (
                id INTEGER DEFAULT nextval('police_role_id_seq'::regclass) NOT NULL DEFAULT nextval('public.police_role_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                CONSTRAINT police_role_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.police_role_id_seq OWNED BY public.police_role.id;

CREATE UNIQUE INDEX ix_police_role_name
 ON public.police_role USING BTREE
 ( name );

CREATE SEQUENCE public.offense_id_seq;

CREATE TABLE public.offense (
                id INTEGER DEFAULT nextval('offense_id_seq'::regclass) NOT NULL DEFAULT nextval('public.offense_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                act TEXT,
                legal_reference TEXT,
                indictable BOOLEAN,
                felony BOOLEAN,
                CONSTRAINT offense_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.offense_id_seq OWNED BY public.offense.id;

CREATE UNIQUE INDEX ix_offense_name
 ON public.offense USING BTREE
 ( name );

CREATE SEQUENCE public.lawfirm_id_seq;

CREATE TABLE public.lawfirm (
                id INTEGER DEFAULT nextval('lawfirm_id_seq'::regclass) NOT NULL DEFAULT nextval('public.lawfirm_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                town VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                managing_partner VARCHAR(60),
                CONSTRAINT lawfirm_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.lawfirm_id_seq OWNED BY public.lawfirm.id;

CREATE UNIQUE INDEX ix_lawfirm_name
 ON public.lawfirm USING BTREE
 ( name );

CREATE INDEX ix_lawfirm_mobile
 ON public.lawfirm USING BTREE
 ( mobile );

CREATE SEQUENCE public.hearingtype_id_seq;

CREATE TABLE public.hearingtype (
                id INTEGER DEFAULT nextval('hearingtype_id_seq'::regclass) NOT NULL DEFAULT nextval('public.hearingtype_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                CONSTRAINT hearingtype_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.hearingtype_id_seq OWNED BY public.hearingtype.id;

CREATE UNIQUE INDEX ix_hearingtype_name
 ON public.hearingtype USING BTREE
 ( name );

CREATE SEQUENCE public.gender_id_seq;

CREATE TABLE public.gender (
                id INTEGER DEFAULT nextval('gender_id_seq'::regclass) NOT NULL DEFAULT nextval('public.gender_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                CONSTRAINT gender_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.gender_id_seq OWNED BY public.gender.id;

CREATE UNIQUE INDEX ix_gender_name
 ON public.gender USING BTREE
 ( name );

CREATE SEQUENCE public.witness_id_seq;

CREATE TABLE public.witness (
                id INTEGER DEFAULT nextval('witness_id_seq'::regclass) NOT NULL DEFAULT nextval('public.witness_id_seq'),
                firstname VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL,
                othernames VARCHAR(100),
                dob DATE,
                age INTEGER,
                marital_status VARCHAR(10),
                picture TEXT,
                bc_id VARCHAR(20),
                bc_number VARCHAR(20),
                bc_serial VARCHAR(20),
                bc_place VARCHAR(20),
                bc_scan TEXT,
                citizenship VARCHAR(20),
                nat_id_num VARCHAR(15),
                nat_id_serial VARCHAR(30),
                nat_id_scan TEXT,
                pp_no VARCHAR(20),
                pp_issue_date DATE,
                pp_issue_place VARCHAR(40),
                pp_scan TEXT,
                pp_expiry_date DATE,
                allergies TEXT,
                chronic_conditions TEXT,
                chronic_medications TEXT,
                hbp BOOLEAN,
                diabetes BOOLEAN,
                hiv BOOLEAN,
                current_health_status TEXT,
                kin1_name VARCHAR(40),
                kin1_phone VARCHAR(50),
                kin1_email VARCHAR(125),
                kin1_addr TEXT,
                kin2_name VARCHAR(40),
                kin2_phone VARCHAR(50),
                kin2_email VARCHAR(125),
                kin2_addr TEXT,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                town VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                special BOOLEAN,
                role VARCHAR(100),
                for_defense BOOLEAN,
                gender_fk INTEGER NOT NULL,
                CONSTRAINT witness_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.witness_id_seq OWNED BY public.witness.id;

CREATE UNIQUE INDEX ix_witness_bc_id
 ON public.witness USING BTREE
 ( bc_id );

CREATE UNIQUE INDEX ix_witness_nat_id_num
 ON public.witness USING BTREE
 ( nat_id_num );

CREATE INDEX ix_witness_bc_number
 ON public.witness USING BTREE
 ( bc_number );

CREATE INDEX ix_witness_bc_place
 ON public.witness USING BTREE
 ( bc_place );

CREATE INDEX ix_witness_bc_serial
 ON public.witness USING BTREE
 ( bc_serial );

CREATE INDEX ix_witness_dob
 ON public.witness USING BTREE
 ( dob );

CREATE INDEX ix_witness_firstname
 ON public.witness USING BTREE
 ( firstname );

CREATE INDEX ix_witness_gender_fk
 ON public.witness USING BTREE
 ( gender_fk );

CREATE INDEX ix_witness_mobile
 ON public.witness USING BTREE
 ( mobile );

CREATE INDEX ix_witness_nat_id_serial
 ON public.witness USING BTREE
 ( nat_id_serial );

CREATE INDEX ix_witness_pp_no
 ON public.witness USING BTREE
 ( pp_no );

CREATE INDEX ix_witness_surname
 ON public.witness USING BTREE
 ( surname );

CREATE SEQUENCE public.prosecutor_id_seq;

CREATE TABLE public.prosecutor (
                id INTEGER DEFAULT nextval('prosecutor_id_seq'::regclass) NOT NULL DEFAULT nextval('public.prosecutor_id_seq'),
                firstname VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL,
                othernames VARCHAR(100),
                dob DATE,
                age INTEGER,
                marital_status VARCHAR(10),
                picture TEXT,
                bc_id VARCHAR(20),
                bc_number VARCHAR(20),
                bc_serial VARCHAR(20),
                bc_place VARCHAR(20),
                bc_scan TEXT,
                citizenship VARCHAR(20),
                nat_id_num VARCHAR(15),
                nat_id_serial VARCHAR(30),
                nat_id_scan TEXT,
                pp_no VARCHAR(20),
                pp_issue_date DATE,
                pp_issue_place VARCHAR(40),
                pp_scan TEXT,
                pp_expiry_date DATE,
                allergies TEXT,
                chronic_conditions TEXT,
                chronic_medications TEXT,
                hbp BOOLEAN,
                diabetes BOOLEAN,
                hiv BOOLEAN,
                current_health_status TEXT,
                kin1_name VARCHAR(40),
                kin1_phone VARCHAR(50),
                kin1_email VARCHAR(125),
                kin1_addr TEXT,
                kin2_name VARCHAR(40),
                kin2_phone VARCHAR(50),
                kin2_email VARCHAR(125),
                kin2_addr TEXT,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                town VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                is_police BOOLEAN NOT NULL,
                gender_fk INTEGER NOT NULL,
                pk_fk INTEGER NOT NULL,
                CONSTRAINT prosecutor_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.prosecutor_id_seq OWNED BY public.prosecutor.id;

CREATE UNIQUE INDEX ix_prosecutor_bc_id
 ON public.prosecutor USING BTREE
 ( bc_id );

CREATE UNIQUE INDEX ix_prosecutor_nat_id_num
 ON public.prosecutor USING BTREE
 ( nat_id_num );

CREATE INDEX ix_prosecutor_bc_number
 ON public.prosecutor USING BTREE
 ( bc_number );

CREATE INDEX ix_prosecutor_bc_place
 ON public.prosecutor USING BTREE
 ( bc_place );

CREATE INDEX ix_prosecutor_bc_serial
 ON public.prosecutor USING BTREE
 ( bc_serial );

CREATE INDEX ix_prosecutor_dob
 ON public.prosecutor USING BTREE
 ( dob );

CREATE INDEX ix_prosecutor_firstname
 ON public.prosecutor USING BTREE
 ( firstname );

CREATE INDEX ix_prosecutor_gender_fk
 ON public.prosecutor USING BTREE
 ( gender_fk );

CREATE INDEX ix_prosecutor_mobile
 ON public.prosecutor USING BTREE
 ( mobile );

CREATE INDEX ix_prosecutor_nat_id_serial
 ON public.prosecutor USING BTREE
 ( nat_id_serial );

CREATE INDEX ix_prosecutor_pk_fk
 ON public.prosecutor USING BTREE
 ( pk_fk );

CREATE INDEX ix_prosecutor_pp_no
 ON public.prosecutor USING BTREE
 ( pp_no );

CREATE INDEX ix_prosecutor_surname
 ON public.prosecutor USING BTREE
 ( surname );

CREATE SEQUENCE public.feeschedule_id_seq;

CREATE TABLE public.feeschedule (
                id INTEGER DEFAULT nextval('feeschedule_id_seq'::regclass) NOT NULL DEFAULT nextval('public.feeschedule_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                amount DOUBLE PRECISION NOT NULL,
                CONSTRAINT feeschedule_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.feeschedule_id_seq OWNED BY public.feeschedule.id;

CREATE UNIQUE INDEX ix_feeschedule_name
 ON public.feeschedule USING BTREE
 ( name );

CREATE SEQUENCE public.district_id_seq;

CREATE TABLE public.district (
                id INTEGER DEFAULT nextval('district_id_seq'::regclass) NOT NULL DEFAULT nextval('public.district_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                region_fk INTEGER NOT NULL,
                capital VARCHAR(30),
                CONSTRAINT district_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.district_id_seq OWNED BY public.district.id;

CREATE UNIQUE INDEX ix_district_name
 ON public.district USING BTREE
 ( name );

CREATE INDEX ix_district_region_fk
 ON public.district USING BTREE
 ( region_fk );

CREATE SEQUENCE public.town_id_seq;

CREATE TABLE public.town (
                id INTEGER DEFAULT nextval('town_id_seq'::regclass) NOT NULL DEFAULT nextval('public.town_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                district_fk INTEGER NOT NULL,
                CONSTRAINT town_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.town_id_seq OWNED BY public.town.id;

CREATE UNIQUE INDEX ix_town_name
 ON public.town USING BTREE
 ( name );

CREATE INDEX ix_town_district_fk
 ON public.town USING BTREE
 ( district_fk );

CREATE SEQUENCE public.prison_id_seq;

CREATE TABLE public.prison (
                id INTEGER DEFAULT nextval('prison_id_seq'::regclass) NOT NULL DEFAULT nextval('public.prison_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                town_fk INTEGER NOT NULL,
                warden VARCHAR(80) NOT NULL,
                CONSTRAINT prison_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.prison_id_seq OWNED BY public.prison.id;

CREATE UNIQUE INDEX ix_prison_name
 ON public.prison USING BTREE
 ( name );

CREATE INDEX ix_prison_mobile
 ON public.prison USING BTREE
 ( mobile );

CREATE INDEX ix_prison_town_fk
 ON public.prison USING BTREE
 ( town_fk );

CREATE SEQUENCE public.policestation_id_seq;

CREATE TABLE public.policestation (
                id INTEGER DEFAULT nextval('policestation_id_seq'::regclass) NOT NULL DEFAULT nextval('public.policestation_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                town_fk INTEGER NOT NULL,
                officer_commanding VARCHAR(60),
                CONSTRAINT policestation_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.policestation_id_seq OWNED BY public.policestation.id;

CREATE UNIQUE INDEX ix_policestation_name
 ON public.policestation USING BTREE
 ( name );

CREATE INDEX ix_policestation_mobile
 ON public.policestation USING BTREE
 ( mobile );

CREATE INDEX ix_policestation_town_fk
 ON public.policestation USING BTREE
 ( town_fk );

CREATE SEQUENCE public.policeman_id_seq;

CREATE TABLE public.policeman (
                id INTEGER DEFAULT nextval('policeman_id_seq'::regclass) NOT NULL DEFAULT nextval('public.policeman_id_seq'),
                firstname VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL,
                othernames VARCHAR(100),
                dob DATE,
                age INTEGER,
                marital_status VARCHAR(10),
                picture TEXT,
                bc_id VARCHAR(20),
                bc_number VARCHAR(20),
                bc_serial VARCHAR(20),
                bc_place VARCHAR(20),
                bc_scan TEXT,
                citizenship VARCHAR(20),
                nat_id_num VARCHAR(15),
                nat_id_serial VARCHAR(30),
                nat_id_scan TEXT,
                pp_no VARCHAR(20),
                pp_issue_date DATE,
                pp_issue_place VARCHAR(40),
                pp_scan TEXT,
                pp_expiry_date DATE,
                allergies TEXT,
                chronic_conditions TEXT,
                chronic_medications TEXT,
                hbp BOOLEAN,
                diabetes BOOLEAN,
                hiv BOOLEAN,
                current_health_status TEXT,
                kin1_name VARCHAR(40),
                kin1_phone VARCHAR(50),
                kin1_email VARCHAR(125),
                kin1_addr TEXT,
                kin2_name VARCHAR(40),
                kin2_phone VARCHAR(50),
                kin2_email VARCHAR(125),
                kin2_addr TEXT,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                town VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                gender_fk INTEGER NOT NULL,
                service_number VARCHAR(50) NOT NULL,
                rank VARCHAR(40),
                police_station_fk INTEGER NOT NULL,
                CONSTRAINT policeman_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.policeman_id_seq OWNED BY public.policeman.id;

CREATE UNIQUE INDEX ix_policeman_bc_id
 ON public.policeman USING BTREE
 ( bc_id );

CREATE UNIQUE INDEX ix_policeman_nat_id_num
 ON public.policeman USING BTREE
 ( nat_id_num );

CREATE INDEX ix_policeman_bc_number
 ON public.policeman USING BTREE
 ( bc_number );

CREATE INDEX ix_policeman_bc_place
 ON public.policeman USING BTREE
 ( bc_place );

CREATE INDEX ix_policeman_bc_serial
 ON public.policeman USING BTREE
 ( bc_serial );

CREATE INDEX ix_policeman_dob
 ON public.policeman USING BTREE
 ( dob );

CREATE INDEX ix_policeman_firstname
 ON public.policeman USING BTREE
 ( firstname );

CREATE INDEX ix_policeman_mobile
 ON public.policeman USING BTREE
 ( mobile );

CREATE INDEX ix_policeman_nat_id_serial
 ON public.policeman USING BTREE
 ( nat_id_serial );

CREATE INDEX ix_policeman_police_station_fk
 ON public.policeman USING BTREE
 ( police_station_fk );

CREATE INDEX ix_policeman_pp_no
 ON public.policeman USING BTREE
 ( pp_no );

CREATE INDEX ix_policeman_surname
 ON public.policeman USING BTREE
 ( surname );

CREATE SEQUENCE public.courtlevel_id_seq;

CREATE TABLE public.courtlevel (
                id INTEGER DEFAULT nextval('courtlevel_id_seq'::regclass) NOT NULL DEFAULT nextval('public.courtlevel_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                CONSTRAINT courtlevel_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.courtlevel_id_seq OWNED BY public.courtlevel.id;

CREATE UNIQUE INDEX ix_courtlevel_name
 ON public.courtlevel USING BTREE
 ( name );

CREATE SEQUENCE public.court_id_seq;

CREATE TABLE public.court (
                id INTEGER DEFAULT nextval('court_id_seq'::regclass) NOT NULL DEFAULT nextval('public.court_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                place_name VARCHAR(40),
                lat DOUBLE PRECISION,
                lng DOUBLE PRECISION,
                alt DOUBLE PRECISION,
                map TEXT,
                info TEXT,
                pin BOOLEAN,
                pin_color VARCHAR(20),
                pin_icon VARCHAR(50),
                centered BOOLEAN,
                nearest_feature VARCHAR(100),
                town_fk INTEGER NOT NULL,
                court_level_fk INTEGER NOT NULL,
                registrar VARCHAR(60),
                CONSTRAINT court_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.court_id_seq OWNED BY public.court.id;

CREATE UNIQUE INDEX ix_court_name
 ON public.court USING BTREE
 ( name );

CREATE INDEX ix_court_court_level_fk
 ON public.court USING BTREE
 ( court_level_fk );

CREATE INDEX ix_court_town_fk
 ON public.court USING BTREE
 ( town_fk );

CREATE SEQUENCE public.judge_id_seq;

CREATE TABLE public.judge (
                id INTEGER DEFAULT nextval('judge_id_seq'::regclass) NOT NULL DEFAULT nextval('public.judge_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                town VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                court_fk INTEGER NOT NULL,
                gender_fk INTEGER NOT NULL,
                court_level_fk INTEGER NOT NULL,
                appelation VARCHAR(100) NOT NULL,
                CONSTRAINT judge_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.judge_id_seq OWNED BY public.judge.id;

CREATE UNIQUE INDEX ix_judge_name
 ON public.judge USING BTREE
 ( name );

CREATE INDEX ix_judge_court_fk
 ON public.judge USING BTREE
 ( court_fk );

CREATE INDEX ix_judge_court_level_fk
 ON public.judge USING BTREE
 ( court_level_fk );

CREATE INDEX ix_judge_mobile
 ON public.judge USING BTREE
 ( mobile );

CREATE SEQUENCE public.casestatus_id_seq;

CREATE TABLE public.casestatus (
                id INTEGER DEFAULT nextval('casestatus_id_seq'::regclass) NOT NULL DEFAULT nextval('public.casestatus_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                CONSTRAINT casestatus_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.casestatus_id_seq OWNED BY public.casestatus.id;

CREATE UNIQUE INDEX ix_casestatus_name
 ON public.casestatus USING BTREE
 ( name );

CREATE SEQUENCE public.casecategory_id_seq;

CREATE TABLE public.casecategory (
                id INTEGER DEFAULT nextval('casecategory_id_seq'::regclass) NOT NULL DEFAULT nextval('public.casecategory_id_seq'),
                name VARCHAR(60) NOT NULL,
                description VARCHAR(100),
                notes TEXT,
                CONSTRAINT casecategory_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.casecategory_id_seq OWNED BY public.casecategory.id;

CREATE UNIQUE INDEX ix_casecategory_name
 ON public.casecategory USING BTREE
 ( name );

CREATE TABLE public.ab_view_menu (
                id INTEGER NOT NULL,
                name VARCHAR(100) NOT NULL,
                CONSTRAINT ab_view_menu_pkey PRIMARY KEY (id)
);


CREATE UNIQUE INDEX ab_view_menu_name_key
 ON public.ab_view_menu USING BTREE
 ( name );

CREATE TABLE public.ab_user (
                id INTEGER NOT NULL,
                first_name VARCHAR(64) NOT NULL,
                last_name VARCHAR(64) NOT NULL,
                username VARCHAR(64) NOT NULL,
                password VARCHAR(256),
                active BOOLEAN,
                email VARCHAR(64) NOT NULL,
                last_login TIMESTAMP,
                login_count INTEGER,
                fail_login_count INTEGER,
                created_on TIMESTAMP,
                changed_on TIMESTAMP,
                created_by_fk INTEGER NOT NULL,
                changed_by_fk INTEGER NOT NULL,
                CONSTRAINT ab_user_pkey PRIMARY KEY (id)
);


CREATE UNIQUE INDEX ab_user_email_key
 ON public.ab_user USING BTREE
 ( email );

CREATE UNIQUE INDEX ab_user_username_key
 ON public.ab_user USING BTREE
 ( username );

CREATE SEQUENCE public.plaintiff_id_seq;

CREATE TABLE public.plaintiff (
                id INTEGER DEFAULT nextval('plaintiff_id_seq'::regclass) NOT NULL DEFAULT nextval('public.plaintiff_id_seq'),
                created_on TIMESTAMP NOT NULL,
                changed_on TIMESTAMP NOT NULL,
                firstname VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL,
                othernames VARCHAR(100),
                dob DATE,
                age INTEGER,
                marital_status VARCHAR(10),
                picture TEXT,
                bc_id VARCHAR(20),
                bc_number VARCHAR(20),
                bc_serial VARCHAR(20),
                bc_place VARCHAR(20),
                bc_scan TEXT,
                citizenship VARCHAR(20),
                nat_id_num VARCHAR(15),
                nat_id_serial VARCHAR(30),
                nat_id_scan TEXT,
                pp_no VARCHAR(20),
                pp_issue_date DATE,
                pp_issue_place VARCHAR(40),
                pp_scan TEXT,
                pp_expiry_date DATE,
                allergies TEXT,
                chronic_conditions TEXT,
                chronic_medications TEXT,
                hbp BOOLEAN,
                diabetes BOOLEAN,
                hiv BOOLEAN,
                current_health_status TEXT,
                kin1_name VARCHAR(40),
                kin1_phone VARCHAR(50),
                kin1_email VARCHAR(125),
                kin1_addr TEXT,
                kin2_name VARCHAR(40),
                kin2_phone VARCHAR(50),
                kin2_email VARCHAR(125),
                kin2_addr TEXT,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                town VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                with_others BOOLEAN NOT NULL,
                gender_fk INTEGER NOT NULL,
                notes TEXT,
                changed_by_fk INTEGER NOT NULL,
                created_by_fk INTEGER NOT NULL,
                CONSTRAINT plaintiff_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.plaintiff_id_seq OWNED BY public.plaintiff.id;

CREATE UNIQUE INDEX ix_plaintiff_bc_id
 ON public.plaintiff USING BTREE
 ( bc_id );

CREATE UNIQUE INDEX ix_plaintiff_nat_id_num
 ON public.plaintiff USING BTREE
 ( nat_id_num );

CREATE INDEX ix_plaintiff_bc_number
 ON public.plaintiff USING BTREE
 ( bc_number );

CREATE INDEX ix_plaintiff_bc_place
 ON public.plaintiff USING BTREE
 ( bc_place );

CREATE INDEX ix_plaintiff_bc_serial
 ON public.plaintiff USING BTREE
 ( bc_serial );

CREATE INDEX ix_plaintiff_dob
 ON public.plaintiff USING BTREE
 ( dob );

CREATE INDEX ix_plaintiff_firstname
 ON public.plaintiff USING BTREE
 ( firstname );

CREATE INDEX ix_plaintiff_gender_fk
 ON public.plaintiff USING BTREE
 ( gender_fk );

CREATE INDEX ix_plaintiff_mobile
 ON public.plaintiff USING BTREE
 ( mobile );

CREATE INDEX ix_plaintiff_nat_id_serial
 ON public.plaintiff USING BTREE
 ( nat_id_serial );

CREATE INDEX ix_plaintiff_pp_no
 ON public.plaintiff USING BTREE
 ( pp_no );

CREATE INDEX ix_plaintiff_surname
 ON public.plaintiff USING BTREE
 ( surname );

CREATE SEQUENCE public.document_id_seq;

CREATE TABLE public.document (
                id INTEGER DEFAULT nextval('document_id_seq'::regclass) NOT NULL DEFAULT nextval('public.document_id_seq'),
                created_on TIMESTAMP NOT NULL,
                changed_on TIMESTAMP NOT NULL,
                document BYTEA,
                doc_content TEXT NOT NULL,
                doc_img BYTEA NOT NULL,
                doc_date DATE NOT NULL,
                changed_by_fk INTEGER NOT NULL,
                created_by_fk INTEGER NOT NULL,
                CONSTRAINT document_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.document_id_seq OWNED BY public.document.id;

CREATE SEQUENCE public.defendant_id_seq;

CREATE TABLE public.defendant (
                id INTEGER DEFAULT nextval('defendant_id_seq'::regclass) NOT NULL DEFAULT nextval('public.defendant_id_seq'),
                created_on TIMESTAMP NOT NULL,
                changed_on TIMESTAMP NOT NULL,
                firstname VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL,
                othernames VARCHAR(100),
                dob DATE,
                age INTEGER,
                marital_status VARCHAR(10),
                picture TEXT,
                bc_id VARCHAR(20),
                bc_number VARCHAR(20),
                bc_serial VARCHAR(20),
                bc_place VARCHAR(20),
                bc_scan TEXT,
                citizenship VARCHAR(20),
                nat_id_num VARCHAR(15),
                nat_id_serial VARCHAR(30),
                nat_id_scan TEXT,
                pp_no VARCHAR(20),
                pp_issue_date DATE,
                pp_issue_place VARCHAR(40),
                pp_scan TEXT,
                pp_expiry_date DATE,
                allergies TEXT,
                chronic_conditions TEXT,
                chronic_medications TEXT,
                hbp BOOLEAN,
                diabetes BOOLEAN,
                hiv BOOLEAN,
                current_health_status TEXT,
                kin1_name VARCHAR(40),
                kin1_phone VARCHAR(50),
                kin1_email VARCHAR(125),
                kin1_addr TEXT,
                kin2_name VARCHAR(40),
                kin2_phone VARCHAR(50),
                kin2_email VARCHAR(125),
                kin2_addr TEXT,
                blood_group VARCHAR(3),
                striking_features TEXT,
                height_m DOUBLE PRECISION,
                weight_kg DOUBLE PRECISION,
                eye_colour VARCHAR(20),
                hair_colour VARCHAR(20),
                complexion VARCHAR(50),
                religion VARCHAR(20),
                ethnicity VARCHAR(40),
                fp_lthumb TEXT,
                fp_left2 TEXT,
                fp_left3 TEXT,
                fp_left4 TEXT,
                fp_left5 TEXT,
                fp_rthumb TEXT,
                fp_right2 TEXT,
                fp_right3 TEXT,
                fp_right4 TEXT,
                fp_right5 TEXT,
                palm_left TEXT,
                palm_right TEXT,
                eye_left TEXT,
                eye_right TEXT,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                town VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                gender_fk INTEGER NOT NULL,
                with_others BOOLEAN NOT NULL,
                notes TEXT,
                changed_by_fk INTEGER NOT NULL,
                created_by_fk INTEGER NOT NULL,
                CONSTRAINT defendant_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.defendant_id_seq OWNED BY public.defendant.id;

CREATE UNIQUE INDEX ix_defendant_bc_id
 ON public.defendant USING BTREE
 ( bc_id );

CREATE UNIQUE INDEX ix_defendant_nat_id_num
 ON public.defendant USING BTREE
 ( nat_id_num );

CREATE INDEX ix_defendant_bc_number
 ON public.defendant USING BTREE
 ( bc_number );

CREATE INDEX ix_defendant_bc_place
 ON public.defendant USING BTREE
 ( bc_place );

CREATE INDEX ix_defendant_bc_serial
 ON public.defendant USING BTREE
 ( bc_serial );

CREATE INDEX ix_defendant_dob
 ON public.defendant USING BTREE
 ( dob );

CREATE INDEX ix_defendant_firstname
 ON public.defendant USING BTREE
 ( firstname );

CREATE INDEX ix_defendant_gender_fk
 ON public.defendant USING BTREE
 ( gender_fk );

CREATE INDEX ix_defendant_mobile
 ON public.defendant USING BTREE
 ( mobile );

CREATE INDEX ix_defendant_nat_id_serial
 ON public.defendant USING BTREE
 ( nat_id_serial );

CREATE INDEX ix_defendant_pp_no
 ON public.defendant USING BTREE
 ( pp_no );

CREATE INDEX ix_defendant_surname
 ON public.defendant USING BTREE
 ( surname );

CREATE TABLE public.defendant_prison (
                defendant INTEGER NOT NULL,
                prison INTEGER NOT NULL,
                CONSTRAINT defendant_prison_pkey PRIMARY KEY (defendant, prison)
);


CREATE INDEX ix_defendant_prison_prison
 ON public.defendant_prison USING BTREE
 ( prison );

CREATE SEQUENCE public.contact_id_seq;

CREATE TABLE public.contact (
                id INTEGER DEFAULT nextval('contact_id_seq'::regclass) NOT NULL DEFAULT nextval('public.contact_id_seq'),
                created_on TIMESTAMP NOT NULL,
                changed_on TIMESTAMP NOT NULL,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                town VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                message TEXT,
                changed_by_fk INTEGER NOT NULL,
                created_by_fk INTEGER NOT NULL,
                CONSTRAINT contact_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.contact_id_seq OWNED BY public.contact.id;

CREATE INDEX ix_contact_mobile
 ON public.contact USING BTREE
 ( mobile );

CREATE TABLE public.contact_plaintiff (
                contact INTEGER NOT NULL,
                plaintiff INTEGER NOT NULL,
                CONSTRAINT contact_plaintiff_pkey PRIMARY KEY (contact, plaintiff)
);


CREATE INDEX ix_contact_plaintiff_plaintiff
 ON public.contact_plaintiff USING BTREE
 ( plaintiff );

CREATE SEQUENCE public.case_1_id_seq;

CREATE TABLE public.case_1 (
                id INTEGER DEFAULT nextval('case_id_seq'::regclass) NOT NULL DEFAULT nextval('public.case_1_id_seq'),
                created_on TIMESTAMP NOT NULL,
                changed_on TIMESTAMP NOT NULL,
                open_date TIMESTAMP NOT NULL,
                court_fk INTEGER NOT NULL,
                case_number VARCHAR(30) NOT NULL,
                is_criminal BOOLEAN,
                case_category_fk INTEGER NOT NULL,
                reporting_officer VARCHAR(80),
                investigating_officer VARCHAR(80),
                arresting_officer TEXT,
                investigation_outcomes TEXT,
                investigation_status VARCHAR(80),
                evidence_collected TEXT,
                evidence_pictures TEXT,
                offender_identification TEXT,
                offenders_arrested TEXT,
                arrest_location TEXT,
                arrest_narrative TEXT,
                warrant_date DATE,
                warrant_details TEXT,
                probable_cause TEXT,
                document_list TEXT,
                document_count INTEGER,
                charge_date DATE,
                charge_description TEXT,
                first_hearing_date DATE,
                hearing_dates TEXT,
                court_outcome TEXT,
                case_duration INTEGER,
                offender_picture TEXT,
                case_closed BOOLEAN,
                changed_by_fk INTEGER NOT NULL,
                created_by_fk INTEGER NOT NULL,
                CONSTRAINT case_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.case_1_id_seq OWNED BY public.case_1.id;

CREATE INDEX ix_case_case_category_fk
 ON public.case_1 USING BTREE
 ( case_category_fk );

CREATE INDEX ix_case_court_fk
 ON public.case_1 USING BTREE
 ( court_fk );

CREATE SEQUENCE public.complaint_id_seq;

CREATE TABLE public.complaint (
                id INTEGER DEFAULT nextval('complaint_id_seq'::regclass) NOT NULL DEFAULT nextval('public.complaint_id_seq'),
                created_on TIMESTAMP NOT NULL,
                changed_on TIMESTAMP NOT NULL,
                place_name VARCHAR(40),
                lat DOUBLE PRECISION,
                lng DOUBLE PRECISION,
                alt DOUBLE PRECISION,
                map TEXT,
                info TEXT,
                pin BOOLEAN,
                pin_color VARCHAR(20),
                pin_icon VARCHAR(50),
                centered BOOLEAN,
                nearest_feature VARCHAR(100),
                report_date TIMESTAMP,
                event_date TIMESTAMP,
                report TEXT NOT NULL,
                is_case BOOLEAN,
                case_1 INTEGER NOT NULL,
                station_id INTEGER NOT NULL,
                complainant_role TEXT,
                complaint_language VARCHAR(80),
                observations TEXT,
                injuries TEXT,
                loss TEXT,
                damage TEXT,
                theft TEXT,
                fraud TEXT,
                death TEXT,
                narcotics BOOLEAN,
                domestic_abuse BOOLEAN,
                complainant_is_victim BOOLEAN,
                victim_name VARCHAR(80),
                victim_phone VARCHAR(80),
                victim_email VARCHAR(80),
                victim_address VARCHAR(80),
                victim_age INTEGER,
                victim_gender_fk INTEGER NOT NULL,
                victim_pwd BOOLEAN,
                victim_religion VARCHAR(80),
                victim_ethnicity VARCHAR(80),
                offender_count INTEGER,
                offenders_known_to_victim BOOLEAN,
                offender_known_to_complainant BOOLEAN,
                offender_description TEXT,
                police_interpretation TEXT,
                is_a_crime BOOLEAN,
                is_a_case BOOLEAN,
                case_number VARCHAR(80),
                closed BOOLEAN,
                changed_by_fk INTEGER NOT NULL,
                created_by_fk INTEGER NOT NULL,
                CONSTRAINT complaint_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.complaint_id_seq OWNED BY public.complaint.id;

CREATE INDEX ix_complaint_case
 ON public.complaint USING BTREE
 ( case_1 );

CREATE TABLE public.complaint_policeman (
                complaint INTEGER NOT NULL,
                policeman INTEGER NOT NULL,
                CONSTRAINT complaint_policeman_pkey PRIMARY KEY (complaint, policeman)
);


CREATE INDEX ix_complaint_policeman_policeman
 ON public.complaint_policeman USING BTREE
 ( policeman );

CREATE TABLE public.complaint_plaintiff (
                complaint INTEGER NOT NULL,
                plaintiff INTEGER NOT NULL,
                CONSTRAINT complaint_plaintiff_pkey PRIMARY KEY (complaint, plaintiff)
);


CREATE INDEX ix_complaint_plaintiff_plaintiff
 ON public.complaint_plaintiff USING BTREE
 ( plaintiff );

CREATE TABLE public.complaint_defendant (
                complaint INTEGER NOT NULL,
                defendant INTEGER NOT NULL,
                CONSTRAINT complaint_defendant_pkey PRIMARY KEY (complaint, defendant)
);


CREATE INDEX ix_complaint_defendant_defendant
 ON public.complaint_defendant USING BTREE
 ( defendant );

CREATE TABLE public.case_witness (
                case_1 INTEGER NOT NULL,
                witness INTEGER NOT NULL,
                notes TEXT,
                CONSTRAINT case_witness_pkey PRIMARY KEY (case_1, witness)
);


CREATE INDEX ix_case_witness_witness
 ON public.case_witness USING BTREE
 ( witness );

CREATE TABLE public.case_prosecutor (
                case_1 INTEGER NOT NULL,
                prosecutor INTEGER NOT NULL,
                CONSTRAINT case_prosecutor_pkey PRIMARY KEY (case_1, prosecutor)
);


CREATE INDEX ix_case_prosecutor_prosecutor
 ON public.case_prosecutor USING BTREE
 ( prosecutor );

CREATE TABLE public.case_policeman (
                case_1 INTEGER NOT NULL,
                policeman INTEGER NOT NULL,
                role INTEGER NOT NULL,
                action_date DATE,
                notes TEXT,
                CONSTRAINT case_policeman_pkey PRIMARY KEY (case_1, policeman)
);


CREATE INDEX ix_case_policeman_policeman
 ON public.case_policeman USING BTREE
 ( policeman );

CREATE TABLE public.case_plaintiff (
                case_1 INTEGER NOT NULL,
                plaintiff INTEGER NOT NULL,
                CONSTRAINT case_plaintiff_pkey PRIMARY KEY (case_1, plaintiff)
);


CREATE INDEX ix_case_plaintiff_plaintiff
 ON public.case_plaintiff USING BTREE
 ( plaintiff );

CREATE TABLE public.case_offense (
                case_1 INTEGER NOT NULL,
                offense INTEGER NOT NULL,
                CONSTRAINT case_offense_pkey PRIMARY KEY (case_1, offense)
);


CREATE INDEX ix_case_offense_offense
 ON public.case_offense USING BTREE
 ( offense );

CREATE TABLE public.case_judge (
                case_1 INTEGER NOT NULL,
                judge INTEGER NOT NULL,
                CONSTRAINT case_judge_pkey PRIMARY KEY (case_1, judge)
);


CREATE INDEX ix_case_judge_judge
 ON public.case_judge USING BTREE
 ( judge );

CREATE TABLE public.case_defendant (
                case_1 INTEGER NOT NULL,
                defendant INTEGER NOT NULL,
                CONSTRAINT case_defendant_pkey PRIMARY KEY (case_1, defendant)
);


CREATE INDEX ix_case_defendant_defendant
 ON public.case_defendant USING BTREE
 ( defendant );

CREATE TABLE public.case_casestatus (
                case_1 INTEGER NOT NULL,
                casestatus INTEGER NOT NULL,
                CONSTRAINT case_casestatus_pkey PRIMARY KEY (case_1, casestatus)
);


CREATE INDEX ix_case_casestatus_casestatus
 ON public.case_casestatus USING BTREE
 ( casestatus );

CREATE TABLE public.bail (
                case_1 INTEGER NOT NULL,
                created_on TIMESTAMP NOT NULL,
                changed_on TIMESTAMP NOT NULL,
                action VARCHAR(40),
                action_description TEXT,
                start_datetime DATE,
                start_notes VARCHAR(100),
                end_datetime TIMESTAMP,
                end_notes VARCHAR(100),
                defendant_fk INTEGER NOT NULL,
                amount DOUBLE PRECISION NOT NULL,
                surety_count INTEGER NOT NULL,
                paid BOOLEAN NOT NULL,
                paid_date DATE,
                receipt_number VARCHAR(50),
                notes TEXT,
                changed_by_fk INTEGER NOT NULL,
                created_by_fk INTEGER NOT NULL,
                CONSTRAINT bail_pkey PRIMARY KEY (case_1)
);


CREATE INDEX ix_bail_defendant_fk
 ON public.bail USING BTREE
 ( defendant_fk );

CREATE TABLE public.casehearing (
                case_fk INTEGER NOT NULL,
                created_on TIMESTAMP NOT NULL,
                changed_on TIMESTAMP NOT NULL,
                hearingtype_fk INTEGER NOT NULL,
                hearing_date TIMESTAMP NOT NULL,
                prosecutor_present BOOLEAN NOT NULL,
                defense_attorney_present BOOLEAN NOT NULL,
                case_outcome TEXT NOT NULL,
                prison_fk INTEGER NOT NULL,
                from_remand BOOLEAN NOT NULL,
                to_remand BOOLEAN NOT NULL,
                to_prison BOOLEAN NOT NULL,
                bail_fk INTEGER NOT NULL,
                notes TEXT NOT NULL,
                changed_by_fk INTEGER NOT NULL,
                created_by_fk INTEGER NOT NULL,
                CONSTRAINT casehearing_pkey PRIMARY KEY (case_fk)
);


CREATE INDEX ix_casehearing_bail_fk
 ON public.casehearing USING BTREE
 ( bail_fk );

CREATE INDEX ix_casehearing_hearingtype_fk
 ON public.casehearing USING BTREE
 ( hearingtype_fk );

CREATE INDEX ix_casehearing_prison_fk
 ON public.casehearing USING BTREE
 ( prison_fk );

CREATE SEQUENCE public.filing_id_seq;

CREATE TABLE public.filing (
                id INTEGER DEFAULT nextval('filing_id_seq'::regclass) NOT NULL DEFAULT nextval('public.filing_id_seq'),
                created_on TIMESTAMP NOT NULL,
                changed_on TIMESTAMP NOT NULL,
                case_fk INTEGER NOT NULL,
                filing_date TIMESTAMP NOT NULL,
                doc_name VARCHAR(50) NOT NULL,
                doc_content TEXT NOT NULL,
                case_hearing_fk INTEGER NOT NULL,
                filing_fee DOUBLE PRECISION NOT NULL,
                receipt_number VARCHAR(20) NOT NULL,
                received_by VARCHAR(50) NOT NULL,
                changed_by_fk INTEGER NOT NULL,
                created_by_fk INTEGER NOT NULL,
                CONSTRAINT filing_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.filing_id_seq OWNED BY public.filing.id;

CREATE INDEX ix_filing_case_fk
 ON public.filing USING BTREE
 ( case_fk );

CREATE INDEX ix_filing_case_hearing_fk
 ON public.filing USING BTREE
 ( case_hearing_fk );

CREATE TABLE public.filing_plaintiff (
                filing INTEGER NOT NULL,
                plaintiff INTEGER NOT NULL,
                CONSTRAINT filing_plaintiff_pkey PRIMARY KEY (filing, plaintiff)
);


CREATE INDEX ix_filing_plaintiff_plaintiff
 ON public.filing_plaintiff USING BTREE
 ( plaintiff );

CREATE TABLE public.feeschedule_filing (
                feeschedule INTEGER NOT NULL,
                filing INTEGER NOT NULL,
                CONSTRAINT feeschedule_filing_pkey PRIMARY KEY (feeschedule, filing)
);


CREATE INDEX ix_feeschedule_filing_filing
 ON public.feeschedule_filing USING BTREE
 ( filing );

CREATE TABLE public.document_filing (
                document INTEGER NOT NULL,
                filing INTEGER NOT NULL,
                CONSTRAINT document_filing_pkey PRIMARY KEY (document, filing)
);


CREATE INDEX ix_document_filing_filing
 ON public.document_filing USING BTREE
 ( filing );

CREATE TABLE public.defendant_filing (
                defendant INTEGER NOT NULL,
                filing INTEGER NOT NULL,
                CONSTRAINT defendant_filing_pkey PRIMARY KEY (defendant, filing)
);


CREATE INDEX ix_defendant_filing_filing
 ON public.defendant_filing USING BTREE
 ( filing );

CREATE TABLE public.casehearing_witness (
                casehearing INTEGER NOT NULL,
                witness INTEGER NOT NULL,
                testimony TEXT,
                credible BOOLEAN,
                cross_examined BOOLEAN,
                notes TEXT,
                CONSTRAINT casehearing_witness_pkey PRIMARY KEY (casehearing, witness)
);


CREATE INDEX ix_casehearing_witness_witness
 ON public.casehearing_witness USING BTREE
 ( witness );

CREATE TABLE public.casehearing_prosecutor (
                casehearing INTEGER NOT NULL,
                prosecutor INTEGER NOT NULL,
                CONSTRAINT casehearing_prosecutor_pkey PRIMARY KEY (casehearing, prosecutor)
);


CREATE INDEX ix_casehearing_prosecutor_prosecutor
 ON public.casehearing_prosecutor USING BTREE
 ( prosecutor );

CREATE TABLE public.casehearing_policeman (
                casehearing INTEGER NOT NULL,
                policeman INTEGER NOT NULL,
                role VARCHAR(40),
                CONSTRAINT casehearing_policeman_pkey PRIMARY KEY (casehearing, policeman)
);


CREATE INDEX ix_casehearing_policeman_policeman
 ON public.casehearing_policeman USING BTREE
 ( policeman );

CREATE TABLE public.casehearing_plaintiff (
                casehearing INTEGER NOT NULL,
                plaintiff INTEGER NOT NULL,
                CONSTRAINT casehearing_plaintiff_pkey PRIMARY KEY (casehearing, plaintiff)
);


CREATE INDEX ix_casehearing_plaintiff_plaintiff
 ON public.casehearing_plaintiff USING BTREE
 ( plaintiff );

CREATE TABLE public.casehearing_judge (
                casehearing INTEGER NOT NULL,
                judge INTEGER NOT NULL,
                CONSTRAINT casehearing_judge_pkey PRIMARY KEY (casehearing, judge)
);


CREATE INDEX ix_casehearing_judge_judge
 ON public.casehearing_judge USING BTREE
 ( judge );

CREATE TABLE public.casehearing_defendant (
                casehearing INTEGER NOT NULL,
                defendant INTEGER NOT NULL,
                CONSTRAINT casehearing_defendant_pkey PRIMARY KEY (casehearing, defendant)
);


CREATE INDEX ix_casehearing_defendant_defendant
 ON public.casehearing_defendant USING BTREE
 ( defendant );

CREATE TABLE public.bail_surety (
                bail INTEGER NOT NULL,
                surety INTEGER NOT NULL,
                CONSTRAINT bail_surety_pkey PRIMARY KEY (bail, surety)
);


CREATE INDEX ix_bail_surety_surety
 ON public.bail_surety USING BTREE
 ( surety );

CREATE SEQUENCE public.attorney_id_seq;

CREATE TABLE public.attorney (
                id INTEGER DEFAULT nextval('attorney_id_seq'::regclass) NOT NULL DEFAULT nextval('public.attorney_id_seq'),
                created_on TIMESTAMP NOT NULL,
                changed_on TIMESTAMP NOT NULL,
                firstname VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL,
                othernames VARCHAR(100),
                dob DATE,
                age INTEGER,
                marital_status VARCHAR(10),
                picture TEXT,
                bc_id VARCHAR(20),
                bc_number VARCHAR(20),
                bc_serial VARCHAR(20),
                bc_place VARCHAR(20),
                bc_scan TEXT,
                citizenship VARCHAR(20),
                nat_id_num VARCHAR(15),
                nat_id_serial VARCHAR(30),
                nat_id_scan TEXT,
                pp_no VARCHAR(20),
                pp_issue_date DATE,
                pp_issue_place VARCHAR(40),
                pp_scan TEXT,
                pp_expiry_date DATE,
                allergies TEXT,
                chronic_conditions TEXT,
                chronic_medications TEXT,
                hbp BOOLEAN,
                diabetes BOOLEAN,
                hiv BOOLEAN,
                current_health_status TEXT,
                kin1_name VARCHAR(40),
                kin1_phone VARCHAR(50),
                kin1_email VARCHAR(125),
                kin1_addr TEXT,
                kin2_name VARCHAR(40),
                kin2_phone VARCHAR(50),
                kin2_email VARCHAR(125),
                kin2_addr TEXT,
                mobile VARCHAR(12),
                other_mobile VARCHAR(12),
                fixed_line VARCHAR(20),
                other_fixed_line VARCHAR(20),
                email VARCHAR(60),
                other_email VARCHAR(60),
                address_line_1 VARCHAR(200),
                address_line_2 VARCHAR(200),
                zipcode VARCHAR(20),
                town VARCHAR(20),
                country VARCHAR(50),
                facebook VARCHAR(40),
                twitter VARCHAR(40),
                instagram VARCHAR(40),
                whatsapp BOOLEAN,
                other_whatsapp BOOLEAN,
                fax VARCHAR(20),
                gcode VARCHAR(40),
                okhi VARCHAR(40),
                bar_number VARCHAR(20) NOT NULL,
                call_to_bar_year INTEGER NOT NULL,
                university VARCHAR(60),
                grad_year INTEGER,
                gender_fk INTEGER NOT NULL,
                lawfirm_fk INTEGER NOT NULL,
                changed_by_fk INTEGER NOT NULL,
                created_by_fk INTEGER NOT NULL,
                CONSTRAINT attorney_pkey PRIMARY KEY (id)
);


ALTER SEQUENCE public.attorney_id_seq OWNED BY public.attorney.id;

CREATE UNIQUE INDEX ix_attorney_bc_id
 ON public.attorney USING BTREE
 ( bc_id );

CREATE UNIQUE INDEX ix_attorney_nat_id_num
 ON public.attorney USING BTREE
 ( nat_id_num );

CREATE INDEX ix_attorney_bc_number
 ON public.attorney USING BTREE
 ( bc_number );

CREATE INDEX ix_attorney_bc_place
 ON public.attorney USING BTREE
 ( bc_place );

CREATE INDEX ix_attorney_bc_serial
 ON public.attorney USING BTREE
 ( bc_serial );

CREATE INDEX ix_attorney_dob
 ON public.attorney USING BTREE
 ( dob );

CREATE INDEX ix_attorney_firstname
 ON public.attorney USING BTREE
 ( firstname );

CREATE INDEX ix_attorney_lawfirm_fk
 ON public.attorney USING BTREE
 ( lawfirm_fk );

CREATE INDEX ix_attorney_mobile
 ON public.attorney USING BTREE
 ( mobile );

CREATE INDEX ix_attorney_nat_id_serial
 ON public.attorney USING BTREE
 ( nat_id_serial );

CREATE INDEX ix_attorney_pp_no
 ON public.attorney USING BTREE
 ( pp_no );

CREATE INDEX ix_attorney_surname
 ON public.attorney USING BTREE
 ( surname );

CREATE TABLE public.attorney_casehearing (
                attorney INTEGER NOT NULL,
                casehearing INTEGER NOT NULL,
                CONSTRAINT attorney_casehearing_pkey PRIMARY KEY (attorney, casehearing)
);


CREATE INDEX ix_attorney_casehearing_casehearing
 ON public.attorney_casehearing USING BTREE
 ( casehearing );

CREATE TABLE public.attorney_case (
                attorney INTEGER NOT NULL,
                case_1 INTEGER NOT NULL,
                CONSTRAINT attorney_case_pkey PRIMARY KEY (attorney, case_1)
);


CREATE INDEX ix_attorney_case_case
 ON public.attorney_case USING BTREE
 ( case_1 );

CREATE TABLE public.ab_role (
                id INTEGER NOT NULL,
                name VARCHAR(64) NOT NULL,
                CONSTRAINT ab_role_pkey PRIMARY KEY (id)
);


CREATE UNIQUE INDEX ab_role_name_key
 ON public.ab_role USING BTREE
 ( name );

CREATE TABLE public.ab_user_role (
                id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                role_id INTEGER NOT NULL,
                CONSTRAINT ab_user_role_pkey PRIMARY KEY (id)
);


CREATE TABLE public.ab_register_user (
                id INTEGER NOT NULL,
                first_name VARCHAR(64) NOT NULL,
                last_name VARCHAR(64) NOT NULL,
                username VARCHAR(64) NOT NULL,
                password VARCHAR(256),
                email VARCHAR(64) NOT NULL,
                registration_date TIMESTAMP,
                registration_hash VARCHAR(256),
                CONSTRAINT ab_register_user_pkey PRIMARY KEY (id)
);


CREATE UNIQUE INDEX ab_register_user_username_key
 ON public.ab_register_user USING BTREE
 ( username );

CREATE TABLE public.ab_permission (
                id INTEGER NOT NULL,
                name VARCHAR(100) NOT NULL,
                CONSTRAINT ab_permission_pkey PRIMARY KEY (id)
);


CREATE UNIQUE INDEX ab_permission_name_key
 ON public.ab_permission USING BTREE
 ( name );

CREATE TABLE public.ab_permission_view (
                id INTEGER NOT NULL,
                permission_id INTEGER NOT NULL,
                view_menu_id INTEGER NOT NULL,
                CONSTRAINT ab_permission_view_pkey PRIMARY KEY (id)
);


CREATE TABLE public.ab_permission_view_role (
                id INTEGER NOT NULL,
                permission_view_id INTEGER NOT NULL,
                role_id INTEGER NOT NULL,
                CONSTRAINT ab_permission_view_role_pkey PRIMARY KEY (id)
);


ALTER TABLE public.bail_surety ADD CONSTRAINT bail_surety_surety_fkey
FOREIGN KEY (surety)
REFERENCES public.surety (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.district ADD CONSTRAINT district_region_fk_fkey
FOREIGN KEY (region_fk)
REFERENCES public.region (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.prosecutor ADD CONSTRAINT prosecutor_pk_fk_fkey
FOREIGN KEY (pk_fk)
REFERENCES public.prosecutor_team (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_policeman ADD CONSTRAINT case_policeman_role_fkey
FOREIGN KEY (role)
REFERENCES public.police_role (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_offense ADD CONSTRAINT case_offense_offense_fkey
FOREIGN KEY (offense)
REFERENCES public.offense (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.attorney ADD CONSTRAINT attorney_lawfirm_fk_fkey
FOREIGN KEY (lawfirm_fk)
REFERENCES public.lawfirm (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing ADD CONSTRAINT casehearing_hearingtype_fk_fkey
FOREIGN KEY (hearingtype_fk)
REFERENCES public.hearingtype (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.attorney ADD CONSTRAINT attorney_gender_fk_fkey
FOREIGN KEY (gender_fk)
REFERENCES public.gender (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.complaint ADD CONSTRAINT complaint_victim_gender_fk_fkey
FOREIGN KEY (victim_gender_fk)
REFERENCES public.gender (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.defendant ADD CONSTRAINT defendant_gender_fk_fkey
FOREIGN KEY (gender_fk)
REFERENCES public.gender (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.judge ADD CONSTRAINT judge_gender_fk_fkey
FOREIGN KEY (gender_fk)
REFERENCES public.gender (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.plaintiff ADD CONSTRAINT plaintiff_gender_fk_fkey
FOREIGN KEY (gender_fk)
REFERENCES public.gender (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.policeman ADD CONSTRAINT policeman_gender_fk_fkey
FOREIGN KEY (gender_fk)
REFERENCES public.gender (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.prosecutor ADD CONSTRAINT prosecutor_gender_fk_fkey
FOREIGN KEY (gender_fk)
REFERENCES public.gender (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.witness ADD CONSTRAINT witness_gender_fk_fkey
FOREIGN KEY (gender_fk)
REFERENCES public.gender (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_witness ADD CONSTRAINT case_witness_witness_fkey
FOREIGN KEY (witness)
REFERENCES public.witness (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_witness ADD CONSTRAINT casehearing_witness_witness_fkey
FOREIGN KEY (witness)
REFERENCES public.witness (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_prosecutor ADD CONSTRAINT case_prosecutor_prosecutor_fkey
FOREIGN KEY (prosecutor)
REFERENCES public.prosecutor (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_prosecutor ADD CONSTRAINT casehearing_prosecutor_prosecutor_fkey
FOREIGN KEY (prosecutor)
REFERENCES public.prosecutor (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.feeschedule_filing ADD CONSTRAINT feeschedule_filing_feeschedule_fkey
FOREIGN KEY (feeschedule)
REFERENCES public.feeschedule (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.town ADD CONSTRAINT town_district_fk_fkey
FOREIGN KEY (district_fk)
REFERENCES public.district (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.court ADD CONSTRAINT court_town_fk_fkey
FOREIGN KEY (town_fk)
REFERENCES public.town (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.policestation ADD CONSTRAINT policestation_town_fk_fkey
FOREIGN KEY (town_fk)
REFERENCES public.town (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.prison ADD CONSTRAINT prison_town_fk_fkey
FOREIGN KEY (town_fk)
REFERENCES public.town (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing ADD CONSTRAINT casehearing_prison_fk_fkey
FOREIGN KEY (prison_fk)
REFERENCES public.prison (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.defendant_prison ADD CONSTRAINT defendant_prison_prison_fkey
FOREIGN KEY (prison)
REFERENCES public.prison (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.complaint ADD CONSTRAINT complaint_station_id_fkey
FOREIGN KEY (station_id)
REFERENCES public.policestation (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.policeman ADD CONSTRAINT policeman_police_station_fk_fkey
FOREIGN KEY (police_station_fk)
REFERENCES public.policestation (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_policeman ADD CONSTRAINT case_policeman_policeman_fkey
FOREIGN KEY (policeman)
REFERENCES public.policeman (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_policeman ADD CONSTRAINT casehearing_policeman_policeman_fkey
FOREIGN KEY (policeman)
REFERENCES public.policeman (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.complaint_policeman ADD CONSTRAINT complaint_policeman_policeman_fkey
FOREIGN KEY (policeman)
REFERENCES public.policeman (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.court ADD CONSTRAINT court_court_level_fk_fkey
FOREIGN KEY (court_level_fk)
REFERENCES public.courtlevel (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.judge ADD CONSTRAINT judge_court_level_fk_fkey
FOREIGN KEY (court_level_fk)
REFERENCES public.courtlevel (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_1 ADD CONSTRAINT case_court_fk_fkey
FOREIGN KEY (court_fk)
REFERENCES public.court (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.judge ADD CONSTRAINT judge_court_fk_fkey
FOREIGN KEY (court_fk)
REFERENCES public.court (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_judge ADD CONSTRAINT case_judge_judge_fkey
FOREIGN KEY (judge)
REFERENCES public.judge (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_judge ADD CONSTRAINT casehearing_judge_judge_fkey
FOREIGN KEY (judge)
REFERENCES public.judge (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_casestatus ADD CONSTRAINT case_casestatus_casestatus_fkey
FOREIGN KEY (casestatus)
REFERENCES public.casestatus (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_1 ADD CONSTRAINT case_case_category_fk_fkey
FOREIGN KEY (case_category_fk)
REFERENCES public.casecategory (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ab_permission_view ADD CONSTRAINT ab_permission_view_view_menu_id_fkey
FOREIGN KEY (view_menu_id)
REFERENCES public.ab_view_menu (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ab_user ADD CONSTRAINT ab_user_changed_by_fk_fkey
FOREIGN KEY (changed_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ab_user ADD CONSTRAINT ab_user_created_by_fk_fkey
FOREIGN KEY (created_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ab_user_role ADD CONSTRAINT ab_user_role_user_id_fkey
FOREIGN KEY (user_id)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.attorney ADD CONSTRAINT attorney_created_by_fk_fkey
FOREIGN KEY (created_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.attorney ADD CONSTRAINT attorney_changed_by_fk_fkey
FOREIGN KEY (changed_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.bail ADD CONSTRAINT bail_changed_by_fk_fkey
FOREIGN KEY (changed_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.bail ADD CONSTRAINT bail_created_by_fk_fkey
FOREIGN KEY (created_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_1 ADD CONSTRAINT case_created_by_fk_fkey
FOREIGN KEY (created_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_1 ADD CONSTRAINT case_changed_by_fk_fkey
FOREIGN KEY (changed_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing ADD CONSTRAINT casehearing_changed_by_fk_fkey
FOREIGN KEY (changed_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing ADD CONSTRAINT casehearing_created_by_fk_fkey
FOREIGN KEY (created_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.complaint ADD CONSTRAINT complaint_changed_by_fk_fkey
FOREIGN KEY (changed_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.complaint ADD CONSTRAINT complaint_created_by_fk_fkey
FOREIGN KEY (created_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.contact ADD CONSTRAINT contact_created_by_fk_fkey
FOREIGN KEY (created_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.contact ADD CONSTRAINT contact_changed_by_fk_fkey
FOREIGN KEY (changed_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.defendant ADD CONSTRAINT defendant_changed_by_fk_fkey
FOREIGN KEY (changed_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.defendant ADD CONSTRAINT defendant_created_by_fk_fkey
FOREIGN KEY (created_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.document ADD CONSTRAINT document_created_by_fk_fkey
FOREIGN KEY (created_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.document ADD CONSTRAINT document_changed_by_fk_fkey
FOREIGN KEY (changed_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.filing ADD CONSTRAINT filing_changed_by_fk_fkey
FOREIGN KEY (changed_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.filing ADD CONSTRAINT filing_created_by_fk_fkey
FOREIGN KEY (created_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.plaintiff ADD CONSTRAINT plaintiff_created_by_fk_fkey
FOREIGN KEY (created_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.plaintiff ADD CONSTRAINT plaintiff_changed_by_fk_fkey
FOREIGN KEY (changed_by_fk)
REFERENCES public.ab_user (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_plaintiff ADD CONSTRAINT case_plaintiff_plaintiff_fkey
FOREIGN KEY (plaintiff)
REFERENCES public.plaintiff (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_plaintiff ADD CONSTRAINT casehearing_plaintiff_plaintiff_fkey
FOREIGN KEY (plaintiff)
REFERENCES public.plaintiff (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.complaint_plaintiff ADD CONSTRAINT complaint_plaintiff_plaintiff_fkey
FOREIGN KEY (plaintiff)
REFERENCES public.plaintiff (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.contact_plaintiff ADD CONSTRAINT contact_plaintiff_plaintiff_fkey
FOREIGN KEY (plaintiff)
REFERENCES public.plaintiff (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.filing_plaintiff ADD CONSTRAINT filing_plaintiff_plaintiff_fkey
FOREIGN KEY (plaintiff)
REFERENCES public.plaintiff (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.document_filing ADD CONSTRAINT document_filing_document_fkey
FOREIGN KEY (document)
REFERENCES public.document (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.bail ADD CONSTRAINT bail_defendant_fk_fkey
FOREIGN KEY (defendant_fk)
REFERENCES public.defendant (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_defendant ADD CONSTRAINT case_defendant_defendant_fkey
FOREIGN KEY (defendant)
REFERENCES public.defendant (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_defendant ADD CONSTRAINT casehearing_defendant_defendant_fkey
FOREIGN KEY (defendant)
REFERENCES public.defendant (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.complaint_defendant ADD CONSTRAINT complaint_defendant_defendant_fkey
FOREIGN KEY (defendant)
REFERENCES public.defendant (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.defendant_filing ADD CONSTRAINT defendant_filing_defendant_fkey
FOREIGN KEY (defendant)
REFERENCES public.defendant (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.defendant_prison ADD CONSTRAINT defendant_prison_defendant_fkey
FOREIGN KEY (defendant)
REFERENCES public.defendant (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.contact_plaintiff ADD CONSTRAINT contact_plaintiff_contact_fkey
FOREIGN KEY (contact)
REFERENCES public.contact (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.attorney_case ADD CONSTRAINT attorney_case_case_fkey
FOREIGN KEY (case_1)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.bail ADD CONSTRAINT bail_case_fkey
FOREIGN KEY (case_1)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_casestatus ADD CONSTRAINT case_casestatus_case_fkey
FOREIGN KEY (case_1)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_defendant ADD CONSTRAINT case_defendant_case_fkey
FOREIGN KEY (case_1)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_judge ADD CONSTRAINT case_judge_case_fkey
FOREIGN KEY (case_1)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_offense ADD CONSTRAINT case_offense_case_fkey
FOREIGN KEY (case_1)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_plaintiff ADD CONSTRAINT case_plaintiff_case_fkey
FOREIGN KEY (case_1)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_policeman ADD CONSTRAINT case_policeman_case_fkey
FOREIGN KEY (case_1)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_prosecutor ADD CONSTRAINT case_prosecutor_case_fkey
FOREIGN KEY (case_1)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.case_witness ADD CONSTRAINT case_witness_case_fkey
FOREIGN KEY (case_1)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing ADD CONSTRAINT casehearing_case_fk_fkey
FOREIGN KEY (case_fk)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.complaint ADD CONSTRAINT complaint_case_fkey
FOREIGN KEY (case_1)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.filing ADD CONSTRAINT filing_case_fk_fkey
FOREIGN KEY (case_fk)
REFERENCES public.case_1 (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.complaint_defendant ADD CONSTRAINT complaint_defendant_complaint_fkey
FOREIGN KEY (complaint)
REFERENCES public.complaint (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.complaint_plaintiff ADD CONSTRAINT complaint_plaintiff_complaint_fkey
FOREIGN KEY (complaint)
REFERENCES public.complaint (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.complaint_policeman ADD CONSTRAINT complaint_policeman_complaint_fkey
FOREIGN KEY (complaint)
REFERENCES public.complaint (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.bail_surety ADD CONSTRAINT bail_surety_bail_fkey
FOREIGN KEY (bail)
REFERENCES public.bail (case_1)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing ADD CONSTRAINT casehearing_bail_fk_fkey
FOREIGN KEY (bail_fk)
REFERENCES public.bail (case_1)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.attorney_casehearing ADD CONSTRAINT attorney_casehearing_casehearing_fkey
FOREIGN KEY (casehearing)
REFERENCES public.casehearing (case_fk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_defendant ADD CONSTRAINT casehearing_defendant_casehearing_fkey
FOREIGN KEY (casehearing)
REFERENCES public.casehearing (case_fk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_judge ADD CONSTRAINT casehearing_judge_casehearing_fkey
FOREIGN KEY (casehearing)
REFERENCES public.casehearing (case_fk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_plaintiff ADD CONSTRAINT casehearing_plaintiff_casehearing_fkey
FOREIGN KEY (casehearing)
REFERENCES public.casehearing (case_fk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_policeman ADD CONSTRAINT casehearing_policeman_casehearing_fkey
FOREIGN KEY (casehearing)
REFERENCES public.casehearing (case_fk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_prosecutor ADD CONSTRAINT casehearing_prosecutor_casehearing_fkey
FOREIGN KEY (casehearing)
REFERENCES public.casehearing (case_fk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.casehearing_witness ADD CONSTRAINT casehearing_witness_casehearing_fkey
FOREIGN KEY (casehearing)
REFERENCES public.casehearing (case_fk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.filing ADD CONSTRAINT filing_case_hearing_fk_fkey
FOREIGN KEY (case_hearing_fk)
REFERENCES public.casehearing (case_fk)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.defendant_filing ADD CONSTRAINT defendant_filing_filing_fkey
FOREIGN KEY (filing)
REFERENCES public.filing (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.document_filing ADD CONSTRAINT document_filing_filing_fkey
FOREIGN KEY (filing)
REFERENCES public.filing (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.feeschedule_filing ADD CONSTRAINT feeschedule_filing_filing_fkey
FOREIGN KEY (filing)
REFERENCES public.filing (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.filing_plaintiff ADD CONSTRAINT filing_plaintiff_filing_fkey
FOREIGN KEY (filing)
REFERENCES public.filing (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.attorney_case ADD CONSTRAINT attorney_case_attorney_fkey
FOREIGN KEY (attorney)
REFERENCES public.attorney (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.attorney_casehearing ADD CONSTRAINT attorney_casehearing_attorney_fkey
FOREIGN KEY (attorney)
REFERENCES public.attorney (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ab_permission_view_role ADD CONSTRAINT ab_permission_view_role_role_id_fkey
FOREIGN KEY (role_id)
REFERENCES public.ab_role (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ab_user_role ADD CONSTRAINT ab_user_role_role_id_fkey
FOREIGN KEY (role_id)
REFERENCES public.ab_role (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ab_permission_view ADD CONSTRAINT ab_permission_view_permission_id_fkey
FOREIGN KEY (permission_id)
REFERENCES public.ab_permission (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ab_permission_view_role ADD CONSTRAINT ab_permission_view_role_permission_view_id_fkey
FOREIGN KEY (permission_view_id)
REFERENCES public.ab_permission_view (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
