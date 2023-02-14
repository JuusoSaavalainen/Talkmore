# :speech_balloon: Talkmore_ , Tietokantasovellus, syksy 2022

Helsingin yliopiston [Aineopintojen harjoitustyön tietokantasovellus](https://hy-tsoha.github.io/materiaali/) 

- [Tietokantarakenteen skeema](https://github.com/JuusoSaavalainen/Tietokantasovellus/blob/main/schema.sql)

## About

Harjoitustyön aiheeksi valitsin keskustelupalstan. Rekisteröityneet käyttäjät voivat luoda foorumille viestiketjuja, joihin he voivat lisätä viestejä. Käyttäjät voivat tykätä viesteistä. Käyttäjät voivat poistaa omia kommentteja. Käyttäjät voivat poistaa aloittamiaan viestiketjuja(topic). Käyttäjät voivat myös poistaa käyttäjänsä.

Viestiketjuja on mahdollista luokitella käyttämällä aihetunnisteita. Foorumin hakutoiminto mahdollistaa viestiketjujen hakemisen ketjujen kommenttejen perusteella.

Sovelluksessa jokaisella käyttäjällä on sama rooli.

## Kehitettävää

Hakutoiminto on hyvin yksipuolinen ja sitä voisi hyvin vielä laajentaa. 

Myös joitain ulkoasun valintoja voisi tehdä uudelleen käytettävyyden parantamiseksi

Aihetunnisteet eivät ole normi käyttäjän lisättävissä, tähän voisi luada ominaisuuden jolla admin voisi lisätä aiheita.

Paljon muutakin olisi mitä voisi parantaa / lisätä , esim etusivu voitaisiin totetuttaa sivuttamalla, etusivun syötettä voitaisiin rajata tunnisteilla jne.

Osa HTML tiedostoista jäivät sekaviksi niitä voisi siistiä koodin luettavuuden kannalta.

Myös käyttäjien ominaisuuksia voisi lisätä, esim kuva profiiliin.

## Demo

Sovellukseen voi tutustua [Herokussa](https://tba-forum.herokuapp.com/).

![Kuvakaappaus avatusta ketjusta puhelimella](https://github.com/JuusoSaavalainen/Tietokantasovellus/blob/main/static/tshomob.png)
![Kuvakaappaus sovelluksen etusivusta tietokoneella](https://github.com/JuusoSaavalainen/Tietokantasovellus/blob/main/static/Screenshot%202023-02-08%20at%2001-29-34%20https%20__tba-forum.herokuapp.com.png)


## Teknologiat

Sovellus on tehty Pythonin [Flask](https://flask.palletsprojects.com/en/1.1.x/)-kirjaston avulla.
HTML-sivujen generoinnissa hyödynnetään [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)-kirjastoa. 
Ulkoasun tyylittelyyn käytetään [Bootsrappia](https://getbootstrap.com/).
Sovellus käyttää Herokussa [Postgresia](https://www.heroku.com/postgres).


