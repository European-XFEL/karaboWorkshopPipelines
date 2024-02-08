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
import pytest

from karabo.middlelayer import State
from karabo.middlelayer.testing import AsyncDeviceContext, event_loop

from ..KaraboWorkshop2024Pipelines import KaraboWorkshop2024Pipelines

_DEVICE_CONFIG = {
    "_deviceId_": "TestKaraboWorkshop2024Pipelines",
    "input": {}
}


@pytest.mark.timeout(30)
@pytest.mark.asyncio
async def test_instantiate(event_loop: event_loop):
    device = KaraboWorkshop2024Pipelines(_DEVICE_CONFIG)
    async with AsyncDeviceContext(device=device) as ctx:
        assert ctx.instances["device"] is device
        assert device.state == State.ON
