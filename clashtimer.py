import sys
import time
import winsound

argv = sys.argv
exit = sys.exit

events = {"0": 0, "1": 0.5, "2": 0.4}

def calculate_time(original_time, gold_pass_reduction = 0, event = 0, builder_potions = 0):
    gold_pass_reduction = 1 - gold_pass_reduction
    event = 1 - events[str(event)]

    reduced_time = original_time * gold_pass_reduction * event

    if builder_potions > 0:
        return max(reduced_time / 10, reduced_time - 9 * builder_potions)

    return reduced_time


def validate_input(original_time, gold_pass_reduction, event, builder_potions):
    # Original Time must be greater than 0
    if original_time <= 0:
        return False

    # Gold Pass Reduction must be between 0 and 1
    if not 0 <= gold_pass_reduction <= 1:
        return False

    # Event Index must exist in events
    if str(event) not in events:
        return False

    # Builder Potion Amount must be non-negative
    if builder_potions < 0:
        return False

    # Valid Input
    return True


def normalizeHours(hours):
    total_minutes = round(hours*60)

    d = total_minutes // (24*60)
    h = (total_minutes % (24*60)) // 60
    m = total_minutes % 60
    return f"{d}d {h}h {m}min"


def countdown(hours):
    remaining_seconds = round(hours * 3600)
    end_time = time.monotonic() + remaining_seconds

    try:
        while True:
            remaining = max(0, round(end_time - time.monotonic()))

            days, remaining = divmod(remaining, 86400)
            hours, remaining = divmod(remaining, 3600)
            minutes, seconds = divmod(remaining, 60)

            print(
                f"\rTime {days}d {hours:02}h {minutes:02}m {seconds:02}s",
                end="",
                flush=True
            )

            if remaining == 0 and time.monotonic() >= end_time:
                break

            time.sleep(1)

        print("\nTime's up!")

        sound = r"C:\Windows\Media\Alarm05.wav"
        winsound.PlaySound(
            sound,
            winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC
        )
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            winsound.PlaySound(None, winsound.SND_PURGE)
            print("\nTimer Stopped.")

    except KeyboardInterrupt:
        print("\nTimer Stopped.")


if __name__ == "__main__":
    if len(argv) != 5:
        """argv:                 [0]             [1]                [2]            [3]         [4]     """
        print("Usage: python clashtimer.py <original_time> <gold_pass_reduction> <event> <builder_potions>")
        exit(1)
    try:
        original_time, gold_pass_reduction, event, builder_potions = int(argv[1]), float(argv[2]), int(argv[3]), int(argv[4])
        if not validate_input(original_time, gold_pass_reduction, event, builder_potions):
            print("Usage: python clashtimer.py <original_time (int: hours)> <gold_pass_reduction (float: 0 <= gold_pass_reduction <= 1)> <event (0: None, 1: Hammer Jam, 2: Summer Jam)> <builder_potions (int: amount)>")
            exit(1)

        remaining_time = calculate_time(original_time, gold_pass_reduction, event, builder_potions)
        print(f"Total Remaining Time: {normalizeHours(remaining_time)} (total: {round(remaining_time)}h)\n")
        countdown(remaining_time)
    except(ValueError):
        print("Usage: python clashtimer.py <original_time (int: hours)> <gold_pass_reduction (float: 0 <= gold_pass_reduction <= 1)> <event (0: None, 1: Hammer Jam, 2: Summer Jam)> <builder_potions (int: amount)>")
        exit(1)