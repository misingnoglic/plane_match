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

![Home Page](http://i.imgur.com/W98ZSqY.png "Home Page")

