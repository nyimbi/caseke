from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db
from .models import *
 
 
 
# Basic Lists 
hide_list = ['created_by', 'changed_by', 'created_on', 'changed_on'] 
 
 
class ActiontypeView(ModelView):
	datamodel=SQLAInterface(Actiontype)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class AttorneyView(ModelView):
	datamodel=SQLAInterface(Attorney)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class BailView(ModelView):
	datamodel=SQLAInterface(Bail)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class CaseView(ModelView):
	datamodel=SQLAInterface(Case)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class CauseofactionView(ModelView):
	datamodel=SQLAInterface(Causeofaction)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class ConstituencyView(ModelView):
	datamodel=SQLAInterface(Constituency)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class CountyView(ModelView):
	datamodel=SQLAInterface(County)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class CourtView(ModelView):
	datamodel=SQLAInterface(Court)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class CourtlevelView(ModelView):
	datamodel=SQLAInterface(Courtlevel)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class DefendantView(ModelView):
	datamodel=SQLAInterface(Defendant)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class DoctemplateView(ModelView):
	datamodel=SQLAInterface(Doctemplate)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class DocumentView(ModelView):
	datamodel=SQLAInterface(Document)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class FilingView(ModelView):
	datamodel=SQLAInterface(Filing)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class FilingtypeView(ModelView):
	datamodel=SQLAInterface(Filingtype)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class HearingView(ModelView):
	datamodel=SQLAInterface(Hearing)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class HearingtypeView(ModelView):
	datamodel=SQLAInterface(Hearingtype)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class InvestigationView(ModelView):
	datamodel=SQLAInterface(Investigation)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class JudgeView(ModelView):
	datamodel=SQLAInterface(Judge)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class LawfirmView(ModelView):
	datamodel=SQLAInterface(Lawfirm)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class NatureofsuitView(ModelView):
	datamodel=SQLAInterface(Natureofsuit)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class PlaintiffView(ModelView):
	datamodel=SQLAInterface(Plaintiff)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class PolicemanView(ModelView):
	datamodel=SQLAInterface(Policeman)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class PoliceroleView(ModelView):
	datamodel=SQLAInterface(Policerole)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class PolicestationView(ModelView):
	datamodel=SQLAInterface(Policestation)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class PrisonView(ModelView):
	datamodel=SQLAInterface(Prison)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class PrisonremandView(ModelView):
	datamodel=SQLAInterface(Prisonremand)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class ProsecutorView(ModelView):
	datamodel=SQLAInterface(Prosecutor)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class ProsecutorteamView(ModelView):
	datamodel=SQLAInterface(Prosecutorteam)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class SubcountyView(ModelView):
	datamodel=SQLAInterface(Subcounty)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class SuretyView(ModelView):
	datamodel=SQLAInterface(Surety)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class TownView(ModelView):
	datamodel=SQLAInterface(Town)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


class WitnesView(ModelView):
	datamodel=SQLAInterface(Witnes)
	#add_title =
	#list_title =
	#list_columns =[]
	#search_exclude_columns =[]
	#list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)
	#related_views =[]
	#show_fieldsets = edit_fieldsets = add_fieldsets = person_fieldset + contact_fieldset
	#show_template = "appbuilder/general/model/show_cascade.html"


 
#View Registration
 
appbuilder.add_view(ActiontypeView, "Actiontypes", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(AttorneyView, "Attorneys", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(BailView, "Bails", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(CaseView, "Cases", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(CauseofactionView, "Causeofactions", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(ConstituencyView, "Constituencys", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(CountyView, "Countys", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(CourtView, "Courts", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(CourtlevelView, "Courtlevels", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(DefendantView, "Defendants", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(DoctemplateView, "Doctemplates", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(DocumentView, "Documents", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(FilingView, "Filings", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(FilingtypeView, "Filingtypes", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(HearingView, "Hearings", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(HearingtypeView, "Hearingtypes", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(InvestigationView, "Investigations", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(JudgeView, "Judges", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(LawfirmView, "Lawfirms", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(NatureofsuitView, "Natureofsuits", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(PlaintiffView, "Plaintiffs", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(PolicemanView, "Policemans", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(PoliceroleView, "Policeroles", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(PolicestationView, "Policestations", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(PrisonView, "Prisons", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(PrisonremandView, "Prisonremands", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(ProsecutorView, "Prosecutors", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(ProsecutorteamView, "Prosecutorteams", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(SubcountyView, "Subcountys", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(SuretyView, "Suretys", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(TownView, "Towns", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(WitnesView, "Witness", icon="fa-folder-open-o", category="Setup") 

#appbuilder.add_separator("Setup")
