import csv

def eb(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        sortierte_wörter = sorted([row[0] for row in reader])
        previous_letter = None
        for word in sortierte_wörter:
            letter = word[0]
            if previous_letter and letter == previous_letter:
                continue
            print(letter, word)
            previous_letter = letter

# Test
eb('Begriffe_Informatik_Amamsiugwudi_3BHWII.csv')

# Kommentar