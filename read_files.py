import pandas
from collections import defaultdict
from zipfile import ZipFile

# read campaign files from ZIP archive
# output a dictionary where the key is the file name and the value is the list of frame ids


def get_sample_campaigns(path):
    dict_campaigns = defaultdict(list)

    zip_file_path = path + "\\sample_campaigns\\" + "Sample Campaigns.zip"
    for file in ZipFile(zip_file_path).namelist()[1:]:

        df = pandas.read_csv(
            ZipFile(zip_file_path).open(file),
            header=None,
            delimiter="\t",
            encoding="UTF-8",
        )

        values = df[0].tolist()

        dict_campaigns[file] = values

    return dict_campaigns
