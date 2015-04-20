import logging
import unittest
import json
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
import librato
from mock_connection import MockConnect, server

#logging.basicConfig(level=logging.DEBUG)
# Mock the server
librato.HTTPSConnection = MockConnect

class TestLibratoCompositeMetrics(unittest.TestCase):
    def setUp(self):
        self.conn = librato.connect('user_test', 'key_test')
        server.clean()

    @unittest.skip("will do it later") 
    def test_create_composite_metric(self):
        name = "composite.name"
        composite = "s('composite','*')"
        self.conn.create_composite(name, composite)
        metric = self.conn.get(name)
        assert metric.name == name
        assert metric.composite == composite

    def test_get_composite_metric(self):
        def mock_composite_list(name):
            server.metrics['composites'][name] = json.loads('{"name":"%s","display_name":"display_name","type":"composite","attributes":{"created_by_ua":"created_by"},"description":"description","period":"period","source_lag":"source_lag","composite":"composite_expression"}' % name)
        name = "composite_name"
        mock_composite_list(name)
        print server.metrics['composites'][name]
        metric = self.conn.get(name)
        assert metric.name == name
        assert metric.composite == composite

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
