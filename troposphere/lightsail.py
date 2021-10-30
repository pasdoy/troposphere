# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 43.1.0


from troposphere import Tags

from . import AWSObject, AWSProperty
from .validators import integer


class AutoSnapshotAddOn(AWSProperty):
    props = {
        "SnapshotTimeOfDay": (str, False),
    }


class AddOn(AWSProperty):
    props = {
        "AddOnType": (str, True),
        "AutoSnapshotAddOnRequest": (AutoSnapshotAddOn, False),
        "Status": (str, False),
    }


class Disk(AWSObject):
    resource_type = "AWS::Lightsail::Disk"

    props = {
        "AddOns": ([AddOn], False),
        "AvailabilityZone": (str, False),
        "DiskName": (str, True),
        "SizeInGb": (integer, True),
        "Tags": (Tags, False),
    }


class Hardware(AWSProperty):
    props = {
        "CpuCount": (integer, False),
        "Disks": ([Disk], False),
        "RamSizeInGb": (integer, False),
    }


class Location(AWSProperty):
    props = {
        "AvailabilityZone": (str, False),
        "RegionName": (str, False),
    }


class Port(AWSProperty):
    props = {
        "AccessDirection": (str, False),
        "AccessFrom": (str, False),
        "AccessType": (str, False),
        "CidrListAliases": ([str], False),
        "Cidrs": ([str], False),
        "CommonName": (str, False),
        "FromPort": (integer, False),
        "Ipv6Cidrs": ([str], False),
        "Protocol": (str, False),
        "ToPort": (integer, False),
    }


class Networking(AWSProperty):
    props = {
        "MonthlyTransfer": (dict, False),
        "Ports": ([Port], True),
    }


class State(AWSProperty):
    props = {
        "Code": (integer, False),
        "Name": (str, False),
    }


class Instance(AWSObject):
    resource_type = "AWS::Lightsail::Instance"

    props = {
        "AddOns": ([AddOn], False),
        "AvailabilityZone": (str, False),
        "BlueprintId": (str, True),
        "BundleId": (str, True),
        "Hardware": (Hardware, False),
        "InstanceName": (str, True),
        "Location": (Location, False),
        "Networking": (Networking, False),
        "State": (State, False),
        "Tags": (Tags, False),
    }