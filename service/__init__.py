"""
Package: service
Package for the application models and service routes
This module initializes the Flask app and database
"""
import os
import sys
import logging
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

# Create Flask application
app = Flask(__name__)

# Initialize Talisman security headers
talisman = Talisman(app, content_security_policy=None, force_https=False)

# Initialize CORS
CORS(app)

# Dependencies require we import routes after creating app
# pylint: disable=wrong-import-position, wrong-import-order
from service import routes, models
from service.common import error_handlers, log_handlers

# Set up logging for production
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
