# AIops-starterkit

**PagerDuty AIops starter kit** _A 2023 Hackweek project_

## Core Goals

-   To help customers quickly deploy sample Automation Actions within their AiOps environment.
-   To showcase and stimulate thinking around what's possible.
-   To help drive lower resolution times by introducing Automation early.

## Deployment Method

The application utilizes the PagerDuty API to deploy a number of sample Automation Actions. These can be scoped to one or more services and assigned to a runner, the component hosted within a customer environment. Learn more about the runner [here](https://www.pagerduty.com/docs/guides/dispatch/runners/).

The application is designed to run either:

-   Standalone
-   As a Docker image

It could be easily deployed on a website (or Github repo).

## Core Technologies

-   PagerDuty API
-   Python 3
-   Flask

The actions are contained in the configuration directory and can be easily modified.

## Installation

### Docker

1.  Pull the Docker image from the registry:


`docker pull pagerduty/aiops-starterkit` 

2.  Run the container:


`docker run -d -p 5000:5000 pagerduty/aiops-starterkit` 

### Manual

1.  Clone the repository:


`git clone https://github.com/pagerduty/aiops-starterkit.git` 

2.  CD to the repository:


`cd aiops-starterkit` 

3.  Install the prerequisites:

Copy code

`pip install -r requirements.txt`

