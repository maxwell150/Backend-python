#!/usr/bin/env python3
"""test for GithubOrgClient
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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
                GithubOrgClient, 'org', new_callable=PropertyMock) as mock_get:
            mock_get.return_value = {"repos_url": "test"}
            test_client = GithubOrgClient('test')
            test_return = test_client._public_repos_url
            self.assertEqual(test_return, mock_get.return_value['repos_url'])

    @patch("client.get_json", return_value=[{"name": "test"}])
    def test_public_repos(self, mock_j):
        """ test mocked property """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_p:
            test_client = GithubOrgClient("test")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["test"])
            mock_j.assert_called_once()
            mock_p.assert_called_once()
