# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class OrganizationCreateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, short_name=None, url=None):  # noqa: E501
        """OrganizationCreateRequest - a model defined in OpenAPI

        :param name: The name of this OrganizationCreateRequest.  # noqa: E501
        :type name: str
        :param short_name: The short_name of this OrganizationCreateRequest.  # noqa: E501
        :type short_name: str
        :param url: The url of this OrganizationCreateRequest.  # noqa: E501
        :type url: str
        """
        self.openapi_types = {
            'name': str,
            'short_name': str,
            'url': str
        }

        self.attribute_map = {
            'name': 'name',
            'short_name': 'shortName',
            'url': 'url'
        }

        self._name = name
        self._short_name = short_name
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'OrganizationCreateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OrganizationCreateRequest of this OrganizationCreateRequest.  # noqa: E501
        :rtype: OrganizationCreateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this OrganizationCreateRequest.

        The organization name  # noqa: E501

        :return: The name of this OrganizationCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationCreateRequest.

        The organization name  # noqa: E501

        :param name: The name of this OrganizationCreateRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this OrganizationCreateRequest.

        The organization short name  # noqa: E501

        :return: The short_name of this OrganizationCreateRequest.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this OrganizationCreateRequest.

        The organization short name  # noqa: E501

        :param short_name: The short_name of this OrganizationCreateRequest.
        :type short_name: str
        """

        self._short_name = short_name

    @property
    def url(self):
        """Gets the url of this OrganizationCreateRequest.

        The URL to the homepage of the organization  # noqa: E501

        :return: The url of this OrganizationCreateRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OrganizationCreateRequest.

        The URL to the homepage of the organization  # noqa: E501

        :param url: The url of this OrganizationCreateRequest.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url
