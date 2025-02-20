
# Product Scraper

This project scrapes product information from the website [Scraping Club](https://scrapingclub.com/exercise/list_basic/), including details such as title, price, description, and image, and stores the data in a structured format (JSON, Excel).

## Features:
- Scrapes product information such as title, price, description, and image.
- Collects data from multiple pages of the website.
- Saves the scraped data in JSON and Excel formats.
- Logs the process to help with debugging and tracking.

## Technologies Used:
- `requests` for sending HTTP requests.
- `beautifulsoup4` for parsing HTML content.
- `lxml` for faster HTML/XML parsing.
- `time`, `datetime` for handling delays and execution time.
- `settings.py` and `utils.py` for configuration and utility functions.

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/product-scraper.git
   cd product-scraper
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage:

To run the scraper and collect product data, execute the `main.py` script:
```bash
python main.py
```

The script will:
1. Scrape product details from multiple pages.
2. Save the collected data in `parsed_data.json` and `parsed_data.xlsx`.

You can customize the scraping behavior by modifying the `settings.py` and `utils.py` files.

## Output:

The collected data will be saved in the following formats:
- **JSON**: A file named `parsed_data.json` containing all product details.
- **Excel**: A file named `parsed_data.xlsx` with the same data in tabular form.

## Logs:

During the scraping process, logs are generated to track the pages and links being processed, and any errors encountered. These logs are saved to a log file defined in `settings.py`.

## License:
This project is licensed under the MIT License.
