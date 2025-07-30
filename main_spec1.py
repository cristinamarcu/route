import json
from read_files import get_sample_campaigns
from post_request import *
from credentials import *



def read_json(path, file):
    with open(path + "\\" + file, "r") as f:
        data = json.load(f)
        f.close()
    return data


def campaign_body(frames_list):

    campaign = {
        "schedule": [
            {"datetime_from": "2025-03-03 00:00", "datetime_until": "2025-03-09 00:00"}
        ],
        "spot_length": 10,
        "spot_break_length": 50,
        "frames": frames_list,
    }

    return campaign


def get_data_by_campaign():

    request_json = read_json(path, "request_body.json")

    campaigns = get_sample_campaigns(path + "\\" + "sample_campaigns")

    output_path = path + "\\outputs_spec1\\"

    for campaign in campaigns.keys():

        frames_list = campaigns[campaign]

        current_campaign = campaign_body(frames_list)

        request_json["campaign"] = []

        request_json["campaign"].append(current_campaign)

        response = get_data(url, username, password, apikey, request_json)

        output_file_name = f"{campaign}_response.json"

        with open(output_path + "\\" + output_file_name, "w") as f:
            json.dump(response, f)


get_data_by_campaign()

