import functions

boolean = 0
while boolean == 0:
    OPTION = input("Menu :\n    1.Install Docker + Ansible.\n    2.Edit Ansible's hosts file.\n    3.Pull image from "
                   "Docker Hub.\n    4.Create custom image and build it.\n    5.Run a Container.\n    6.Push an image to "
                   "Docker Hub.\n    7.Remove an image.\n    8.Run a single "
                   "command on hosts.\n    9.Exit.\n")
    if OPTION == "1":
        functions.installations()
        boolean = 1
    elif OPTION == "2":
        functions.edit_hosts()
        boolean = 1
    elif OPTION == "3":
        functions.pull_image()
        boolean = 1
    elif OPTION == "4":
        functions.custom_image()
        boolean = 1
    elif OPTION == "5":
        functions.run_container()
        boolean = 1
    elif OPTION == "6":
        functions.push_image()
        boolean = 1
    elif OPTION == "7":
        functions.remove_image()
        boolean = 1
    elif OPTION == "8":
        functions.ad_hoc()
        boolean = 1
    elif OPTION == "9":
        boolean = 1