
# WhatsOnMalta Scraper

One Paragraph of project description goes here
<br>
<h4 align="left"> Try out the live demo <a href="http://vajkturi.com/whatson_scrape/" target="_blank">Link</a>.</h4>



<p float="left">
<a href="https://www.linkedin.com/in/vajkturi/"><img src="https://github.com/VTuri/readme_template/blob/master/linkedin-logo.png" alt="LinkedIn" width="60" height="60"></a> </t>
<a href="https://medium.com/@turi.vajk"><img src="https://github.com/VTuri/readme_template/blob/master/medium-icon.png" alt="Medium" width="60" height="60"></a>  
 </t> </p>




<h4 align="left"> Check out my website for demos and blog posts <a href="http://vajkturi.com/" target="_blank">VajkTuri</a>.</h4>




## What was the goal of the project?
The goal of the project is to simplify a manual task for a small Maltese company. With the help of the live application a process which took a lot of time and manual work, now can be done in a few click. 

## How does it work
The scraper runs in a docker container. It is built with Python and Selenium. The container itself waits for an API call which contains the search parametest "number" "from" and "to".  
### Usage
Simply provide the search parameters to the running container and wait for the response
### Results
A JSON response. A list of dictionaries with the following fields: "date", "event", "venue", "type" and "location"

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installing


* Clone the repository
* CD into the directory
* Build the conatiner
```
docker-compose build .
```



## Deployment

* Run the container
```
docker-compose up
```
It will run on port 5000

## Built With

* [Docker-compose](https://docs.docker.com/compose/) - Container management
* [Flask](https://www.palletsprojects.com/p/flask/) - Web application framework
* [Selenium](https://selenium.dev/) - Web automation tool



## Versioning

1.0
