from plyer import gps

def start_gps():
    gps.configure(on_location=on_location)
    gps.start()

def on_location(**kwargs):
    print("GPS Location:", kwargs)
