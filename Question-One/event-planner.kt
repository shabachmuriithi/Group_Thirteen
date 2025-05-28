fun main(){
    val eventManager = EventPlanner()
    eventManager.addEvent("Monday", "Live coding")
    eventManager.addEvent("Monday", "Project deadline")
    eventManager.addEvent("Monday", "Google trip")
    eventManager.listEvents("Monday")
    eventManager.removeEvent("Monday", "Live coding")
    eventManager.listEvents("Monday")
}


data class Event(val details: String)

class EventPlanner {
    private val events: MutableMap<String, MutableList<Event>> = mutableMapOf()

    fun addEvent(day: String, eventDetails: String) {
        val event = Event(eventDetails)
        if (events.containsKey(day)) {
            events[day]?.add(event)
        }
        else {
            events[day] = mutableListOf(event)
        }
        println("Event added on $day: $eventDetails")
    }

    fun removeEvent(day: String, eventDetails: String) {
        val eventToRemove = Event(eventDetails)
        if (events[day]?.remove(eventToRemove) == true) {
            println("Event removed from $day: $eventDetails")
        }
        else {
            println("Event not found on $day: $eventDetails")
        }
    }

    fun listEvents(day: String) {
        if (events.containsKey(day)) {
            println("Events on $day:")
            events[day]?.forEach { event -> println("- ${event.details}") }
        } else {
            println("No events scheduled for $day")
        }
    }
}