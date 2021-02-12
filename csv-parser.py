import csv
import requests
from requests_html import HTMLSession
import time


make_list = []
model_list = []
sku_list = []
year_from_list = ['2000']
year_to_list = ['2010']
url_list = []
stock_list = []
id = 0

def make_new_filter_csv():

    with open('Produktu_listas.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for i, line in enumerate(csv_reader):
            make_list.append(line[9])
            model_list.append(line[10])
            sku_list.append(line[0])

        with open('make_model_filter.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('product_sku', 'make', 'model', 'year_from', 'year_to'))
            writer.writerows(zip(sku_list, make_list, model_list, year_from_list, year_to_list))


def update_current_csv():
    with open('Produktu_listas.csv', 'r') as csv_file:
        with open('Produktu_listas.csv', 'r') as csv_file2: 
            csv_reader = csv.reader(csv_file)
            csv_reader2 = csv.reader(csv_file2)

            lines = list(csv_reader2) 

            for i, line in enumerate(csv_reader):
                url_list.append(line[16])
                lines[i][2] = get_stock_info(url_list[i])

            csv_writer = csv.writer(open('Produktu_listas_modified.csv', 'w'))
            csv_writer.writerows(lines)


def get_stock_info(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        
        response.html.render(sleep=0.00001)
        title = response.html.find('span.availability_status', first=True)
        global id
        id+=1
        print('%d : %s' % (id, title.text))

        if title.text == "Out of stock!":
            return 0
        elif title.text == "Ready to ship!":
            return 3
        elif title.text == "Last one!":
            return 1 
        else:
            return 0

    except requests.exceptions.RequestException as e:
        print(e)
        return "In stock"

update_current_csv()
# make_new_filter_csv()



        # with open('make_model_filter.csv', 'w', encoding="cp437", errors='ignore') as new_file:
        #     csv_writer = csv.writer(new_file,  lineterminator='\n', delimiter='\t')

        #     for i, line in enumerate(csv_reader):
        #         csv_writer.writerow([line[9], line[10]])






