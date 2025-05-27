def new_event(weekly_event, event_details):
    for daily_event in weekly_event:
        if event_details["day"] == daily_event["day"]:
            if isinstance(event_details["event"], list):
                daily_event["event"].extend(event_details["event"])
            else:
                daily_event["event"].append(event_details["event"])
            return weekly_event

    weekly_event.append({
        "day": event_details["day"],
        "event": [event_details["event"]]
    })
    return weekly_event

def remove_event(weekly_event, event_details):
    for daily_event in weekly_event:
        if event_details["day"] == daily_event["day"]:

            if isinstance(event_details["event"], list):
                for evt in event_details["event"]:
                    if evt in daily_event["event"]:
                        daily_event["event"].remove(evt)
            else:
                if event_details["event"] in daily_event["event"]:
                    daily_event["event"].remove(event_details["event"])
            if not daily_event["event"]:
                weekly_event.remove(daily_event)
            return weekly_event
    return weekly_event


def list_events(weekly_event, day):
    for daily_event in weekly_event:
        if daily_event["day"] == day:
            return daily_event["event"]
    return []

weekly_event = [{"day": "Monday", "event": ["Meeting"]}, {"day": "Tuesday", "event": ["Concert"]}]

event_details_add = {"day": "Tuesday", "event": "Workshop"}
print(new_event(weekly_event, event_details_add))

event_details_remove = {"day": "Tuesday", "event": "Concert"}
print(remove_event(weekly_event, event_details_remove))

print("Tuesday events:", list_events(weekly_event, "Tuesday"))
print("Monday events:", list_events(weekly_event, "Monday")) 
