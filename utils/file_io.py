import json
import os
import csv


def dataset_create_with_check():
    """ data set create with check """
    if os.path.isfile("data/data.json"):
        print("Dataset exist, You want to delete previous dataset? (y/Y)")
        x = input()

        if x == 'y' or x == 'Y':
            print("")
            os.remove('data/data.json')
            if os.path.isfile("data/data.csv"):
                os.remove('data/data.csv')
        else:
            return -1


def create_json(all_data):
    """ get all data and create json output file """
    with open('data/data.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)
    print("JSON dataset created")


def create_csv(all_data):
    """ get all data and create csv joutput file """
    a = all_data[0]
    with open('data/data.csv', 'a') as f:
        w = csv.DictWriter(f, a.keys())
        w.writeheader()
    for i in all_data:
        with open('data/data.csv', 'a') as f:
            w = csv.DictWriter(f, i.keys())
            w.writerow(i)
    print("CSV dataset created")
