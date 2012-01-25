# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import fab.host.linux
import fab.tasks.base


class LinuxHostBaseTask(fab.tasks.base.BaseDeploymentTask):
    """Base deployment task for actions that required a configured Linux host"""

    def run(self, config_type, host_alias=None, repository_branch=None, database_name=None, custom_config_module_path=None):
        host_config = self.config_loader.host_config_for(config_type, host_alias, repository_branch, database_name, custom_config_module_path)
        self.linux_host = self._configure_linux_host_with(host_config)

    def _configure_linux_host_with(self, host_config):
        return fab.host.linux.LinuxHost.create_with(host_config)
