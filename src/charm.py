#!/usr/bin/env python3
# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""A Juju charm for configuring Charmed Ory Oathkeeper with downstream applications."""

import logging

from ops.charm import CharmBase
from ops.main import main

logger = logging.getLogger(__name__)


class OathkeeperConfiguratorCharm(CharmBase):
    """Charmed Oathkeeper Configurator."""

    def __init__(self, *args):
        super().__init__(*args)


if __name__ == "__main__":
    main(OathkeeperConfiguratorCharm)
