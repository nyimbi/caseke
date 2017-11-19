import csv
import sh

h = open('output.sql','a')
with open('all_emails1.csv') as csvfile:
    reader = csv.reader(csvfile,quotechar='\t')
    for row in reader:
        sh('create_mail_user_SQL.sh', row[0], row[1], _out=h)
        print(row[0] row[1])