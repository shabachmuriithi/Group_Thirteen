def new_event(weekly_event, event_details):
    for daily_event in weekly_event:
        if event_details["day"] == daily_event["day"]:
           daily_event["event"].extend(event_details["event"])
 

    for daily_event in weekly_event:
        if event_details["day"] == daily_event["day"]:
           daily_event["event"].remove(event_details["event"])
   

    for daily_event in weekly_event:
        if event_details["day"] == daily_event["day"]:
           daily_event["event"]
    return weekly_event