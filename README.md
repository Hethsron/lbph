# LBPH

## Welcome to **LBPH**, Mwoo facial recognition solution !

## Features

*   Real-Time face tracking
*   Real-Time facial recognition
*   Facial character analysis
*   Facial motion capture

## Platforms

LBPH has been used on a variety of plateforms:

*   GNU/Linux
*   macOS X
*   Windows
*   Raspberry Pi 3+

## Requirements

LBPH is designed too have fairly minimal requirements to build and use with your projects, but there are somes. If you notice any problems on your platform, please notify [`Hethsron Jedaël BOUEYA`](mailto:hetshron-jeadel.boueya@uha.fr) or [`Yassine BENOMAR`](mailto:yassine.benomar@uha.fr). Patches and fixing them for welcome !

All items to be installed for this project have been simply defined in a requirement file named [`requirements.txt`](requirements.txt). This file is used to hold the result from `pip3 freeze` for the purpose of achieving repeatable installations.

## Development
For developement, before running the application, you need to create your own virtual environment on your local repository, activate it and install on it requirements, as follows :

1. Clone the `lbph` repo locally :

    ```console
        $ git clone https://github.com/Hethsron/lbph.git
    ```

2. Create your virtual environment locally :

    ```console
        $ cd lbph
        $ python3 -m venv env
    ```

3. Activate your virtual environment :

    *  On macOS X, GNU/Linux or Raspberry Pi 3+, run :

        ```console
            $ source env/bin/activate
        ```

    *   On Windows, run :

        ```console
           PS C:\> .\env\Scripts\activate
        ```

4. Install requirements :

    ```console
        $ pip3 install -r requirements.txt
    ```
    
    On Raspberry Pi 3+ only, run :

    ```console
        $ pip3 install -r requirements.1.txt
    ```

5. Run the application

    ```console
        $ python3 main.py --help
    ```

For Windows Users, before running help, it is necessary to set the excution policy to `RemoteSigned` as follows :

    ```
        PS C:\> Set-ExecutionPolicy RemoteSigned
    ```

For development, before committing the changes on the `master` branch, it is necessary to define locally a `.gitignore` file which must contain the following lines to remove byte-compiled, byte-optimized files and packaging, as follows :

    **/__pycache__
    **/[Bb]in
    **/[Dd]atasets/train
    **/[Dd]atasets/validation
    **/[Dd]ocs
    **/[Ii]nclude
    **/[Ll]ib
    **/[Ll]ib64
    **/[Mm]odels/mwoo.yml
    **/[Ss]hare
    **/[Ss]cripts
    **/env
    **/pyvenv.cfg
    **/.venv

To commit your changes and push it on `master` branch to GitHub, it is necessary to run the following commands :

    $ git add .
    $ git commit -m "Your detailed description of your changes"
    $ git push -u origin master

## Contributing change

Please read the [`CONTRIBUTING.md`](CONTRIBUTING.md) for details on how to contribute to this project.

## Work Based In Research

![LBPH based Enhanced Real Time Face Recognition](LBPH.pdf)