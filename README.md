# Dinopark Zone State

## How to set up and run the code

* To run the code you will need Python installed and virtualenv (`pip install virtualenv`)
* cd to `dinopark` and then execute `source ./venv/bin/activate`. This will create your isolated Python Environment.
* To run the code, `cd backend` on Terminal and execute `FLASK_APP=api.py flask run`. This will start start your server.
* Go to your browser and enter the following URL: `http://127.0.0.1:5000/dinopark/state/?time=2019-07-27T10:06:38.930Z` (if your port is 5000).
* Using the inspect tool you will see the response in the Network tab.

## How I approached the problem

It was apparent to me early on that there were quite a few components to the project that needed to be thought through. I initially drew out the problem on paper, highlighting the important components such as time, dinosaurs that were herbivores, what was needed to generate the grid.

I then started off constructing my data structures for my algorithm that contained the state of the park after every given event. I started off working on the maintenance component and then worked on the dinosaurs, first adding and removing them, then checking location and feeding.

Once I had built my simulation of the state of the park, I built the component that would represent which zones were safe and had maintenance due. Finally I used Flask to include the HTTP request and response.

## What you would do differently if you had to do it again

Smaller increments with included Unit tests. I would probably reconsider my nested data structure too. I would also make use of the webhook and cache log data so that it isn't always loaded fully. 

## What you learned during the project

Dealing with a lot of different data can be confusing and needs to be thought through carefully. Made some silly mistakes with mutating my dict on the way and had to debug. Naming things well and structuring code well from the beginning is so important to make everything easier to reason about.

## How you think we can improve this challenge
Representing data of this problem is quite challenging but really great for problem solving. The downside is it doesn't leave much time to show off other skills one might have, or include things such as tests. Maybe tell candidates that they can use more than 2-4 hours. Otherwise a really cute, fun project :)
