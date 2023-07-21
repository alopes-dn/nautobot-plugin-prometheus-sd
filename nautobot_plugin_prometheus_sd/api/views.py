from nautobot.dcim.filters import DeviceFilterSet
from nautobot.dcim.models.devices import Device
from nautobot.extras.api.views import \
    CustomFieldModelViewSet as NautobotModelViewSet
from nautobot.ipam.filters import IPAddressFilterSet
from nautobot.ipam.models import IPAddress

from .serializers import PrometheusDeviceSerializer


class DeviceViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    queryset = Device.objects.prefetch_related(
        "device_type__manufacturer",
        "device_role",
        "tenant",
        "platform",
        "site",
        # "region",
        "location",
        "rack",
        "parent_bay",
        "virtual_chassis__master",
        "tags",
    )
    filterset_class = DeviceFilterSet
    serializer_class = PrometheusDeviceSerializer
    pagination_class = None


# class IPAddressViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
#     queryset = IPAddress.objects.prefetch_related("tenant", "tags")
#     serializer_class = PrometheusIPAddressSerializer
#     filterset_class = IPAddressFilterSet
#     pagination_class = None
