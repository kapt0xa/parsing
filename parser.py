import requests
from bs4 import BeautifulSoup
import time
import random;

# output_file = open('./output/filename.txt', 'w', encoding='utf-8')
# output_file.close()

def parse_all_chem_elements_links_redox_voltages_from_MSU():
    MSU_chem_redox_voltage = 'https://www.chem.msu.ru/rus/handbook/redox/welcome.html'
    MSU_chem_redox_voltage_prefix = 'https://www.chem.msu.ru/rus/handbook/redox/'
    MSU_chem_redox_voltage_marker = 'elem_dat'


    # STEP 1: Get the main page and extract hidden links
    main_url = MSU_chem_redox_voltage
    response = requests.get(main_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all links (modify the class name based on your target website)
    links = []
    for a_tag in soup.find_all('a', href = True):
        href = a_tag['href']
        if MSU_chem_redox_voltage_marker in href:
            absolute_link = MSU_chem_redox_voltage_prefix + href
            links.append(absolute_link)

    return links

def parse_all_chem_elements_links_redox_voltages_from_MSU_and_save_to_file():
    links = parse_all_chem_elements_links_redox_voltages_from_MSU()
    redox_data_links = open('./output/redox_links.txt', 'w', encoding='utf-8')
    for link in links:
        redox_data_links.write(f'{link}\n')
    redox_data_links.close()

def parse_carbon():
    MSU_chem_redox_voltage_carbon_data = 'https://www.chem.msu.ru/rus/handbook/redox/elem_dat/c.html'


    # STEP 1: Get the main page and extract hidden links
    main_url = MSU_chem_redox_voltage_carbon_data
    response = requests.get(main_url)
    carbon_data = open('./output/carbon_data.txt', 'w', encoding='utf-8')
    carbon_data.write(response.text)
    carbon_data.close()

def parse_all_chem_elemrnts_redox_voltages_from_MSU():
    links = parse_all_chem_elements_links_redox_voltages_from_MSU()

    all_elements_data = open('./output/elements_redox_voltages.txt', 'w', encoding='utf-8')
    for i, url in enumerate(links, 1):
        print(f'[{i}/{len(links)}] parsing: {url}')

        try:
            time.sleep(1 + random.uniform(0, 3))
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            center_tags = soup.find_all('center')

            for center in center_tags:
                all_elements_data.write(str(center) + '\n\n')
            print(f'sucsess {i}')
        except Exception as e:
            all_elements_data.write(f'<center><h1>failure for index {i}</h1></center>' + '\n\n')
            print(f'failure {i}')

    all_elements_data.close()


def rework_parsed_chemical_elements_data():
    from chem_elements import chem_elements_indexes
    links_file = open('./output/elements_redox_voltages.txt', 'w', encoding='utf-8')