# Karabo Workshop 2024: Handling Fast Data through Pipelines

This repository contains material for the third session (Handling Fast Data
through Pipelines) of the Karabo developer workshop 2024:
https://indico.desy.de/event/43185/


## Outline of the Session

- Introduction: 10'
- Use of Input Channels: 25' + 5' for the live demo
- Use of Output Channels: 15' + 5' for the live demo

### Introduction

TODO: add here text or link to slides

### Use of Input Channels

Documentation and examples are available here:
https://rtd.xfel.eu/docs/howtomiddlelayer/en/latest/chap4/intro_advanced.html#pipelining-channels

The goal is to add an input channel to a Karabo MDL device and read data from
it.

More in detail:

1. Check-out this project:

   ``karabo -g https://git.xfel.eu checkout karaboWorkshop2024Pipelines``

   ``cd karaboWorkshop2024Pipelines``

   ``git checkout main``

2. Create your branch

   ``git checkout -b some_meaningful_name``

3. Add an input channel to device as described in the documentation

4. Receive image data from a simulated camera

5. Process the data and publish the result as a device property
   (e.g. average min, max, average value)

6. Optional: use end-of-stream and input close signals to update device state
   (normally: ON, PROCESSING, ERROR)

7. Save your work!

   ``git commit -a -m"Some description"``

   ``git push origin some_meaningful_name``

8. A working example can be found in the `step1` branch of this repository

   ``git checkout step1``


### Use of Output Channels

The aim of this second part of the session is to add an output channel to the
device.

1. Depending on how far you went in the first part of the session, you can
   either start from your branch, from `step1` branch, or from this other
   branch where we have already added the output channel

   ``git checkout step2_initial``

2. If you are not on your branch, create it now

   ``git checkout -b some_other_name``

3. Prepare the schema for the output channel, i.e. some property to be written

4. Write data to the output channel

5. Look at the data in the GUI

6. Optional: send end-of-stream

7. Save your work!

   ``git commit -a -m"Some description"``

   ``git push origin some_other_name``
 
8. A working example can be found in the `step1` branch of this repository

   ``git checkout step2``


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
