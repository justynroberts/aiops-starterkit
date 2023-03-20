# AIops Starter Kit

**PagerDuty AIops starter kit** _A 2023 Hackweek project by Justyn Roberts (jroberts@pagerduty.com) & Constant Fischer(cfischer@pagerduty.com)_

## Core Goals

-   To help customers quickly deploy sample Automation Actions within their AiOps environment.
-   To showcase and stimulate thinking around what's possible.
-   To help drive lower resolution times by introducing Automation early.

## Deployment Methods

The application utilizes the PagerDuty API to deploy a number of sample Automation Actions. These can be scoped to one or more services and assigned to a runner, the component hosted within a customer environment. Learn more about the runner [here](https://www.pagerduty.com/docs/guides/dispatch/runners/).

The application is designed to run either:

-   Standalone
-   As a Docker image via docker-compose or directly from the container repository

It could be easily deployed on a website (or Github repo).

## Core Technologies

-   PagerDuty API
-   Python 3
-   Flask

The actions are contained in the configuration directory and can be easily modified.

## Prerequisites

you MUST have a runner installed as per https://www.pagerduty.com/docs/guides/dispatch/runners/


## Installation

### Docker - Compose
1.  Clone the repository:


`git clone https://github.com/justynroberts/aiops-starterkit.git` 

2. To start

`docker-compose up`

3. To stop

### Docker - Direct from Repo

1.  Pull the Docker image from the registry:


`docker run public.ecr.aws/s4g5u2s4/aiops-starterkit:latest` 


### Run Manually

1.  Clone the repository:


`git clone https://github.com/justynroberts/aiops-starterkit.git` 

2.  CD to the repository:

`cd aiops-starterkit/application` 

3.  Install the prerequisites:

Copy code

`pip install -r requirements.txt`

Run the application

`python3 main.py`

Thats it. Simple. Default port is 5001

### Included Jobs:

Category

- Diagnostics - Node.js Health
- Diagnostics - Docker Health
- Diagnostics - System Config
- Diagnostics - System Health Check.
- Python script - System Health Chec
- Troubleshooting - Displays Alert Payloa
- Troubleshooting - Runner Basic Information
- Ansible - Playbook
- Ansible - Simple Command
- Diagnostics - AWS EC2 Instance Health Check
- Diagnostics - Docker Container Health Check
- Diagnostics - Kubernetes Health Check
- Diagnostics - Network Connectivity Check
- PagerDuty API - Add Alert Description to Incident Note
- PagerDuty API - Sends Incident Details via Email.
- Framework - Restart Service

### Future Plans.
At the moment the PagerDuty API is used. This could be modified for Terraform in the future
A Runner Configuration could also be built
