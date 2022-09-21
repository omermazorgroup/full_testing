# Full Testing Project
## by Omer Mazor

In this project I created a tests for bookstore website both UI and API:

## Introdaction
First download the docker-compose-v1.yaml file 
* To start the system use `docker-compose -f docker-compose.yaml up`
* Add the `-d` flag at the end for detached execution
4 containers will start running(the first run take some time)
The swagger (API) can be found  - http://localhost:7017/swagger/index.html
The Website (UI) can be found - http://localhost/

## Tests

To run the tests first install all requirements.txt
packages
* run test_api - `python -m pytest --url http://localhost ./api/test_api.py`
* run test_ui with playright - `python -m pytest --url http://localhost --framework playwright --browser (chrome/firefox/webkit) ./playwright/test_api.py`
* run test_ui with selenium - `python -m pytest --url http://localhost --framework selenium --browser (chrome/firefox/edge) ./selenium/test_api.py`

## Results Reports 

API:

![scripts](https://res.cloudinary.com/dwsdrdv3w/image/upload/v1663797192/%D7%A6%D7%99%D7%9C%D7%95%D7%9D_%D7%9E%D7%A1%D7%9A_191_aznww8.png)

UI:

![scripts](https://res.cloudinary.com/dwsdrdv3w/image/upload/v1663797196/%D7%A6%D7%99%D7%9C%D7%95%D7%9D_%D7%9E%D7%A1%D7%9A_190_wzfalr.png)

Some tests fail becouse some timeout or 500 errors
