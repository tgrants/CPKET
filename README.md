# CET

Centralizēto un profesionālās kvalifikācijas eksāmenu testu daļu jautājumi un to pareizās atbildes.

Testi pieejami https://tomsgrants.com/CET vai https://tgrants.github.io/CET

Skaidrojumi atbildēm [pieejami šeit](https://github.com/tgrants/CET/wiki).

> [!NOTE]
>
> Repozitorijs tiks pārsaukts uz CPKET.
> Visas saites uz repozitoriju tiks mainītas.

## Saturs

* CPKE jautājumi un pareizās atbildes
	* Profesionālā kvalifikācija "programmēšanas tehniķis"
		* 2023
		* 2025
	* Profesionālā kvalifikācija "mašīnbūves tehniķis"
		* 2023 (daļa jautājumu)

## Satura pievienošana un citi uzlabojumi

Jebkāda veida ierosinājumi un uzlabojumi ir vienmēr gaidīti.
Pirms izmaiņu veikšanas, svarīgi iepazīties ar [ieguldījumu vadlīnijām](CONTRIBUTING.md).
Neskaidrību gadījumā iespējams sazināties ar projekta uzturētājiem.

## Komandas un rīki

* Palaist web serveri testēšanai `python3 -m http.server`
* Pārveidot datus no csv uz json formātu `python3 tools/csv-to-json.py ./data/jautajumi.csv ./data/data.json`
* Iegūt jautājumu skaitu `python3 tools/get-count.py`
	* Ar opciju `-s` iespējams apskatīt neatbildētos jautājumus `python3 tools/get-count.py -s`

## Licence

Šis projekts licencēts ar [MIT licenci](https://lv.wikipedia.org/wiki/MIT_licence).
Plašāka informācija pieejama [LICENSE](LICENSE) datnē.
Projekta autori uzskaitīti [CREDITS.md](CREDITS.md).
