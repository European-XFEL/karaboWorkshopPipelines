# Karabo Workshop 2024: Handling Fast Data through Pipelines

This repository contains material for the third session (Handling Fast Data
through Pipelines) of the Karabo developer workshop 2024:
https://indico.desy.de/event/43185/


## Testing

Every Karabo device in Python is shipped as a regular python package.
In order to make the device visible to any device-server you have to install
the package to Karabo's own Python environment.

Simply type:

``pip install -e .``

in the directory of where the ``setup.py`` file is located, or use the ``karabo``
utility script:

``karabo develop karaboWorkshop2024Pipelines``

## Running

If you want to manually start a server using this device, simply type:

``karabo-middlelayerserver serverId=middleLayerServer/1 deviceClasses=KaraboWorkshop2024Pipelines``

Or just use (a properly configured):

``karabo-start``
