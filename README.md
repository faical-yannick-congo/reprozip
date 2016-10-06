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

## Additional Usage Requirement

The integration of this requirement to CoRR yielded some extra steps in using the original code.
Originally to trace a project with Reprozip, one would do:

    $ reprozip trace MyProject cmd_to_run

To Use Reprozip with your CoRR account. Retrieve your access token in your home page account and do:

    $ reprozip trace -api=http://localhost:5100/corr/api/v0.1/private/b6b458cecd92bf0f6308645d783d2a14f55e4d30c248482bbc6b82637de5c410 MyProject cmd_to_run
    
You will need the api domain and port. This is accessible through your account by downloading the 
config file. We are working to make this init part be able to load the config file.

For example, in my local development CoRR instance i have setup this way:

    reprozip trace -api=http://localhost:5100/corr/api/v0.1/private/b6b458cecd92bf0f6308645d783d2a14f55e4d30c248482bbc6b82637de5c410 reprozip-python python main.py default.param

## Developers & Users

This Reprozip code is currently in development mode and is registered in a localhost instance of CoRR.
It will soon be linked to an official CoRR instance and be added as an application that users registered
could use to push their Reprozip records.

After standing an instance of CoRR, to allow users to use this version of Reprozip, please contact me
(Faical Yannick P. Congo) or look into reprozip/reprozip/main.py and search for:

    token = "48a81007a6bda75b2543d4a0bc97e6ea6665c0e1f16237ad492f00f15a32198c"

Replace the token by the newly created application token of Reprozip produced by your CoRR instance and
provide this code to your user.

We are working to make many instances of CoRR interoperable with the same Reprozip code. So contacting me
would be the most sustainable effort.

## Note

This effort is part of part of CoRR flexible integration capability and includes many other software 
management tools.
