from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/token_price', methods=['GET'])
def get_token_price():
    try:
        # GeckoTerminal API endpoint for the specific pool
        api_url = 'https://api.geckoterminal.com/api/v2/networks/polygon_pos/pools/0x0c9f1ffc02d6d001effdbdf90bb80e1438140895'

        # Send a GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract the token price in USD
        token_price_usd = data['data']['attributes']['base_token_price_usd']

        # Return the price as a JSON response
        return jsonify({'token_price_usd': token_price_usd})

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the API request
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
