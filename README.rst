Judiciary Case management system
--------------------------------------------------------------
Some basic notes:
1. I have automated most of the development so that you need only write the very barest minimum of code
2. The data models are generted from Pony ORM - makes it ridiculously simple to gather and encode domain specific knowledge
3. The Pony datamodels are used to generate a database (postgresql in this case)
4. I use a sqlalchmey schema builder to generate a sqlalchemy data model (bit os a pain - but use the includes to do most of the work and set basic defaults)
5. Generate the input and report screens - they have intelligent defaults and know a lot about people, places, cases and the police.
6. generate custom report formats and tweek them till the users are happy
7. Run it using the gevent-run.py

RTFM







