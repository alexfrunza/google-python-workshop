import time

from selenium.webdriver.common.by import By
import pandas as pd

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

header_list = ["NR. CRT", "Judet", "01.03", "02.03", "03.03", "04.03", "05.03"]
dataset = []

not_in_country = ["43", "Din străinătate"]

nealocated_cases = ["44", "Cazuri noi nealocate pe judete"]
total_cases = ["TOTAL", ""]


def extract_data(link: str):
    global browser
    browser.get(link)
    time.sleep(10)
    table = browser.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[1]/main/article/div/div/table[1]')
    rows = table.text.split("\n")
    for index, row in enumerate(rows[1:]):
        if index == 42:
            break

        splitted_row = row.split(" ")
        covid_cases = splitted_row[-3]

        if len(dataset) < index + 1:
            nr_crt = splitted_row[0][:-1]
            if index == 31 or index == 41:
                county = splitted_row[1] + ' ' + splitted_row[2]
            else:
                county = splitted_row[1]
            dataset.append([nr_crt, county, covid_cases])
        else:
            dataset[index].append(covid_cases)

    # For citizens which are not in country
    not_in_country.append(rows[43].split(" ")[3])

    # For new cases nealocated to a county
    new_cases = rows[44:-1]
    if len(new_cases) == 1:
        nealocated_cases.append(new_cases[0].split(" ")[6][:-1])
    else:
        nealocated_cases.append(new_cases[1][2:-1])

    # For total cases
    total_cases.append(rows[-1].split(" ")[2])


# extract_data("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/")

# Extract data for first 3 days of March
for i in range(1, 4):
    extract_data(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{i}-martie-ora-13-00-2/")

# Extract data for 5th day of March (the link have different structure)
extract_data("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-3/")
# Extract data for 5th day of March (the link have different structure)
extract_data("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/")

browser.close()
dataset.append(not_in_country)
dataset.append(nealocated_cases)
dataset.append(total_cases)

df = pd.DataFrame(dataset, columns=header_list)
with pd.ExcelWriter('results.xlsx') as writer:
    df.to_excel(writer, index=False)
