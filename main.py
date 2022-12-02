from bs4 import BeautifulSoup
import requests


def main_scr():
    html_text = requests.get('https://www.dsebd.org/company_listing.php').text
    soup = BeautifulSoup(html_text, 'lxml')

    main_div = soup.find('div', class_='al-li')

    # more button click
    # for div in main_div:

    all_link = main_div.find_all('a', class_='ab1')

    all_complanies_link = []

    for link in all_link:
        all_complanies_link.append(link['href'])

    all_data = []
    for c in all_complanies_link:
        if c.split('name=')[1][0] != 'T':
            data = single_companies(url=c)
            all_data.append(data)

    f = open("data/data.json", "a")
    f.write(all_data)
    f.close()
    print("Done")


def single_companies(url: str):
    base_url = 'https://www.dsebd.org'
    company_url = base_url+'/'+url

    html_text = requests.get(company_url).text
    soup = BeautifulSoup(html_text, 'lxml')

    main_div = soup.find('div', class_='row')
    all_table_body = soup.find_all('div', class_='table-responsive')

    company_name = main_div.find('h2', class_='topBodyHead').text.split(':')[1].strip()
    code_obj = main_div.find('tr', class_='alt')
    trading_code = code_obj.find_all('th')[0].text.split(':')[1].strip()
    scrip_code = code_obj.find_all('th')[1].text.split(':')[1].strip()

    # market table
    last_trading_price = all_table_body[1].find_all('td')[0].text
    closing_price = all_table_body[1].find_all('td')[1].text
    last_update = all_table_body[1].find_all('td')[2].text
    days_range = all_table_body[1].find_all('td')[3].text
    change_prev = all_table_body[1].find_all('td')[4].text
    change_next = all_table_body[1].find_all('td')[6].text
    days_value = all_table_body[1].find_all('td')[5].text
    fiftytwo_weeks_moving_range = all_table_body[1].find_all('td')[7].text
    opening_price = all_table_body[1].find_all('td')[8].text
    days_volume = all_table_body[1].find_all('td')[9].text
    adjusted_opening_price = all_table_body[1].find_all('td')[10].text
    days_trade = all_table_body[1].find_all('td')[11].text
    yesterday_closing_price = all_table_body[1].find_all('td')[12].text
    market_capitalization = all_table_body[1].find_all('td')[13].text
    authorized_capital = all_table_body[2].find_all('td')[0].text
    debut_trading_date = all_table_body[2].find_all('td')[1].text
    paid_up_capital = all_table_body[2].find_all('td')[2].text
    type_of_instrument = all_table_body[2].find_all('td')[3].text
    face_par_value = all_table_body[2].find_all('td')[4].text
    market_lot = all_table_body[2].find_all('td')[5].text
    total_outstanding_security = all_table_body[2].find_all('td')[6].text
    sector = all_table_body[2].find_all('td')[7].text
    address_head_office = all_table_body[-2].find_all('td')[2].text
    address_factory = all_table_body[-2].find_all('td')[4].text
    contact_phone = all_table_body[-2].find_all('td')[6].text
    fax = all_table_body[-2].find_all('td')[8].text
    email = all_table_body[-2].find_all('td')[10].text
    web = all_table_body[-2].find_all('td')[12].text
    company_secretary_name = all_table_body[-2].find_all('td')[14].text
    secretary_cell_no = all_table_body[-2].find_all('td')[16].text
    secretary_telephone_no = all_table_body[-2].find_all('td')[18].text
    secratary_email = all_table_body[-2].find_all('td')[20].text

    listing_year = all_table_body[9].find_all('td')[1].text
    market_catagory = all_table_body[9].find_all('td')[3].text
    electronic_share = all_table_body[9].find_all('td')[5].text

    try:
        share_holding_percent_1 = all_table_body[9].find_all('td')[6].text
        share_holding_obj_1 = all_table_body[9].find_all('td')[7]
        sponsor_or_director_1 = share_holding_obj_1.find_all('td')[0].text.split(':')[1].strip()
        govt_1 = share_holding_obj_1.find_all('td')[1].text.split(':')[1].strip()
        institute_1 = share_holding_obj_1.find_all('td')[2].text.split(':')[1].strip()
        foreign_1 = share_holding_obj_1.find_all('td')[3].text.split(':')[1].strip()
        public_1 = share_holding_obj_1.find_all('td')[4].text.split(':')[1].strip()
    except:
        share_holding_percent_1 = 'N/A'
        sponsor_or_director_1 = 'N/A'
        govt_1 = 'N/A'
        institute_1 = 'N/A'
        foreign_1 = 'N/A'
        public_1 = 'N/A'

    try:
        share_holding_percent_2 = all_table_body[9].find_all('td')[13].text
        share_holding_obj_2 = all_table_body[9].find_all('td')[14]
        sponsor_or_director_2 = share_holding_obj_2.find_all('td')[0].text.split(':')[1].strip()
        govt_2 = share_holding_obj_2.find_all('td')[1].text.split(':')[1].strip()
        institute_2 = share_holding_obj_2.find_all('td')[2].text.split(':')[1].strip()
        foreign_2 = share_holding_obj_2.find_all('td')[3].text.split(':')[1].strip()
        public_2 = share_holding_obj_2.find_all('td')[4].text.split(':')[1].strip()
    except:
        share_holding_percent_2 = 'N/A'
        sponsor_or_director_2 = 'N/A'
        govt_2 = 'N/A'
        institute_2 = 'N/A'
        foreign_2 = 'N/A'
        public_2 = 'N/A'

    try:
        share_holding_percent_3 = all_table_body[9].find_all('td')[20].text
        share_holding_obj_3 = all_table_body[9].find_all('td')[21]
        sponsor_or_director_3 = share_holding_obj_3.find_all('td')[0].text.split(':')[1].strip()
        govt_3 = share_holding_obj_3.find_all('td')[1].text.split(':')[1].strip()
        institute_3 = share_holding_obj_3.find_all('td')[2].text.split(':')[1].strip()
        foreign_3 = share_holding_obj_3.find_all('td')[3].text.split(':')[1].strip()
        public_3 = share_holding_obj_3.find_all('td')[4].text.split(':')[1].strip()
    except:
        share_holding_percent_3 = 'N/A'
        sponsor_or_director_3 = 'N/A'
        govt_3 = 'N/A'
        institute_3 = 'N/A'
        foreign_3 = 'N/A'
        public_3 = 'N/A'

    if all_table_body[9].find_all('td')[-1]:
        remarks = all_table_body[9].find_all('td')[-1].text
    else:
        remarks = 'N/A'

    print(company_url)
    print(remarks)

    return {
        "company_name": company_name,
        "company_url": company_url,
        "trading_code": trading_code,
        "scrip_code": scrip_code,
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


if __name__ == '__main__':
    main_scr()
