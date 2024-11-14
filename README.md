# Cloudflare Radar Data Visualization

A Python application to fetch and visualize data from the Cloudflare Radar API.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/thrive-spectre/radarv.git
   cd radarv
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Set up your API token:
   . Rename .env.example to .env.
   . Add your Cloudflare API token in the .env file
   ```bash
    RADAR_API_TOKEN = "your_cloudflare_radar_api_token_here"

## Usage

1. Run the main script to fetch data from multiple endpoints and store it locally:
   ```bash
    python main.py

The data will be saved in the data/ directory.

## API Documentation
For more information on the Cloudflare Radar API, refer to https://developers.cloudflare.com/radar/.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests.

## License
- These scripts are licensed under the [MIT License](LICENSE).

 
