# rescomp-todo
2015 ResComp Programmers Workshop

[For Windows Users](#windows)<br />
[For *nix Users](#unix)<br />
[Setting up your environment](#env)<br />
[Running your app](#running)<br />

<a name="windows"></a>
## For Windows Users

Unix environments have many important advantages for developers which allow for easy development, testing and deployment of applications. For this reason, it's useful to have access to a unix-like environment. [Cygwin](https://www.cygwin.com/) provides a native unix-like environment for Windows users. For this project in particular, we require git (for managing changes to your code), curl or wget (for grabbing the pip installer off the internet) and python. There are lots of other extremely useful packages in the cygwin distribution, and I encourage you to look through and install anything you want to experiment with. However, you can always re-run the installer at a later time and update the installed packages.

<a name="unix"></a>
## For *nix Users
You'll need the same packages as above (git, curl/wget, python), though many *nix flavors have some or all of these pre-installed. If you don't have them installed, you should to install them with your package manager ([Homebrew](http://brew.sh) is a good choice for Mac users)

<a name="env"></a>
## Setting up your envorinment

A robust development environment makes development of any project much simpler in the long run. Especially important is the ability to quickly prototype and test changes. It is also important for your development environment to mirror your production environment as closely as possible, so that there are no unpleasant surprises when you deploy your code.

One of the primary difficulties developers encounter when working on multiple projects is conflicting dependencies. I may have an app that depends on a legacy version of Flask, for instance, but want to start a new app with the latest version. One extremely simple solution for managing project requirements is called a virtualenv. Virtualenvs handle things like project specific packages or environment variables, so that separate apps in separate virtualenvs can run side by side.

To prepare your environment, do the following (If you already have pip installed, you should skip the first two steps):
```
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
python get-pip.py
pip install virtualenv
virtualenv todo-app
source todo-app/bin/activate
git clone https://github.com/AllanYangZhou/rescomp-todo
cd rescomp-todo
pip install -r requirements.txt
```
 (you can download the file with `wget https://bootstrap.pypa.io/get-pip.py` if your system doesn't have curl)
 
 You can check to see what packages you have installed in your virtualenv with `pip freeze`.

`curl` is a command which simply downloads a web resource. By default, curl will print the output to STDOUT (your terminal). You can't manipulate this output - it simply appears on your screen. We use the `>` character to write the output of curl to a file, get-pip.py.

`python get-pip.py` is a script which installs pip, the python package manager. We'll use pip to manage python dependencies. `pip install virtualenv` will install the virtualenv framework, which will allow you to create a project environment for your website without installing anything globally on your system.

We now create a new virtualenv with `virtualenv todo-app` (you may call it whatever you like). This will automatically create a directory called todo-app which houses your project's dependencies. Note that while your dependencies live here, your project doesn't need to! When you enter your virtualenv (source the activation script), your application will know to look for packages in this directory. `source todo-app/bin/activate` is how you enter your virtualenv. All this does is modify your environment variables to point your application to the packages in `todo-app/`. When inside a virtualenv, `pip install` will install packages into `todo-app/` rather than your global packages.

<a name="running"></a>
## Running your app

Now that everything's installed, you can run your app. To do so, you'll need to activate your virtualenv (if you don't, python will try to find the flask framework but won't know where to look). Then, `cd` into your project directory (`~/rescomp-todo` in this example) and run the server with `python todo.py`. You should be able to view the app by launching a web browser and navigating to `localhost:5000`.
