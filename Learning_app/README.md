# Learning App #

Met deze applicatie wil ik mezelf helpen met leren. De bedoeling is dat een gebruiker zelf vragen en de daarbij horende oplossingen kan ingeven. Hij kan dan vragen aan de applicatie om bevraagd te worden. Dit kan op verschillende manieren maar het zal meestal gebeuren via meerkeuze vragen. De applicatie zal, naarmate dat de gebruiker vaker de app gebruikt, beter begrijpen wat de gebruiker nog niet goed onder de knie heeft. De applicatie moet dus proberen te achterhalen wat de gebruiker nog niet goed kent en dat ondervragen.

De gebruiker moet ook context kunnen geven over de vraag, zodat hij gerichter kan oefenen. Bijvoorbeeld, de gebruiker heeft zowel vragen over geschiedenis als vragen over netwerken in de applicatie gestoken. Maar hij wilt nu alleen zijn kennis testen over netwerken, dan kan hij dit aangeven. Een vraag kan ook onder meerdere onderwerpen vallen. De vraag "Wanneer werd Frans Ferdinand vermoord?" kan dan bijvoorbeeld de volgende onderwerpen bevatten: Oostenrijk, Eerste Wereldoorlog, Geschiedenis.

De gebruiker moet ook aangeven wat voor antwoord de vraag verwacht. Het antwoord op de bovenstaande vraag is bijvoorbeeld 28 juni 1914. Dit is een datum. Om tijdens de meerkeuze interessantere keuzes te geven is het interessant om andere datums uit de lijst van vragen te halen. Hiervoor is het dus belangrijk dat het programma weet wat voor antwoord dat er gegeven is. Een aantal andere voorbeelden van soorten antwoorden zijn: Namen, plaatsnamen, voorwerp, enz...

Om te achterhalen wat de gebruiker minder goed in is, zullen drie gegevens worden bewaard over elke vraag: Hoe vaak de vraag is beantwoord, hoe vaak de vraag correct is beantwoord, en hoe lang het geleden is dat het antwoord bevraagd is. De combinatie van deze drie zaken kan een goede indicatie geven in hoe goed de vraag gekend is. Er moet logica geschreven worden die deze drie indicatoren gebruikt om een aantal vragen te genereren uit de pool. 

Een paar voorbeeld vragen staan in list_questions.csv. Deze lijst zal ik naarmate ik mijn programma ontwikkel, blijven aanvullen met meerdere vragen zodat ik de applicatie goed kan testen.

Opgesommend moet er voor een vraag de volgende informatie bewaard blijven:
  * De vraag
  * het antwoord
  * Het soort antwoord
  * De onderwerpen waarbij de vraag hoort
  * aantal keer beantwoord
  * aantal keer correct beantwoord
  * laatste keer bevraagd

Om dit voor elkaar te krijgen moet ik leren werken met het volgende:
  * Werken met databanken in Python
  * GUI schrijven in Python (in Qt)
  * parsing van CSV bestanden (om lijst van vragen in het programma te steken)

