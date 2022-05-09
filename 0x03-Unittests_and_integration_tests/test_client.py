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

     def test_public_repos_url(self):
        '''unittest result is based on the mocked payload'''
        with patch.object(
                GithubOrgClient, 'org', new_callable=PropertyMock) as mock:
            mock.return_value = {"repos_url": "test"}
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, mock.return_value['repos_url'])
