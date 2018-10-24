from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import xml.etree.ElementTree as ET
from lxml import etree
import random
import psutil
import sys

running = True
while(running):
    try:
        # Creates a webdriver for Firefox
        browser = webdriver.Firefox()

        # Loads the webpage from where you want to start
        file = open('town_links.txt', 'r')
        towns = file.read().split('\n')[:-1]
        file.close()
        # Creates list of towns for both election years (2006 and 2012)
        results_from_year_strings = ['tabel_uitslagen2006', 'tabel_uitslagen2012']

        for town in towns:
            #sleep(1)
            browser.get(town)
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, results_from_year_strings[1])))
            # Get name of current town and create an XML object to hold all information about that town
            town_name = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/ul/li[4]").text
            print(town_name)
            data_town = ET.Element(town_name)
            for year in results_from_year_strings:
                browser.find_element_by_xpath('//*[@id="tab_uitslagen"]').click()
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="table_statsvotes"]')))

                data_year = ET.SubElement(data_town, year)
                # Opens link for the next town and wait untill the table is loaded to make sure there are no errors




                # Get results of current town
                data_results = ET.SubElement(data_year, "results")
                element_present = EC.presence_of_element_located((By.ID, year))
                WebDriverWait(browser, 10).until(element_present)
                sleep(0.2)
                tabel2012 = browser.find_element_by_id(year)
                tbody = tabel2012.find_element_by_tag_name('tbody')
                ophalenKandidaten = False
                length = len(tbody.find_elements_by_tag_name('tr')[1:-1])
                name = ""
                for number in range(length):
                    browser.refresh()
                    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, year)))
                    tr = browser.find_element_by_id(year).find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')[number + 1]
                    if not ophalenKandidaten:
                        name = tr.get_attribute('id')
                        print(tr.get_attribute('id'))
                        data_party = ET.SubElement(data_year, tr.get_attribute('id'))
                        town_information = tr.find_elements_by_tag_name('td')
                        data_number = ET.SubElement(data_party, "number")
                        data_number.text = town_information[1].find_element_by_xpath(".//*").text
                        data_party_name = ET.SubElement(data_party, "party_name")
                        data_party_name.text = town_information[2].find_element_by_xpath(".//*").text
                        data_votes = ET.SubElement(data_party, "votes")
                        data_votes.text = town_information[3].find_element_by_xpath(".//*").text
                        data_percent = ET.SubElement(data_party, "percent")
                        data_percent.text = town_information[4].find_element_by_xpath(".//*").text
                        data_seats = ET.SubElement(data_party, "seats")
                        data_seats.text = town_information[5].find_element_by_xpath(".//*").text
                        town_information_comma = ""
                        for td in tr.find_elements_by_tag_name('td'):
                            a = td.find_element_by_xpath(".//*")
                            town_information_comma += a.text + ","
                        print(town_information_comma[1:-1])


                        #sleep(0.1)
                        ophalenKandidaten = True
                    else:

                        browser.find_element_by_id(year).find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')[number].find_element_by_tag_name('td').find_element_by_tag_name('a').click()
                        WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))
                        sleep(3)
                        tbody = tr.find_element_by_tag_name('tbody')
                        data_candidates = ET.SubElement(data_party, "candidates")
                        for tr in tbody.find_elements_by_tag_name('tr')[1:]:
                            kandidaat_informatie_comma = ""
                            candidate_information = tr.find_elements_by_tag_name('td')
                            data_candidate_number = ET.SubElement(data_candidates, "Candidate" + candidate_information[0].text)
                            data_candidate_name = ET.SubElement(data_candidate_number, "name")
                            data_candidate_name.text = candidate_information[1].text
                            data_candidate_namevotes = ET.SubElement(data_candidate_number, "namevotes")
                            data_candidate_namevotes.text = candidate_information[2].text
                            data_candidate_titular = ET.SubElement(data_candidate_number, "titular")
                            data_candidate_titular.text = candidate_information[3].text
                            data_candidate_opvolger = ET.SubElement(data_candidate_number, "opvolger")
                            data_candidate_opvolger.text = candidate_information[4].text
                            for td in tr.find_elements_by_tag_name('td'):
                                kandidaat_informatie_comma += td.text + ","
                            print(kandidaat_informatie_comma[:-1])
                        ophalenKandidaten = False

                browser.find_element_by_xpath('//*[@id="tab_statistieken"]').click()
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="table_statsvotes"]')))
                data_vote_counts = ET.SubElement(data_year, "vote_counts")
                tbody = browser.find_element_by_xpath('//*[@id="table_statsvotes"]').find_element_by_tag_name('table').find_element_by_tag_name('tbody')
                number_of_voters = tbody.find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text
                print("ingeschreven kiezers: " + number_of_voters)
                data_number_of_votes = ET.SubElement(data_vote_counts, "number_of_votes")
                data_number_of_votes.text = number_of_voters
                actual_votes = tbody.find_elements_by_tag_name('tr')[2].find_elements_by_tag_name('td')[1].text
                print("actual votes: " + actual_votes)
                data_actual_votes = ET.SubElement(data_vote_counts, "actual_votes")
                data_actual_votes.text = actual_votes
                valid_votes = tbody.find_elements_by_tag_name('tr')[3].find_elements_by_tag_name('td')[1].text
                print("valid votes: " + valid_votes)
                data_valid_votes = ET.SubElement(data_vote_counts, "valid_votes")
                data_valid_votes.text = valid_votes
                invalid_votes = tbody.find_elements_by_tag_name('tr')[4].find_elements_by_tag_name('td')[1].text
                print("invalid votes: " + invalid_votes)
                data_invalid_votes = ET.SubElement(data_vote_counts, "invalid_votes")
                data_invalid_votes.text = invalid_votes
            mydata = ET.ElementTree(data_town)
            mydata.write("towns/" + town_name + ".xml")
            towns = towns[1:]
            file = open("town_links.txt", "w")
            new_towns = ""
            for town in towns:
                new_towns += town + "\n"
            file.write(new_towns)
            print("writen file for: " + town_name)
    except KeyboardInterrupt as e:
        print('interrupted by user')
        sys.exit()
    except Exception as e:
        PROCNAME = 'firefox'

        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc.kill()
        print('error occured... running again!')
