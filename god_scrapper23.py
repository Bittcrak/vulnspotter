import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

import csv
import time


filename = "vuln.csv"
# writing to csv file
rows=[]

driver = webdriver.Firefox()

def nvidia():
    row=[]
    driver.get('https://www.nvidia.com/en-us/security/')
    time.sleep(3)
    element=driver.find_element(By.ID,"onetrust-reject-all-handler")
    element.click()
    html=driver.page_source
    soup=bs(html,'lxml')
    table=soup.find('table',class_='responsive compare-table')
    for row in table.tbody.find_all('tr',class_='content'):
            columns=row.find_all('td')
            if columns!=[]:
                prod_name=columns[0].text.strip()
                prod_ver="na"
                oem="nvidia"
                vuln=columns[3].text.strip()
                sev=columns[2].text.strip()
                mit_strat=columns[0].a.href
                pub=columns[4].text.strip()
                arow =[prod_name,',', prod_ver,',', oem,',', sev,',', vuln,',', mit_strat,',', pub,", NA"]
                row.append(arow)
    return row



# def redhat():
#     row=[]
#     driver.get('https://access.redhat.com/security/security-updates/')
#     time.sleep(3)
#     element=driver.find_element(By.ID,"truste-consent-button")
#     element.click()
#     html=driver.page_source
#     soup=bs(html)
#     table=soup.find('cp-table',id='Security-Errata-Table')
#     for row in table.body.find_all('cp-tr'):
#             columns=row.find_all('cp-td')
#             if columns!=[]:
#                 prod_name=columns[3].text.strip()
#                 prod_ver="na"
#                 oem="redhat"
#                 vuln=columns[1].text.strip()
#                 sev=columns[2].text.strip()
#                 mit_strat=columns[0].a.href
#                 pub=columns[4].text.strip()
#                 arow =[prod_name,',', prod_ver,',', oem,',', sev,',', vuln,',', mit_strat,',', pub,", NA"]
#                 row.append(arow)
#     return row


# redhat()


# def cisco():
#     row=[]
#     driver.get('https://www.nvidia.com/en-us/security/')
#     time.sleep(3)
#     element=driver.find_element(By.ID,"onetrust-reject-all-handler")
#     element.click()
#     html=driver.page_source
#     soup=bs(html,'lxml')
#     table=soup.find('table',class_='responsive compare-table')
#     for row in table.tbody.find_all('tr',class_='content'):
#             columns=row.find_all('td')
#             if columns!=[]:
#                 prod_name=columns[0].text.strip()
#                 prod_ver="na"
#                 oem="nvidia"
#                 vuln=columns[3].text.strip()
#                 sev=columns[2].text.strip()
#                 mit_strat=columns[0].a.href
#                 pub=columns[4].text.strip()
#                 arow =[prod_name,',', prod_ver,',', oem,',', sev,',', vuln,',', mit_strat,',', pub,", NA"]
#                 row.append(arow)
#     return row


def cisco():
    row=[]
    driver.get('https://sec.cloudapps.cisco.com/security/center/publicationListing.x')
    time.sleep(1)
    # element=driver.find_element(By.ID,"onetrust-reject-all-handler")
    # element.click()
    html=driver.page_source
    soup=bs(html,'lxml')
    table=soup.find('table')
    for row in table.tbody.find_all('tr'):
            columns=row.find_all('td')
            if columns!=[]:
                prod_name=columns[0].text.strip()
                prod_ver=columns[4].text.strip()
                oem="cisco"
                vuln=columns[0].text.strip()
                sev=columns[1].text.strip()
                mit_strat="NA"
                pub=columns[3].text.strip()
                cve=columns[2].text.strip()
                arow =[prod_name,',', prod_ver,',', oem,',', sev,',', vuln,',', mit_strat,',', pub, cve]
                row.append(arow)
    return row

# rows=nvidia()
cisco()
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the data rows
    csvwriter.writerows(rows)