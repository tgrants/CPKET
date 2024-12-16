# CET

Centralizēto un profesionālās kvalifikācijas eksāmenu testu daļu jautājumi un to pareizās atbildes.

Testi pieejami https://tomsgrants.com/CET vai https://tgrants.github.io/CET

Skaidrojumi atbildēm [pieejami šeit](https://github.com/tgrants/CET/wiki).

## Saturs

* Centralizētie eksāmeni
* Centralizētie profesionālās kvalifikācijas eksāmeni (CPKE)
	* Profesionālā kvalifikācija "programmēšanas tehniķis"
		* 2023
		* 2025
	* Profesionālā kvalifikācija "mašīnbūves tehniķis"
		* 2023 (daļa jautājumu)

## Komandas / rīki

* Palaist web serveri testēšanai `python3 -m http.server`
* Pārveidot datus no csv uz json formātu `python3 tools/csv-to-json.py ./data/jautajumi.csv ./data/data.json`
* Iegūt jautājumu skaitu `python3 tools/get-count.py`
	* Ar opciju `-s` iespējams apskatīt neatbildētos jautājumus `python3 tools/get-count.py -s`

# Licence

Šis projekts licencēts ar MIT licenci (skat. `LICENSE`).
Projekta autori uzskaitīti failā `CREDITS.md`.
