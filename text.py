import tkinter as tk
from geopy.geocoders import Nominatim

class GeoLocatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Geolocation Tracker")

        self.label = tk.Label(root, text="Enter Location:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Get Location", command=self.get_location)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def get_location(self):
        location_name = self.entry.get()

        if location_name:
            try:
                geolocator = Nominatim(user_agent="geo_locator")
                location = geolocator.geocode(location_name)

                if location:
                    latitude = location.latitude
                    longitude = location.longitude
                    address = location.address

                    result_text = f"Latitude: {latitude}\nLongitude: {longitude}\nAddress: {address}"
                    self.result_label.config(text=result_text)
                else:
                    self.result_label.config(text="Location not found.")
            except Exception as e:
                self.result_label.config(text=f"Error: {str(e)}")
        else:
            self.result_label.config(text="Please enter a location.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeoLocatorApp(root)
    root.mainloop()
