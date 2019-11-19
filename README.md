# elevador_project
The goal of this project was to create a temporary website for Elevador.

![Elevador logo](https://github.com/Jethet/elevador_project/blob/master/placeholder/static/images/elevador_logo.jpg)

Elevador is an initiative in Barcelona that offers an open, safe space to people who want to organize events, small exhibitions, music activities, workshops etc. It is important that people can find Elevador online. Since my skills in building websites are still limited, the goal is to build a 'placeholder' website for now. This temporary website will be replaced by something more advanced in the future.

The initial idea was to create:

* a home page with general information, a nice background picture and some smaller pictures that give a good impression
* a form to contact Elevador
* deploying the website with Heroku (domainname elevador-bcn.es is available)

The current project includes a bit more:

* Home page (general description, pictures, sidebar for navigation)
* About page with more information regarding the concept and practical info on the Elevador space and resources
* Gallery with photos from past activities
* Contact page with contact details, directions and map (OpenStreetMaps), opening hours, a 'Contact us! Send email' button with mailto functionality, and links to the Elevador account on Meetup.
* Code of Conduct: on every page there is a link to the Code of Conduct, instead of having a separate page for this. The idea is that people will see (and hopefully read) the CoC quicker.

Future ambition is to link the Meetup calendar to the website so that new events that are created in Meetup will automatically show on the website.

The website is built with Python and Django, using HTML and some Bootstrap elements. As initial database, Django's dbsqlite3 is used. The website is deployed on Heroku and is accessible under the elevador-bcn.es URL.

Isues to solve: 
* Some pictures do not load or load very slow. This has been improved by changing from png to jpg format, but is still not as fast as I would like. Also, I'd like to have them in the same format.
* The sidebar with navigation almost disappears on smaller screens. I specifically chose this sidebar to avoid too much of a 'bootstrap' look, and would really like to keep it. 

