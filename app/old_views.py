from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from app import appbuilder, db
# from .models import (Region, District, Town, CaseCategory, Case, CaseType,
#                      Constituency, Court, PoliceStation, Person, Complaint)
# for fieldsets
from .mixins import *
from .models import *
"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

hide_list = ['created_by', 'changed_by', 'created_on', 'changed_on']

class GenderView(ModelView):
    datamodel = SQLAInterface(Gender)
    list_fieldset = ref_fieldset


class TownView(ModelView):
    datamodel = SQLAInterface(Town)
    list_columns = add_columns = edit_columns = ['name']

class DistrictView(ModelView):
    datamodel = SQLAInterface(District)
    related_views = [TownView]
    list_columns = add_columns = edit_columns = [ 'name', 'capital', 'towns']

class RegionView(ModelView):
    datamodel = SQLAInterface(Region)
    list_columns = ['id','name','capital']
    add_columns = edit_columns = ['name', 'capital', 'districts']
    related_views = [DistrictView]


class ConstituencyView(ModelView):
    datamodel = SQLAInterface(Constituency)
    hidden_list = hide_list
    list_columns = add_columns = edit_columns = ['name']

class CaseTypeView(ModelView):
    datamodel = SQLAInterface(CaseType)
    hidden_list = hide_list
    list_columns = add_columns = edit_columns = ['name', 'description']

class CaseCategoryView(ModelView):
    datamodel = SQLAInterface(CaseCategory)
    list_columns = add_columns = edit_columns = ['name', 'description']

class CourtView(ModelView):
    datamodel = SQLAInterface(Court)
    list_columns = add_columns = edit_columns = ['name', 'description', 'district' ] #'mobile', 'alt_mobile', 'email', 'facebook','twitter' , 'gcode' ]
    search_list = ['name','district', 'mobile','email']


class PoliceStatView(ModelView):
    datamodel = SQLAInterface(PoliceStation)
    list_columns = add_columns = edit_columns = ['name', 'description', 'officer_commanding', 'mobile', 'alt_mobile', 'email', 'facebook','twitter' , 'gcode']


class PersonView(ModelView):
    datamodel = SQLAInterface(Person)


class CaseView(ModelView):
    datamodel = SQLAInterface(Case)
    list_columns = ['open_date', 'ob_number', 'case_type', 'case_category','case_closed']
    #add_columns = ['ob_number', 'open_date', 'case_type', 'case_category', 'status', 'report', 'people' ]
    related_views = [PersonView]
    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_exclude_columns = hide_list

    add_fieldsets = show_fieldsets = [
        ('Category', {'fields': ['open_date', 'case_type', 'case_category', 'status']}),
        ('Responsibility', {'fields': ['reporting_officer', 'investigating_officer'], 'expanded': False}),
        ('Investigation', {'fields': ['investigating_officer','investigation_status','investigation_outcomes'], 'expanded': False}),
        ('Arrest', {'fields': ['arresting_officer', 'arrest_location','arrest_narrative','warrant_date','warrant_details'], 'expanded': False}),
        ('Documentation', {'fields': ['evidence_collected', 'evidence_pictures', 'document_list','document_count','documents'], 'expanded': False}),
        ('Charge', {'fields': ['charge_date', 'charge_description','document_count','documents'], 'expanded': False}),
        ('Court', {'fields': ['charge_court','first_hearing_date','hearing_dates','court_outcome','case_duration'], 'expanded': False}),
        ('Offenders', {'fields': ['offender_picture'], 'expanded': False}),

    ]

class ComplaintView(ModelView):
    datamodel = SQLAInterface(Complaint)
    show_exclude_columns = edit_exclude_columns = hide_list
    edit_exclude_columns = hide_list

    add_fieldsets = show_fieldsets = [
        ('Category', {'fields': ['report_date', 'case_type', 'case_category']}),
        ('Complainant', {'fields': ['complainant_is_victim','complainant', 'comp_phone', 'comp_email','comp_address','comp_age','comp_dob','comp_is_minor','comp_gender']}),
        ('Complaint', {'fields': ['complainant_role', 'complaint', 'complaint_language','observations']}),
        ('Observations', {'fields': ['injuries', 'loss', 'damage','theft','narcotics','fraud','domestic_abuse']}),
        ('Victim', {'fields': ['victim_name', 'victim_phone', 'victim_email','victim_address','victim_age','victim_dob','victim_gender','victim_pwd','victim_religion','victim_ethnicity']}),
        ('Offender', {'fields': ['offender_count', 'offenders_known_to_victim', 'offender_known_to_complainant','offender_description','police_interpretation','is_a_crime','is_a_case','case_number','closed']}),
        # ('Responsibility', {'fields': ['reporting_officer', 'investigating_officer'], 'expanded': False}),
        # ('Investigation', {'fields': ['investigating_officer','investigation_status','investigation_outcomes'], 'expanded': False}),
        # ('Arrest', {'fields': ['arresting_officer', 'arrest_location','arrest_narrative','warrant_date','warrant_details'], 'expanded': False}),
        # ('Documentation', {'fields': ['evidence_collected', 'evidence_pictures', 'document_list','document_count','documents'], 'expanded': False}),
        # ('Charge', {'fields': ['charge_date', 'charge_description','document_count','documents'], 'expanded': False}),
        # ('Court', {'fields': ['charge_court','first_hearing_date','hearing_dates','court_outcome','case_duration'], 'expanded': False}),
        # ('Offenders', {'fields': ['offender_picture'], 'expanded': False}),

    ]

#class RDBView(RegisterUserDBView):


# class PersonCaseView(ModelView):
#     datamodel = SQLAInterface(personcase)
#     list_columns = ['case_id', 'person_id']
#     related_views =[CaseView]
"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()
appbuilder.add_view_no_menu(PersonView, "PersonView")

appbuilder.add_view(RegionView, "Regions", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(DistrictView, "Districts", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(TownView, "Towns", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(GenderView, "Gender", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(ConstituencyView, "Constituencies", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CourtView, "Courts", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(PoliceStatView, "Police Stations", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CaseTypeView, "Case Types", icon="fa-folder-open-o", category="Setup")
appbuilder.add_view(CaseCategoryView, "Case Categories", icon="fa-folder-open-o", category="Setup")

appbuilder.add_view(CaseView, "Cases", icon="fa-folder-open-o", category="Cases")
appbuilder.add_view(ComplaintView, "Complaints", icon="fa-folder-open-o", category="Cases")

