[![Docker build](https://github.com/pranavkakde/SeleniumPythonBDD/actions/workflows/docker-image.yml/badge.svg)](https://github.com/pranavkakde/SeleniumPythonBDD/actions/workflows/docker-image.yml)

# SeleniumPythonBDD
This is a BDD Test Automation framework written in Python and Selenium. It generates html reports using Allure. This framework uses `behave` module for BDD tests.

- [SeleniumPythonBDD](#seleniumpythonbdd)
  - [Components](#components)
  - [Install dependencies](#install-dependencies)
  - [Run tests command line](#run-tests-command-line)
    - [Run tests without Selenium Grid](#run-tests-without-selenium-grid)
    - [Run tests with Selenium Grid](#run-tests-with-selenium-grid)
  - [Build project with Docker](#build-project-with-docker)
    - [Run tests without Selenium Grid](#run-tests-without-selenium-grid-1)
    - [Run tests with Selenium Grid](#run-tests-with-selenium-grid-1)
  - [Copy results from docker container](#copy-results-from-docker-container)
  - [View results using Allure](#view-results-using-allure)
  - [Start Selenium Grid](#start-selenium-grid)
  - [Start Allure Containers](#start-allure-containers)

## Components

1. **features** - contains all BDD feature files.
2. **pages** - contains all page objects.
3. **steps** - contains step definitions.
4. **environment.py** contains web driver manager.

## Install dependencies 

```powershell
# Install pip

python -m pip install --upgrade pip
```
```powershell
# Install dependencies

pip install -r requirements.txt
```

## Run tests command line

### Run tests without Selenium Grid

```powershell
python -m behave -Dbrowser=chrome -f allure -o ./reports/allure-result
```
### Run tests with Selenium Grid

```powershell
python -m behave -D browser=chrome -DgridUrl=http://<IP Address of Grid>:4444 -f allure -o ./reports/allure-result
```
> -DgridUrl argument is required only to run the tests on Selenium Grid. 

> -Dbrowser argument can only contain value from one of the these values (chrome, firefox, edge)  

## Build project with Docker

```powershell
docker build -t pranavkakde/seleniumframeworkpython . 
```

### Run tests without Selenium Grid

```powershell
docker run --name seleniumpy-test-run pranavkakde/seleniumframeworkpython:latest -Dbrowser=firefox -f allure -o /app/reports/allure-result
```

### Run tests with Selenium Grid

```powershell
docker run --name seleniumpy-test-run pranavkakde/seleniumframeworkpython:latest -Dbrowser=firefox -DgridUrl=http://<IP Address of Grid>:4444 -f allure -o /app/reports/allure-result
```

## Copy results from docker container

```powershell
docker cp seleniumpy-test-run:/app/reports/allure-result ./reports
```

## View results using Allure

```
http://<IP address of docker host>:5252/allure-docker-service-ui/projects/default
```

## Start Selenium Grid

> Pre-requisite - Install Docker Desktop

For setting up selenium grid using docker run;

```powershell
docker-compose -f docker-compose-grid.yaml -p selenium-grid-python up -d
```

Selenium Grid Url

```
http://<IP Address of docker host>:4444
```

## Start Allure Containers

1. Start Allure docker containers

```powershell
docker-compose -f docker-compose-allure.yaml -p allure-report up -d
```

2. View Allure reports

```
http://<IP Address of docker host>:5252/allure-docker-service-ui/projects/default
```
