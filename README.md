# Karabo Workshop: Handling Fast Data through Pipelines

This repository contains material for the
"Hands-on: Handling Fast Data through Pipelines"
part of the Satellite Workshop
"A developer's introduction to the Karabo SCADA Framework" of the
NOBUGS 2026 conference, see https://indico.xfel.eu/event/2/sessions/40/.

For instructions, please see the material attached to that agenda.

### General Background

- Karabo data communication can be split in two categories: slow data and fast data.

- Slow data is comprised of message exchanges intermediated by a broker.

- Fast data is about larger amounts of data exchanged directly between devices through pipelines.

- Fast data is transmitted in a point-to-point fashion over TCP/IP.

- The connection details like host and port are exchanged using broker communication.

- The most common use case is one output device connected to one or several input devices.

- Documentation about how to work with pipeline data in the Karabo middlelayer API is at
  https://karabodevices3.pages.xfel.eu/HowToMiddlelayer/chap4/intro_advanced.html#pipelining-channels

## Running

If you want to manually start a server using this device, simply type:

``karabo-middlelayerserver serverId=middleLayerServer/1 deviceClasses=KaraboWorkshopPipelines``

Or just use (a properly configured):

``karabo-start``
