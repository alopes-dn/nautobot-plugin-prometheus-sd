from nautobot.ipam.models import IPAddress
from nautobot.virtualization.models import VirtualMachine
from nautobot.dcim.models.devices import Device
from nautobot.extras.api.views import CustomFieldModelViewSet as NautobotModelViewSet
from nautobot.ipam.filters import IPAddressFilterSet
from nautobot.dcim.filters import DeviceFilterSet
from nautobot.virtualization.filters import VirtualMachineFilterSet

from .serializers import (
    PrometheusIPAddressSerializer,
    PrometheusDeviceSerializer,
    PrometheusVirtualMachineSerializer,
)


class VirtualMachineViewSet(
    NautobotModelViewSet
):  # pylint: disable=too-many-ancestors
    queryset = VirtualMachine.objects.prefetch_related(
        "cluster__site",
        "role",
        "tenant",
        "platform",
        "primary_ip4",
        "primary_ip6",
        "tags",
        "services",
        "contacts",

    )
    filterset_class = VirtualMachineFilterSet
    serializer_class = PrometheusVirtualMachineSerializer
    pagination_class = None


class DeviceViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = Device.objects.prefetch_related(
        "device_type__manufacturer",
        "device_role",
        "tenant",
        "platform",
        "site",
        "location",
        "rack",
        "parent_bay",
        "virtual_chassis__master",
        "tags",
    )
    filterset_class = DeviceFilterSet
    serializer_class = PrometheusDeviceSerializer
    pagination_class = None


class IPAddressViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = IPAddress.objects.prefetch_related("tenant", "tags")
    serializer_class = PrometheusIPAddressSerializer
    filterset_class = IPAddressFilterSet
    pagination_class = None
