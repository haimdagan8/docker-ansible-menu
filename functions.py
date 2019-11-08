import os
from time import sleep
import docker


client = docker.from_env()

def installations():
    os.system('sudo apt-get update -y && apt-get install curl -y && curl -fsSL https://get-docker.com/ -o get-docker.sh && sh get-docker.sh && apt-get install ansible -y')
    print("Installation completed !!")

def edit_hosts():
    f = open("/etc/ansible/hosts" ,"w")
    boolean = 0
    ip_list = []
    while boolean == 0:
        x = input("1.Add IP\n2.Save file\n3.Return to main menu\n")
        if x == "1":
            ip_list.append(input("Enter IP's : "))
        elif x == "2":
            f.write("[all-hosts]\n" + '\n'.join(ip_list))
            f.close()
            print("Hosts file edited !")
            os.system('cat /etc/ansible/hosts')
            boolean = 1
        elif x == "3":
            boolean = 1

def pull_image():
    global client
    x = input("Enter image : ")
    image = client.images.pull(x + ":latest")
    print(image.id)
    print("Image successfully pulled.")


def run_container():
    global client
    PORTS_DICT = {}
    y = input("Enter image name of container would you like to run : ")
    p = input("Enter port  : ")
    PORTS_DICT[p] = p
    container = client.containers.run(y + ":latest", detach=True, ports=PORTS_DICT)
    print(container.id)

def custom_image():
    global client
    f = open("Dockerfile" ,"w")
    image = input("Enter image : ")
    f.write("FROM " + image + ":latest")
    f.close()
    boolean = 0
    f = open("Dockerfile" ,"a")
    while boolean == 0:
        x = input("1.Enter command\n2.Finish the image\n")
        if x == "1":
            command = input("Enter command : \n")
            f.write("\nRUN " + command )
        elif x == "2":
            f.close()
            boolean = 1
    client.images.build(path="./")

def ad_hoc():
    command = input("Enter command \n")
    os.system('ansible all-hosts -i /etc/ansible/hosts -m shell -a ' + '"' + command '"')