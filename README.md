# docker_network

=============================Task===============================

- Install docker and get familiar with docker-curriculum: https://docker-curriculum.com/
- Get to know docker compose and the ability to compose your own stack of applications in containers 
- Read more about:
  
	mininet: https://mininet.org/

        SDN controller floodlight: https://github.com/floodlight/floodlight

- Write an example mininet python script that creates a network with a topology from <XYZ> the switch and <YX> host connected in a topology of your choice.

X - the penultimate digit of your faculty number;

Y - the first digit of your faculty number;

Z - the last digit of your faculty number;

*In our scenario 519 switches and 15 host 

- Create your own docker-compose setup into the GitHub repo, which should contains:
  
+ mininet
  
+ floodlight

+ mininet python script

=========================== Demonstartion ===============================
- Demonstrate how you configure two-way traffic rules between the two farthest hosts of your network with a script to the floodlight API.
- Demonstrate that your script works by ping between the two hosts for which you created the rules.

* To start the Docker compose run: 


command for docker:

sudo apt-get update
sudo apt install docker.io
sudo docker run hello-world //to confirm that the docker is working
sudo docker images //list all of the available docker images 
sudo docker ps -a //lists all of the available running images 


From docker hub we need to select one of the floodlight images 
https://hub.docker.com/search

-depending of the usage you can select one, in my project I have selected latarc/floodlight

docker pull latarc/floodlight
sudo docker images

docker run -d -p 6653:6653 -p 8080:8080 --name=floodlight latarc/floodlight
docker start floodlight 
sudo docker ps -a

lsb_release -a  //to check the operation system version 

sudo apt-get install mininet

mn -- custom MininetScript.py --topo mytopo --conroller=remote
exit
docker stop floodlight 

========================= END =================================

*The project has been properеd for New Bulgarian University, course: "Introduction to Network Engineering – part II", teacher: Nikolay Milovanov, student : Kristiyana Stoyanova.



