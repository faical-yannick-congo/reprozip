<p align="center">
    <img src="https://rawgit.com/usnistgov/corr/master/corr-view/frontend/images/logo.svg"
         height="240"
         alt="CoRR logo"
         class="inline">
</p>

<p align="center"><sup><strong>
Access the platform docs at <a href="http://corr.readthedocs.io/en/latest/rst/README.html">readthedocs/corr</a>.
</strong></sup></p>

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
    
You will need an application toke. To have one, you can either create an app instance in your dashboard or
use the token of a pre-existing app accessible through query. In your config file place the token in the value
of the key: app. Your config file should look like the following:

```
{
    "default": {
        "api": {
            "host": "https://localhost",
            "key": "7b37a3ff1184cb4f5ae04b3b175cfb6a63d2c6843ed051ccebfa87d8b35df4f4",
            "path": "/corr/api/v0.1",
            "port": 5100
        },
        "app": "b6edbb796704956a78cc91a4a83e46b689f578f0ee1785170b097de68747bf0a"
    }
}
```
In this case the app token is: b6edbb796704956a78cc91a4a83e46b689f578f0ee1785170b097de68747bf0a.
Your account access api key is: 7b37a3ff1184cb4f5ae04b3b175cfb6a63d2c6843ed051ccebfa87d8b35df4f4.

For example, in my local development CoRR instance i have setup this way:

    $ reprozip trace -config=/home/fyc/config.json reprozip-python python main.py default.param

By running reprozip trace you allow the tool to identify itself as the instance app token provided
and push content to your account space.

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
