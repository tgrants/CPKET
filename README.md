# CET

* Centralizētie eksāmeni
* Centralizētie profesionālās kvalifikācijas eksāmeni (CPKE)
	* Profesionālā kvalifikācija "programmēšanas tehniķis"
		* 2023
	* Profesionālā kvalifikācija "mašīnbūves tehniķis"
		* 2023 (daļa jautājumu)

Testi pieejami https://klappscheinwerfer.github.io/CET vai https://tomsgrants.com/CET

Skaidrojumi atbildēm: [Wiki](https://github.com/klappscheinwerfer/CET/wiki)

## Komandas

* Palaist web serveri testēšanai `python3 -m http.server`
* Pārveidot datus no csv uz json formātu `python3 tools/csv-to-json.py ./data/jautajumi.csv ./data/data.json`
* Iegūt jautājumu skaitu `python3 tools/get-count.py`
	* Ar opciju `-s` iespējams apskatīt neatbildētos jautājumus `python3 tools/get-count.py -s`

# Licence

Šis projekts licencēts ar MIT licenci (skat. `LICENSE`).
Projekta autori uzskaitīti failā `CREDITS.md`.