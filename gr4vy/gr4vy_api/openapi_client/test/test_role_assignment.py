"""
    Gr4vy API

    Welcome to the Gr4vy API reference documentation. Our API is still very much a work in product and subject to change.  # noqa: E501

    The version of the OpenAPI document: 1.1.0-beta
    Contact: code@gr4vy.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.role import Role
from openapi_client.model.role_assignment_assignee import RoleAssignmentAssignee
globals()['Role'] = Role
globals()['RoleAssignmentAssignee'] = RoleAssignmentAssignee
from openapi_client.model.role_assignment import RoleAssignment


class TestRoleAssignment(unittest.TestCase):
    """RoleAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRoleAssignment(self):
        """Test RoleAssignment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RoleAssignment()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()