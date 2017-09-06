# Ars Item Catalog App Deployed on Linux Server
This is the Item Catalog app which allows the user to sign in with Google or Facebook profile and allows to perform CRUD functionality on the app.

# Accessing the app

This app is hosted on Amazon's Lightsail Linux Server Instance.

The app is available on the following URL:
http://ec2-13-126-197-223.ap-south-1.compute.amazonaws.com/

or

Public IP : http://13.126.197.223/


### Git

If you don't already have Git installed, [download Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.

On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash).  
(On Mac or Linux systems you can use the regular terminal program.)

You will need Git to install the configuration for the VM. If you'd like to learn more about Git, [take a look at our course about Git and Github](http://www.udacity.com/course/ud775).


## Fetch the Source Code and VM Configuration

**Windows:** Use the Git Bash program (installed with Git) to get a Unix-style terminal.  
**Other systems:** Use your favorite terminal program.

From the terminal, run:

    git clone https://github.com/VirtuosArs/ARS_ItemCatalog.git arsItemCatalog

This will give you a directory named **arsItemCatalog** complete with the source code. 

## Run the virtual machine!

Using the terminal, change directory to oauth (**cd arsItemCatalog**), then type **vagrant up** to launch your virtual machine.


## About the Project

* In this project I have took a baseline installation of a Linux distribution on a virtual machine and prepare it to host the Item catalog web application, to include installing updates, securing it from a number of attack vectors and installing/configuring web and database servers.
* `SSH` (port 2200)
* `HTTP` (port 80)
* `NTP` (port 123)


## Steps Followed

1. Create your Virtual Machine with Amazon Web Services.
2. Create a new user and grant sudo permissions (information on this step can be found in the Udacity Course, [Linux Security](https://classroom.udacity.com/nanodegrees/nd004/parts/ab002e9a-b26c-43a4-8460-dc4c4b11c379).
3. Update all currently installed packages.
4. Configure the local timezone to UTC (use sudo dpkg-reconfigure tzdata).
5. Change SSH port to 2200.
6. Configure firewall to only allow incoming for ssh (port 2200), http (port 80), and ntp (port 123).
7. Install and configure Apache to serve a Python mod_wsgi appliction. Helpful instructions at [DigitalOcean Tutorial](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps).
8. Pip install postgresql and sqlalchemy and any other modules needed.
9. Configure postgresql to not allow remote connections and create a new user that has limited permissions (CRUD).
10. Install git on the remote server and clone this project to the project folder on the remote server. Info on doing this on the GitHub Site. You'll need to replace keys in the application with your own keys.