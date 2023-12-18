# Music Streaming Service

## Description

This application is a prototype music streaming service. The application caches music by regions and if a certain audio is called many times in another region the audio is cached to the other region aswell.

The service consists of the following stack:
-------
frontend [NextJs]https://nextjs.org/
backend [Python]https://www.python.org/
global sql data [Postgresql]https://www.postgresql.org/
regional sql data [Postgresql]https://www.postgresql.org/
regional nosql data [MongoDB]https://www.mongodb.com/


This prototype is done to demonstrate skills and knowledge about data-intensive systems.


## Installation

This project is fully dockered so there is no need for local installation.

<c>git clone https://github.com/KeManen/Data-Intensive-Project.git</c>
<c>cd ./data-intensive-project</c>


## How to start

<c>docker compose up</c>

User interface can be found at http://localhost
