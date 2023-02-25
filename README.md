# nautobot-plugin-prometheus-sd

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/FlxPeters/netbox-plugin-prometheus-sd/workflows/CI/badge.svg?event=push)](https://github.com/FlxPeters/netbox-plugin-prometheus-sd/actions?query=workflow%3ACI)
Provide Prometheus http_sd compatible API Endpoint with data from Nautobot.

HTTP SD is a new feature in Prometheus 2.28.0 that allows hosts to be found via a URL instead of just files.
This plugin implements API endpoints in Nautobot to make devices, IPs and virtual machines available to Prometheus.

## Usage

The plugin only provides a new API endpoint on the Nautobot API. There is no further action required after installation.

### API

The plugin reuses Nautobot API view sets with new serializers for Prometheus.
This means that all filters that can be used on the Nautobot api can also be used to filter Prometheus targets.
Paging is disabled because Prometheus does not support paged results.

The plugin also reuses the Nautobot authentication and permission model.
Depending on the Nautobot configuration, a token with valid object permissions must be passed to Nautobot.

```
GET        /api/plugins/prometheus-sd/devices/              Get a list of devices in a prometheus compatible format
GET        /api/plugins/prometheus-sd/virtual-machines/     Get a list of vms in a prometheus compatible format
GET        /api/plugins/prometheus-sd/ip-addresses/         Get a list of ip in a prometheus compatible format
```

## Development

We use Poetry for dependency management and invoke as task runner.
As Nautobot plugins cannot be tested standalone, we need invoke to start all code embedded in Nautobot Docker containers.

All code to run in docker is located under `development`.
To start a virtual env managed by poetry run `poetry shell`.
All following commands are started inside this environment.

``` bash
# Start a local Netbox with docker
invoke debug


Visit http://0.0.0.0:8080 and log in with admin/admin
You can now define Nautobot entities and test around.

API endpoints for testing can be found at http://0.0.0.0:8080/api/plugins/prometheus-sd/
