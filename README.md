**** CareWatch ****


~ Registratie pagina.
	User moet eerst registreren voordat hij kan inloggen
	Na registratie wordt in de database alle informatie gechecked, mocht de email adres er al instaan wordt dat gemeld
	anders wordt het in de database gezet

~ User login.
	Als het in de database staat kan de user inloggen waarbij hij meerder functies kan selecteren en verschillen sensoren die de gebruiker kan instellen.
	Functies:
		~ Informatie
		~ Agenda
		~ Medical ( Medicijnen, artsen e.d )
		~ Reminders 
	Sensoren:
		~ Heartbeat
		~ Temprature
		~ Knop op raspberry pi
	 	( Andere sensoren kunnen eventueel toegevoegd worden)

~ Alarmcentrale Login
	Alarm centrale zal moeten inloggen met extra beveiliging door middel van een pincode
	Mocht de alarm centrale medewerker ingelogd zijn heeft deze toegang tot alle users.
	Als de user dan op een knop drukt op zijn/haar watch gaat er door middel van een API een bericht naar de database
	intussen staat een stukje ajax constant te vragen of er wat is, komt er dan iets binnen dan komt dit terecht op het alarm landing page.
	Ook heeft deze toegang tot het inzien van geschiedenis betreffende alarm meldingen en ingestelde sensoren


~ Database
	Hier wordt de  volgende data opgeslagen na registratie van de user
	Eerst wordt er een id gegenereert, dan wordt de data opgeslagen in de naw gegegvens
		~ Voornaam
		~ Achternaam
		~ Adres
		~ Username
		~ Wachtwoord
		~ En andere eventuele informatie


~ Raspberry PI
	In de python scripts staat beschreven wat iedere functie doet
	Ook is ingesteld dat bepaalde script opstarten als de raspberry is opgestart
			etc/rclocal <- verschilt per device en beschrijving hiervan is makkelijk te vinden

Eventuele link om een launcher te creeren.
http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/