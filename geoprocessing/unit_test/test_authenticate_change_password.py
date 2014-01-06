# import modules
import unittest
from geoprocessing.arcgis_server_util import authenticate_change_password

# variables
# you will need to populate these for the unit tests to successfully run
username = ''
old_password = ''
new_password = ''


class TestAuthenticateChangePassword(unittest.TestCase):
    def test_authenticate_change_password(self):
        status = authenticate_change_password(username, old_password, new_password)
        if status:
            authenticate_change_password(username, new_password, old_password)
        self.assertTrue(status, 'failed to change user password')


# main function
def main():
    unittest.main()

# run main function
if __name__ == '__main__':
    main()