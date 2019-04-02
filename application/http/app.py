from flask import Flask, jsonify

from application.http.error import Error
from application.http.exceptions.bad_request import BadRequest
from domain.reports.report_generator import ReportGenerator
from infrastructure.decoder.custom_json_decoder import CustomJSONEncoder

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder


@app.errorhandler(BadRequest)
def handle_bad_request(error):
    response = jsonify(error.to_json())
    response.status_code = error.status_code
    return response


@app.errorhandler(404)
def route_not_found(e):
    error_404 = jsonify(Error(type='VALIDATION', key='route_not_found', message='this route not exists').to_json)
    error_404.status_code = 404
    return error_404


@app.route('/reports', methods=['GET'])
def default():
    return process()


@app.route('/reports/<report>', methods=['GET'])
def show_report(report):
    return process(report)


def process(report_name='default'):
    report = ReportGenerator().process_report(report_name)

    if report.is_right:
        return jsonify(report.value)

    raise BadRequest(messages=report.value)


if __name__ == '__main__':
    app.run()
