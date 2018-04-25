import os.path

def paraula_existeix(paraula):
    return os.path.isfile("videos/" + paraula.lower() + ".mp4")

def url(paraula):
    paraula = paraula.lower();
    if paraula_existeix(paraula):
        return "../backend/videos/" + paraula + ".mp4"
    else:
        return "SenseResultat"
