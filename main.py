from bs4 import BeautifulSoup
import requests


def main_scr():
    html_text = requests.get('https://www.dsebd.org/company_listing.php').text
    soup = BeautifulSoup(html_text, 'lxml')

    main_div = soup.find('div', class_='al-li')

    # for div in main_div:

    all_link = main_div.find_all('a', class_='ab1')

    all_complanies_link = []

    for link in all_link:
        all_complanies_link.append(link['href'])

    for c in all_complanies_link:
        data = single_companies(url=c)
        print(data)


def single_companies(url: str):
    base_url = 'https://www.dsebd.org'
    company_url = base_url+'/'+url

    html_text = requests.get(company_url).text
    soup = BeautifulSoup(html_text, 'lxml')

    main_div = soup.find('div', class_='row')

    company_name = main_div.find('h2', class_='topBodyHead').text.split(':')[1].strip()
    code_obj = main_div.find('tr', class_='alt')
    trading_code = code_obj.find_all('th')[0].text.split(':')[1].strip()
    scrip_code = code_obj.find_all('th')[1].text.split(':')[1].strip()

    return {
        "company_name": company_name,
        "company_url": company_url,
        "trading_code": trading_code,
        "scrip_code": scrip_code
    }


if __name__ == '__main__':
    main_scr()
