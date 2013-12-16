"""
Author:     Joel McCune (joelmccune@gmail.com)
DOB:        15 Dec 2013
Purpose:    This is little more than the toolbox wrapper for the arcgis_server_util module.
"""
# import arcpy
import arcpy
from arcgis_server_util import authenticate_change_password


def parameter(displayName, name, datatype, defaultValue=None, parameterType='Required', direction='Input'):
    # create parameter with a few defaults
    param = arcpy.Parameter(
        displayName=displayName,
        name=name,
        datatype=datatype,
        parameterType=parameterType,
        direction=direction)

    # set new parameter to a default value
    param.value = defaultValue

    # return the complete parameter object
    return param


class Toolbox(object):
    def __init__(self):
        self.label = 'arcgis_server_utility'
        self.alias = 'ArcGIS Server Utility'

        # List of tool classes associated with this toolbox
        self.tools = [ChangeUserPassword]


class ChangeUserPassword(object):
    def __init__(self):
        self.label = 'Change User Password'
        self.canRunInBackground = False

        self.parameters = [
            parameter('User Name', 'username', 'GPString'),
            parameter('Current Password', 'password_current', 'GPString'),
            parameter('New Password', 'password_new', 'GPString')
        ]

    def getParameterInfo(self):
        return self.parameters

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # get user credentials
        user_name = parameters[0].valueAsText
        user_old_pass = parameters[1].value
        user_new_pass = parameters[2].value
        arcpy.AddMessage('\n{}\n{}\n{}'.format(user_name, user_old_pass, user_new_pass))

        if authenticate_change_password(user_name, user_old_pass, user_new_pass):
            return
        else:
            arcpy.AddError("Failed to change password")