#!/usr/bin/env python

import datetime
import pprint
import sys
import time

import requests

# Optionally specify an email that will receive notification of functional prediction job results upon completion
EMAIL = ''

# Begin demo
print (
	"This script demonstrates how FNTM API can be called from Python to access FNTM data and computational methods.\n"
	"Examples 1-3 show how to query basic resources such as gene and context lists; Examples 4-9 show how to query\n"
	"functional networks and supporting datasets; and Examples 10-13 illustrate how to start and monitor functional\n"
	"prediction jobs.\n")
print "Started {0} at {1}\n".format(sys.argv[0], datetime.datetime.now())

print "1. Get list of organisms supported by the API"
q = 'http://fntm-api.princeton.edu/organisms'
print "QUERY:", q
r = requests.get(q)
j = r.json()
print "RESPONSE:"
pp = pprint.PrettyPrinter(indent=4, width=120)
pp.pprint(j)
print
time.sleep(1)

print "2. Get list of genes recognized by the API"
q = 'http://fntm-api.princeton.edu/genes'
print "QUERY:", q
r = requests.get(q)
j = r.json()
print "RESPONSE (first 10 symbols):"
pp.pprint(j[0:10])
print
time.sleep(1)

print "3. Get list of contexts (i.e., tissues) recognized by the API"
q = 'http://fntm-api.princeton.edu/contexts'
print "QUERY:", q
r = requests.get(q)
j = r.json()
print "RESPONSE (first 10 contexts):"
pp.pprint(j[0:10])
print
time.sleep(1)

print "4. Get network in brain tissue around PTGS2 gene"
q = 'http://fntm-api.princeton.edu/networks/brain/ptgs2'
print "QUERY:", q
r = requests.get(q)
j = r.json()
print "RESPONSE (first 3 genes in enumeration):"
pp.pprint(j['genes'][0:3])
print "RESPONSE (first 5 edges):"
pp.pprint(j['edges'][0:5])
print
time.sleep(1)

print "5. Get network in brain tissue around PTGS2 and PARK7 genes"
q = 'http://fntm-api.princeton.edu/networks/brain/ptgs2+park7'
print "QUERY:", q
r = requests.get(q)
j = r.json()
print "RESPONSE (first 5 edges):"
pp.pprint(j['edges'][0:5])
print
time.sleep(1)

print "6. Recompute edge weights of previous query with specified prior probability"
q = 'http://fntm-api.princeton.edu/networks/brain/ptgs2+park7?prior=0.15'
print "QUERY:", q
r = requests.get(q)
j = r.json()
print "RESPONSE (first 5 edges):"
pp.pprint(j['edges'][0:5])
print
time.sleep(1)

print "7. Subset previous network around the 10 most connected genes"
q = 'http://fntm-api.princeton.edu/networks/brain/ptgs2+park7?prior=0.15&size=10'
print "QUERY:", q
r = requests.get(q)
j = r.json()
print "RESPONSE (first 5 edges):"
pp.pprint(j['edges'][0:5])
print
time.sleep(1)

print "8. Get datasets supporting PTGS2-PARK7 interaction in brain"
q = 'http://fntm-api.princeton.edu/evidence/brain?source=ptgs2&target=park7'
print "QUERY:", q
r = requests.get(q)
j = r.json()
print "RESPONSE (top 3 datasets):"
pp.pprint(j['datasets'][0:3])
print
time.sleep(1)

print "9. Recompute previous dataset posteriors using updated prior"
q = 'http://fntm-api.princeton.edu/evidence/brain?source=ptgs2&target=park7&prior=0.15'
print "QUERY:", q
r = requests.get(q)
j = r.json()
print "RESPONSE (top 3 datasets):"
pp.pprint(j['datasets'][0:3])
print
time.sleep(1)

print "10. Predict genes functionally related to a given set of genes"
q = 'http://fntm-api.princeton.edu/funpred/jobs'
data = {'context': 'brain', 'email': EMAIL, 'title': 'FNTM API Python Demo'}
files = {'gene_file': ('positive-symbols.txt', open('positive-symbols.txt'))}
print "URL:", q
print "PARAMETERS:", data
print "GENE FILE: positive-symbols.txt"
r = requests.post(q, data=data, files=files)
j = r.json()
print "RESPONSE:"
pp.pprint(j)
print
time.sleep(1)

print "Wait 10 s for functional prediction job to complete on FNTM server"
for i in range(10):
    sys.stdout.write('.')
    time.sleep(1)
print "\n\n"

print "11. Check status of previous functional prediction job"
q = 'http://fntm-api.princeton.edu/funpred/jobs/' + j['id']
print "QUERY:", q
r = requests.get(q)
j = r.json()
print "RESPONSE:"
pp.pprint(j)
print
time.sleep(1)

print "12. Check SVM progress of previous functional prediction job"
q = j['log_file']
print "QUERY:", q
r = requests.get(q)
#j = r.json()
print "RESPONSE:"
print r.text
time.sleep(1)

print "13. Check prediction results of previous functional prediction job"
q = j['result_file']
print "QUERY:", q
r = requests.get(q)
#j = r.json()
print "RESPONSE (first 25 lines):"
print "\n".join(r.text.splitlines()[0:25])
print
time.sleep(1)

# End demo
print "Completed {0} at {1}".format(sys.argv[0], datetime.datetime.now())
