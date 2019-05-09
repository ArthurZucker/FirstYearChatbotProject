# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_stlab_tools_fred_get(self):
        """Test case for stlab_tools_fred_get

        
        """
        query_string = [('text', 'text_example'),
                        ('prefix', 'prefix_example'),
                        ('namespace', 'namespace_example'),
                        ('wsd', true),
                        ('wfd', true),
                        ('wfd_profile', 'b'),
                        ('tense', true),
                        ('roles', true),
                        ('textannotation', 'earmark'),
                        ('semantic_subgraph', true)]
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/stlab-tools/fred',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
