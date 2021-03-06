# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class GrantCreateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, url=None):  # noqa: E501
        """GrantCreateRequest - a model defined in OpenAPI

        :param name: The name of this GrantCreateRequest.  # noqa: E501
        :type name: str
        :param description: The description of this GrantCreateRequest.  # noqa: E501
        :type description: str
        :param url: The url of this GrantCreateRequest.  # noqa: E501
        :type url: str
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'url': str
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'url': 'url'
        }

        self._name = name
        self._description = description
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'GrantCreateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GrantCreateRequest of this GrantCreateRequest.  # noqa: E501
        :rtype: GrantCreateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this GrantCreateRequest.

        The grant name  # noqa: E501

        :return: The name of this GrantCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GrantCreateRequest.

        The grant name  # noqa: E501

        :param name: The name of this GrantCreateRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this GrantCreateRequest.

        A description of the grant  # noqa: E501

        :return: The description of this GrantCreateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GrantCreateRequest.

        A description of the grant  # noqa: E501

        :param description: The description of this GrantCreateRequest.
        :type description: str
        """

        self._description = description

    @property
    def url(self):
        """Gets the url of this GrantCreateRequest.

        The URL to the grant  # noqa: E501

        :return: The url of this GrantCreateRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GrantCreateRequest.

        The URL to the grant  # noqa: E501

        :param url: The url of this GrantCreateRequest.
        :type url: str
        """

        self._url = url
