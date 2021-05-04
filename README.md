# Ohjelmistotekniikka, harjoitustyö

Harjoitustyö on elokuvien kirjallapito-sovellus. Käyttäjä voi etsiä elokuvia ja lisätä niitä tietokantaan. Elokuvien tiedoista löytyy esim. ohjaaja, julkaisupäivä ja imdb-rating. Halutessaan käyttäjä voi myös lisätä oman arvostelun ja katsomispäivän elokuvan tietoihin. Käyttäjä pystyy selaamaan katsomiaan elokuvian ja järjestelemään niitä niiden tietojen mukaan. 

## Nykyinen versio

Tämänhetkisen version tarkoitus on täyttää kolmannen viikon vaatimukset.

### Toiminnallisuus

Tämänhetkisessä versiossa on implentoitu käyttöliittymä, jonka avulla käyttäjä pystyy hakemaan elokuvia elokuvan nimen perusteella. Ohjelma palauttaa listaan parhaiten osuvat elokuvat ja käyttäjä voi lisätä haluamansa elokuvat omaan tietokantaan, johon tallenetaan elokuvan tiedot. Käyttäjä voi selata lisäämiään elokuvia käyttöliittymän kautta

### Käyttöohje

Ennen ensimmäistä käyttökertaa riippuvuudet tulee asentaa komennolla: 
```bash
poetry install
```
Ohjelma tulee myös alustaa ennen ensimmäistä käyttökertaa komennolla:
```bash
poetry run invoke build
```
Ohjelma suoritetaan komennolla:
```bash
poetry run invoke start
```
Testaus suoritetaan komennolla:
```bash
poetry run invoke test
```
Coverage-report luodaan komennolla:
```bash
poetry run invoke coverage-report
```
Tämän jälkeen juurihakemistosta löytyy hakemisto htmlcov/, josta voi katsoa raportin.

### Tiedetyt ongelmat

Virhetilanteet ovat edelleen huonosti käsiteltyjä, eli ohjelma pääosin olettaa kaiken toimivan hyvin ja käyttäjän olevan järkevä. Tietokannan tutkiminen on vielä alkuvaiheessa. Kolumnit eivät ole nimettyjä eikä tietokantaa pysty järjestämään tai editoida.

Etätyöpöydällä tietokanta ei toimi (locked), mutta käyttöliittymä toimii, ja ssh-melkillä tietokanta toimii, mutta käyttöliittymä ei.

Api-kutsut ovat rajoittuneet 5000:n päivässä. On epätodennäköistä, että tämä tulisi täyteen, mutta kannattaa silti ottaa huomioon. Haku vie aina yhden api-kutsun, elokuvan lisäys yhden ja testaus kolme.

## Dokumentaatio

- [Työaikakirja](./documentation/tyoaikakirja.md)
- [Vaatimusmäärittely](./documentation/vaatimusmaarittely.md)
- [Arkkitehtuuri](./documentation/arkkitehtuuri.md)
- [Käyttöohje](./documentation/kayttohje.md)

## Python-versio

Ohjelma on testattu Python-versioilla 3.6.9 ja 3.8.5. Ohjelman pitäisi pystyä toimimaan millä tahansa Pythonin versiolla joka on korkeampi kuin 3.6.0. 

## Huomioita pylintistä

Pylint tuottaa ongelmia kun muokkaan sys.pathia, jotta löytäisin omat moduulit, joten se on laitettu pois. Käyttöliittymäkoodia ei testata, sillä PyQt5 tuottaa paljon ongelmia pylintissä. 

## Viimeisin release

[Viikko 5](https://github.com/meitsin-ohte/ot-harjoitustyo/releases/tag/viikko5)
