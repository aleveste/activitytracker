# Activitytracker

Sovellus luo yhteisön niille, jotka ovat kiinnostuneita kuntoilemisesta, missä käyttäjät voivat lähettää omat urheilusuorituksensa muiden nähtäväksi.

Ominaisuudet:

* Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
* Etusivulla käyttäjä näkee kaikista viimeisimmät suoritukset, sekä kaikki sovelluksen toiminnallisuudet.
* Käyttäjä voi sovelluksessa lisätä profiiliinsa erilaisia urheilusuorituksia, joita muut voivat hänen profiilistaan katsoa.
* Myös ryhmillä ja tapahtumilla ovat omat sivut, mistä voi nähdä osallistujien määrät ja ryhmien tapauksissa myös jäsenien päivitykset.
* Hakutoiminto auttaa muiden käyttäjien, ryhmien ja tapahtumien löytämistä.
* Käyttäjä voi luoda ryhmän liittyen tiettyyn liikuntamuotoon tai alueseen, johon muut voivat liittyä vapaasti.
* Ylläpitäjä voi luoda tapahtumia, minne käyttäjät voivat ilmoittautua.

Nykyinen tilanne: 

7.4 Sovellukseen voi kirjautua sekä tehdä uusia julkaisuja, vielä tekemättä ovat kavereiden haku, ystävät, ja ryhmät. Nykyinen versio on mallinnettu keskusteluesimerkin avulla joka antaa sille hyvän pohjan, mistä voi seuraavaan palautukseen parannella ja muuntaa sovellusta sen oikeaan käyttötarkoitukseen.

21.4 Profiilisivu lisätty, ryhmän ja tapahtuman luonti lisätty, etsintä lisätty. Tekemättä vielä ylläpitäjän rooli, ryhmien/tapahtumien etsintä ja etusivu ja sivujen ulkonäkö.

5.5 Ominaisuudet jotka ovat listattu ovat kaikki sovelluksessa toimivia. Hieman muutoksia toiminnallisuuteen alkuperäisestä ajatuksesta. Ylläpitäjän roolin saa käyttäjälle painamalla ylläpitäjä-nappia.

Sovellusta voi testata kloonaamalla repositorio, luomalla .env minne lisätään DATABASE_URL ja SECRET_KEY, jonka jälkeen suoritetaan seuraavat komennot:

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r ./requirements.txt

$ psql < schema.sql

$ flask run
