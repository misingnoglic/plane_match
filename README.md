plane_match
===========

This was our project for Hack@1050, the hackathon at Amadeus (travel data company)

The project allows people to create accounts and use them to find people to sit with on flights, so that they can have 
a more enjoyable flight experience.

This is accomplished by having users list their interests, and then listing flights that they are going on. That way 
they can see who has already committed on going on the same flights and plan accordingly. There's also a messaging
system that's connected with sendgrid, so people can send emails to each other to coordinate their plans.

A feature that was half-baked was the idea of saying what hotel you're going to after, so that you can find people to 
share a taxi with, possibly saving 2/3rds of your expenses there. Currently all we can do is query all the hotels
near a certain airport.

This was a fairly ambitious project for all of us, since it was my first time making user registration and profiles for
people, and the first time anyone else on my team even used Python. In general the roles worked out like this.

Arya: Django backend, database stuff, answering any questions about django/python, getting page running
Sofiya: Translated pages to templates, CSS, and forms
Ari: HTML/CSS formatting on pages
Jacob: Worked on APIs to get the correct input/output

We don't have this hosted anywhere (yet), but here are some screenshots (all production working):

Home Page
![Home Page](http://i.imgur.com/W98ZSqY.png "Home Page")

User Registration
![User Registration](http://i.imgur.com/2KrW1OB.png "User Registration")

User Login
![Login](http://i.imgur.com/AsWDh3K.png)

User Profile (initially empty)
![User Profile](http://i.imgur.com/3qYI6CN.png )

Can add interests to profile by typing into textbox and clicking add
![Interests](http://i.imgur.com/zmzEiM9.png)

Interests are created as models in order to be able to query people with similar interests

Clicking "Add Flight" prompts you for info about your flight to find the right one
![Add flight](http://i.imgur.com/Hx1XHXK.png)

Supports all major US airlines
![airports](http://i.imgur.com/QxN3vMp.png)

This information is sent to the Amadeus API to get a list of flights leaving that day
![Add flight](http://i.imgur.com/idivZTe.png)
![Add flight](http://i.imgur.com/620GMes.png)

This creates a model of a flight in the database so multiple people can be on the same flight
This flight is added to the user's profile
![profile with flight](http://i.imgur.com/jP8HH8J.png)

Clicking on the flight allows you to see the profile of everyone else on that same flight
![flight profiles](http://i.imgur.com/Opbu8en.png)

You can click on a person's picture (filler for now) to view their profile and message them
![person's profile](http://i.imgur.com/NXpUQRb.png)
This is largely useless now but eventually people will be able to add more to their profiles

Messaging system (sends an email via sendgrid)
![message](http://i.imgur.com/S7SFBru.png)

We can also use the Amadeus API to get a list of hotels near the area. In the future we would like to implement a system
that allows people to find others going to the same hotel from their flight, so that they can save on taxi fees.
![hotels](http://i.imgur.com/z9dbKkY.png)

Thank you for looking at our website!
![logout](http://i.imgur.com/4vQ0gds.png)
