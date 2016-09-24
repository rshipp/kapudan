# Kapudan

A fork of Pardus's "Kaptan", for Chakra.

## License

GPLv2 (please read the COPYING file)

## Dependencies

* Python 3
* PyQt5
* KDE Frameworks 5
* Python libraries: Xlib, v4l2capture, PIL

## Building & Installation

* Build Kapudan without installing to your system:

    python3 setup.py build

* Running Kapudan after building:

    python3 build/kapudan.py

* Build and install Kapudan to your system:

    python3 setup.py install


## Testing (for Developers)

* Build and run the source in a seperate dir:

    ./go


## Translations

### Developers

To regenerate the translation template, ‘po/kapudan.pot’ (requires
`intltool`):

    python3 setup.py update_messages

Don’t forget to upload this template to Transifex: https://www.transifex.com/chakra/chakra/

If you plan on releasing a new version of the software shortly, you should
post an announcement on Transifex asking translators to update Kapudan
translations as soon as possible.

To retrieve the latest translations (give translators at least two weeks
since the last time you uploaded a modified POT file to Transifex):

    tx pull -af --minimum-perc=90

Note: You need to install the Transifex client (‘transifex-client’) first.
You will also need to have a Transifex account and configure your credentials
in the ‘~/.transifexrc’ file as described in http://docs.transifex.com/client/setup/

If asked to change the host URL in the command line (.net/.com issue), answer ‘n’.

### Translators

If you haven't already, request to be added to the Chakra group on Transifex:
https://www.transifex.com/chakra/chakra/. Edit the translations there.
