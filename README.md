# Talkmore_ // keskustelu foorumi // Tietokantasovellus, kesä 2020

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


## Demo

Sovellukseen voi tutustua [Herokussa](https://tba-forum.herokuapp.com/).

![Kuvakaappaus sovelluksen etusivusta tietokoneella](https://github.com/JuusoSaavalainen/Tietokantasovellus/blob/main/static/koneelmeny.png)
![Kuvakaappaus avatusta ketjusta puhelimella](https://github.com/JuusoSaavalainen/Tietokantasovellus/blob/main/static/Screen%20Shot%202022-10-23%20at%2022.44.44.png)


## Teknologiat

Sovellus on tehty Pythonin [Flask](https://flask.palletsprojects.com/en/1.1.x/)-kirjaston avulla.
HTML-sivujen generoinnissa hyödynnetään [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)-kirjastoa. 
Ulkoasun tyylittelyyn käytetään [Bootsrappia](https://getbootstrap.com/).
Sovellus käyttää Herokussa [Postgresia](https://www.heroku.com/postgres).


