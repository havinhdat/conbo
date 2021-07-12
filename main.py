import csv
import requests

DATA_FILE = "data.csv"
OUTPUT_DIR = "out"


def is_downloadable(url):
    h = requests.head(url)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def download_file(url, new_name):
    original_name = url.split('/')[-1]
    extension = original_name.split(".")[-1]
    local_filename = f"{new_name}.{extension}"

    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(f"{OUTPUT_DIR}/{local_filename}", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


if __name__ == '__main__':
    with open(DATA_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        first_record = True
        for row in csv_reader:
            if first_record:
                first_record = False
                continue
            file_name = row[0].strip()
            download_url = row[1].strip()

            if not is_downloadable(download_url):
                print(f"ERROR: {file_name} is not downloadable (wrong content type)")
            else:
                download_file(download_url, file_name)
