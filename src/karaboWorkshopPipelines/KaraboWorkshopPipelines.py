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
    AccessMode, Device, Double, InputChannel, State, UInt16, UInt32)

from ._version import version as deviceVersion


class KaraboWorkshopPipelines(Device):
    __version__ = deviceVersion

    def __init__(self, configuration):
        super().__init__(configuration)

    @InputChannel(displayedName="Input")
    async def input(self, data, meta):
        # "data.image" is the path where the camera provides the image
        image = data.data.image
        pixels = image.pixels.value  # ndarray

        await self.process_image(pixels)

        self.framesAcquired += 1

    framesAcquired = UInt32(
        displayedName="Frames Acquired",
        accessMode=AccessMode.READONLY,
        defaultValue=0)

    pixelMean = Double(
        displayedName="Pixel Average",
        accessMode=AccessMode.READONLY)

    pixelMin = UInt16(
        displayedName="Min Pixel Value",
        accessMode=AccessMode.READONLY)

    pixelMax = UInt16(
        displayedName="Max Pixel Value",
        accessMode=AccessMode.READONLY)

    async def process_image(self, pixels):
        self.pixelMean = pixels.mean()
        self.pixelMin = pixels.min()
        self.pixelMax = pixels.max()

    async def onInitialization(self):
        """ This method will be called when the device starts.

            Define your actions to be executed after instantiation.
        """
        self.state = State.ON
