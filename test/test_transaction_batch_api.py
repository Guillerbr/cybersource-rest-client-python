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
from CyberSource.apis.transaction_batch_api import TransactionBatchApi


class TestTransactionBatchApi(unittest.TestCase):
    """ TransactionBatchApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.transaction_batch_api.TransactionBatchApi()

    def tearDown(self):
        pass

    def test_pts_v1_transaction_batches_id_get(self):
        """
        Test case for pts_v1_transaction_batches_id_get

        Get an individual batch file Details processed through the Offline Transaction Submission Services
        """
        pass


if __name__ == '__main__':
    unittest.main()
