#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from helpers.nosetestloaders import *

from api.xml.xml_api_test_suite import xml_api_suite

def all_suites():
    return create_test_suite_from_suites([xml_api_suite()])

if __name__ == "__main__":
    run_test_suite(all_suites())
