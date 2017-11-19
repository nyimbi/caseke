from base64 import b64encode
import calendar
from base64 import b64encode
from datetime import MINYEAR, date, datetime, timedelta
from hashlib import sha256

import humanize, hashlib
import os
import sqlalchemy.types as types
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy.orm import validates
from sqlalchemy_utils import observes
from flask import Markup, escape, url_for
# from flask_appbuilder.filemanager import ImageManager, get_file_original_name
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import (
	Boolean, CheckConstraint, Column, Date, DateTime, Float, ForeignKey, Integer, Numeric, String,
	Text, Interval
	)
from flask.ext.sqlalchemy import  BaseQuery #SQLAlchemy,
from sqlalchemy_searchable import SearchQueryMixin
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy_searchable import make_searchable

from sqlalchemy_mixins import AllFeaturesMixin

from sqlalchemy.dialects.postgresql import (
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE,
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER,
    INTERVAL, JSON, JSONB, MACADDR, NUMERIC, OID, REAL, SMALLINT, TEXT,
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE,
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR )

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy_continuum import make_versioned


##################################################################
#### Utility Functions
# pip install SQLAlchemy-Searchable
# pip install SQLAlchemy-Continuum
# pip install sqlalchemy-mixins
##################################################################

make_searchable()


mindate = date(MINYEAR, 1, 1)

def today():
	return datetime.today().strftime('%Y-%m-%d')

# This implements a lower case string
class LowerCaseString(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        return value.lower()
    
class UpperCaseString(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        return value.upper()
    
class TitleCaseString(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        return value.title()
    
    

audit_exclude_columns = ['created_by', 'created_on', 'changed_by', 'changed_on']
add_exclude_columns = edit_exclude_columns = audit_exclude_columns


### UTILITY Classes #####
class AuditMixinNullable(AuditMixin):
	"""Altering the AuditMixin to use nullable fields
	Allows creating objects programmatically outside of CRUD
	"""
	
	created_on = Column(DateTime, default=func.now(), nullable=True)
	changed_on = Column(
			DateTime, default=func.now(),
			onupdate=func.now(), nullable=True)
	
	@declared_attr
	def created_by_fk(cls):  # noqa
		return Column(Integer, ForeignKey('ab_user.id'),
					  default=cls.get_user_id, nullable=True)
	
	@declared_attr
	def changed_by_fk(cls):  # noqa
		return Column(
				Integer, ForeignKey('ab_user.id'),
				default=cls.get_user_id, onupdate=cls.get_user_id, nullable=True)
	
	def _user_link(self, user):
		if not user:
			return ''
		url = '/prn/profile/{}/'.format(user.username)
		return Markup('<a href="{}">{}</a>'.format(url, escape(user) or ''))
	
	@renders('created_by')
	def creator(self):  # noqa
		return self._user_link(self.created_by)
	
	@property
	def changed_by_(self):
		return self._user_link(self.changed_by)
	
	@renders('changed_on')
	def changed_on_(self):
		return Markup(
				'<span class="no-wrap">{}</span>'.format(self.changed_on))
	
	@renders('changed_on')
	def modified(self):
		s = humanize.naturaltime(datetime.now() - self.changed_on)
		return Markup('<span class="no-wrap">{}</span>'.format(s))
	
	@property
	def icons(self):
		return """
        <a
                href="{self.datasource_edit_url}"
                data-toggle="tooltip"
                title="{self.datasource}">
            <i class="fa fa-database"></i>
        </a>
        """.format(**locals())


ref_fieldset = [
	('Reference', {'fields': ['name', 'description', 'notes'], 'expanded': True})
	]

ref_columns = ['name', 'description']


class RefTypeMixin(object):
	# id = Column(Integer, autoincrement=True, primary_key=True)
	name = Column(String(100), unique=True, nullable=False, index=True)
	# code = Column(String(20), default='0000')
	description = Column(String(100))
	notes = Column(Text, default='')
	
	# # def __init__(self, name):
	# #     self.name = name
	#
	def __repr__(self):
		return self.name


class NameMixin(object):
	# id = Column(Integer, autoincrement=True, primary_key=True)
	name = Column(String(100))
	# code = Column(String(20), default='0000')
	description = Column(String(100))
	notes = Column(Text, default='')
	
	def __repr__(self):
		return self.name
	
	
	
	
case_activity = [
	('Activity', {'fields': ['action', 'activity_description', 'status']}),
	('Budget', {'fields': ['budget', 'spend_td']}),
	('Start', {'fields': ['planned_start', 'start_notes']}),
	('End', {'fields': ['planned_end', 'end_notes'], 'expanded': False}),
	
	('Details', {'fields': ['task_group', 'segment', 'priority'], 'expanded': False}),
	('Tracking', {'fields': ['not_started',  'actual_start', 'actual_end', 'completed'],
	              'expanded': False}),
	('Contingency', {'fields': ['contingency_plan'], 'expanded': False}),
	]

activity_fieldset = [
	('Activity', {'fields': ['action', 'activity_description','status']}),
	('Budget', {'fields': ['budget', 'spend_td']}),
	('Start', {'fields': ['planned_start','start_notes']}),
	('End', {'fields': ['planned_end', 'end_notes'], 'expanded': False}),
	
	('Details', {'fields': ['task_group', 'segment','priority'], 'expanded': False}),
	('Tracking', {'fields': ['not_started','planned_start','actual_start', 'planned_end', 'actual_end','completed'], 'expanded': False}),
	('Contingency', {'fields': ['contingency_plan'], 'expanded': False}),
	]

act_List_columns = ['action', 'deadline', 'budget', 'spend_td']

class ActivityMixin(object):
	priority = Column(Integer, default=5)
	segment = Column(Integer)
	task_group = Column(Integer)
	sequence = Column(Integer)
	
	
	action = Column(String(40))
	activity_description = Column(Text)
	goal = Column(Text)
	status = Column(String(40))
	
	planned_start = Column(Date, default=func.now())
	actual_start = Column(Date, default=func.now())
	start_delay = Column(Interval)
	start_notes = Column(String(100))
	
	@observes('actual_start', 'planned_start')
	def start_delay_observer(self, actual_start, planned_start):
		self.start_delay = planned_start - actual_start


	# @validates('actual_start')
	# def update_start_delay(self, key, value):
	# 	self.start_delay = datetime(self.actual_start) - datetime(self.planned_start)
	# 	if self.start_delay > 0:
	# 		self.late_start = True
	# 		self.early_start = False
	# 	else:
	# 		self.late_start = False
	# 		self.early_start = True
	#
	# @renders('delay_of_start')
	# def start_delay_(self):
	# 	return humanize.naturaltime(self.start_delay)
	
	planned_end = Column(Date, default=func.now())
	actual_end = Column(DateTime, nullable=True, default=func.now())
	end_delay = Column(Interval)
	end_notes = Column(String(100))
	
	@observes('actual_end', 'planned_end')
	def end_delay_observer(self, actual_end, planned_end):
		self.end_delay = planned_end - actual_end
	
	# @validates('actual_end')
	# def update_send_delay(self, key, value):
	# 	self.end_delay = self.actual_end - self.planned_end
	# 	if self.end_delay > 0:
	# 		self.late_end = True
	# 	else:
	# 		self.late_end = False
	# 	self.early_end = not self.late_end
	#
	# @renders('delay_of_end')
	# def send_delay_(self):
	# 	return humanize.naturaltime(self.end_delay)
	
	
	deadline = Column(Date, default=func.now())
	# Admin Stuff
	not_started = Column(Boolean, default=True)
	early_start = Column(Boolean, default=False)
	late_start =  Column(Boolean, default=False)
	completed = Column(Boolean, default=False)
	early_end = Column(Boolean, default=False)
	late_end =  Column(Boolean, default=False)
	deviation_expected = Column(Boolean, default=False)
	
	contingency_plan = Column(Text)
	
	# Money
	budget = Column(Numeric(10,2), default=0.00)
	spend_td = Column(Numeric(10,2), default=0.00)
	balance_avail = Column(Numeric(10,2), default=0.00)
	over_budget = Column(Boolean, default=False)
	under_budget =Column(Boolean, default=False)
	
	CheckConstraint('actual_start >= actual_end')
	
	def __repr__(self):
		return self.action + ':' + str(self.actual_start)
	
	@renders('actual_start')
	def started(self):
		s = humanize.naturaltime(datetime.now() - self.actual_start)
		return Markup('<span class="no-wrap">Start: {}</span>'.format(s))
	
	@renders('delayed')
	def delayed(self):
		s = humanize.naturaltime(datetime.now() - self.planned_end)
		return Markup('<span class="no-wrap"> Delayed by: {}</span>'.format(s))
	
	@renders('duration')
	def lasted(self):
		dur = humanize.naturaltime(self.actual_end - self.actual_start)
		return Markup('<span class="no-wrap">Lasted: {}</span>'.format(dur))
		
	
	def __repr__(self):
		return str(self.action) + ' ' + str(self.actual_start)


place_fieldset = [
	('Where', {'fields': ['place_name', 'nearest_feature', 'lat', 'lng', 'alt'], 'expanded': False}),
	('Map', {'fields': ['map', 'pin', 'pin_color', 'centered'],'expanded': False})
	]


# Flask_googlemap entities
class PlaceMixin(object):
	place_name = Column(String(40))
	lat = Column(Float)
	lng = Column(Float)
	alt = Column(Float)
	map = Column(Text, default='')
	info = Column(Text, default='')
	pin = Column(Boolean)  # Do we put a pin
	pin_color = Column(String(20))
	pin_icon = Column(String(50))
	centered = Column(Boolean)
	nearest_feature = Column(String(100))
	
	def __repr__(self):
		return self.place_name


person_docs_fieldset = [
	('National ID', {'fields': ['citizenship', 'nat_id_num', 'nat_id_serial', 'nat_id_scan'], 'expanded': False}),
	('Birth Certificate', {'fields': ['bc_id', 'bc_number', 'bc_serial', 'bc_place', 'bc_scan'], 'expanded': False}),
	
	('Passport',
	 {'fields': ['pp_no', 'pp_issue_date', 'pp_issue_place', 'pp_expiry_date', 'pp_scan'], 'expanded': False}),
	
	('Next of Kin', {
		'fields': ['kin1_name', 'kin1_phone', 'kin1_email', 'kin1_addr', 'kin2_name', 'kin2_phone', 'kin2_email',
				   'kin2_addr'], 'expanded': False}),
	]
medical_fieldset = [
	('Medical Conditions', {
		'fields': ['allergies', 'chronic_conditions', 'chronic_medications', 'hbp', 'diabetes', 'hiv',
				   'current_health_status'], 'expanded': False}),
	]
person_fieldset = [
	('Picture', {'fields': ['photo']}),
	('Identity', {'fields': ['firstname', 'surname', 'othernames', 'gender1', 'dob', 'marital_status'], 'expanded': True})
	]

person_show_fieldset = [
	('Picture', {'fields': ['photo_img','photo']}),
	('Identity', {'fields': ['firstname', 'surname', 'othernames', 'gender1', 'age', 'dob', 'marital_status'], 'expanded': True})
	]
	
person_biometric_fieldset = [
	('Biometrics',
	 {'fields': ['fp_l1', 'fp_l2', 'fp_l3', 'fp_l4', 'fp_l5', 'fp_r1', 'fp_r2', 'fp_r3', 'fp_r4', 'fp_r5']}),
	('Palm & Retina', {'fields': ['finger_palm_left', 'finger_palm_right', 'eye_left', 'eye_right']})
	]

full_person_fieldset = person_fieldset + person_docs_fieldset + medical_fieldset + person_biometric_fieldset

person_search_exclude_columns = ['photo','photo_img','photo_img_thumbnail','fp_l1', 'fp_l2', 'fp_l3', 'fp_l4', 'fp_l5', 'fp_r1', 'fp_r2', 'fp_r3', 'fp_r4',
								 'fp_r5'] + ['finger_palm_left', 'finger_palm_right', 'eye_left', 'eye_right']

person_list_columns = ['firstname', 'surname', 'gender1','dob'] #'_age_today'
person_exclude_columns = ['photo', 'bc_scan', 'nat_id_scan', 'pp_scan','start_delay','end_delay','wsq','pgm','xyt']






class PersonMedicalMixin(object):
	# Medical Conditions
	allergies = Column(Text)
	chronic_conditions = Column(Text)
	chronic_medications = Column(Text)
	hbp = Column(Boolean)
	diabetes = Column(Boolean)
	hiv = Column(Boolean)
	current_health_status = Column(Text)
	
	
	
	
class PersonDocMixin(object):
	# Birth Certificate
	bc_id = Column(String(20), index=True, nullable=True)
	bc_number = Column(String(20), index=True)
	bc_serial = Column(String(20), index=True)
	bc_place = Column(String(20), index=True)
	bc_scan = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	
	# NationalID
	citizenship = Column(String(20), default='Kenyan')
	nat_id_num = Column(String(15), index=True)
	nat_id_serial = Column(String(30), index=True)
	nat_id_scan = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	
	# Passport
	pp_no = Column(String(20), index=True)
	pp_issue_date = Column(Date)
	pp_issue_place = Column(String(40))
	pp_scan = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	pp_expiry_date = Column(Date)
	
	# Next of Kin
	kin1_name = Column(String(100))
	kin1_relation = Column(String(100))
	kin1_phone = Column(String(50))
	kin1_email = Column(String(125))
	kin1_addr = Column(Text)
	
	kin2_name = Column(String(100))
	kin1_relation = Column(String(100))
	kin2_phone = Column(String(50))
	kin2_email = Column(String(125))
	kin2_addr = Column(Text)

class PersonMixin(object):
	# prn_id = Column(Integer, index=True)
	# prn = Column(String(6), unique=True, index=True)
	id = Column(Integer, autoincrement=True, primary_key=True)
	firstname = Column(String(40), nullable=False, index=True)
	surname = Column(String(40), nullable=False, index=True)
	othernames = Column(String(40), nullable=True, index=True)
	dob = Column(Date, default=func.now())
	
	marital_status = Column(String(10))
	photo = Column(ImageColumn(thumbnail_size=(30, 30, True), size=(300, 300, True)))
	
	
	
	# @declared_attr
	# def age_today(self):
	# 	today = date.today()
	# 	born = self.dob
	# 	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
	
	age_today = Column(Integer)
	
	@hybrid_property
	def _age_today(self):
		"""Property calculated from (current time - :attr:`User.date_of_birth` - leap days)"""
		if self.dob:
			today = (datetime.utcnow() + timedelta(hours=self.timezone)).date()
			birthday = self.dob
			if isinstance(birthday, datetime):
				birthday = birthday.date()
			age = today - (birthday or (today - timedelta(1)))
			self._age_today =  (age.days - calendar.leapdays(birthday.year, today.year)) / 365
			return self._age_today
		return -1
	
	@declared_attr
	def age(self):
		if isinstance(self.dob, datetime):
			doby = self.dob.date()
		else:
			doby = mindate
		dur = humanize.naturaltime(datetime.now().date() - doby)
		return Markup('<span class="no-wrap">{}</span>'.format(dur))
	
	
	# @declared_attr
	@hybrid_property
	def dob_month_year(self):
		if isinstance(self.dob, datetime):
			doby = self.dob.date()
		else:
			doby = mindate
		return datetime(doby.year, doby.month, 1)

	def month_year(self):
		date = self.dob or mindate
		return datetime(date.year, date.month, 1) or mindate
	
	def year(self):
		date = self.dob or mindate
		return datetime(date.year, 1, 1)
	
	def ViewName(self):
		return self.__class__.__name__ +'View.show'
	
	
	def __repr__(self):
		return '('+str(self.id) +') ' + self.firstname + ' ' + self.surname
	
	############# Challenge ###############
	# @hybrid_property
	# def photo_img(self):
	# 	im = ImageManager()
	#
	# 	vn = self.ViewName()
	# 	if self.photo:
	# 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	# 		              '" class="thumbnail"><img src="' + im.get_url(self.photo) + \
	# 		              '" alt="Photo" class="img-rounded img-responsive"></a>')
	# 	else:
	# 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	# 		              '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')
	# @hybrid_property
	# def photo_img_thumbnail(self):
	# 	im = ImageManager()
	# 	vn = self.ViewName()
	# 	if self.photo:
	# 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	# 		              '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) + \
	# 		              '" alt="Photo" class="img-rounded img-responsive"></a>')
	# 	else:
	# 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	# 		              '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')




biometric_fieldset = [
	('Bio Data', {'fields': ['eye_colour', 'hair_colour', 'complexion', 'blood_group', 'height_m', 'weight_kg',
							 'striking_features', 'religion', 'ethnicity'], 'expanded': False}),
	
	('Biometrics',
	 {'fields': ['fp_lthumb', 'fp_left2', 'fp_left3', 'fp_left4', 'fp_left5', 'fp_rthumb', 'fp_right2', 'fp_right3',
				 'fp_right4', 'fp_right5'],  'expanded': False}),
	('Palm & Retina',
	 {'fields': ['palm_left', 'palm_right', 'eye_left', 'eye_right'], 'expanded': False})
	]

biometric_columns = ['fp_lthumb', 'fp_left2', 'fp_left3', 'fp_left4', 'fp_left5',
					 'fp_rthumb', 'fp_right2', 'fp_right3', 'fp_right4', 'fp_right5',
					 'palm_left', 'palm_right', 'eye_left', 'eye_right']


class BiometricMixin(object):
	# Biodata
	blood_group = Column(String(3))
	striking_features = Column(Text)
	height_m = Column(Float, nullable=True)
	weight_kg = Column(Float, nullable=True)
	eye_colour = Column(String(20))
	hair_colour = Column(String(20))
	complexion = Column(String(50))
	religion = Column(String(20))
	ethnicity = Column(String(40))
	
	# Biometrics
	fp_lthumb = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	pgm = Column(BYTEA)
	wsq = Column(BYTEA)
	xyt = Column(BYTEA)
	fp_left2 = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	fp_left3 = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	fp_left4 = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	fp_left5 = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	fp_rthumb = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	fp_right2 = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	fp_right3 = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	fp_right4 = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	fp_right5 = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	
	palm_left = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	palm_right = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	
	eye_left = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))
	eye_right = Column(ImageColumn(thumbnail_size=(30, 60, True), size=(300, 600, True)))


class PRNMixin(object):
	@declared_attr
	def prn_id(cls):
		return Column(Integer, ForeignKey('humans.prn_id'), nullable=True, index=True)
	
	# prn_id = Column(Integer, ForeignKey('humans.prn_id'), nullable=False, index=True)
	def prn(self, cls):
		return relationship('Humans')
	
	# prn = relationship('Humans')


parentage_fieldset = [
	('Mother', {
		'fields': ['m_prn', 'm_firstname', 'm_surname', 'm_othernames', 'm_nat_id_num', 'm_education', 'm_occupation',
				   'm_income'], 'expanded': True}),
	('Father', {
		'fields': ['f_prn', 'f_firstname', 'f_surname', 'f_othernames', 'f_nat_id_num', 'f_education', 'f_occupation',
				   'f_income'], 'expanded': True})
	]

employment_fieldset = [
	('Employment', {'fields': ['employed', 'employer', 'employer_contact'], 'expanded': True}),
	('Employment Dates',
	 {'fields': ['employ_role', 'employ_date', 'termination_date', 'supervisor', 'supervisor_contact'], 'expanded': True}),
	]


class EmploymentMixin(object):
	employed = Column(Boolean)
	employer = Column(String(60))
	employer_contact = Column(Text)
	employ_date = Column(Date)
	employ_duration = Column(Integer)
	termination_date = Column(Date)
	employ_role = Column(String(50))
	supervisor = Column(String(50))
	supervisor_contact = Column(Text)


class ParentageMixin(object):
	# Mother
	m_prn = Column(String(6), index=True)
	m_firstname = Column(String(40), nullable=True)
	m_surname = Column(String(40), nullable=True)
	m_othernames = Column(String(100))
	m_nat_id_num = Column(String(15), index=True)
	m_education = Column(String(40))
	m_occupation = Column(String(40))
	m_income = Column(String(50))
	
	# Father
	f_prn = Column(String(6), index=True)
	f_firstname = Column(String(40), nullable=True)
	f_surname = Column(String(40), nullable=True)
	f_othernames = Column(String(100))
	f_nat_id_num = Column(String(15), index=True)
	f_education = Column(String(40))
	f_occupation = Column(String(40))
	f_income = Column(String(50))


# "addr_ln_1", "addr_ln_1"
#  'mobile', 'alt_mobile', 'email', 'facebook','twitter' , 'gcode'


case_fieldset = [
('Initiation',
	 {'fields': ['policestation','ob_number','report_date','report_notes'], 'expanded': True}),
# ('Evaluation',
# 	 {'fields': ['natureofsuit','policeman','initial_report','plaintiff','defendant','observer','priority','evaluation_conclusion','should_investigate_further'], 'expanded': False}),
# ('Investigation',
	 # {'fields': ['investigation_assigment_date','policeman1','investigation_assignment_note','investigation_plan','investigation_summary'], 'expanded': False}),

# ('Geek Stuff',
# 	 {'fields': ['mime_type','file_size_bytes', 'char_count','doc_type','char_count','word_count','lines','paragraphs','page_count'], 'expanded': False}),
	]


casey_fieldset = [
	('Initiation',
	    {'fields' : ['born_digital','policestation','polofficer','ob_number','report_date','complaint','casecategory'], 'expanded': True}),
	('Evaluation',
	    {'fields': ['natureofsuit','polofficer1','plaintiff','defendant','witness','priority','evaluation_conclusion','should_investigate_further'], 'expanded': False}),
	('Investigation',
	    {'fields': ['investigation_assigment_date', 'polofficer2','investigation_assignment_note','investigation_plan','investigation_summary','investigation_review', 'investigation_complete'], 'expanded': False}),
	('DPP Advice',
	    {'fields':['dpp_advice_requested','dpp_advice_request_date','dpp_advice','dpp_advice_date','send_to_trial','charge_date'], 'expanded': False}),
	('Prosecution',
	    {'fields':['causeofaction','docketnumber', 'case_name','charge_sheet','prosecutor','prosecution_notes','defense_notes'], 'expanded': False}),
	('Judgement',
	    {'fields':['judgement_date','judgement','case_closed','close_date'], 'expanded': False}),
	('Sentencing',
	    {'fields':['fine_amount','sentence_length_years','sentence_start_date','sentence_end_date','case_appealed','appeal_date','appeal_granted'], 'expanded': False}),
	('Tags',
	    {'fields':['tags']})
	]

full_contact_fieldset = [
	('Contact', {'fields': ['mobile', 'other_mobile', 'fixed_line', 'other_fixed_line', 'email',
							'other_email', 'address_line_1',
							'address_line_2', 'zipcode', 'town', 'country'],
	             'expanded': False}),
	('Social', {
		'fields': ['facebook', 'twitter', 'instagram', 'whatsapp', 'other_whatsapp']}),
	('Location', {'fields': ['gcode', 'okhi'], 'expanded': False})
	]

contact_fieldset = [
	('Contact', {'fields': ['mobile', 'fixed_line', 'email',
							'address_line_1',
							'address_line_2', 'zipcode'], 'expanded': False}), #'town', 'country'
	]

contact_columns = ['mobile', 'fixed_line', 'email'] #, 'town'


class ContactMixin(object):
	mobile = Column(String(30), index=True)
	other_mobile = Column(String(30))
	fixed_line = Column(String(30))
	other_fixed_line = Column(String(20))
	email = Column(String(60))
	other_email = Column(String(60))
	address_line_1 = Column(String(200))
	address_line_2 = Column(String(200))
	zipcode = Column(String(30))
	town = Column(String(40))
	country = Column(String(50), default='Ghana')
	facebook = Column(String(40))
	twitter = Column(String(40))
	instagram = Column(String(40))
	whatsapp = Column(Boolean)
	other_whatsapp = Column(Boolean)
	fax = Column(String(30))
	gcode = Column(String(40))
	okhi = Column(String(40))



# class LocationMixin(object):
# 	lat = Column(String(30))
# 	lon = Column(String(30))
# 	alt_m = Column(Float)
# 	gmap=Column(String(200))





web_fieldset = [
	('Web Location',
	 {'fields': ['full_url', 'scheme', 'domain', 'web_netloc', 'web_path', 'web_params', 'web_query', 'web_fragment']}),
	('Hashes', {'fields': ['canonical_link', 'link_hash', 'content_hash']}),
	('Data', {'fields': ['title', 'description', 'summary', 'html', 'txt']}),
	('Metadata',
	 {'fields': ['lang', 'tags', 'word_count', 'category_count', 'article_count', 'link_count', 'apparent_encoding']}),
	('Publication', {'fields': ['author', 'publish_date', 'download_date', 'edit_date']}),
	('Admin', {'fields': ['version', 'is_downloaded', 'is_image', 'is_video', 'is_feed', 'is_text', 'has_risk_words']}),
	('Ranking',
	 {'fields': ['of_interest', 'ranking', 'for_review', 'is_positive', 'is_negative', 'is_neutral', 'iterations']}),
	('Nouns', {'fields': ['noun_count', 'nouns']})
	]


class WebMixin(object):
	# Where
	scheme = Column(String(10), default='http', nullable=False)
	domain = Column(String(300))
	web_netloc = Column(String(400))
	web_path = Column(String(1000))
	web_params = Column(String(1000))
	web_query = Column(String(1000))
	web_fragment = Column(String(1000))
	
	full_url = Column(String(1000))
	url = Column(String(1000),
				 nullable=False)  # Use this to load the list of urls, we process url to get the other things
	canonical_link = Column(String(1000))
	link_hash = Column(String(128))  # So that we never re-crawl the link
	content_hash = Column(String(128))  # We dont want the same content over and over
	
	_salt = Column(String(12))
	@hybrid_property
	def salt(self):
		"""Generates a cryptographically random salt and sets its Base64 encoded
		version to the salt column, and returns the encoded salt.
		"""
		if not self.id and not self._salt:
			self._salt = b64encode(os.urandom(8))
		
		return self._salt
	
	# What
	title = Column(String(300))
	description = Column(String(200))
	html = Column(Text)
	txt = Column(Text)
	summary = Column(Text, default='')
	# keywords = Column(String(500))
	asset = Column(ImageColumn(thumbnail_size=(30, 30, True), size=(300, 300, True)))
	lang = Column(String(20))
	tags = Column(String(500))
	word_count = Column(Integer)
	category_count = Column(Integer)
	article_count = Column(Integer)
	link_count = Column(Integer)  # Number of links on the page
	apparent_encoding = Column(String(15))
	
	# Who : Setup in the model
	author = Column(String(500))
	
	# When
	publish_date = Column(DateTime)
	download_date = Column(DateTime, default=func.now())
	edit_date = Column(DateTime, default=func.now())
	
	# Admin
	version = Column(String(20))
	is_downloaded = Column(Boolean, default=False)
	is_image = Column(Boolean, default=False)
	is_video = Column(Boolean, default=False)
	is_feed = Column(Boolean, default=False)
	is_text = Column(Boolean, default=False)
	has_risk_words = Column(Boolean)
	
	# Ranking
	of_interest = Column(Boolean, default=False)
	ranking = Column(Integer, CheckConstraint('(ranking >= 0) and (ranking <=10)'))
	for_review = Column(Boolean, default=False)
	
	# Trinary Ranking
	is_positive = Column(Boolean, default=False)
	is_negative = Column(Boolean, default=False)
	is_neutral = Column(Boolean, default=True)
	iterations = Column(Integer, default=0)
	
	# Sentiment Analysis
	sentiment = Column(String(100))
	sentiment_colour = Column(String(50))
	
	# Proper Nouns
	noun_count = Column(Integer)
	nouns = Column(Text)

doc_edit_fieldset = [
('Data',
	 {'fields': ['doc_title','doc', 'doc_text'], 'expanded': True}),
('Context',
	 {'fields': ['subject', 'author', 'keywords','comments'], 'expanded': False}),

('Geek Stuff',
	 {'fields': ['mime_type', 'file_size_bytes', 'char_count','doc_type','char_count','word_count','lines','paragraphs','page_count'], 'expanded': False}),
	]

doc_show_fieldset = [
('Data',
	 {'fields': ['doc_title','doc_img', 'doc_text','play_audio'], 'expanded': True}),
('Context',
	 {'fields': ['subject', 'author', 'keywords','comments'], 'expanded': False}),

# ('Geek Stuff',
# 	 {'fields': ['mime_type','file_size_bytes', 'char_count','doc_type','char_count','word_count','lines','paragraphs','page_count'], 'expanded': False}),
	]


audio_show_fieldset = [
('Data',
	 {'fields': ['doc_title','play_audio', 'doc_text'], 'expanded': True}),
('Context',
	 {'fields': ['subject', 'author', 'keywords','comments'], 'expanded': False}),

('Geek Stuff',
	 {'fields': ['mime_type','file_size_bytes', 'char_count','doc_type','char_count','word_count','lines','paragraphs','page_count'], 'expanded': False}),
	]


doc_columns = ['doc_title','subject','author','doc_type']

doc_exclude_columns = ['photo_img','photo_img_thumbnail','print_button','play_audio','doc','doc_binary']

class DocQuery(BaseQuery, SearchQueryMixin):
    pass

class DocMixin(object):
	query_class = DocQuery
	mime_type = Column(String(60), default='application/pdf')
	doc = Column(ImageColumn(thumbnail_size=(30, 30, True), size=(300, 300, True)))
	doc_text = Column(Text)
	doc_binary = Column(FileColumn)
	doc_title = Column(String(200))
	subject = Column(String(100))
	author = Column(String(100))
	keywords = Column(String(200))
	comments = Column(Text)
	
	# Metadata
	doc_type = Column(String(5), default='pdf')
	char_count = Column(Integer)
	word_count = Column(Integer)
	lines = Column(Integer)
	paragraphs = Column(Integer)
	
	file_size_bytes = Column(Integer)
	producer_prog = Column(String(40))
	immutable = Column(Boolean, default = False)
	
	page_size = Column(String(40))
	page_count = Column(Integer)
	hashx = Column(String(40))
	
	
	# if is Audio
	audio_duration_secs = Column(Integer)
	audio_frame_rate = Column(Integer)
	audio_channels = Column(Integer)
	
	search_vector = Column(TSVectorType('doc_text','doc_title'))
	
	# Automatically updated hashx
	@observes('doc_text')
	def doc_text_observer(self, doc_text):
		self.hashx = hashlib.sha256(doc_text).hexdigest()
		
		
	# # Hashes
	# @hybrid_property
	# def hashx(self):
	# 	return self._hashx
	#
	#
	# @hashx.setter
	# def hash(self, hash):
	# 	if self.doc_text is not None:
	# 		self._hashx = func.md5(self.doc_text)
	# 	else:
	# 		self._hashx = '0000'
	#
	# @validates('doc_text')
	# def set_hashx(self):
	# 	if self.doc_text is not None:
	# 		self._hashx = func.md5(self.doc_text)
	# 	else:
	# 		self._hashx = '0000'
	#
	# @hybrid_property
	# def bin_hash(self):
	# 	return self._bin_hash
	# #
	# @bin_hash.setter
	# def bin_hash(self):
	# 	if self.doc_binary:
	# 		self._bin_hash = self._get_hash(self.doc_binary)
	# 	else:
	# 		self._bin_hash = '0'
	# #
	# _text_hash = Column(String(20))
	#
	# @property
	# def text_hash(self):
	# 	return self._text_hash
	#
	# @text_hash.setter
	# def text_hash(self, bin_hash):
	# 	self._text_hash = self._get_hash(self.doc_text)

	# def ViewName(self):
	# 	return self.__class__.__name__ +'View.show'
	#
	#
	# @hybrid_property
	# def doc_img(self):
	# 	im = ImageManager()
	# 	vn = self.ViewName()
	#
	# 	if self.doc:
	# 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	# 		              '" class="thumbnail"><img src="' + im.get_url(self.doc) + \
	# 		              '" alt="Photo" class="img-rounded img-responsive"></a>')
	# 	else:
	# 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	# 		              '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')
	# @hybrid_property
	# def doc_img_thumbnail(self):
	# 	im = ImageManager()
	# 	vn = self.ViewName()
	# 	if self.doc:
	# 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	# 		              '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.doc) + \
	# 		              '" alt="Photo" class="img-rounded img-responsive"></a>')
	# 	else:
	# 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	# 		              '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')
	#
	# def download(self):
	# 	return Markup(
	# 			# '<a href="' + url_for('ProjectFilesModelView.download', filename=str(self.file)) + '">Download</a>')
	# 			'<a href="' + url_for(self.__class__.__name__ +'View.download', filename=str(self.doc)) + '">Download</a>')
	#
	# def file_name(self):
	# 	return get_file_original_name(str(self.doc))

investigation_fieldset = [
	('Activity',{'fields': ['investigator', 'case1', 'actiondate', 'action', 'activity_description', 'status'], 'expanded':True}),
	('Context',{'fields': ['weather', 'location', 'witness'], 'expanded':True}),
	('Findings',{'fields': ['narrative'], 'expanded':True}),
	# ('Evidence',{'fields': ['evidence_desc','pic1_img','pic2_img','pic3_img'], 'expanded':False})
	('Evidence',{'fields': ['evidence_desc', 'pic1', 'pic2', 'pic3'], 'expanded':False})
	]
