from flask import Flask, jsonify, abort, make_response, request
from main import Scrape

app = Flask(__name__)


@app.route('/scrape/')
def get_data():
    """
    Example:
    /scrape/?number=100&from=01/02/2020&to=10/02/2020
    :return: json scraped data
    """
    item_number = request.args.get("number")
    from_date = request.args.get("from")
    to_date = request.args.get("to")

    scrape = Scrape(numbers_per_page=item_number, from_date=from_date, to_date=to_date)
    scrape.startSelenium()
    # Without this the API stores the previous result and it returns is
    scrape.clear()

    scrape.parseData()
    scrape.clean_data()
    scraped_list = scrape.get_data()
    result = scraped_list.copy()
    scraped_list.clear()
    scrape.quit()
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
