import time
import threading

# Global state representing an event or condition
event_occurred = False

def trigger_event(delay=0.5):
    """Simulates an external system triggering an event after a delay."""
    global event_occurred
    print(f"\n[{time.time():.2f}] External system: Event will be triggered in {delay}s...")
    time.sleep(delay)
    event_occurred = True
    print(f"[{time.time():.2f}] External system: Event triggered!")

def wait_for_event_flawed(timeout=3):
    """
    A flawed wait function: it 'consumes' the event by resetting the flag
    after detecting it, preventing subsequent waits from succeeding for the *same* event.
    """
    global event_occurred
    start_time = time.time()
    print(f"[{time.time():.2f}] Flawed wait: Waiting for event (timeout={timeout}s)...")
    while time.time() - start_time < timeout:
        if event_occurred:
            print(f"[{time.time():.2f}] Flawed wait: Event detected!")
            # THE FLAW: The wait step itself resets the condition it's waiting for.
            # This makes it a one-time check for this specific flag state.
            event_occurred = False
            return True
        time.sleep(0.1) # Polling interval
    print(f"[{time.time():.2f}] Flawed wait: Timeout - event not detected.")
    return False

def wait_for_event_correct(timeout=3):
    """
    A correct wait function: it checks the event flag without modifying it.
    The flag's state management (setting/resetting) is external to the wait logic.
    """
    global event_occurred
    start_time = time.time()
    print(f"[{time.time():.2f}] Correct wait: Waiting for event (timeout={timeout}s)...")
    while time.time() - start_time < timeout:
        if event_occurred:
            print(f"[{time.time():.2f}] Correct wait: Event detected!")
            # CORRECT: The wait step does NOT modify the condition it's waiting for.
            # External logic is responsible for resetting the flag if a new event is desired.
            return True
        time.sleep(0.1) # Polling interval
    print(f"[{time.time():.2f}] Correct wait: Timeout - event not detected.")
    return False

def reset_event_state():
    """Resets the global event state for a new test scenario."""
    global event_occurred
    event_occurred = False
    print(f"\n[{time.time():.2f}] Event state reset for new scenario.")

# --- DEMONSTRATION SCENARIOS ---

print("--- Scenario 1: Flawed Wait - Works once, then stops ---")
reset_event_state()
# Start a thread to trigger the event
threading.Thread(target=trigger_event, args=(0.5,)).start()
time.sleep(0.1) # Give trigger thread a moment to start

# First attempt to wait: This will succeed
print("\nAttempt 1 with flawed wait:")
wait_for_event_flawed(timeout=2)

# Second attempt to wait for the *same* event: This will fail because the flag was reset
print("\nAttempt 2 with flawed wait (expecting failure):")
wait_for_event_flawed(timeout=2) # Fails because event_occurred was set to False by the first wait

print("\n--- Scenario 2: Correct Wait - Works multiple times for the same event ---")
reset_event_state()
# Start a thread to trigger the event
threading.Thread(target=trigger_event, args=(0.5,)).start()
time.sleep(0.1) # Give trigger thread a moment to start

# First attempt to wait: This will succeed
print("\nAttempt 1 with correct wait:")
wait_for_event_correct(timeout=2)

# Second attempt to wait for the *same* event: This will also succeed
# because the 'correct' wait function does not modify the event_occurred flag.
print("\nAttempt 2 with correct wait (expecting success):")
wait_for_event_correct(timeout=2)

print("\n--- Scenario 3: Correct Wait - Waiting for distinct events ---")
reset_event_state()
print("\nFirst event cycle:")
threading.Thread(target=trigger_event, args=(0.5,)).start()
time.sleep(0.1)
wait_for_event_correct(timeout=2)

reset_event_state() # External system resets state for a new, distinct event
print("\nSecond event cycle:")
threading.Thread(target=trigger_event, args=(0.5,)).start()
time.sleep(0.1)
wait_for_event_correct(timeout=2)
