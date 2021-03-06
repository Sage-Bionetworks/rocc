# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.person import Person
from openapi_server.models.response_page_metadata_paging import ResponsePageMetadataPaging  # noqa: E501
from openapi_server import util


class PageOfPersons(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=None, limit=None, paging=None, total_results=None, persons=None):  # noqa: E501
        """PageOfPersons - a model defined in OpenAPI

        :param offset: The offset of this PageOfPersons.  # noqa: E501
        :type offset: int
        :param limit: The limit of this PageOfPersons.  # noqa: E501
        :type limit: int
        :param paging: The paging of this PageOfPersons.  # noqa: E501
        :type paging: ResponsePageMetadataPaging
        :param total_results: The total_results of this PageOfPersons.  # noqa: E501
        :type total_results: int
        :param persons: The persons of this PageOfPersons.  # noqa: E501
        :type persons: List[Person]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'paging': ResponsePageMetadataPaging,
            'total_results': int,
            'persons': List[Person]
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'paging': 'paging',
            'total_results': 'totalResults',
            'persons': 'persons'
        }

        self._offset = offset
        self._limit = limit
        self._paging = paging
        self._total_results = total_results
        self._persons = persons

    @classmethod
    def from_dict(cls, dikt) -> 'PageOfPersons':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PageOfPersons of this PageOfPersons.  # noqa: E501
        :rtype: PageOfPersons
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self):
        """Gets the offset of this PageOfPersons.

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this PageOfPersons.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfPersons.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this PageOfPersons.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOfPersons.

        Maximum number of results returned  # noqa: E501

        :return: The limit of this PageOfPersons.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfPersons.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this PageOfPersons.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def paging(self):
        """Gets the paging of this PageOfPersons.


        :return: The paging of this PageOfPersons.
        :rtype: ResponsePageMetadataPaging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this PageOfPersons.


        :param paging: The paging of this PageOfPersons.
        :type paging: ResponsePageMetadataPaging
        """
        if paging is None:
            raise ValueError("Invalid value for `paging`, must not be `None`")  # noqa: E501

        self._paging = paging

    @property
    def total_results(self):
        """Gets the total_results of this PageOfPersons.

        Total number of results in the result set  # noqa: E501

        :return: The total_results of this PageOfPersons.
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this PageOfPersons.

        Total number of results in the result set  # noqa: E501

        :param total_results: The total_results of this PageOfPersons.
        :type total_results: int
        """

        self._total_results = total_results

    @property
    def persons(self):
        """Gets the persons of this PageOfPersons.

        An array of Persons  # noqa: E501

        :return: The persons of this PageOfPersons.
        :rtype: List[Person]
        """
        return self._persons

    @persons.setter
    def persons(self, persons):
        """Sets the persons of this PageOfPersons.

        An array of Persons  # noqa: E501

        :param persons: The persons of this PageOfPersons.
        :type persons: List[Person]
        """

        self._persons = persons
