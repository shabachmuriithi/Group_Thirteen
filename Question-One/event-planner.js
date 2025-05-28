class EventPlanner {
    constructor() {
        this.events = {
            'Sunday': [],
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],
            'Saturday': []
        };
    }
    addEvent(day, event) {
     if (this.events[day]) {
            this.events[day].push({
                day : day,
                details: event
            });
        }
    }
    removeEvent(day, eventId) {
        if (this.events[day]) {
            const index = this.events[day].findIndex(e => e.id === eventId);
            if (index !== -1) {
                this.events[day].splice(index, 1);
            }
        }
    }
    listEvents(day) {
        return this.events[day] || [];
    }
}
const monday = new EventPlanner();
monday.addEvent("Monday", "Live coding");
monday.addEvent("Monday", "Project deadline");
monday.addEvent('Monday', "Google trip")
console.log(monday.listEvents("monday"));
const tuesday= new EventPlanner();
tuesday.addEvent("Tuesday", "Start ideation")
console.log(tuesday.listEvents("tuesday"))
monday.removeEvent('Monday', "Live coding")
console.log(monday.listEvents('monday'))