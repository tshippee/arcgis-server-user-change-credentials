# import modules
import unittest
import urllib
import json
from geoprocessing import arcgis_server_util

# variables
# you will need to populate these for the unit tests to successfully run
server = ''
admin_user = ''
admin_pass = ''
user_name = ''
user_pass = ''
new_pass = ''


# create test case object instance
class TestAgs(unittest.TestCase):
    def test__post_to_server(self):
        """
        Test post to serer function using services rest endpoint to get version number
        """
        # REST path relative to server url for getting a token
        url = '/arcgis/admin/generateToken'

        # control for speical characters in string
        url = urllib.quote(url.encode('utf-8'))

        # use urlencode to format input parameters
        params = urllib.urlencode({'username': admin_user,
                                   'password': admin_pass,
                                   'client': 'requestip',
                                   'f': 'json'})

        # create ags object instance
        ags = arcgis_server_util.Ags(server)

        # call post to server and get response
        response, data = ags._post_to_server(url, params)

        # asert 200 (OK) status is received from the server
        self.assertEqual(response.status, 200,
                         'The server responded with a {0} ({1}) status'.format(response.status, response.reason))

        # load the json into a variable
        obj = json.loads(data)

        # assert error is not received from server in json message
        if 'status' in obj:
            self.assertEqual(obj['status'], "error",
                             'The server responded with a 200 (OK) status, but a JSON error was returned')

        # assert can find correct value in response
        self.assertTrue(len(obj['token']) > 0,
                        'Although no errors were returned from the server, the expected response was not received from the server')

    # authenticate function
    def test_authenticate(self):
        # create ArcGIS Server object instance
        ags = arcgis_server_util.Ags(server)

        # authenticate with admin rest endpoint
        status = ags.authenticate(admin_user, admin_pass)

        # test if authentication works
        self.assertTrue(status, 'administrator authentication failed')

    # validate user function
    def test_validate_user(self):
        # create ArcGIS Server object instance
        ags = arcgis_server_util.Ags(server)

        # authenticate with rest endpoint
        status = ags.validate_user(user_name, user_pass)

        # test if authentication worked
        self.assertTrue(status, 'user authentication failed')

    def test_change_user_password(self):
        # create ArcGIS Server object instance
        ags = arcgis_server_util.Ags(server)

        # authenticate with admin rest endpoint
        auth_bool = ags.authenticate(admin_user, admin_pass)

        # if authentication successful
        if auth_bool:
            user_valid = ags.validate_user(user_name, user_pass)

        # if the user is who they say they are
        if user_valid:
            change_pass_bool = ags.change_user_password(user_name, new_pass)
        else:
            change_pass_bool = False

        self.assertTrue(change_pass_bool, 'could not change user password')

        if change_pass_bool:
            ags.change_user_password(user_name, user_pass)


# main function
def main():
    unittest.main()

# run main function
if __name__ == '__main__':
    main()
