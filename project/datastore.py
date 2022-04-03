import json
global dataset 
dataset = {
    'users': [],
    'posts':[]
}

def jsonsave(data):
    with open("ProjectData.json", "w") as fl:
        json.dump(data,fl)
        fl.close()

def jsonread():
    with open("ProjectData.json", 'r') as fl:
        dataset = json.load(fl)
        fl.close()
    return dataset