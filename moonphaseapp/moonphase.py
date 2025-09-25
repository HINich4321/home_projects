import datetime
from zoneinfo import ZoneInfo
import ephem
import tkinter as tk
from PIL import ImageTk, Image
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# get times in local timezone
local_tz = ZoneInfo('America/Chicago')
now = datetime.datetime.now(local_tz)
yesterday = datetime.datetime.now(local_tz) - datetime.timedelta(days=1)
tomorrow = datetime.datetime.now(local_tz) + datetime.timedelta(days=1)
formatted_date = now.strftime("%Y/%m/%d")

# get current moon phase percentage
current_phase = ephem.Moon(now).moon_phase * 100

# get previous and next major moon phases
prev_phase = ephem.Moon(yesterday).moon_phase * 100
next_phase = ephem.Moon(tomorrow).moon_phase * 100

# Create main window
root = tk.Tk()
root.title("Moon Phase App")
root.geometry("650x400+400+250")
root.configure(bg="#000038")
root.resizable(width=True, height=True)

# get what phase of the moon it is currently
if current_phase == 0:
    #new moon
    moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock0.jpg")))
    phase_label = tk.Label(root, text=f"Phase: New Moon", bg="#000038", fg='#ff0')
elif 0 < current_phase <= 5.55555555556:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock1.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Crescent", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock35.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Crescent", bg="#000038", fg='#ff0')
elif 5.55555555556 < current_phase <= 11.1111111111:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock2.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Crescent", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock34.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Crescent", bg="#000038", fg='#ff0')
elif 11.1111111111 < current_phase <= 16.6666666667:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock3.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Crescent", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock33.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Crescent", bg="#000038", fg='#ff0')
elif 16.6666666667 < current_phase <= 22.2222222222:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock4.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Crescent", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock32.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Crescent", bg="#000038", fg='#ff0')
elif 22.2222222222 < current_phase <= 27.77777777789:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock5.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Crescent", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock31.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Crescent", bg="#000038", fg='#ff0')
elif 27.7777777778 < current_phase <= 33.3333333334:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock6.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Crescent", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock30.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Crescent", bg="#000038", fg='#ff0')
elif 33.3333333334 < current_phase <= 38.8888888889:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock7.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Crescent", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock29.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Crescent", bg="#000038", fg='#ff0')
elif 38.8888888889 < current_phase <= 44.4444444445:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock8.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Crescent", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock28.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Crescent", bg="#000038", fg='#ff0')
elif 44.4444444445 < current_phase <= 50:
    # First Quarter
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock9.jpg")))
        phase_label = tk.Label(root, text=f"Phase: First Quarter", bg="#000038", fg='#ff0')
    # Last Quarter
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock27.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Crescent", bg="#000038", fg='#ff0')
elif 50 < current_phase <= 55.5555555556:
    # First Quarter
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock10.jpg")))
        phase_label = tk.Label(root, text=f"Phase: First Quarter", bg="#000038", fg='#ff0')
    # Last Quarter
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock26.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Last Quarter", bg="#000038", fg='#ff0')
elif 55.5555555556 < current_phase <= 61.1111111112:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock11.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Gibbous", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock25.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Last Quarter", bg="#000038", fg='#ff0')
elif 61.1111111112 < current_phase <= 66.6666666667:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock12.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Gibbous", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock24.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Gibbous", bg="#000038", fg='#ff0')
elif 66.6666666667 < current_phase <= 72.2222222223:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock13.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Gibbous", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock23.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Gibbous", bg="#000038", fg='#ff0')
elif 72.2222222223 < current_phase <= 77.7777777778:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock14.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Gibbous", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock22.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Gibbous", bg="#000038", fg='#ff0')
elif 77.7777777778 < current_phase <= 83.3333333334:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock14.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Gibbous", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock22.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Gibbous", bg="#000038", fg='#ff0')
elif 83.3333333334 < current_phase <= 88.888888889:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock15.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Gibbous", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock21.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Gibbous", bg="#000038", fg='#ff0')
elif 88.888888889 < current_phase <= 94.4444444445:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock16.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Gibbous", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock20.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Gibbous", bg="#000038", fg='#ff0')
elif 94.4444444445 < current_phase < 100:
    # waxing
    if prev_phase < current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock17.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waxing Gibbous", bg="#000038", fg='#ff0')
    # waning
    elif prev_phase > current_phase:
        moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock19.jpg")))
        phase_label = tk.Label(root, text=f"Phase: Waning Gibbous", bg="#000038", fg='#ff0')
elif current_phase == 100:
    # full moon
    moon_img = ImageTk.PhotoImage(Image.open(resource_path("moonclock18.jpg")))
    phase_label = tk.Label(root, text=f"Phase: Full Moon", bg="#000038", fg='#ff0')
else:
    print("Error")

# get dates and times of major moon phases
next_new_moon = ephem.next_new_moon(now)
next_first_quarter_moon = ephem.next_first_quarter_moon(now)
next_full_moon = ephem.next_full_moon(now)
next_last_quarter_moon = ephem.next_last_quarter_moon(now)

# Create a label widget
now_label = tk.Label(root, text=f"Today's Date: {formatted_date}", bg="#000038", fg='#ff0')
current_phase_label = tk.Label(root, text=f"Illumination: {current_phase:.2f}", bg="#000038", fg='#ff0')
next_moons_label = tk.Label(root, text=f"Next Full Moon: {next_full_moon}\n\n"
                                       f"Next Last Quarter Moon: {next_last_quarter_moon}\n\n"
                                       f"Next New Moon: {next_new_moon}\n\n"
                                       f"Next First Quarter Moon: {next_first_quarter_moon}", bg="#000038", fg='#ff0')
moon_img_label = tk.Label(root, image=moon_img)

# Pack the label into the window
now_label.pack(side=tk.TOP)
current_phase_label.pack(side=tk.TOP)
phase_label.pack(side=tk.TOP)
next_moons_label.pack(side=tk.RIGHT, anchor=tk.E)
moon_img_label.pack(side=tk.LEFT, anchor=tk.W)

# Start the main event loop
root.mainloop()
