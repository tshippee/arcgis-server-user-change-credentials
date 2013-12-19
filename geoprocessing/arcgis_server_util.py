"""
Author:     Joel McCune (joelmccune@gmail.com)
DOB:        15 Dec 2013
Purpose:    ArcGIS for Server provides the capability for updating user credentials only by the administrator. This
            script provides the foundation to create a geoprocessing service allowing users to update their own
            password without needing the intervention of an administrator. The script expects three parameters from
            four fields. The first field is the username. The second is the current user password. The last two are the
            desired new password. The user is first validated to ensure they are, in fact, who they purport to be. Next,
            the new passwords are compared to ensure they are identical. Finally, using the administrator credentials
            saved in the script, the user password is updated.

WARNING:    This script does contain your administrator credentials. Ensure this script is saved in a secure location.
"""
# variables
admin_username = ''
admin_password = ''
server_name = ''

# import modules
import json
import urllib
import httplib


class Ags(object):
    """
    Provide single stop shopping for administrative functionality.
    """

    def __init__(self, server, port=6080):
        """
        Server name is required when initializing object instance. Port number defaults to 6080, specify if you need
        a different port.
        """
        self.server = server
        self.port = port
        self.token = ""

    def authenticate(self, admin_user, admin_pass):
        """
        Log into ArcGIS for Server as an administrator. Get token. Return boolean indicating status.
        """

        # REST path relative to server url for getting a token
        token_url = '/arcgis/admin/generateToken'

        # user urlencode to format input parameters
        params = urllib.urlencode({'username': admin_user,
                                   'password': admin_pass,
                                   'client': 'requestip',
                                   'f': 'json'})

        # submit request to server
        response, data = self._post_to_server(token_url, params)

        # if not successful or not properly formatted json, fail
        if response.status != 200 or not assert_json_success(data):
            print "{} {}".format(response.status, response.reason)
            return False

        else:
            # load the json into an object instance
            json_token = json.loads(data)

            # extract the token from the json and save it
            self.token = json_token['token']

            # return success
            return True

    def validate_user(self, user_name, user_pass):
        """
        Check user's credentials to ensure they are who they proport to be.
        """
        # REST path relative to server url for validating a user's credentials and generating a token
        token_url = '/arcgis/tokens/generateToken'

        # user urlencode to format input parameters
        params = urllib.urlencode({'username': user_name,
                                   'password': user_pass,
                                   'client': 'requestip',
                                   'f': 'json'})

        # submit request to server
        response, data = self._post_to_server(token_url, params)

        # if not successful or not properly formatted json, fail
        if response.status != 200 or not assert_json_success(data):
            return False

        else:
            # load the json into an object instance
            json_token = json.loads(data)

            # check to make sure the token is present and the length is greater than zero
            if 'token' in json_token and len(json_token['token']) > 0:
                return True

            else:
                return False

    def change_user_password(self, user_name, new_pass):
        """
        Change a user's password.
        """
        # REST path relative to server url for modifying a user in the user store
        token_url = '/arcgis/admin/security/users/update'

        # user urlencode to format input parameters
        params = urllib.urlencode({'username': user_name,
                                   'password': new_pass,
                                   'token': self.token,
                                   'f': 'json'})

        # submit request to server
        response, data = self._post_to_server(token_url, params)

        # if not successful or not properly formatted json, fail
        if response.status != 200 or not assert_json_success(data):
            return False

        else:
            # return false
            return True

    def _post_to_server(self, url, params):

        # create connection object instance
        http_conn = httplib.HTTPConnection(self.server, self.port)

        # headers to submit as part of requests
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

        # use utf-8, quoting any special characters in the url string
        url = urllib.quote(url.encode('utf-8'))

        # Build the connection to add the roles to the server
        http_conn.request("POST", url, params, headers)

        # get teh response from the connection object
        response = http_conn.getresponse()

        # extract teh data
        data = response.read()

        # close the connection
        http_conn.close()

        # return the results
        return response, data


def assert_json_success(data):
    """
    Check json responses for errors.
    """
    obj = json.loads(data)
    if 'status' in obj and obj['status'] == "error":
        return False
    else:
        return True


def authenticate_change_password(username, old_password, new_password):
    # create ArcGIS Server object instance
    ags = Ags(server_name)

    # check to make sure user is, in fact, who they purport to be
    user_valid = ags.validate_user(username, old_password)

    # if the user is who they say they are
    if user_valid:

        # authenticate with admin rest endpoint
        ags.authenticate(admin_username, admin_password)

        # change the password and report status of attempting to change password
        return ags.change_user_password(username, new_password)