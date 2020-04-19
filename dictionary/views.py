from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {
    }
    return render(request, 'dictionary/index.html', context)
def searchTerm(request):
    import csv
    language_from=request.GET['language_from'].lower()
    language_to = request.GET['language_to'].lower()
    search_term=request.GET['search_term'].lower()
    synonims=[]
    definition=None
    translations=[]
    if language_from=='english' and language_to=='german':
        with open('../terms_english_to_german.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                if row[0]==search_term:
                    definition=row[1]
                    for i in range(2,row.index('__________')):
                        synonims.append(row[i])
                    for i in range(row.index('__________')+1,len(row)):
                        translations.append(row[i])
                    break
        csv_file.close()
    if language_from=='german' and language_to=='english':
        with open('../terms_german_to_english.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                if row[0] == search_term:
                    definition = row[1]
                    for i in range(2, row.index('__________')):
                        synonims.append(row[i])
                    for i in range(row.index('__________') + 1, len(row)):
                        translations.append(row[i])
                    break
        csv_file.close()
    context = {
        'definition':definition,
        'translations':translations,
        'synonims':synonims,
    }
    return render(request, 'dictionary/index.html', context)
