arcgis-server-user-change-credentials
=====================================

ArcGIS for Server provides the capability for updating user credentials only by the administrator. This script provides the foundation to create a geoprocessing service allowing users to update their own password without needing the intervention of an administrator. The script expects three parameters from four fields. The first field is the username. The second is the current user password. The last two are the desired new password. The user is first validated to ensure they are, in fact, who they purport to be. Next, the new passwords are compared to ensure they are identical. Finally, using the administrator credentials saved in the script, the user password is updated.
