import sys
import datetime
import json
import yaml
from growatt import hash_password, GrowattApi, Timespan

username = "ooandioo"
password = "oobieneoo0706"

with GrowattApi() as api:
    api.login(username, password)
    plant_info = api.plant_list()
    print("Plant Info: " + str(yaml.load(json.dumps(plant_info))))

    plant_id = str(plant_info["data"][0]["plantId"])
    print("Plant Detail: " + str(yaml.load(json.dumps(api.plant_detail(plant_id, Timespan.day, datetime.date.today())))))
    print("User Center Energy Data: " + str(yaml.load(json.dumps(api.get_user_center_energy_data()))))

    device_list = api.get_all_device_list(plant_id)
    print("Device List: " + str(yaml.load(json.dumps(device_list))))

    storage_sn = str(device_list["deviceList"][0]["deviceSn"])
    print("Storage SN: " + storage_sn)

    print("Energy Overview: " + str(yaml.load(json.dumps(api.get_energy_overview_data(plant_id, storage_sn)))))
    #print("System Status: " + str(yaml.load(json.dumps(api.get_system_status_data(plant_id, storage_sn)))))
    #print("Storage Energy: " + str(yaml.load(json.dumps(api.get_storage_energy_data(plant_id, storage_sn, "2020-05-15")))))
    #print("Energy Prod and Cons: " + str(yaml.load(json.dumps(api.get_energy_prod_and_cons_data(plant_id, storage_sn, "2020-05-15")))))
    #print("Storage Params: " + str(yaml.load(json.dumps(api.get_storage_params(storage_sn)))))