from collections import deque
class EventProcessingSystem:
    def __init__(self):
        self.event_queue = deque()
    def add_event(self, event_name):
        self.event_queue.append(event_name)
        print(f"Event '{event_name}' added to the queue.") 
    def process_next_event(self):
        if self.event_queue:
            event = self.event_queue.popleft()
            print(f"Processing event: {event}")
        else:
            print("No events to process.") 
    def display_pending_events(self):
        if self.event_queue:
            print("Pending events:", list(self.event_queue))
        else:
            print("No pending events.") 
    def cancel_event(self, event_name):
        if event_name in self.event_queue:
            self.event_queue.remove(event_name)
            print(f"Event '{event_name}' has been canceled.")
        else:
            print(f"Event '{event_name}' not found in the queue.")            
if __name__ == "__main__":
    system = EventProcessingSystem()
    while True:
        print("\n--- Event Processing System ---")
        print("1. Add Event")
        print("2. Process Next Event")
        print("3. Display Pending Events")
        print("4. Cancel Event")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            event_name = input("Enter event name: ")
            system.add_event(event_name) 
        elif choice == "2":
            system.process_next_event()
        elif choice == "3":
            system.display_pending_events()
        elif choice == "4":
            event_name = input("Enter event name to cancel: ")
            system.cancel_event(event_name) 
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")   
