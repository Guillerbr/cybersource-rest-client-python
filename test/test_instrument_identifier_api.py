# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.instrument_identifier_api import InstrumentIdentifierApi


class TestInstrumentIdentifierApi(unittest.TestCase):
    """ InstrumentIdentifierApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.instrument_identifier_api.InstrumentIdentifierApi()

    def tearDown(self):
        pass

    def test_tms_v1_instrumentidentifiers_token_id_delete(self):
        """
        Test case for tms_v1_instrumentidentifiers_token_id_delete

        Delete an Instrument Identifier
        """
        pass

    def test_tms_v1_instrumentidentifiers_token_id_get(self):
        """
        Test case for tms_v1_instrumentidentifiers_token_id_get

        Retrieve an Instrument Identifier
        """
        pass

    def test_tms_v1_instrumentidentifiers_token_id_patch(self):
        """
        Test case for tms_v1_instrumentidentifiers_token_id_patch

        Update a Instrument Identifier
        """
        pass


if __name__ == '__main__':
    unittest.main()
