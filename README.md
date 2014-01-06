arcgis-server-user-change-credentials
=====================================

ArcGIS for Server provides the capability for updating user credentials only by the administrator. This script provides the foundation to create a geoprocessing service allowing users to update their own password without needing the intervention of an administrator. The repository contains two directories, one for each componet of this solution; geoprocessing and web.

The geoprocessing directory contains all the resources needed to publish the geoprocessing service to your ArcGIS for Server instance and create a geoprocessing service. The critical resources in this directory are the arcgis_server_util.py script and the Toolbox.tbx files. The other resources were for unit testing during my development process and can be used if you want to modify or extend the functionality.

When executed, the Python script first attempts to log in and get a token through the normal rest endpoint using the current user credentials. This ensures the user is, in fact, who they purport to be.  Next, using the administrator credentials saved in the script (on the server), the user password is updated.

The tool in the geoprocessing toolbox must be run once successfully in ArcMap. Once run once successfully, a result object will be available in the results window inside ArcMap. This result object can be published to your ArcGIS for Server site. Once published, a geoprocessing service will be available through the rest endpoint on your ArcGiS for Server site.

The web directory contains all the resources to publish a very simple web application to your web server (IIS, Apache2, etc). Copy all resources in this directory to your web server as it uses Bootstrap for styling and a combination of jQuery and jQuery Validate for processing the form.

The web form expects three parameters from four fields. The first field is the username. The second is the current user password. The last two are the desired new password. Although only the first password is used when posting to the published rest endpoint on the server, the form will not submit unless both passwords match. Once both passwords match, the form is allowed to be submitted and posted to the rest endpoint exposed by publishing the enclosed Python script tool.


