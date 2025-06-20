# Ieguldījumu vadlīnijas

Jebkāda veida uzlabojumi ir vienmēr gaidīti.
Pirms izmaiņu veikšanas vēlams rūpīgi izlasīt šo dokumentu.

Pirms būtisku izmaiņu veikšanas jāsazinās ar projekta uzturētājiem.
Ja izmaiņas nav saskaņotas, tās var netikt pieņemtas.

## Darbplūsma

### Zaru struktūra

Mēs izmantojam vienkāršu zaru struktūru:
- **main**: Galvenais zars. Tam vienmēr būtu jāsatur strādājošs un pārbaudīts kods.
- **izmaiņu zari**: Jaunas funkcionalitātes pievienošana vai labojumi būtu jāveic atsevišķos zaros.

#### Zaru nosaukumi
- **Uzlabojumi** feature/short-description (piemēram, feature/correct-solution-explanations)
- **Labojumi** fix/short-description (piemēram, fix/json-formatting)

### Ziņojumi (*issues*)

Pieejamas 3 ziņojumu veidnes tipiskiem gadījumiem:
- Problēmziņojums (*bug report*)
- Satura labojums (*content fix*)
- Funkcionalitātes pievienošanas ziņojums (*feature request*)

Ja neviens no dotajiem ziņojumu veidiem neder, iespējams to izveidot bez veidnes.
Pirms ziņojumu izveides vēlams pārskatīt esošos, lai novērstu duplikātus.

### PR (*Pull request*) process

- Izveido savu zaru (*fork*) šim repozitorijam
	- Klikšķini uz **Fork** pogas [šī repozitorija lapas](https://github.com/tgrants/CPKET) kreisajā augšējā stūrī
	- Šī darbība izveidos repozitorija kopiju zem Jūsu GitHub konta
- Klonē repozitoriju no **sava *fork***
	- `git clone https://github.com/tgrants/CPKET.git`
	- `cd CPKET`
- Izveido zaru savām izmaiņām
	- `git checkout -b feature/feature-name`
- Veic izmaiņas
	- `git add .`
	- `git commit -m "Description of the change"`
- Pievieno veiktās izmaiņas savam repozitorijam
	- `git push origin feature/your-feature-name`
- Kad viss gatavs, izveido *pull request*

## Saturs

### Valodas

Projektā izmantojamas sekojošas valodas:
- latviešu
	- mājaslapas saturs, jautājumi un atbildes
	- dokumentācija un instrukcijas
- angļu
	- programmatūras kods un komentāri
	- Git (*commit messages*, u.c.)

### Avotu formāts

Jautājumu avoti definēti datnē `sources.json`.
Iespējams pievienot arī ārējos avotus.

### Jautājumu un atbilžu formāts

Jautājumu saraksts sastāv no atslēgu-vērtību pāriem:
- **id** - jautājuma identifikators
	- Sastāv no skatļiem, kas atdalīti ar punktiem, piem. 1.1.1
- **question** - jautājuma teksts
- **image** - saite uz jautājuma attēlu
	- Nav obligāts
- **correct** - pareizās atbildes indekss
	- Sāk skaitīt no 1
- **anwers** - atbližu sarakts
