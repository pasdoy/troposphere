# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import double


class AssertionAttributes(AWSProperty):
    """
    `AssertionAttributes <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-assertionattributes.html>`__
    """

    props: PropsDictType = {
        "Email": (str, False),
        "Groups": (str, False),
        "Login": (str, False),
        "Name": (str, False),
        "Org": (str, False),
        "Role": (str, False),
    }


class IdpMetadata(AWSProperty):
    """
    `IdpMetadata <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-idpmetadata.html>`__
    """

    props: PropsDictType = {
        "Url": (str, False),
        "Xml": (str, False),
    }


class RoleValues(AWSProperty):
    """
    `RoleValues <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-rolevalues.html>`__
    """

    props: PropsDictType = {
        "Admin": ([str], False),
        "Editor": ([str], False),
    }


class SamlConfiguration(AWSProperty):
    """
    `SamlConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-samlconfiguration.html>`__
    """

    props: PropsDictType = {
        "AllowedOrganizations": ([str], False),
        "AssertionAttributes": (AssertionAttributes, False),
        "IdpMetadata": (IdpMetadata, True),
        "LoginValidityDuration": (double, False),
        "RoleValues": (RoleValues, False),
    }


class VpcConfiguration(AWSProperty):
    """
    `VpcConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-grafana-workspace-vpcconfiguration.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], True),
        "SubnetIds": ([str], True),
    }


class Workspace(AWSObject):
    """
    `Workspace <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html>`__
    """

    resource_type = "AWS::Grafana::Workspace"

    props: PropsDictType = {
        "AccountAccessType": (str, True),
        "AuthenticationProviders": ([str], True),
        "ClientToken": (str, False),
        "DataSources": ([str], False),
        "Description": (str, False),
        "Name": (str, False),
        "NotificationDestinations": ([str], False),
        "OrganizationRoleName": (str, False),
        "OrganizationalUnits": ([str], False),
        "PermissionType": (str, True),
        "RoleArn": (str, False),
        "SamlConfiguration": (SamlConfiguration, False),
        "StackSetName": (str, False),
        "VpcConfiguration": (VpcConfiguration, False),
    }
