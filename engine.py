import primeSpacing


def getRevisions(record):
    with open('subjects.txt', 'r') as file:
        for subject in file:
            print('For ' + subject + ':')

