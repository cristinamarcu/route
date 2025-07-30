import json
from read_files import get_sample_campaigns
from post_request import *
from credentials import *


campaign_name = "{R51_UndergroundStation-LondonDigital}_Schd1_W100.txt"


def read_json(path, file):
    with open(path + "\\" + file, "r") as f:
        data = json.load(f)

        f.close()

    return data


def campaign_body(frame):

    campaign = {
        "schedule": [{"date": "2025-07-21"}],
        "spot_length": 10,
        "spot_break_length": 50,
        "frames": frame,
    }

    return campaign


def get_data_by_quarter_hour(campaign_name):

    request_json = read_json(path, "request_body_spec2.json")

    campaigns = get_sample_campaigns(path + "\\" + "sample_campaigns")

    frames_list = campaigns[campaign_name]

    output_path = path + "\\outputs_spec2\\"

    for frame in frames_list:

        frame_to_list = []

        frame_to_list.append(frame)

        current_campaign = campaign_body(frame_to_list)

        request_json["campaign"] = []

        request_json["campaign"].append(current_campaign)

        response = get_data(url, username, password, apikey, request_json)

        output_file_name = f"{campaign_name}_response_spec2_{frame}.json"

        with open(output_path + "\\" + output_file_name, "w") as f:
            json.dump(response, f)


get_data_by_quarter_hour(campaign_name)
