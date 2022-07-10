#!/usr/bin/env python3

"""
This module tests the get_added_removed function.
"""

import unittest

from src.IntuneCD.update_assignment import get_added_removed


class TestCleanFilename(unittest.TestCase):
    """Test class for get_added_removed."""

    def test_get_added_removed(self):
        """The list of added and removed should be returned."""
        self.object = {
            'assignments': {
                'intent': 'apply',
                'target': {
                    '@odata.type': '#microsoft.graph.allDevicesAssignmentTarget',
                    'deviceAndAppManagementAssignmentFilterId': "1234",
                    'deviceAndAppManagementAssignmentFilterType': 'device'}}}

        result = get_added_removed(self.object)

        self.assertEqual(
            result,
            ['intent: apply, Filter ID: 1234, Filter Type: device, target: All Devices'])
