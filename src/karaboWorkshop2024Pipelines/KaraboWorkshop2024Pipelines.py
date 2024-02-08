#############################################################################
# Author: parenti
#
# Created on February 08, 2024, 03:42 PM
# from template 'minimal middlelayer' of Karabo 2.19.3
#
# This file is intended to be used together with Karabo:
#
# http://www.karabo.eu
#
# IF YOU REQUIRE ANY LICENSING AND COPYRIGHT TERMS, PLEASE ADD THEM HERE.
# Karabo itself is licensed under the terms of the MPL 2.0 license.
#############################################################################

from karabo.middlelayer import (
    AccessMode, Assignment, Configurable, Device, Double, InputChannel, Node,
    OutputChannel, State, UInt16, get_timestamp)

from ._version import version as deviceVersion


class DataNode(Configurable):
    pixelMean = Double(
        displayedName="Pixel Average",
        accessMode=AccessMode.READONLY)

    pixelMin = UInt16(
        displayedName="Min Pixel Value",
        accessMode=AccessMode.READONLY)

    pixelMax = UInt16(
        displayedName="Max Pixel Value",
        accessMode=AccessMode.READONLY)


class ChannelNode(Configurable):
    data = Node(DataNode)


class KaraboWorkshop2024Pipelines(Device):
    __version__ = deviceVersion

    def __init__(self, configuration):
        super().__init__(configuration)

    @InputChannel(
        raw=False,
        displayedName="Input",
        accessMode=AccessMode.INITONLY,
        assignment=Assignment.MANDATORY)
    async def input(self, data, meta):
        try:
            # "data.image" is the path where the camera provides the image
            image = data.data.image
            pixels = image.pixels.value  # ndarray

            ts = get_timestamp(meta.timestamp.timestamp)
            await self.process_image(pixels, ts)

            if self.state != State.PROCESSING:
                self.state = State.PROCESSING
                self.status = "PROCESSING"

        except Exception as e:
            if self.state != State.ERROR:
                self.state = State.ERROR
                self.status = str(e)

    output = OutputChannel(
        ChannelNode,
        displayedName="Output"
    )

    async def process_image(self, pixels, ts):
        self.output.schema.data.pixelMean = pixels.mean()
        self.output.schema.data.pixelMin = pixels.min()
        self.output.schema.data.pixelMax = pixels.max()

        # Write to the output channel with the same timestamp as in the input
        await self.output.writeData(timestamp=ts)

    @input.endOfStream
    async def input(self, name):
        if self.state != State.ON:
            self.state = State.ON
            self.status = "IDLE"
        await self.output.writeEndOfStream()

    async def onInitialization(self):
        """ This method will be called when the device starts.

            Define your actions to be executed after instantiation.
        """
        self.status = "IDLE"
        self.state = State.ON
