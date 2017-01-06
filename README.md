<p align="center">
    <img src="https://rawgit.com/usnistgov/corr/master/corr-view/frontend/images/logo.svg"
         height="240"
         alt="CoRR logo"
         class="inline">
</p>

<p align="center"><sup><strong>
Check the platform source code at <a href="https://github.com/usnistgov/corr">usnistgov/corr</a>.
</strong></sup></p>

[![Gitter Chat](https://img.shields.io/gitter/room/gitterHQ/gitter.svg)](https://gitter.im/usnistgov/corr)


This repository is part of a effort in integrating most popular software management tools to CoRR.
The current repository is a fork of the Reprozip Code with the integration capabilities built-in.
* **[README](ABOUT)** – Original Reprozip Readme.

## Installing this version

To use this integrated version of Reprozip to CoRR, place yourself in the base of this repository and run:

    $ python setup.py install

This small tutorial on how to get started with this integrated version of reprozip of CoRR requires the
[CoRR examples](https://github.com/usnistgov/corr-examples). Please download it and install the requirements
for the project you want to run it for. Let's assume you are using: project-corr-python.

	$ cd project-corr-python

To Use Reprozip with your CoRR account. Retrieve your config file in your home page account and do:

    $ reprozip trace -config=path_to_config MyProject cmd_to_run
    
You will need the api domain and port. This is accessible through your account by downloading the 
config file. We are working to make this init part be able to load the config file.

For example, in my local development CoRR instance i have setup this way:

    reprozip trace -config=/home/fyc/config.json reprozip-python python main.py default.param

## Developers & Users

This Reprozip code is currently in development mode and is registered in a localhost instance of CoRR.
It will soon be linked to an official CoRR instance and be added as an application that users registered
could use to push their Reprozip records.

After standing an instance of CoRR, to allow users to use your version of Reprozip or any tools, you
must create your application instance in CoRR and provide the access token to the users.You will find
it on the applications dashboard.

Inform the users to place the token in the app key of the config file downloadable from their home account
view.

The aim here is to minimize many instances of the same app running. So before creating records from an app
that you provide, please ensure that this app is not provisionned already by querying its name.

## Note

This effort is part of part of CoRR flexible integration capability and includes many other software 
management tools.
