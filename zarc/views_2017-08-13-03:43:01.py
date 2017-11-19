# coding: utf-8 
# views.py AUTOGENERATED BY gen_script.sh from kp3.py
# Copyright (C) Nyimbi Odero, Sun Aug 13 03:41:46 EAT 2017
 
 
import calendar
from flask import redirect, flash, url_for, Markup
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView, BaseView, MasterDetailView, MultipleView, RestCRUDView, CompactCRUDMixin
from flask_appbuilder import ModelView, CompactCRUDMixin, aggregate_count, action, expose, BaseView, has_access
from flask_appbuilder.charts.views import ChartView, TimeChartView, GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.widgets import ListThumbnail, ListWidget
from flask_appbuilder.widgets import FormVerticalWidget, FormInlineWidget, FormHorizontalWidget, ShowBlockWidget
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction as FA
from app import appbuilder, db
 
 
from .models import *
 
 
 
# Basic Lists 
hide_list = ['created_by', 'changed_by', 'created_on', 'changed_on'] 
 
 
#To pretty Print from PersonMixin 
def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)
 
 
def pretty_year(value):
    return str(value.year)
 
 
def fill_gender():
  try:
      db.session.add(Gender(name='Male'))
      db.session.add(Gender(name='Female'))
      db.session.commit()
  except:
      db.session.rollback()
 
class LawyerChartView(GroupByChartView):
    datamodel = SQLAInterface(Lawyer , db.session)
    chart_title = 'Grouped Lawyer by Birth'
    chart_3d = 'true'
    label_columns = LawyerView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class LawyerTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Lawyer , db.session)
 
    chart_title = 'Grouped Birth Lawyer'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = LawyerView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class PlaintiffChartView(GroupByChartView):
    datamodel = SQLAInterface(Plaintiff , db.session)
    chart_title = 'Grouped Plaintiff by Birth'
    chart_3d = 'true'
    label_columns = PlaintiffView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class PlaintiffTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Plaintiff , db.session)
 
    chart_title = 'Grouped Birth Plaintiff'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PlaintiffView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class WitnesChartView(GroupByChartView):
    datamodel = SQLAInterface(Witnes , db.session)
    chart_title = 'Grouped Witnes by Birth'
    chart_3d = 'true'
    label_columns = WitnesView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class WitnesTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Witnes , db.session)
 
    chart_title = 'Grouped Birth Witnes'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = WitnesView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class SuretyChartView(GroupByChartView):
    datamodel = SQLAInterface(Surety , db.session)
    chart_title = 'Grouped Surety by Birth'
    chart_3d = 'true'
    label_columns = SuretyView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class SuretyTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Surety , db.session)
 
    chart_title = 'Grouped Birth Surety'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = SuretyView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class ProsecutorChartView(GroupByChartView):
    datamodel = SQLAInterface(Prosecutor , db.session)
    chart_title = 'Grouped Prosecutor by Birth'
    chart_3d = 'true'
    label_columns = ProsecutorView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class ProsecutorTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Prosecutor , db.session)
 
    chart_title = 'Grouped Birth Prosecutor'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = ProsecutorView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class PoliceofficerChartView(GroupByChartView):
    datamodel = SQLAInterface(Policeofficer , db.session)
    chart_title = 'Grouped Policeofficer by Birth'
    chart_3d = 'true'
    label_columns = PoliceofficerView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class PoliceofficerTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Policeofficer , db.session)
 
    chart_title = 'Grouped Birth Policeofficer'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PoliceofficerView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class JudicialofficerChartView(GroupByChartView):
    datamodel = SQLAInterface(Judicialofficer , db.session)
    chart_title = 'Grouped Judicialofficer by Birth'
    chart_3d = 'true'
    label_columns = JudicialofficerView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class JudicialofficerTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Judicialofficer , db.session)
 
    chart_title = 'Grouped Birth Judicialofficer'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = JudicialofficerView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class DefendantChartView(GroupByChartView):
    datamodel = SQLAInterface(Defendant , db.session)
    chart_title = 'Grouped Defendant by Birth'
    chart_3d = 'true'
    label_columns = DefendantView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class DefendantTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Defendant , db.session)
 
    chart_title = 'Grouped Birth Defendant'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DefendantView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class VisitorChartView(GroupByChartView):
    datamodel = SQLAInterface(Visitor , db.session)
    chart_title = 'Grouped Visitor by Birth'
    chart_3d = 'true'
    label_columns = VisitorView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class VisitorTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Visitor , db.session)
 
    chart_title = 'Grouped Birth Visitor'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = VisitorView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class WarderChartView(GroupByChartView):
    datamodel = SQLAInterface(Warder , db.session)
    chart_title = 'Grouped Warder by Birth'
    chart_3d = 'true'
    label_columns = WarderView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class WarderTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Warder , db.session)
 
    chart_title = 'Grouped Birth Warder'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = WarderView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class VisitChartView(GroupByChartView):
    datamodel = SQLAInterface(Visit , db.session)
    chart_title = 'Grouped Visit by Birth'
    chart_3d = 'true'
    label_columns = VisitView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class VisitTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Visit , db.session)
 
    chart_title = 'Grouped Birth Visit'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = VisitView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class DisciplineChartView(GroupByChartView):
    datamodel = SQLAInterface(Discipline , db.session)
    chart_title = 'Grouped Discipline by Birth'
    chart_3d = 'true'
    label_columns = DisciplineView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class DisciplineTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Discipline , db.session)
 
    chart_title = 'Grouped Birth Discipline'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = DisciplineView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class MedeventChartView(GroupByChartView):
    datamodel = SQLAInterface(Medevent , db.session)
    chart_title = 'Grouped Medevent by Birth'
    chart_3d = 'true'
    label_columns = MedeventView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class MedeventTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Medevent , db.session)
 
    chart_title = 'Grouped Birth Medevent'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = MedeventView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class HearingChartView(GroupByChartView):
    datamodel = SQLAInterface(Hearing , db.session)
    chart_title = 'Grouped Hearing by Birth'
    chart_3d = 'true'
    label_columns = HearingView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class HearingTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Hearing , db.session)
 
    chart_title = 'Grouped Birth Hearing'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = HearingView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class PrisoncommitalChartView(GroupByChartView):
    datamodel = SQLAInterface(Prisoncommital , db.session)
    chart_title = 'Grouped Prisoncommital by Birth'
    chart_3d = 'true'
    label_columns = PrisoncommitalView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class PrisoncommitalTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Prisoncommital , db.session)
 
    chart_title = 'Grouped Birth Prisoncommital'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = PrisoncommitalView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


 
class CaseChartView(GroupByChartView):
    datamodel = SQLAInterface(Case , db.session)
    chart_title = 'Grouped Case by Birth'
    chart_3d = 'true'
    label_columns = CaseView.label_columns
    chart_type = 'PieChart'
 
    definitions = [
        {
            'group' : 'age_today',
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group' : 'gender',
            "series" : [(aggregate_count,"age_today")]
        }
    ]
 
 
class CaseTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Case , db.session)
 
    chart_title = 'Grouped Birth Case'
    chart_type = 'AreaChart'
    chart_3d = 'true'
    label_columns = CaseView.label_columns
    definitions = [
        {
            'group' : 'age_today',
            'formatter': pretty_month_year,
            "series" : [(aggregate_count,"age_today")]
        },
        {
            'group': 'age_today',
            'formatter': pretty_year,
            "series" : [(aggregate_count,"age_today")]
        }
    ]


# How to create a MasterDetailView
 
#class DetailView(ModelView):
#    datamodel = SQLAInterface(DetailTable, db.session)
 
#class MasterView(MasterDetailView):
#    datamodel = SQLAInterface(MasterTable, db.session)
#    related_views = [DetailView]
 
 
# How to create a MultipleView
#class MultipleViewsExp(MultipleView):
#    views = [GroupModelView, ContactModelView]
 
#View Registration
db.create_all()
fill_gender()
 
 
 
appbuilder.add_view(LawyerChartView(), 'Lawyer Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(LawyerTimeChartView(), 'Lawyer Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(PlaintiffChartView(), 'Plaintiff Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(PlaintiffTimeChartView(), 'Plaintiff Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(WitnesChartView(), 'Witnes Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(WitnesTimeChartView(), 'Witnes Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(SuretyChartView(), 'Surety Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(SuretyTimeChartView(), 'Surety Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(ProsecutorChartView(), 'Prosecutor Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(ProsecutorTimeChartView(), 'Prosecutor Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(PoliceofficerChartView(), 'Policeofficer Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(PoliceofficerTimeChartView(), 'Policeofficer Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(JudicialofficerChartView(), 'Judicialofficer Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(JudicialofficerTimeChartView(), 'Judicialofficer Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(DefendantChartView(), 'Defendant Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(DefendantTimeChartView(), 'Defendant Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(VisitorChartView(), 'Visitor Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(VisitorTimeChartView(), 'Visitor Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(WarderChartView(), 'Warder Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(WarderTimeChartView(), 'Warder Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(VisitChartView(), 'Visit Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(VisitTimeChartView(), 'Visit Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(DisciplineChartView(), 'Discipline Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(DisciplineTimeChartView(), 'Discipline Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(MedeventChartView(), 'Medevent Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(MedeventTimeChartView(), 'Medevent Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(HearingChartView(), 'Hearing Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(HearingTimeChartView(), 'Hearing Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(PrisoncommitalChartView(), 'Prisoncommital Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(PrisoncommitalTimeChartView(), 'Prisoncommital Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(CaseChartView(), 'Case Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(CaseTimeChartView(), 'Case Time Chart', icon='fa-dashboard', category='Reports')
 
#appbuilder.add_separator("Setup")
#appbuilder.add_separator("My Views")
#appbuilder.add_link(name, href, icon='', label='', category='', category_icon='', category_label='', baseview=None)
