import os

def cleanstr(text, str):
    pos_end = text.find(str)
    if pos_end > 0:
        text = text[0:pos_end]
    return text

file_dir = "./textFolder_old"
files = os.listdir(file_dir)
file_list = []

for file in files:
    fo = open(file_dir+"/"+file, 'r', encoding='utf-8')
    iter_f = iter(fo)
    file_str = []
    for line in iter_f:
        file_str.append(line)
    file_list.append(file_str)

disease_list = []

for page_text in file_list:
    disease = page_text[0]
    # step 1 clean out everything after' -'
    pos_end = disease.find(' -')
    if pos_end < 0:
        pos_end = disease.find(' (')
    disease = disease[0:pos_end]
    # step 2 clean out 'UPDATE'
    disease = cleanstr(disease, 'UPDATE')
    # step 3 clean out '20XX'
    disease = cleanstr(disease, ' 20')
    # step 4 clean out everything after ' :'
    disease = cleanstr(disease, ' :')
    disease = cleanstr(disease, ':')
    # step 5 clean out ' ('
    disease = cleanstr(disease, ' (')
    disease = cleanstr(disease, '(')
    print(disease)

    


