import sys
from cleaneventinput import EventInput
from eventdetails import Event

cleaner = EventInput()
e = Event()

event_name_raw = sys.argv[1]
date = sys.argv[2]
time = sys.argv[3]
place_raw = sys.argv[4]
host_first_raw = sys.argv[5]
host_last_raw = sys.argv[6]

event_name_clean = cleaner.clean_event_name(event_name_raw)
place_clean = cleaner.clean_place(place_raw)
host_clean = cleaner.clean_name(host_first_raw, host_last_raw)

e.set_event_name(event_name_clean)
e.set_date(date)
e.set_time(time)
e.set_place(place_clean)
e.set_host(host_clean)

e.write_to_event()
