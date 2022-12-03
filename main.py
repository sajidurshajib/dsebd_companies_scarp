from bs4 import BeautifulSoup
import requests
import json
import os


def main_scr():
    html_text = requests.get('https://www.dsebd.org/company_listing.php').text
    soup = BeautifulSoup(html_text, 'lxml')

    # data sets exist check
    if os.path.isfile("data/data.json"):
        print("Dataset exist, You want to delete previous dataset? (y/Y)")
        x = input()

        if x == 'y' or x == 'Y':
            print("")
            os.remove('data/data.json')
        else:
            return -1
    # get all list link
    main_div = soup.find('div', class_='al-li')

    # more button click
    # for div in main_div:

    all_link = main_div.find_all('a', class_='ab1')

    all_complanies_link = []

    for link in all_link:
        all_complanies_link.append(link['href'])

    all_data = []
    for c in all_complanies_link:
        if c.split('name=')[1][0:2] != 'TB':
            data = single_companies(url=c)
            all_data.append(data)
        else:
            data = tb_type_company(url=c)
            all_data.append(data)

    # count = 378
    # while count > 350 and count < 500:
    #     c = all_complanies_link[count]
    #     print(count)
    #     if c.split('name=')[1][0:2] != 'TB':
    #         data = single_companies(url=c)
    #         all_data.append(data)
    #     else:
    #         data = tb_type_company(url=c)
    #         all_data.append(data)
    #     count += 1

    # json file write

    with open('data/data.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

    print("Done")


def string_handle(s):
    """ this function handle empty value from a string """
    if len(s) == 0:
        return 'N/A'
    elif s == '-':
        return 'N/A'
    else:
        return s.strip()


def single_companies(url: str):
    base_url = 'https://www.dsebd.org'
    company_url = base_url+'/'+url

    html_text = requests.get(company_url).text
    soup = BeautifulSoup(html_text, 'lxml')

    main_div = soup.find('div', class_='row')
    all_table_body = soup.find_all('div', class_='table-responsive')

    company_name = string_handle(main_div.find('h2', class_='topBodyHead').text.split(':')[1])
    code_obj = main_div.find('tr', class_='alt')
    trading_code = string_handle(code_obj.find_all('th')[0].text.split(':')[1])
    scrip_code = string_handle(code_obj.find_all('th')[1].text.split(':')[1])

    # market table
    last_trading_price = string_handle(all_table_body[1].find_all('td')[0].text)
    closing_price = string_handle(all_table_body[1].find_all('td')[1].text)
    last_update = string_handle(all_table_body[1].find_all('td')[2].text)
    days_range = string_handle(all_table_body[1].find_all('td')[3].text)
    change_prev = string_handle(all_table_body[1].find_all('td')[4].text)
    change_next = string_handle(all_table_body[1].find_all('td')[6].text)
    days_value = string_handle(all_table_body[1].find_all('td')[5].text)
    fiftytwo_weeks_moving_range = string_handle(all_table_body[1].find_all('td')[7].text)
    opening_price = string_handle(all_table_body[1].find_all('td')[8].text)
    days_volume = string_handle(all_table_body[1].find_all('td')[9].text)
    adjusted_opening_price = string_handle(all_table_body[1].find_all('td')[10].text)
    days_trade = string_handle(all_table_body[1].find_all('td')[11].text)
    yesterday_closing_price = string_handle(all_table_body[1].find_all('td')[12].text)
    market_capitalization = string_handle(all_table_body[1].find_all('td')[13].text)

    # basic information
    authorized_capital = string_handle(all_table_body[2].find_all('td')[0].text)
    debut_trading_date = string_handle(all_table_body[2].find_all('td')[1].text)
    paid_up_capital = string_handle(all_table_body[2].find_all('td')[2].text)
    type_of_instrument = string_handle(all_table_body[2].find_all('td')[3].text)
    face_par_value = string_handle(all_table_body[2].find_all('td')[4].text)
    market_lot = string_handle(all_table_body[2].find_all('td')[5].text)
    total_outstanding_security = string_handle(all_table_body[2].find_all('td')[6].text)
    sector = string_handle(all_table_body[2].find_all('td')[7].text)

    # address
    address_head_office = string_handle(all_table_body[-2].find_all('td')[2].text)
    address_factory = string_handle(all_table_body[-2].find_all('td')[4].text)
    contact_phone = string_handle(all_table_body[-2].find_all('td')[6].text)
    fax = string_handle(all_table_body[-2].find_all('td')[8].text)
    email = string_handle(all_table_body[-2].find_all('td')[10].text)
    web = string_handle(all_table_body[-2].find_all('td')[12].text)
    company_secretary_name = string_handle(all_table_body[-2].find_all('td')[14].text)
    secretary_cell_no = string_handle(all_table_body[-2].find_all('td')[16].text)
    secretary_telephone_no = string_handle(all_table_body[-2].find_all('td')[18].text)
    secratary_email = string_handle(all_table_body[-2].find_all('td')[20].text)

    listing_year = string_handle(all_table_body[9].find_all('td')[1].text)
    market_catagory = string_handle(all_table_body[9].find_all('td')[3].text)
    electronic_share = string_handle(all_table_body[9].find_all('td')[5].text)

    try:
        share_holding_percent_1 = string_handle(all_table_body[9].find_all('td')[6].text)
        share_holding_obj_1 = all_table_body[9].find_all('td')[7]
        sponsor_or_director_1 = string_handle(share_holding_obj_1.find_all('td')[0].text.split(':')[1])
        govt_1 = string_handle(share_holding_obj_1.find_all('td')[1].text.split(':')[1])
        institute_1 = string_handle(share_holding_obj_1.find_all('td')[2].text.split(':')[1])
        foreign_1 = string_handle(share_holding_obj_1.find_all('td')[3].text.split(':')[1])
        public_1 = string_handle(share_holding_obj_1.find_all('td')[4].text.split(':')[1])
    except:
        share_holding_percent_1 = 'N/A'
        sponsor_or_director_1 = 'N/A'
        govt_1 = 'N/A'
        institute_1 = 'N/A'
        foreign_1 = 'N/A'
        public_1 = 'N/A'

    try:
        share_holding_percent_2 = string_handle(all_table_body[9].find_all('td')[13].text)
        share_holding_obj_2 = all_table_body[9].find_all('td')[14]
        sponsor_or_director_2 = string_handle(share_holding_obj_2.find_all('td')[0].text.split(':')[1])
        govt_2 = string_handle(share_holding_obj_2.find_all('td')[1].text.split(':')[1])
        institute_2 = string_handle(share_holding_obj_2.find_all('td')[2].text.split(':')[1])
        foreign_2 = string_handle(share_holding_obj_2.find_all('td')[3].text.split(':')[1])
        public_2 = string_handle(share_holding_obj_2.find_all('td')[4].text.split(':')[1])
    except:
        share_holding_percent_2 = 'N/A'
        sponsor_or_director_2 = 'N/A'
        govt_2 = 'N/A'
        institute_2 = 'N/A'
        foreign_2 = 'N/A'
        public_2 = 'N/A'

    try:
        share_holding_percent_3 = string_handle(all_table_body[9].find_all('td')[20].text)
        share_holding_obj_3 = all_table_body[9].find_all('td')[21]
        sponsor_or_director_3 = string_handle(share_holding_obj_3.find_all('td')[0].text.split(':')[1])
        govt_3 = string_handle(share_holding_obj_3.find_all('td')[1].text.split(':')[1])
        institute_3 = string_handle(share_holding_obj_3.find_all('td')[2].text.split(':')[1])
        foreign_3 = string_handle(share_holding_obj_3.find_all('td')[3].text.split(':')[1])
        public_3 = string_handle(share_holding_obj_3.find_all('td')[4].text.split(':')[1])
    except:
        share_holding_percent_3 = 'N/A'
        sponsor_or_director_3 = 'N/A'
        govt_3 = 'N/A'
        institute_3 = 'N/A'
        foreign_3 = 'N/A'
        public_3 = 'N/A'

    if all_table_body[9].find_all('td')[-1]:
        remarks = string_handle(all_table_body[9].find_all('td')[-1].text)
    else:
        remarks = 'N/A'

    print(company_url)

    return {
        "company_name": company_name,
        "security_name": "N/A",
        "company_url": company_url,
        "trading_code": trading_code,
        "scrip_code": scrip_code,
        "isin": "N/A",

        "last_trading_price": last_trading_price,
        "closing_price": closing_price,
        "last_update": last_update,
        "days_range": days_range,
        "change_prev": change_prev,
        "change_next": change_next,
        "days_value": days_value,
        "fiftytwo_weeks_moving_range": fiftytwo_weeks_moving_range,
        "opening_price": opening_price,
        "days_volume": days_volume,
        "adjusted_opening_price": adjusted_opening_price,
        "days_trade": days_trade,
        "yesterday_closing_price": yesterday_closing_price,
        "market_capitalization": market_capitalization,

        "authorized_capital": authorized_capital,
        "debut_trading_date": debut_trading_date,
        "paid_up_capital": paid_up_capital,
        "type_of_instrument": type_of_instrument,
        "face_par_value": face_par_value,
        "market_lot": market_lot,
        "total_outstanding_security": total_outstanding_security,
        "sector": sector,

        "address_head_office": address_head_office,
        "address_factory": address_factory,
        "address_issuer": "N/A",
        "concern_department": "N/A",
        "contact_phone": contact_phone,
        "fax": fax,
        "email": email,
        "web": web,
        "company_secretary_name": company_secretary_name,
        "secretary_cell_no": secretary_cell_no,
        "secretary_telephone_no": secretary_telephone_no,
        "secratary_email": secratary_email,

        "listing_year": listing_year,
        "market_catagory": market_catagory,
        "electronic_share": electronic_share,
        "share_holding_percent_1": share_holding_percent_1,
        "sponsor_or_director_1": sponsor_or_director_1,
        "govt_1": govt_1,
        "institute_1": institute_1,
        "foreign_1": foreign_1,
        "public_1": public_1,
        "share_holding_percent_2": share_holding_percent_2,
        "sponsor_or_director_2": sponsor_or_director_2,
        "govt_2": govt_2,
        "institute_2": institute_2,
        "foreign_2": foreign_2,
        "public_2": public_2,
        "share_holding_percent_3": share_holding_percent_3,
        "sponsor_or_director_3": sponsor_or_director_3,
        "govt_3": govt_3,
        "institute_3": institute_3,
        "foreign_3": foreign_3,
        "public_3": public_3,
        "remarks": remarks
    }


def tb_type_company(url: str):
    base_url = 'https://www.dsebd.org'
    company_url = base_url+'/'+url

    html_text = requests.get(company_url).text
    soup = BeautifulSoup(html_text, 'lxml')

    main_div = soup.find('div', class_='row')
    all_table_body = soup.find_all('div', class_='table-responsive')

    company_name = 'N/A'
    security_name = string_handle(main_div.find('h2', class_='topBodyHead').text.split(':')[1])
    code_obj = main_div.find_all('tr', class_='alt')
    trading_code = string_handle(code_obj[0].find_all('th')[0].text.split(':')[1])
    scrip_code = string_handle(code_obj[0].find_all('th')[1].text.split(':')[1])
    isin = string_handle(code_obj[1].find_all('th')[0].text.split(':')[1])

    # market information table
    last_trading_price = string_handle(all_table_body[1].find_all('td')[0].text)
    closing_price = string_handle(all_table_body[1].find_all('td')[1].text)
    last_update = string_handle(all_table_body[1].find_all('td')[4].text)
    days_range = string_handle(all_table_body[1].find_all('td')[3].text)
    change_prev = string_handle(all_table_body[1].find_all('td')[6].text)
    change_next = string_handle(all_table_body[1].find_all('td')[8].text)
    days_value = string_handle(all_table_body[1].find_all('td')[5].text)
    fiftytwo_weeks_moving_range = string_handle(all_table_body[1].find_all('td')[7].text)
    opening_price = string_handle(all_table_body[1].find_all('td')[10].text)
    days_volume = string_handle(all_table_body[1].find_all('td')[9].text)
    adjusted_opening_price = string_handle(all_table_body[1].find_all('td')[12].text)
    days_trade = string_handle(all_table_body[1].find_all('td')[11].text)
    yesterday_closing_price = string_handle(all_table_body[1].find_all('td')[14].text)
    market_capitalization = string_handle(all_table_body[1].find_all('td')[13].text)

    # basic information
    # authorized_capital = string_handle(all_table_body[2].find_all('td')[0].text)
    # debut_trading_date = string_handle(all_table_body[2].find_all('td')[1].text)
    # paid_up_capital = string_handle(all_table_body[2].find_all('td')[2].text)
    type_of_instrument = string_handle(all_table_body[2].find_all('td')[1].text)
    face_par_value = string_handle(all_table_body[2].find_all('td')[4].text)
    market_lot = string_handle(all_table_body[2].find_all('td')[5].text)
    total_outstanding_security = string_handle(all_table_body[2].find_all('td')[2].text)
    sector = string_handle(all_table_body[2].find_all('td')[3].text)

    # address
    address_issuer = string_handle(all_table_body[-2].find_all('td')[1].text)
    concern_department = string_handle(all_table_body[-2].find_all('td')[5].text)
    contact_phone = string_handle(all_table_body[-2].find_all('td')[7].text)
    email = string_handle(all_table_body[-2].find_all('td')[9].text)
    web = string_handle(all_table_body[-2].find_all('td')[3].text)

    return {
        "company_name": company_name,
        "security_name": security_name,
        "company_url": company_url,
        "trading_code": trading_code,
        "scrip_code": scrip_code,
        "isin": isin,

        "last_trading_price": last_trading_price,
        "closing_price": closing_price,
        "last_update": last_update,
        "days_range": days_range,
        "change_prev": change_prev,
        "change_next": change_next,
        "days_value": days_value,
        "fiftytwo_weeks_moving_range": fiftytwo_weeks_moving_range,
        "opening_price": opening_price,
        "days_volume": days_volume,
        "adjusted_opening_price": adjusted_opening_price,
        "days_trade": days_trade,
        "yesterday_closing_price": yesterday_closing_price,
        "market_capitalization": market_capitalization,

        "authorized_capital": "N/A",
        "debut_trading_date": "N/A",
        "paid_up_capital": "N/A",
        "type_of_instrument": type_of_instrument,
        "face_par_value": face_par_value,
        "market_lot": market_lot,
        "total_outstanding_security": total_outstanding_security,
        "sector": sector,

        "address_head_office": "N/A",
        "address_factory": "N/A",
        "address_issuer": address_issuer,
        "concern_department": concern_department,
        "contact_phone": contact_phone,
        "fax": "N/A",
        "email": email,
        "web": web,
        "company_secretary_name": "N/A",
        "secretary_cell_no": "N/A",
        "secretary_telephone_no": "N/A",
        "secratary_email": "N/A",

        "listing_year": "N/A",
        "market_catagory": "N/A",
        "electronic_share": "N/A",
        "share_holding_percent_1": "N/A",
        "sponsor_or_director_1": "N/A",
        "govt_1": "N/A",
        "institute_1": "N/A",
        "foreign_1": "N/A",
        "public_1": "N/A",
        "share_holding_percent_2": "N/A",
        "sponsor_or_director_2": "N/A",
        "govt_2": "N/A",
        "institute_2": "N/A",
        "foreign_2": "N/A",
        "public_2": "N/A",
        "share_holding_percent_3": "N/A",
        "sponsor_or_director_3": "N/A",
        "govt_3": "N/A",
        "institute_3": "N/A",
        "foreign_3": "N/A",
        "public_3": "N/A",
        "remarks": "N/A"
    }


if __name__ == '__main__':
    main_scr()
