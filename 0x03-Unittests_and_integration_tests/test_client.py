#!/usr/bin/env python3
"""test for GithubOrgClient
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''unittest for GithubOrgClient.org'''

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock: unittest.mock.patch):
        '''unittest for org request is called once'''
        test_class = GithubOrgClient(org_name)
        self.assertEqual(test_class.org, mock.return_value)
        mock.assert_called_once
