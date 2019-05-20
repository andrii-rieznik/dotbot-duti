import os
import subprocess

import dotbot


class Duti(dotbot.Plugin):
    _directive = 'duti'
    _default_filename = 'Dutifile'

    def can_handle(self, directive):
        return directive == self._directive

    def handle(self, directive, data):
        try:
            if not self._is_dutifile_exist(data):
                raise ValueError('Duti file does not exist.')

            if not self._is_duti_installed():
                raise ValueError('duti required: brew install duti')

            self._process_associations(data)
            return True
        except ValueError as e:
            self._log.error(e)
            return False

    @property
    def cwd(self):
        return self._context.base_directory()

    def _dutifile_path(self, data):
        return os.path.join(self.cwd, data.get('file', self._default_filename))

    def _is_dutifile_exist(self, data):
        return os.path.isfile(self._dutifile_path(data))

    def _process_associations(self, data):
        subprocess.call(['duti', self._dutifile_path(data)])

    @staticmethod
    def _is_duti_installed():
        status_code = subprocess.call(['command', '-v', 'duti'])
        return True if status_code is 0 else False
