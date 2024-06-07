# docker_network

=======================================Task========================================

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

================================== Demonstartion ======================================
- Demonstrate how you configure two-way traffic rules between the two farthest hosts of your network with a script to the floodlight API.
- Demonstrate that your script works by ping between the two hosts for which you created the rules.

* To start the Docker compose run: 

command for docker:
command for script: 
sudo -s
cd /home/kristiyana/Mininet_project/docker_network
mn --custom MininetScript.py --topo mytopo --test pingall

======================================= END ============================================

*The project has been properеd for New Bulgarian University, course: "Introduction to Network Engineering – part II", teacher: Nikolay Milovanov, student : Kristiyana Stoyanova.



