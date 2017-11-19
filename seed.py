from app import app, models, db
from faker import Factory
from random import randint, choice





db.s = db.session
#

# print "adding roles"

print "creating regions"
# # Load up the Regions
rg = models.Region()
rg.name = 'Ashanti'; rg.capital='Kumasi'; rg.changed_by_fk = 1;rg.created_by_fk = 1;
db.s.add(rg)

rg = models.Region()
rg.name = 'Brong Ahafo';	rg.capital='Sunyani'; rg.changed_by_fk = 1;rg.created_by_fk = 1;
db.s.add(rg)

rg = models.Region()
rg.name = 'Central';	rg.capital='Cape Coast';rg.changed_by_fk = 1;rg.created_by_fk = 1;
db.s.add(rg)

rg = models.Region()
rg.name = 'Eastern';	rg.capital='Koforidua';rg.changed_by_fk = 1;rg.created_by_fk = 1;
db.s.add(rg)

rg = models.Region()
rg.name = 'Greater Accra';  	rg.capital='Accra';rg.changed_by_fk = 1;rg.created_by_fk = 1;
db.s.add(rg)

rg = models.Region()
rg.name = 'Northern';	rg.capital='Tamale';rg.changed_by_fk = 1;rg.created_by_fk = 1;
db.s.add(rg)

rg = models.Region()
rg.name = 'Upper East';	rg.capital='Bolgatanga';rg.changed_by_fk = 1;rg.created_by_fk = 1;
db.s.add(rg)

rg = models.Region()
rg.name = 'Upper West';	rg.capital='Wa';rg.changed_by_fk = 1;rg.created_by_fk = 1;
db.s.add(rg)

rg = models.Region()
rg.name = 'Volta';	rg.capital='Ho';rg.changed_by_fk = 1;rg.created_by_fk = 1;
db.s.add(rg)

rg = models.Region()
rg.name = 'Western';	rg.capital='Sekondi-Takoradi';rg.created_by_fk = 1;rg.changed_by_fk=1;
db.s.add(rg)

db.s.commit()

print "Loading Districts"
# Districts
# AShanti
ds = models.District();  ds.name='Adansi North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Adansi South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Afigya-Kwabre District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Ahafo Ano North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Ahafo Ano South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Amansie Central District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Amansie West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Asante Akim Central Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Asante Akim North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Asante Akim South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Asokore Mampong Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Atwima Kwanwoma District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Atwima Mponua District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Atwima Nwabiagya District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Bekwai Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Bosome Freho District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Botsomtwe District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Ejisu-Juaben Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Ejura - Sekyedumase District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Kumasi Metropolitan District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Kumawu District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Kwabre East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Mampong Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Obuasi Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Offinso North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Offinso South Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Sekyere Afram Plains District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Sekyere Central District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Sekyere East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
ds = models.District();  ds.name='Sekyere South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 1;db.s.add(ds);
db.s.commit()


# Brong Ahafo
ds = models.District(); ds.name='Asunafo North Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Asunafo South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Asutifi District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Asutifi South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Atebubu-Amantin District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Banda District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Berekum Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Dormaa East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Dormaa Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Dormaa West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Jaman North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Jaman South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Kintampo North Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Kintampo South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Nkoranza North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Nkoranza South Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Pru District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Sene District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Sene West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Sunyani Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Sunyani West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Tain District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Tano North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Tano South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Techiman Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Techiman North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
ds = models.District(); ds.name='Wenchi Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 2;db.s.add(ds);
db.s.commit()


# Central
ds = models.District(); ds.name='Abura/Asebu/Kwamankese District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Agona East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Agona West Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Ajumako/Enyan/Essiam District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Asikuma/Odoben/Brakwa District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Assin North Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Assin South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Awutu-Senya District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Awutu Senya East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Cape Coast Metropolitan District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Effutu Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Ekumfi District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Gomoa East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Gomoa West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Komenda/Edina/Eguafo/Abirem Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Mfantsiman Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Twifo-Ati Mokwa District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Twifo/Heman/Lower Denkyira District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Upper Denkyira East Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
ds = models.District(); ds.name='Upper Denkyira West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 3;db.s.add(ds);
db.s.commit()

# Eastern
ds = models.District(); ds.name='Akuapim South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Afram Plains South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Akuapim North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Akuapim South Municipal'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Akyemansa District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Asuogyaman District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Ayensuano District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Atiwa District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Birim Central Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Birim North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Birim South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Denkyembour District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='East Akim Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Fanteakwa District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Kwaebibirem District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Kwahu East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Kwahu North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Kwahu South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Kwahu West Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Lower Manya Krobo District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='New-Juaben Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Suhum/Kraboa/Coaltar District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Upper Manya Krobo District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Upper West Akim District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='West Akim Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
ds = models.District(); ds.name='Yilo Krobo Municipal'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 4;db.s.add(ds);
db.s.commit()


# Greater Accra
ds = models.District(); ds.name='Accra Metropolitan District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Ada West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Adenta Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Ashaiman Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Dangme East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Dangme West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Ga Central District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Ga East Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Ga South Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Ga West Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Kpone Katamanso District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='La Dade Kotopon Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='La Nkwantanang Madina District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Ledzokuku-Krowor Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Ningo Prampram District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
ds = models.District(); ds.name='Tema Metropolitan District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 5;db.s.add(ds);
db.s.commit()

# Northern Region
ds = models.District(); ds.name='Bole District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Bunkpurugu-Yunyoo District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Central Gonja District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Chereponi District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='East Gonja District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='East Mamprusi District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Gushegu District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Karaga District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Kpandai District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Kumbungu District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Mamprugo Moaduri District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Mion District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Nanumba North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Nanumba South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='North Gonja District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Saboba District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Sagnarigu District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Savelugu-Nanton District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Sawla-Tuna-Kalba District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Tamale Metropolitan District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Tatale Sangule District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Tolon District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='West Gonja District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='West Mamprusi District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name='Yendi Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
ds = models.District(); ds.name=ds = models.District(); ds.name='Zabzugu District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 6;db.s.add(ds);
db.s.commit()


# Upper East
ds = models.District(); ds.name='Bawku Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Bawku West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Binduri District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Bolgatanga Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Bongo District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Builsa District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Builsa South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Garu-Tempane District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Kassena Nankana East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Kassena Nankana West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Nabdam District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Pusiga District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
ds = models.District(); ds.name='Talensi District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 7;db.s.add(ds);
db.s.commit()

# Upper West
ds = models.District(); ds.name='Daffiama Bussie Issa District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 8;db.s.add(ds);
ds = models.District(); ds.name='Jirapa District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 8;db.s.add(ds);
ds = models.District(); ds.name='Lambussie Karni District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 8;db.s.add(ds);
ds = models.District(); ds.name='Lawra District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 8;db.s.add(ds);
ds = models.District(); ds.name='Nadowli District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 8;db.s.add(ds);
ds = models.District(); ds.name='Nandom District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 8;db.s.add(ds);
ds = models.District(); ds.name='Sissala East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 8;db.s.add(ds);
ds = models.District(); ds.name='Sissala West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 8;db.s.add(ds);
ds = models.District(); ds.name='Wa East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 8;db.s.add(ds);
ds = models.District(); ds.name='Wa Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 8;db.s.add(ds);
ds = models.District(); ds.name='Wa West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 8;db.s.add(ds);
db.s.commit()

# Volta
ds = models.District(); ds.name='Adaklu District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Afadjato South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Agotime Ziope District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Akatsi North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Akatsi South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Biakoye District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Central Tongu District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Ho Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Ho West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Hohoe Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Jasikan District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Kadjebi District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Keta Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Ketu North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Ketu South Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Kpando Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Krachi East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Krachi Nchumuru District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Krachi West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Nkwanta North District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='Nkwanta South District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='North Dayi District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='North Tongu District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='South Dayi District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
ds = models.District(); ds.name='South Tongu District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 9;db.s.add(ds);
db.s.commit()

# Western Regin
ds = models.District(); ds.name='Ahanta West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Aowin/Suaman District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Bia District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Bia East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Bibiani/Anhwiaso/Bekwai District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Bodi District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Ellembele District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Jomoro District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Juabeso District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Mpohor District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Mpohor/Wassa East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Nzema East Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Prestea-Huni Valley District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Sefwi Akontombra District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Sefwi-Wiawso District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Sekondi Takoradi Metropolitan Assembly'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Shama District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Suaman District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Tarkwa-Nsuaem Municipal District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Wasa Amenfi East District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Wasa Amenfi West District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
ds = models.District(); ds.name='Wassa Amenfi Central District'; ds.created_by_fk=1; ds.changed_by_fk=1; ds.region_fk = 10;db.s.add(ds);
db.s.commit()

# Gender
gd = models.Gender(); gd.name = 'Female'; db.s.add(gd); db.s.commit()
gd = models.Gender(); gd.name = 'Male'; db.s.add(gd); db.s.commit()


# Case Status
gd = models.Casestatus(); gd.name = 'Initated'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Reported'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Under Investigation'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Investigation Complete'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Referred to AG'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Remanded'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'First Hearing'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Arrested'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Awaiting Sentencing'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Acquitted'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Nolle Prosequi'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Sentenced'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Closed'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Bail pending Appeal'; db.s.add(gd); db.s.commit()
gd = models.Casestatus(); gd.name = 'Bail pending Trial'; db.s.add(gd); db.s.commit()




cc = models.Casecategory(); cc.name = 'Cybercrime';  cc.created_by_fk=1; cc.changed_by_fk=1; db.s.add(cc); db.s.commit()
cc = models.Casecategory(); cc.name = 'Border';  cc.created_by_fk=1; cc.changed_by_fk=1; db.s.add(cc); db.s.commit()
cc = models.Casecategory(); cc.name = 'Fraud';  cc.created_by_fk=1; cc.changed_by_fk=1; db.s.add(cc); db.s.commit()
cc = models.Casecategory(); cc.name = 'Violence';  cc.created_by_fk=1; cc.changed_by_fk=1; db.s.add(cc); db.s.commit()
cc = models.Casecategory(); cc.name = 'Domestic Abuse';  cc.created_by_fk=1; cc.changed_by_fk=1; db.s.add(cc); db.s.commit()
cc = models.Casecategory(); cc.name = 'Narcotics';  cc.created_by_fk=1; cc.changed_by_fk=1; db.s.add(cc); db.s.commit()
cc = models.Casecategory(); cc.name = 'Maritime';  cc.created_by_fk=1; cc.changed_by_fk=1; db.s.add(cc); db.s.commit()

cl = models.Courtlevel(); cl.name = 'Supreme Court'; db.s.add(cl); db.s.commit()
cl = models.Courtlevel(); cl.name = 'Court of Appeal'; db.s.add(cl); db.s.commit()
cl = models.Courtlevel(); cl.name = 'High Court'; db.s.add(cl); db.s.commit()
cl = models.Courtlevel(); cl.name = 'Circuit'; db.s.add(cl); db.s.commit()


#
# from mixer.backend.flask import mixer
# from app import app
# mixer.init_app(app)

from faker import Faker
fake = Faker()

# Now load Towns
print "Creating Towns"
for ds in db.session.query(models.District):
    for _ in range(0,10):
        town = models.Town()
        town.name = fake.city() + ' '+ fake.name()
        town.district_fk = ds.id
        town.created_by_fk = 1
        town.changed_by_fk = 1
        town.lat = fake.latitude()
        town.lng = fake.longitude()
        db.s.add(town)
        db.s.commit()


# Load Courts
print 'Creating some courts'
for ds in db.session.query(models.Town):
    for _ in range(0,3):
        court = models.Court() # + ' ' +fake.city()
        court.name = fake.company() + ' Court'+str(randint(2000, 50000))
        court.town_fk = randint(1,1000)
        court.court_level_fk = 4
        # court.town_fk = randint(1,600)
        court.created_by_fk = 1
        court.changed_by_fk = 1
        court.lat = fake.latitude()
        court.lng = fake.longitude()
        db.s.add(court)
        db.s.commit()


print 'Give 50 Judges Italian names :-)'
fake = Factory.create('it_IT')
for _ in range(0,50):
    t = models.Judge()
    t.name = fake.name()
    t.court_level_fk = randint(1,4)
    t.court_fk = randint(1,10)
    t.appelation = 'Justice'
    # t.changed_by_fk = 1
    # t.lat = fake.latitude()
    # t.lon = fake.longitude()
    db.s.add(t)
    db.s.commit()

print "Police Stations"
for _ in range(0,200):
    court = models.Policestation() # + ' ' +fake.city()
    court.name = fake.company() + ' Station'+str(randint(2, 50000))
    court.town_fk = randint(1,1000)
    #court.court_level_fk = 4
    # court.town_fk = randint(1,600)
    court.created_by_fk = 1
    court.changed_by_fk = 1
    court.lat = fake.latitude()
    court.lng = fake.longitude()
    db.s.add(court)

print 'Generating 300 German policemen'
fake = Factory.create('de_DE')
for _ in range(0,300):
    t = models.Policeman()
    t.firstname = fake.first_name()
    t.surname =fake.last_name()
    t.service_number = fake.ssn()
    t.gender_fk = randint(1,2)
    t.police_station_fk = randint(1,100)
    # t.court_level_fk = 3
    # t.court = fake.random(10)
    # t.changed_by_fk = 1
    # t.lat = fake.latitude()
    # t.lon = fake.longitude()
    db.s.add(t)
    db.s.commit()

print "Czech Defendants"
fake = Factory.create('cs_CZ')
for _ in range(0,300):
    t = models.Defendant()
    t.firstname = fake.first_name()
    t.surname =fake.last_name()
    #t.service_number = fake.ssn()
    t.gender_fk = randint(1,2)
    # t.court_level_fk = 3
    # t.court = fake.random(10)
    t.changed_by_fk = 1
    t.created_by_fk =1
    # t.lat = fake.latitude()
    # t.lon = fake.longitude()
    db.s.add(t)
    db.s.commit()


print "Danish Plaintiffs"
fake = Factory.create('dk_DK')
for _ in range(0,300):
    t = models.Plaintiff()
    t.firstname = fake.first_name()
    t.surname =fake.last_name()
    #t.service_number = fake.ssn()
    t.gender_fk = randint(1,2)
    # t.court_level_fk = 3
    # t.court = fake.random(10)
    t.changed_by_fk = 1
    t.created_by_fk = 1
    # t.lat = fake.latitude()
    # t.lon = fake.longitude()
    db.s.add(t)
    db.s.commit()

print "Witnesses"
fake = Factory.create('es_ES')
for _ in range(0,300):
    t = models.Witness()
    t.firstname = fake.first_name()
    t.surname =fake.last_name()
    #t.service_number = fake.ssn()
    t.gender_fk = randint(1,2)
    # t.court_level_fk = 3
    # t.court = fake.random(10)
    t.changed_by_fk = 1
    t.created_by_fk = 1
    t.special = False
    # t.lat = fake.latitude()
    # t.lon = fake.longitude()
    db.s.add(t)
    db.s.commit()


print "Law Firms"
fake = Factory.create('es_ES')
for _ in range(0,30):
    t = models.Lawfirm()
    t.name = fake.company()
    t.surname =fake.last_name()
    #t.service_number = fake.ssn()
    #t.gender_fk = randint(1,2)
    # t.court_level_fk = 3
    # t.court = fake.random(10)
    # t.changed_by_fk = 1
    # t.created_by_fk = 1
    # t.special = False
    # t.lat = fake.latitude()
    # t.lon = fake.longitude()
    db.s.add(t)
    db.s.commit()

print "Attorneys"
fake = Factory.create('en_GB')
for _ in range(0,100):
    t = models.Attorney()
    t.firstname = fake.first_name()
    t.surname =fake.last_name()
    #t.service_number = fake.ssn()
    t.lawfirm_member = randint(1,20)
    t.gender_fk = randint(1,2)
    t.bar_number = fake.ssn()
    t.call_to_bar_year = randint(1980,2016)
    # t.court_level_fk = 3
    # t.court = fake.random(10)
    t.changed_by_fk = 1
    t.created_by_fk = 1
    # t.special = False
    # t.lat = fake.latitude()
    # t.lon = fake.longitude()
    db.s.add(t)
    db.s.commit()

# print "Policemen"
# fake = Factory.create('en_GB')
# for _ in range(0,100):
#     t = models.Policeman()
#     t.firstname = fake.first_name()
#     t.surname =fake.last_name()
#     #t.service_number = fake.ssn()
#     t.lawfirm_member = randint(1,20)
#     t.gender_fk = randint(1,2)
#     t.bar_number = fake.ssn()
#     t.call_to_bar_year = randint(1980,2016)
#     # t.court_level_fk = 3
#     # t.court = fake.random(10)
#     t.changed_by_fk = 1
#     t.created_by_fk = 1
#     # t.special = False
#     # t.lat = fake.latitude()
#     # t.lon = fake.longitude()
#     db.s.add(t)
#     db.s.commit()


# print " Loading Cases"
# for i in range(0, 1000):
#     cs = models.Case()
#     cs.changed_by_fk = 1;
#     cs.created_by_fk = 1;
#     cs.arrest_location = fake.city()
#     cs.arrest_narrative = fake.text(max_nb_chars=200)
#     cs.arresting_officer = fake.name()
#     cs.charge_date = fake.date_time_this_month()
#     cs.charge_description = fake.text(max_nb_chars=200)
#     cs.document_count = fake.random_digit_or_empty()
#     cs.first_hearing_date = fake.date_time_this_month()
#     cs.ob_numbern= fake.uuid4()
#     cs.report = fake.text(max_nb_chars=400)
#     cs.reporting_officer = fake.name()
#
#     cs.case_category_id = 1
#     cs.casetype_id = 1
#
#     db.s.add(cs)
#     db.s.commit()
#
#
#
# print " Loading Complaints"
# for i in range(0, 1000):
#     cs = models.Complaint()
#     cs.changed_by_fk = 1;
#     cs.created_by_fk = 1;
#     cs.arrest_location = fake.city()
#     cs.arrest_narrative = fake.text(max_nb_chars=200)
#     cs.arresting_officer = fake.name()
#     cs.charge_date = fake.date_time_this_month()
#     cs.charge_description = fake.text(max_nb_chars=200)
#     cs.document_count = fake.random_digit_or_empty()
#     cs.first_hearing_date = fake.date_time_this_month()
#     cs.ob_numbern= fake.uuid4()
#     cs.report = fake.text(max_nb_chars=400)
#     cs.reporting_officer = fake.name()
#
#     cs.case_category_id = 1
#     cs.casetype_id = 1
#
#     db.s.add(cs)
#     db.s.commit()
