# Gemeenteraadsverkiezing Web Scraping #

Mijn eerste project heb ik bedacht tijdens het vak Business Intelligence. Wij kregen de opdracht om een dataset te vinden om mee aan de slag te gaan in QlikView. Ik wilde iets doen rond de verkiezingen maar een dataset was niet te vinden. Ik vond echter wel alle data op de volgende website: [Lokale verkiezingen 2012](https://www.vlaanderenkiest.be/verkiezingen2012/).

Ik heb dus besloten om een web scraper te bouwen in Python om deze data om te zetten in een mooi cvs bestand.

Ik hoop bij te leren over:
 * Web scraping
 * werken met packages in Python
 * virtual environments in Python
 * Werken met CVS bestanden in Python

Ik ga starten bij de volgende website:
 * [Practical Introduction to Web Scraping in Python](https://realpython.com/python-web-scraping-practical-introduction/)

Scraping zoals hierboven wordt uitgelegd was niet voldoende voor wat ik wilde doen. Dit zou alleen werken voor statische websites. Daarom ben ik begonnen met (https://www.seleniumhq.org/)[Selenium]. Het is een tool om browsers te automatiseren.

# Hoe heb ik het aangepakt? #

Eerst en vooral wilde ik de link naar de resultaten van elke gemeente. Hiervoor schreef ik get_links.py. Dit gaf mij de town_links.txt bestand. Hier kon ik doorgaan om de informatie te krijgen die ik nodig had per gemeente. Individuele onderdelen van de website halen bleek niet al te moeilijk zijn, en zelfs een volledige tabel eruit halen en mooi in xml gieten was niet zo moeilijk. Ik vond echter op twee moeilijkheden:
  * Ten eerste duurde het soms lang voordat een subtabel (met informatie over de voorkeurstemmen) werd geladen. Dit gaf een foutmelding omdat die een bepaald element nog niet vond. Dit heb ik op de meeste plekken kunnen oplossen via WebDriverWait. Dit kreeg ik echter alleen opgelost wanneer ik duidelijk wist op wat ik moest wachten. Dit geldde niet voor alles. Een simpele sleep() was een optie maar vertraagde het proces natuurlijk ontzettend hard.
  * Het tweede probleem was dat de website op sommige momenten zichzelf ververste waardoor mijn script natuurlijk bepaalde elementen op de pagina niet meer vond. De enige oplossing dat ik gevonden had, was om die fouten op te vangen en gewoon de applicatie opnieuw op te starten. Dit is natuurlijk geen propere manier om dit op te lossen maar met de beperkte tijd die ik had, leek me dit de enige oplossing.

Het enige dat ik nu nog moest toevoegen was een manier om de browser telkens opnieuw te sluiten wanneer er zich een fout voordeed. Dit kreeg ik opgelost door het process zelf af te sluiten. Omwille van de werkwijze werkt dit daarom alleen in Linux. Een voorbeeld hiervan staat in kill_proces.py.

Het laatste dat ik nu nog most doen is alle xml bestanden van elke gemeente samenbrengen in een mooie xml file. Dit doe ik in merge_all_xml_files.py
