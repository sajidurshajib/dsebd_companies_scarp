from bs4 import BeautifulSoup
import asyncio
import aiohttp
import time
from utils import string_handle, create_csv, create_json, dataset_create_with_check, market_table, basic_table, address_table


all_data = []


def main_scr():

    # data sets exist check
    dataset_create_with_check()

    start_time = time.time()

    html_text = asyncio.run(get_url_from_text('https://www.dsebd.org/company_listing.php'))

    soup = BeautifulSoup(html_text, 'lxml')

    # loop = asyncio.new_event_loop()
    # soup = loop.run_in_executor(None, BeautifulSoup, html_text, 'lxml')

    # get all list link
    main_div = soup.find('div', class_='al-li')

    # more button
    more_btn(main_div_obj=main_div)

    # for div in main_div:
    all_link = main_div.find_all('a', class_='ab1')

    all_complanies_link = []
    # all_complanies_link.append('displayCompany.php?name=INTECH')

    for link in all_link:
        all_complanies_link.append(link['href'])

    print(len(all_complanies_link))

    mem_main = asyncio.run(main_scrap(urls=all_complanies_link))

    end_time = time.time()
    total_time = end_time - start_time

    create_json(all_data=all_data)
    create_csv(all_data=all_data)

    print("-----------------")
    print("Done")
    print(f'Scraping time: %.2f seconds.' % total_time)


async def scrap(url: str):
    base_url = 'https://www.dsebd.org'
    company_url = base_url + '/' + url

    async with aiohttp.ClientSession() as session:
        async with session.get(company_url) as response:

            html = await response.text()

            if url[0:2] != 'TB':
                data = single_companies(html_text=html, company_url='https://www.dsebd.org/'+url)
            else:
                data = tb_type_company(html_text=html, company_url='https://www.dsebd.org/'+url)

            all_data.append(data)


async def main_scrap(urls):
    tasks = []
    for u in urls:
        # task = asyncio.create_task(scrap(url=u))
        tasks.append(scrap(url=u))

    await asyncio.gather(*tasks)


async def get_url_from_text(url: str):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        return await response.text()


def more_btn(main_div_obj):
    more_btns = main_div_obj.find_all('a', class_='showClass')
    for mb in more_btns:
        mb.get('onclik')


def single_companies(html_text, company_url):
    print(company_url)

    soup = BeautifulSoup(html_text, 'lxml')

    main_div = soup.find('div', class_='row')
    all_table_body = soup.find_all('div', class_='table-responsive')

    company_name = string_handle(main_div.find('h2', class_='topBodyHead').text.split(':')[1])
    code_obj = main_div.find('tr', class_='alt')
    trading_code = string_handle(code_obj.find_all('th')[0].text.split(':')[1])
    scrip_code = string_handle(code_obj.find_all('th')[1].text.split(':')[1])

    # market table
    market_tbl = market_table(table_td=all_table_body[1].find_all('td'), company_type_td=False)

    # basic information
    basic_tbl = basic_table(table_td=all_table_body[2].find_all('td'), company_type_td=False)

    # address
    address_tbl = address_table(table_td=all_table_body[-2].find_all('td'), company_type_td=False)

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

    return {
        "company_name": company_name,
        "security_name": "N/A",
        "company_url": company_url,
        "trading_code": trading_code,
        "scrip_code": scrip_code,
        "isin": "N/A",

        **market_tbl,
        **basic_tbl,
        **address_tbl,

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


def tb_type_company(html_text, company_url):
    # base_url = 'https://www.dsebd.org'
    # company_url = base_url+'/'+url

    # # html_text = requests.get(company_url).text
    # html_text = asyncio.run(get_url_from_text(url=company_url))

    soup = BeautifulSoup(html_text, 'lxml')

    main_div = soup.find('div', class_='row')
    all_table_body = soup.find_all('div', class_='table-responsive')

    security_name = string_handle(main_div.find('h2', class_='topBodyHead').text.split(':')[1])
    code_obj = main_div.find_all('tr', class_='alt')
    trading_code = string_handle(code_obj[0].find_all('th')[0].text.split(':')[1])
    scrip_code = string_handle(code_obj[0].find_all('th')[1].text.split(':')[1])
    isin = string_handle(code_obj[1].find_all('th')[0].text.split(':')[1])

    # market information table
    market_tbl = market_table(table_td=all_table_body[1].find_all('td'), company_type_td=True)

    # basic information
    # all_table_body[2].find_all('td')
    basic_tbl = basic_table(table_td=all_table_body[2].find_all('td'), company_type_td=True)

    # address
    address_tbl = address_table(table_td=all_table_body[-2].find_all('td'), company_type_td=True)

    return {
        "company_name": "N/A",
        "security_name": security_name,
        "company_url": company_url,
        "trading_code": trading_code,
        "scrip_code": scrip_code,
        "isin": isin,

        **market_tbl,
        **basic_tbl,
        **address_tbl,

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
