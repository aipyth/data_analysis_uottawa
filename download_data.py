import requests

def download_csv(url, save_path):
    """
    Downloads a CSV file from the specified URL and saves it to the given path.

    :param url: The URL of the CSV file to download.
    :param save_path: The local path where the CSV file will be saved.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        # Open the file in write-binary mode and write the content in chunks
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # Filter out keep-alive chunks
                    file.write(chunk)

        print(f"CSV file has been downloaded and saved to {save_path}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # HTTP error
    except Exception as err:
        print(f"An error occurred: {err}")  # Other errors

# Example usage
if __name__ == "__main__":
    csv_url = "https://www.data-action-lab.com/wp-content/uploads/2021/08/polls_us_election_2016.csv"  # Replace with your CSV URL
    save_file_path = "polls_us_elections_2016.csv"

    download_csv(csv_url, save_file_path)
