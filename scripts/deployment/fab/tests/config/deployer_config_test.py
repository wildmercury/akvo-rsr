#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import imp, os, unittest

from testing.helpers.execution import TestSuiteLoader, TestRunner

CONFIG_TEMPLATE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'deployer.py.template'))
imp.load_source('deployer_config', CONFIG_TEMPLATE_PATH)

from deployer_config import DeployerConfig


class DeployerConfigTest(unittest.TestCase):

    def setUp(self):
        super(DeployerConfigTest, self).setUp()
        self.expected_hosts = "somehost:port1,anotherhost:port2"
        self.expected_user = "joesoap"

        self.config = DeployerConfig(self.expected_hosts, self.expected_user)

    def test_deployment_hosts_are_set_on_initialisation(self):
        """fab.tests.config.deployer_config_test  Deployment hosts and user are set on initialisation"""

        self.assertEqual(self.expected_hosts, self.config.deployment_hosts)
        self.assertEqual(self.expected_user, self.config.user)

    def test_has_rsr_branch(self):
        """fab.tests.config.deployer_config_test  Has RSR branch setting"""

        self.assertTrue(len(self.config.rsr_branch) > 0, "Expected some value for rsr_branch setting")

    def test_has_repo_checkout_root(self):
        """fab.tests.config.deployer_config_test  Has repository checkout root setting"""

        self.assertTrue(len(self.config.repo_checkout_root) > 0, "Expected some value for repo_checkout_root setting")

    def test_has_expected_repo_archives_dir(self):
        """fab.tests.config.deployer_config_test  Has expected repository archives directory"""

        expected_repo_archives_dir = os.path.join(self.config.repo_checkout_root, "archives")

        self.assertEqual(expected_repo_archives_dir, self.config.repo_archives_dir)

    def test_has_expected_rsr_deployment_dir_name(self):
        """fab.tests.config.deployer_config_test  Has expected RSR deployment directory name"""

        self.assertEqual("akvo-rsr_%s" % self.config.rsr_branch, self.config.rsr_deployment_dir_name)

    def test_has_expected_rsr_deployment_root(self):
        """fab.tests.config.deployer_config_test  Has expected RSR deployment root"""

        expected_rsr_deployment_root = os.path.join(self.config.repo_checkout_root, self.config.rsr_deployment_dir_name)

        self.assertEqual(expected_rsr_deployment_root, self.config.rsr_deployment_root)

    def test_has_virtualenvs_home_setting(self):
        """fab.tests.config.deployer_config_test  Has virtualenvs home setting"""

        self.assertTrue(len(self.config.virtualenvs_home) > 0, "Expected some value for virtualenvs_home setting")

    def test_has_expected_rsr_env_name(self):
        """fab.tests.config.deployer_config_test  Has expected RSR virtualenv name"""

        self.assertEqual("rsr_%s" % self.config.rsr_branch, self.config.rsr_env_name)

    def test_has_expected_rsr_env_path(self):
        """fab.tests.config.deployer_config_test  Has expected RSR virtualenv path"""

        expected_rsr_env_path = os.path.join(self.config.virtualenvs_home, self.config.rsr_env_name)

        self.assertEqual(expected_rsr_env_path, self.config.rsr_env_path)

    def test_has_expected_pip_install_log_file_path(self):
        """fab.tests.config.deployer_config_test  Has expected pip install log file path"""

        pip_file_name = "pip_install_%s.log" % self.config.rsr_env_name
        expected_pip_log_file_path = os.path.join(self.config.virtualenvs_home, pip_file_name)

        self.assertEqual(expected_pip_log_file_path, self.config.pip_install_log_file)

    def test_has_expected_pip_requirements_home(self):
        """fab.tests.config.deployer_config_test  Has expected pip requirements home"""

        expected_pip_requirements_home = os.path.join(self.config.rsr_deployment_root, "scripts/deployment/pip/requirements")

        self.assertEqual(expected_pip_requirements_home, self.config.pip_requirements_home)


def suite():
    return TestSuiteLoader().load_tests_from(DeployerConfigTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())