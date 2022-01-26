from flask import render_template, request
from app import app
import json, time
from urllib import request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


'''@app.route('/update_data')
def update_data:'''

@app.route('/test')
def test():
    if not "controller_data" in app.config:
        app.config["controller_data"] = "a"
    return json.dumps(app.config["controller_data"])

@app.route('/view')
def view():
    return render_template("view.html")



@app.route('/update_data', methods=["POST"])
def update_data():
    if request.method == 'POST':
        # print("before")
        # print(jsonstr(request.data))
        # print(json.loads(request.data)[0])
        app.config["controller_data"] = json.loads(request.data)
        # print("after")
    return "good"

# -------------------------------------------------------------
# JSON-filer til kommunikasjon mellom ROV og brukergrensesnitt

status_data = {"status_data": {
    "teller": 0,
    "tid":  0,
    "manuel": 1,
    "start": 1,
    "lys": 1,
    "manip_paa": 0,
    "depth_regulator": 0,
    "stamp_regulator": 1,
    "rull_regulator": 1,
    "lekasje": 0,
    "dybde": 0,
    "hoyde": 0,
    "temp_vann": 0,
    "aks_x": 1,
    "aks_y": 12,
    "aks_z": 12,
    "vinkel_x": 21,
    "vinkel_y": 54,
    "vinkel_z": 65,
    "strom1": 1,
    "strom2": 0.3,
    "spenn": 0.432,
    "hvf": 0,
    "hhf": 0,
    "hvb": 0,
    "hhb": 0,
    "vvf": 0,
    "vhf": 0,
    "vvb": 0,
    "vhb": 0,
    "manip1": 33,
    "manip2": -22,
    "manip3": -59,
    "manip4": -5,
    "KP_depth": 0.125,
    "KP_stamp": 0.99,
    "KP_rull": 1.44,
    "KI_depth": 0.25,
    "KI_stamp": 0.56,
    "KI_rull": 4.22,
    "KD_depth": 0.5,
    "KD_stamp": 0.24,
    "KD_rull": 5.11,
    "skalering": 50
}}


control_data = {"control_data" : {
    "venstre_x": 0,
    "venstre_y": 0,
    "hoyre_x": 0,
    "hoyre_y": 0,
    "manip1": 0,
    "manip2": 0,
    "manip3": 0,
    "manip4": 0,
    "skalering": 50,
    "manuel": 1,
    "manip_paa": 0,
    "depth_regulator": 0,
    "stamp_regulator": 0,
    "rull_regulator": 0,
    "lys": 1,
    "KP_depth":0,
    "KP_stamp":0,
    "KP_rull": 0,
    "KI_depth":0,
    "KI_stamp":0,
    "KI_rull": 0,
    "KD_depth":0,
    "KD_stamp":0,
    "KD_rull": 0,
    "tid": 0
}}

teller = 1


@app.route("/get_status_data")
def get_status_data():
    global teller
    global start

    teller = teller + 1
    tid = 0
    start = time.perf_counter()
    tid = 0.01 * round(time.perf_counter() - start, 4) + 0.99 * tid



    send = True
    
    while True:
        print("true")
        try:
            # Status data som vi mottar fra mini-PC i ROV
            status_data = {"status_data": {
                "teller": 0,
                "tid": tid,
                "manuel": 1,
                "start": 1,
                "lys": 1,
                "manip_paa": 0,
                "depth_regulator": 0,
                "stamp_regulator": 1,
                "rull_regulator": 1,
                "lekasje": 0,
                "dybde": 0,
                "hoyde": 0,
                "temp_vann": 0,
                "aks_x": 1,
                "aks_y": 12,
                "aks_z": 12,
                "vinkel_x": 21,
                "vinkel_y": 54,
                "vinkel_z": 65,
                "strom1": 1,
                "strom2": 0.3,
                "spenn": 0.432,
                "hvf": 0,
                "hhf": 0,
                "hvb": 0,
                "hhb": 0,
                "vvf": 0,
                "vhf": 0,
                "vvb": 0,
                "vhb": 0,
                "manip1": 33,
                "manip2": -22,
                "manip3": -59,
                "manip4": -5,
                "KP_depth": 0.125,
                "KP_stamp": 0.99,
                "KP_rull": 1.44,
                "KI_depth": 0.25,
                "KI_stamp": 0.56,
                "KI_rull": 4.22,
                "KD_depth": 0.5,
                "KD_stamp": 0.24,
                "KD_rull": 5.11,
                "skalering": 50
            }}
            break
        except:
            print('Kommunikasjonsfeil i get_status_data!!!')
    print(status_data)
    return status_data