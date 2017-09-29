# devops-django

This is the repository for the devops project at [Kings Digital Lab](https://kdl.kcl.ac.uk)

This project is configured to use [Vagrant](https://www.vagrantup.com/) for local development and [Fabric](http://www.fabfile.org/) for deployment. 

## WARNING
This software is not production ready.

## About 
DevOps is a tool for simplifying all aspects of Server Management and Application Deployment.

### Features
* Automatic detection of running services
* Monitoring of server and service status
* Scheduling of maintenance tasks such as updates
* Hypervisor integration for automatioc snapshot creation and deletion
* Fully agentless operation

### Host Hardware Requirements

Hardware requirements vary based on the number of servers and services being managed, along with monitoring intervals and other settings. Generally, with default settings:
* 1 CPU Core
* 2GB RAM

per 50 servers. Adjust as necessary.

Additionally, 20GB of disk space is required on-disk for caching, logging and scratch.

### Host Software Requirements
* Ubuntu 16.04
* Apache Traffic Server, Nginx and Uwsgi
* Postgresql

## Installation

An installation script is provided in /installer/install.sh - this will install all necessary helper services
## Development

### Getting started
1. Enter the project directory: `cd devops-django`
2. Start the virtual machine: `vagrant up`
3. SSH into the virtual machine: `vagrant ssh`
4. Run the local development server: `./manage.py runserver 0:8000`

You can then access the site locally at [http://localhost:8000](http://localhost:8000)

If the project is ldap-enabled, you can login using your LDAP credentials. Note: LDAP authentication will only work within the college firewall. Alternatively, use the default superuser login:

username: `vagrant`
password: `vagrant`

Note: This login will only work on a locally deployed virtual machine.

### Requirements 
* Ansible >= 2.3
* NodeJS
* Vagrant >= 1.9
* VirtualBox >= 5.0
