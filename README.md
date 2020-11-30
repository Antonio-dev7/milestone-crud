# Code institute - Data Centric Development Project

This is my third project of the course.
I decided to build a movie review website which allows people to review superhero movies.
I allows users to go and see add and review or delete movie reviews.


### User Experience -  How can use the App?

These are the actions the user can perform on the app.


* The user can - add a review for a movie
* The user can - search for a movie
* The user can - edit review
* The user can - delete a review
* The user can - add a review search for a movie



## Wireframes

Wireframes are attached to the folder

### Database

Database is MongoDB, and you must be able to store a review, movie name, remove files and add and edit files.

## Design

I took inspiration from movie reviews from the 1998 or so.
* Use - https://materializecss.com/color.html as a templates.
* Images come from wikipedia and and unsplash.


## Implementation
* I used several marvel movie titles and I connected to the database. 
* Used python3 and flask render tamplates and connected via URL_links to connect it to the database.
* To perform search, edit , delete , and add movies.



## Features

## Many more Potential Additional Features

* Could add users/admin
* Could get more movies and films
* Could create bigger database to accomodate users.

## Testing

Everything works on all browsers and is extremely resposive.



## Deployment

Application was deployed to Heroku. The steps for this are as follows:

1. After logging into my Heroku account, I clicked 'New' and then 'Create New App'
2. I have to give my new app a name and pick my region as Europe.
3. I had to link my GitHub repository, containing all my code, to Heroku so I clicked the 'Deploy' tab.
4. I enter the details of my account and repository to link the two.
5. I then have to enable automatic deploys, so when I push to GitHub, it deploys my code to Heroku; so I click on that.
6. I had to enable environment variables for my project, so I click on 'Settings' > 'Reveal Config Vars' and enter in the ones my project uses.
7. I have to generate a Procfile for my project, which I did by typing "echo web: python run.py > Procfile" into the terminal.
8. I had to generate a requirements file as well, which I did by typing "sudo pip3 freeze --local > requirements.txt" into the terminal.
9. I had to disable the debug environment before deployment, which I did by removing 'True' from the line in my run.py file, and replacing it with 'False'
10. Once I have these changes added and committed using git, I had to push them to my git repository using 'git push' in the terminal. This also pushed the project to Heroku, where it began automatically installing dependencies and deploying the project.


## Credits

## Content

* Book icon on navbar courtesy of Font Awesome
* Navbar font and general site font taken from Google Fonts

## Media

* wikipedia for the movie information.
* https://www.rottentomatoes.com/
* Images https://www.marvel.com/movies. / Not all images

## Code

* https://materializecss.com/color.html for the responsiveness of the page.
