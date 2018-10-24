from selenium import webdriver

# Creates a webdriver for Firefox
browser = webdriver.Firefox()
# loads the webpage from where you want to start.
browser.get("https://www.vlaanderenkiest.be/verkiezingen2012/#/gemeente/uitslagen")

# searches for the ul where the provinces are stored, then created a list of each li in that ul.
provincie = browser.find_element_by_id('navlist')
ul_provincie = provincie.find_elements_by_tag_name('li')
# should be 5
print(len(ul_provincie))
towns_links = ""

for li_provincie in ul_provincie:
    # Clicks list open. This has to happen because otherwise the links for each town wont be there.
    li_provincie.find_element_by_xpath(".//*").click()
    # Getting the ul from a province, then created a list of each li (a town).
    ul = li_provincie.find_element_by_tag_name('ul')
    li = ul.find_elements_by_tag_name('li')
    # Work through every li and getting the href attribute out of the a tag.
    for item in li:
        town_link = item.find_element_by_tag_name('a').get_attribute('href')
        print(town_link)
        towns_links += town_link + '\n'
    print(len(li))
# creates a text file and adds all town links.
town_links_file = open("town_links.txt", "w")
town_links_file.write(towns_links)
