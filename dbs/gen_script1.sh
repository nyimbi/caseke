#!/usr/bin/env bash

# Copyright Nyimbi Odero, (c) 2017
# How to Use
# gen_script pony_model.py

# You need to have
# - sed, awk, cut and obviously Postgresql-Client
# Get flask-sqlacodegen from the bitbucket repo. Needed to modify it on how to generate tables
# Use PonyOrm to design and generate a python script
# use pony-sript.py to create ctmp (The temp database)
# use flask-sqlacodegen to reverse-engineer the ctmp into a Flask-SQLAlchemy file
# tweek and edit the resulting file using sed etc to add mixins, and code

# Create a model in pony orms and save the python script to kpony1.py
# run gen_script.py in the same directory It will generate kmodel.py and kviews.py
# mv kmodel and kviews to your app and continue
# need to remove the quotes around secondary=u't_some_table' to work
# SET THESE UP FOR YOUR MODEL
# Look in kclass_tables and kjoin_tables for a comprehensive list

# TO DO
# Parameterize all the PersonMixin, Contact Code as add_mixin



#######################################################
#######################################################
# Add a PersonMixin NOTE no comma's in the array
#######################################################
#######################################################
PEOPLE=("Attorney" "Plaintiff" "Observer" "Surety" "Prosecutor" "Policeman" "Judge" "Defendant")

# Reference tables
# Change these to suit your case
REFS=("Causeofaction" "Constituency" "Court" "County" "Courtlevel" "Doctemplate" "Lawfirm" "Natureofsuit" "Policerole" "Subcounty" "Town" )

## Basic Setup
# Out Temporary Working Database
dropdb ctmp;
createdb ctmp;
python $1;




flask-sqlacodegen postgresql://nyimbi:abcd1234@localhost/ctmp --flask --outfile kmodel.py;
awk '/^class/' kmodel.py > c1.txt
cut -d ' ' -f2 c1.txt > c2.txt
cut -d '(' -f1 c2.txt > kclass_tables.txt
rm c1.txt c2.txt
awk '/^t_/' kmodel.py > jtbl.txt
cut -d ' ' -f1 jtbl.txt > kjoin_table_list.txt
rm jtbl.txt

echo "Generating Views"
###########################
# Create VIEWS
###########################
echo "# coding: utf-8 " > kview.py
echo "# AUTOGENERATED BY gen_script.sh from $1" >> kview.py
echo "# Copyright (C) Nyimbi Odero, $(date)" >> kview.py
echo " " >> kview.py
echo " " >> kview.py
echo "import calendar" >> kview.py
echo "from flask import redirect, flash, url_for, Markup, g" >>kview.py
echo "from flask import render_template" >> kview.py
echo "from flask_appbuilder.models.sqla.interface import SQLAInterface" >> kview.py
echo "from flask_appbuilder.views import ModelView, BaseView, MasterDetailView, MultipleView, RestCRUDView, CompactCRUDMixin" >> kview.py
echo "from flask_appbuilder import ModelView, CompactCRUDMixin, aggregate_count, action, expose, BaseView, has_access" >> kview.py
echo "from flask_appbuilder.charts.views import ChartView, TimeChartView, GroupByChartView" >> kview.py
echo "from flask_appbuilder.models.group import aggregate_count" >> kview.py
echo "from flask_appbuilder.widgets import ListThumbnail, ListWidget" >>kview.py
echo "from flask_appbuilder.widgets import FormVerticalWidget, FormInlineWidget, FormHorizontalWidget, ShowBlockWidget" >>kview.py
echo "from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction" >>kview.py
echo "from app import appbuilder, db" >> kview.py
echo " " >> kview.py
echo " " >> kview.py
echo "from .models import *" >> kview.py
echo " " >> kview.py
echo " " >> kview.py
echo " " >> kview.py
echo "# Basic Lists " >> kview.py
echo "hide_list = ['created_by', 'changed_by', 'created_on', 'changed_on'] " >> kview.py
echo " " >> kview.py
echo " " >> kview.py
echo "#To pretty Print from PersonMixin " >> kview.py
echo "def pretty_month_year(value):" >> kview.py
echo "    return calendar.month_name[value.month] + ' ' + str(value.year)" >> kview.py
echo " " >> kview.py
echo " " >> kview.py
echo "def pretty_year(value):" >> kview.py
echo "    return str(value.year)" >> kview.py
echo " " >> kview.py
echo " " >> kview.py

echo "def get_user():" >> kview.py
echo "    return g.user" >> kview.py
echo " " >> kview.py
echo " " >> kview.py
echo "def fill_gender():" >> kview.py
echo "  try:" >> kview.py
echo "      db.session.add(Gender(name='Male'))" >> kview.py
echo "      db.session.add(Gender(name='Female'))" >> kview.py
echo "      db.session.commit()" >> kview.py
echo "  except:" >> kview.py
echo "      db.session.rollback()" >> kview.py

echo " " >> kview.py
echo " " >> kview.py





# This generates the classes based on kclass_tables based on the awk script above
awk '{print "\
class "$0"View(ModelView):#MasterDetailView, MultipleView\
    datamodel=SQLAInterface("$0", db.session)\
    #add_title =\
    #list_title =\
    #edit_title =\
    #show_title =\
    #add_widget = (FormVerticalWidget|FormInlineWidget)\
    #show_widget = ShowBlockWidget\
    #list_widget = (ListThumbnail|ListWidget)\
    #base_order = (\"name\", \"asc\")\
    # Use base_filers to limit view to only personally Created data
    #base_filters = [[\"created_by\", FilterEqualFunction, get_user]]\
    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns\
    add_exclude_columns = edit_exclude_columns = audit_exclude_columns\
    #add_columns = person_list_columns + ref_columns + contact_columns\
    #edit_columns = person_list_columns + ref_columns + contact_columns\
    #list_columns = person_list_columns + ref_columns + contact_columns\
    #list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)\
    #related_views =[]\
    #show_fieldsets = person_show_fieldset + contact_fieldset\
    #edit_fieldsets = add_fieldsets = \\ \n\t\t\t# ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset\
    #description_columns = {\"name\":\"your models name column\",\"address\":\"the address column\"}\
    #show_template = \"appbuilder/general/model/show_cascade.html\"\
    #edit_template = \"appbuilder/general/model/edit_cascade.html\"\n\n\
    @action(\"muldelete\", \"Delete\", Markup(\"<p>Delete all Really?</p><p>Ok then...</p>\"), \"fa-rocket\")\
    def muldelete(self, items):\
        self.datamodel.delete_all(items)\
        self.update_redirect()\
        return redirect(self.get_redirect())\

    \n\n"}' kclass_tables.txt >> kview.py




for i in "${PEOPLE[@]}"
do

echo " " >> kview.py
echo "class ${i}ChartView(GroupByChartView):" >> kview.py
echo "    datamodel = SQLAInterface($i , db.session)" >> kview.py
echo "    chart_title = 'Grouped $i by Birth'" >> kview.py
echo "    label_columns = ${i}View.label_columns" >> kview.py
echo "    chart_type = 'PieChart'" >> kview.py
echo " " >> kview.py
echo "    definitions = [" >> kview.py
echo "        {" >> kview.py
echo "            'group' : 'age_today'," >> kview.py
echo '            "series" : [(aggregate_count,"age_today")]' >> kview.py
echo "        }," >> kview.py
echo "        {" >> kview.py
echo "            'group' : 'gender'," >> kview.py
echo '            "series" : [(aggregate_count,"age_today")]' >> kview.py
echo "        }" >> kview.py
echo "    ]" >> kview.py
echo " " >> kview.py
echo " " >> kview.py

echo "class ${i}TimeChartView(GroupByChartView):" >> kview.py
echo "    datamodel = SQLAInterface($i , db.session)" >> kview.py
echo " " >> kview.py
echo "    chart_title = 'Grouped Birth $i'" >> kview.py
echo "    chart_type = 'AreaChart'" >> kview.py
echo "    label_columns = ${i}View.label_columns" >> kview.py
echo "    definitions = [" >> kview.py
echo "        {" >> kview.py
echo "            'group' : 'age_today'," >> kview.py
echo "            'formatter': pretty_month_year," >> kview.py
echo '            "series" : [(aggregate_count,"age_today")]' >> kview.py
echo "        }," >> kview.py
echo "        {" >> kview.py
echo "            'group': 'age_today'," >> kview.py
echo "            'formatter': pretty_year," >> kview.py
echo '            "series" : [(aggregate_count,"age_today")]' >> kview.py
echo "        }" >> kview.py
echo "    ]" >> kview.py
echo "" >> kview.py
echo "" >> kview.py

done


# Create Registration of views
#appbuilder.add_view(RegionView, "Regions", icon="fa-folder-open-o", category="Setup")
echo "# How to create a MasterDetailView" >> kview.py
echo " " >> kview.py
echo "#class DetailView(ModelView):" >> kview.py
echo "#    datamodel = SQLAInterface(DetailTable, db.session)" >> kview.py
echo " " >> kview.py
echo "#class MasterView(MasterDetailView):" >> kview.py
echo "#    datamodel = SQLAInterface(MasterTable, db.session)" >> kview.py
echo "#    related_views = [DetailView]" >> kview.py
echo " " >> kview.py
echo " " >> kview.py
echo "# How to create a MultipleView" >> kview.py
echo "#class MultipleViewsExp(MultipleView):" >> kview.py
echo "#    views = [GroupModelView, ContactModelView]" >> kview.py


echo " " >> kview.py
echo "#View Registration" >> kview.py
echo "db.create_all()" >>kview.py
echo "fill_gender()" >>kview.py
echo " " >> kview.py
awk '{print "appbuilder.add_view("$0"View(), \""$0"s\", icon=\"fa-folder-open-o\", category=\"Setup\") \n"}' kclass_tables.txt >> kview.py


echo " " >> kview.py
echo " " >> kview.py

## REGISTER Report Views
for i in "${PEOPLE[@]}"
do
echo "appbuilder.add_view(${i}ChartView(), '${i} Age Chart', icon='fa-dashboard', category='Reports')"    >> kview.py
echo "appbuilder.add_view(${i}TimeChartView(), '${i} Time Chart', icon='fa-dashboard', category='Reports')"    >> kview.py
echo " " >> kview.py
done


echo "#appbuilder.add_separator(\"Setup\")" >> kview.py
echo '#appbuilder.add_separator("My Views")'  >> kview.py
echo "#appbuilder.add_link(name, href, icon='', label='', category='', category_icon='', category_label='', baseview=None)" >> kview.py



# Now Massage the kmodel file to conform to Flask-Appbuilder
# Adding
#from sqlalchemy import func
#from flask_appbuilder import Model
##from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
#from flask_appbuilder.models.decorators import renders
#from sqlalchemy import (Column, Integer, String, ForeignKey,
#                        Sequence, Float, Text, BigInteger, Date,
#                        DateTime, Time, Boolean, CheckConstraint,
#                        UniqueConstraint, Table)
#
#from sqlalchemy.orm import relationship, query, defer, deferred
#from sqlalchemy_utils import aggregated
#from .mixins import *
#from datetime import timedelta, datetime, date

function add_mixin(){
# Takes two arguments class and minin
sed "s:class $1(:class $1($2, :g" k1.py > k2.py
cp k2.py k1.py
}


function add_view_mixin(){
# Takes two arguments class and minin
sed "s:class $1View(:class $1View(CompactCRUDMixin, :g" kview.py > kv.py
cp kv.py kview.py
# rm kv.py
}

################################################################
echo "Generating Models"
################################################################
# Remove old imports
sed '1d' kmodel.py > k1.py
sed '/^from/d' k1.py > kmodel.py


echo -e "        return self.name\n$(cat kmodel.py)" > kmodel.py
echo -e "    def __repr__(self):\n$(cat kmodel.py)" > kmodel.py
echo -e "    \n$(cat kmodel.py)" > kmodel.py
echo -e "    name = Column(String(50), unique = True, nullable=False)\n$(cat kmodel.py)" > kmodel.py
echo -e "    id = Column(Integer, primary_key=True)\n$(cat kmodel.py)" > kmodel.py
echo -e "class Gender(Model):\n$(cat kmodel.py)" > kmodel.py


echo -e "#    contact_group = relationship('ContactGroup')\n$(cat kmodel.py)" > kmodel.py
echo -e "#    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=True)\n$(cat kmodel.py)" > kmodel.py
echo -e "#class UserExtended(Model, UserExtensionMixin):\n$(cat kmodel.py)" > kmodel.py

echo -e "# Here is how to extend the User model\n$(cat kmodel.py)" > kmodel.py
echo -e "\n$(cat kmodel.py)" > kmodel.py
echo -e "from .mixins import *\n$(cat kmodel.py)" > kmodel.py
echo -e "from sqlalchemy.dialects.postgresql import *\n$(cat kmodel.py)" > kmodel.py
echo -e "from datetime import timedelta, datetime, date\n$(cat kmodel.py)" > kmodel.py
echo -e "\tUniqueConstraint, Numeric, LargeBinary , Table)\n$(cat kmodel.py)" > kmodel.py
echo -e "\tDateTime, Time, Boolean, CheckConstraint,\n$(cat kmodel.py)" > kmodel.py
echo -e "\tSequence, Float, Text, BigInteger, Date,\n$(cat kmodel.py)" > kmodel.py
echo -e "from sqlalchemy import (Column, Integer, String, ForeignKey,\n$(cat kmodel.py)" > kmodel.py
echo -e "\n$(cat kmodel.py)" > kmodel.py

echo -e "from sqlalchemy.orm import relationship, query, defer, deferred\n$(cat kmodel.py)" > kmodel.py
echo -e "from sqlalchemy_utils import aggregated\n$(cat kmodel.py)" > kmodel.py
echo -e "from flask_appbuilder.filemanager import ImageManager\n$(cat kmodel.py)" > kmodel.py
echo -e "from flask_appbuilder.models.decorators import renders\n$(cat kmodel.py)" > kmodel.py
echo -e "from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn, UserExtensionMixin \n$(cat kmodel.py)" > kmodel.py
echo -e "from flask_appbuilder import Model\n$(cat kmodel.py)" > kmodel.py
echo -e "from sqlalchemy import func\n$(cat kmodel.py)" > kmodel.py
echo -e " \n$(cat kmodel.py)" > kmodel.py
echo -e "# Copyright (C) Nyimbi Odero, $(date)\n$(cat kmodel.py)" > kmodel.py
echo -e "# AUTOGENERATED BY gen_script.sh from $1\n$(cat kmodel.py)" > kmodel.py
echo -e "# coding: utf-8\n$(cat kmodel.py)" > kmodel.py

# Change the db. in the file
sed '/^#db = /d' kmodel.py > k1.py
sed 's/db\.//g' k1.py > k2.py
sed 's/Float(53)/Numeric(10,2)/g' k2.py > k1.py
cp k1.py k2.py

# Remove :server_default=FetchedValue() and replace with autoincrement=True
sed 's/server_default=FetchedValue()/autoincrement=True/g' k2.py > k1.py
sed 's/LargeBinary,/ImageColumn,/g' k1.py > k2.py
sed 's/(Model)/(AuditMixin, Model)/g' k2.py > k1.py
cp k1.py k2.py
echo "Changing secondary"
sed "s/\(secondary=u'\)\(.*\)\(',\)/secondary=\2,/g" k2.py > k1.py

# We always use type to indicate classes of fields
sed 's/type(/type(RefTypeMixin, /g' k1.py > k2.py

## Need to add Model.metadata in join_table definitions
#quote=\'
# sed "s/^ *\('.*'\),/    \1, Model.metadata,/" k2.py > k1.py

#Kludge
cp k2.py k1.py


#counter = 0
#counter=$((counter+1))
#########################
# App Specific Class Changes
# for Attorney, Plaintiff, Witness, Surety, Prosecutor, Policeman, Judge, Defendant


echo "Adding Mixins"

for i in "${PEOPLE[@]}"
do
#echo "s/class $i(/class $i(PersonMixin, ContactMixin,  /g"
sed "s:class $i(:class $i(PersonMixin, ContactMixin,  :g" k1.py > k2.py
cp k2.py k1.py
done


for i in "${REFS[@]}"
do
#echo "s/class $i(/class $i(RefTypeMixin,  /g"
sed "s:class $i(:class $i(RefTypeMixin, :g" k1.py > k2.py
cp k2.py k1.py
done

#######################################
#       ADDING MIXINS
########################################
# ADDING MIXINS
add_mixin Defendant EmploymentMixin
add_mixin Defendant BiometricMixin
add_mixin Hearing ActivityMixin
add_view_mixin Causeofaction
add_mixin Document DocMixin
add_mixin Doctemplate DocMixin



#sed "s/class Attorney(/class Attorney(PersonMixin, ContactMixin,  /g" k1.py > k2.py
#sed "s/class Plaintiff(/class Plaintiff(PersonMixin, ContactMixin,  /g" k2.py > k1.py
#sed "s/class Witnes(/class Witnes(PersonMixin, ContactMixin,  /g" k1.py > k2.py
#sed "s/class Surety(/class Surety(PersonMixin, ContactMixin,  /g" k2.py > k1.py
#sed "s/class Prosecutor(/class Prosecutor(PersonMixin,ContactMixin,  /g" k1.py > k2.py
#sed "s/class Policeman(/class Policeman(PersonMixin,ContactMixin,  /g" k2.py > k1.py
#sed "s/class Judge(/class Judge(PersonMixin,ContactMixin,  /g" k1.py > k2.py
#sed "s/class Defendant(/class Defendant(PersonMixin,ContactMixin, BiometricMixin, /g" k2.py > kmodel.py

read -r -d '' VAR << EOM

	 def photo_img(self):
	 	im = ImageManager()

	 	vn = self.ViewName()
	 	if self.photo:
	 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	 		              '" class="thumbnail"><img src="' + im.get_url(self.photo) + \
	 		              '" alt="Photo" class="img-rounded img-responsive"></a>')
	 	else:
	 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	 		              '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

	 def photo_img_thumbnail(self):
	 	im = ImageManager()
	 	vn = self.ViewName()
	 	if self.photo:
	 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	 		              '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) + \
	 		              '" alt="Photo" class="img-rounded img-responsive"></a>')
	 	else:
	 		return Markup('<a href="' + url_for(vn, pk=str(self.id)) + \
	 		              '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

EOM
#VAR1="\tdef photo_img(self):\n\t\tim = self.ImageManager()\n\t\tif self.picture:\n\t\t\treturn Markup(\'<a href=\"' + url_for(self.__class__.__name__ + 'View.show', \n\t\t\tpk=str(self.id)) + '\" class=\"thumbnail\"><img src=\"' + self.im.get_url(self.picture) + '\" alt=\"Photo\" class=\"img-rounded img-responsive\"></a>')\n\t\telse:\n\t\t\treturn Markup('<a href=\"' + url_for(self.__class__.__name__ + '.show', pk=str(self.id)) + '\" class=\"thumbnail\"><img src=\"//:0\" alt=\"Photo\" class=\"img-responsive\"></a>')\n"
VAR1="\n\tdef photo_img(self):\n\t\tim = ImageManager()\n\n\t\tvn = self.ViewName()\n\t\tif self.photo:\n\t\t\treturn Markup('<a href=\"' + url_for(vn, pk=str(self.id)) + \\n\t\t\t\t\t\t\t\t\t\t'\" class=\"thumbnail\"><img src=\"' + im.get_url(self.photo) + \\n\t\t\t\t\t\t\t\t\t\t'\" alt=\"Photo\" class=\"img-rounded img-responsive\"></a>')\n\t\telse:\n\t\t\treturn Markup('<a href=\"' + url_for(vn, pk=str(self.id)) + \\n\t\t\t\t\t\t\t\t\t\t'\" class=\"thumbnail\"><img src=\"//:0\" alt=\"Photo\" class=\"img-responsive\"></a>')\n\n\tdef photo_img_thumbnail(self):\n\t\tim = ImageManager()\n\t\tvn = self.ViewName()\n\t\tif self.photo:\n\t\t\treturn Markup('<a href=\"' + url_for(vn, pk=str(self.id)) + \\n\t\t\t\t\t\t\t\t\t\t'\" class=\"thumbnail\"><img src=\"' + im.get_url_thumbnail(self.photo) + \\n\t\t\t\t\t\t\t\t\t\t'\" alt=\"Photo\" class=\"img-rounded img-responsive\"></a>')\n\t\telse:\n\t\t\treturn Markup('<a href=\"' + url_for(vn, pk=str(self.id)) + \\n\t\t\t\t\t\t\t\t\t\t'\" class=\"thumbnail\"><img src=\"//:0\" alt=\"Photo\" class=\"img-responsive\"></a>')\n"







# This adds the photo_img field to PersonMixin Classes: Doesn't work
cp k2.py kmodel.py
awk -v pat="$VAR1" '1;/PersonMixin/{c=3}c&&!--c{print pat }' kmodel.py > k2.py
## Change the tabs to spaces
expand -t4 < k2.py >kmodel.py


## Assuming we are in the dbs directory
mv ../app/models.py ../app/models_$(date +%F-%T).py
mv ../app/views.py ../app/views_$(date +%F-%T).py

cp kmodel.py ../app/models.py
cp kview.py ../app/views.py



