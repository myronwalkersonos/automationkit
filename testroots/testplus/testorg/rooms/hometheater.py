from typing import Generator

import akit.testing.testplus as testplus

from akit.testing.testplus.resourcelifespan import ResourceLifespan

from akit.testing.testplus.scopemixin import ScopeMixIn

from testorg.integrations.automationpod import automation_pod

class HTRoom(ScopeMixIn):
    """
    """

# Scopes can have varying lifespans. Scopes are a mechanism to include integrations
# and to establish conditions.
@testplus.scope()
def hometheater_room(apod) -> Generator[HTRoom, None, None]:
    yield None
