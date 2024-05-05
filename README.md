# Activitytracker

Sovellus luo yhteisön niille, jotka ovat kiinnostuneita kuntoilemisesta, missä käyttäjät voivat lähettää omat urheilusuorituksensa muiden nähtäväksi.

Ominaisuudet:

* Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
* Etusivulla käyttäjä näkee kavereidensa viimeisimmät suoritukset. 
* Käyttäjä voi sovelluksessa lisätä profiiliinsa erilaisia urheilusuorituksia, jotka hän voi myös jakaa muiden (kavereiden) nähtäväksi. 
* Käyttäjä voi luoda ryhmän liittyen tiettyyn liikuntamuotoon tai alueseen, johon voi liittyä joko vapaasti tai kutsun kautta.
* Omalta sivulta käyttäjä näkee yhteenvedon omista suorituksista, sekä voi asettaa tavoitteita eri aikaväleille. 
* Ylläpitäjä voi luoda tapahtumia, minne käyttäjät voivat ilmoittautua.
* Ylläpitäjä voi jakaa uutisia sovellukseen liittyvistä asioista ja uusista tapahtumista.

Nykyinen tilanne: 

7.4 Sovellukseen voi kirjautua sekä tehdä uusia julkaisuja, vielä tekemättä ovat kavereiden haku, ystävät, ja ryhmät. Nykyinen versio on mallinnettu keskusteluesimerkin avulla joka antaa sille hyvän pohjan, mistä voi seuraavaan palautukseen parannella ja muuntaa sovellusta sen oikeaan käyttötarkoitukseen.

21.4 Profiilisivu lisätty, ryhmän ja tapahtuman luonti lisätty, etsintä lisätty. Tekemättä vielä ylläpitäjän rooli, ryhmien/tapahtumien etsintä ja etusivu ja sivujen ulkonäkö.

Sovellusta voi testata kloonaamalla repositorio, luomalla .env minne lisätään DATABASE_URL ja SECRET_KEY, jonka jälkeen suoritetaan seuraavat komennot:

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r ./requirements.txt

$ psql < schema.sql

$ flask run
