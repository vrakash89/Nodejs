# Nodejs
Asignment

node-js-getting-started
## Requirements

For development, you will only need Node.js and a node global package, Yarn, installed in your environement.

### Node
- #### Node installation on Windows

  Just go on [official Node.js website](https://nodejs.org/) and download the installer.
Also, be sure to have `git` available in your PATH, `npm` might need it (You can find git [here](https://git-scm.com/)).

- #### Node installation on Ubuntu

  You can install nodejs and npm easily with apt install, just run the following commands.

      $ sudo apt install nodejs
      $ sudo apt install npm

- #### Other Operating Systems
  You can find more information about the installation on the [official Node.js website](https://nodejs.org/) and the [official NPM website](https://npmjs.org/).

If the installation was successful, you should be able to run the following command.

    $ node --version
       NODE_VERSION 20.6.1
    $ npm --version

If you need to update `npm`, you can make it using `npm`! Cool right? After running the following command, just open again the command line and be happy.

    $ npm install npm -g

###
### Yarn installation
  After installing node, this project will need yarn too, so just run the following command.

      $ npm install -g yarn

---

## Install

    $ git clone https://github.com/YOUR_USERNAME/PROJECT_TITLE
    $ cd PROJECT_TITLE
    $ yarn install

## Configure app

Open `a/nice/path/to/a.file` then edit it with your settings. You will need:

- A setting;
- Another setting;
- One more setting;

## Running the project

    $ yarn start

## Simple build for production
   $ yarn build

## Created a dockefile file for the nodejs application

## Created a shell script named as docker-entrypoint.sh

## Updated the dockerfile
COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

CMD [ "node" ] 

## Docker installed locally on Ubunutu

## build the dockerfile for nodejs application
sudo docker build -t app/nodeapp .

## Run the image for for nodejs application
sudo docker run -p 5001:5001 -td app/nodeapp
## Prepared a docker-compose.yaml file with Loki, Grafana, Promtail, and nodeJS application
## To run the nodejs application use below command
sudo docker compose up
## Tryed accesing the application is accessible
## Tried below commands and follows the logs
sudo docker compose down
sudo docker compose removed
sudo docker compose up
## Able to access the grafana,promatil and Loki with specific port which are asigned on docker compose file.
## Named on grafana with job-log and container-logs able to see the  application logs are generated

