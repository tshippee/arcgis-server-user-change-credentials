# import modules
import unittest
from arcgis_server_util import authenticate_change_password

# variables
username = 'testUser'
old_password = 'test'
new_password = 'test01'


class TestAuthenticateChangePassword(unittest.TestCase):
    def test_authenticate_change_password(self):
        status = authenticate_change_password(username, old_password, new_password)
        self.assertTrue(status, 'failed to change user password')


# main function
def main():
    unittest.main()

# run main function
if __name__ == '__main__':
    main()