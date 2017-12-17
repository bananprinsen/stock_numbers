from flask import jsonify
import pkg_resources

from stock_numbers import app


@app.route('/api/v1.0/version', methods=['GET'])
def version():
    version_number = pkg_resources.require("stock_numbers")[0].version
    version_name = pkg_resources.require("stock_numbers")[0].project_name
    version_response = [
        {
            'version': version_number,
            'title': version_name
        }
    ]
    return jsonify(version_response)