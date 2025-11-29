# CPKET

Questions, correct answers, and explanations for the test sections of the Latvian centralized professional qualification exams.

Centralizēto profesionālās kvalifikācijas eksāmenu testu daļu jautājumi, pareizās atbildes un to skaidrojumi.

Testi pieejami https://tomsgrants.com/CPKET vai https://tgrants.github.io/CPKET

> [!NOTE]
>
> Projekts tika pārsaukts no CET uz CPKET.
> Lūgums atjaunināt visas saites uz repozitoriju.

## Saturs

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

* Palaist tīmekļa serveri testēšanai `python3 -m http.server`
* Pārveidot datus no csv uz json formātu `python3 tools/csv-to-json.py ./data/jautajumi.csv ./data/data.json`
* Iegūt jautājumu skaitu `python3 tools/get-count.py`
	* Ar opciju `-s` iespējams apskatīt neatbildētos jautājumus `python3 tools/get-count.py -s`
* Salīdzināt atbildes divu testu vienādiem jautājumiem `python3 tools/compare.py file1 file2`

## Licence

Šis projekts licencēts ar [MIT licenci](https://lv.wikipedia.org/wiki/MIT_licence).
Plašāka informācija pieejama [LICENSE](LICENSE) datnē.
Projekta autori uzskaitīti [CREDITS.md](CREDITS.md).
