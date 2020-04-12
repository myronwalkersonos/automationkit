
import logging
import os

import akit.environment.activate

from akit.integration.agents.upnpagent import UpnpAgent
from akit.integration.landscaping import Landscape

landscape = Landscape()

upnp_agent = UpnpAgent()
upnp_agent.start()

from flask import Flask, url_for
from flask_restplus import apidoc

from restapis import register_rest_blueprints
from website import register_website_blueprints

DIR_THIS = os.path.dirname(__file__)
DIR_STATIC = os.path.join(DIR_THIS, "website", "static")
DIR_TEMPLATES = os.path.join(DIR_THIS, "website", "templates")

logger = logging.getLogger("scms")

app = Flask(__name__, template_folder=DIR_TEMPLATES, static_folder=DIR_STATIC)
app.config.SWAGGER_UI_JSONEDITOR = True

#if environment.DEVELOPER_MODE:
#    app.debug = True

# Prevent flask-restplus from registering docs so we
# can customize the route
app.extensions.setdefault("restplus", {
    "apidoc_registered": True
})


# Register the URL route blueprints
register_rest_blueprints(app, "api")
register_website_blueprints(app)

# Setup route redirect for the documentation
redirect_apidoc = apidoc.Apidoc('restplus_doc', apidoc.__name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/api/swaggerui')

@redirect_apidoc.add_app_template_global
def swagger_static(filename):
    static_url = url_for('restplus_doc.static', filename=filename )
    logger.critical("filename: %s" % filename)
    return static_url

expected_upnp_devices = landscape.get_upnp_devices()

upnp_agent.begin_search()
upnp_agent.wait_for_devices(expected_upnp_devices)

app.register_blueprint(redirect_apidoc)

# =================================================================
# This main entry point is utilized for debug runs only, when we
# install our service into NGINX and use Green Unicorn, the service
# is launch by Green Unicorn by referencing the 'app' instance in
# this module.
def controller_main():

    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(port=8888, debug=False)

    return

if __name__ == "__main__":
    controller_main()
