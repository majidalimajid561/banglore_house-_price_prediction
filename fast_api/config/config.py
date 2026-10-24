import joblib
try:
    with open('../models/valid_locations.pkl','rb') as f:
        VALID_LOCATIONS=joblib.load(f)
        print("done")
except:
    raise "Location did not load"

