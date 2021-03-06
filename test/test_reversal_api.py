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
from CyberSource.apis.reversal_api import ReversalApi


class TestReversalApi(unittest.TestCase):
    """ ReversalApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.reversal_api.ReversalApi()

    def tearDown(self):
        pass

    def test_auth_reversal(self):
        """
        Test case for auth_reversal

        Process an Authorization Reversal
        """
        pass


if __name__ == '__main__':
    unittest.main()
