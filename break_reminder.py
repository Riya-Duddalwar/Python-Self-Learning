import time

import schedule
from plyer import notification


def send_break_alert(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5,
    )


def hydration_alert():
    send_break_alert("Hydration Alert", "Time to drink some water!")


def posture_check():
    send_break_alert("Posture Check", "Sit straight and relax your shoulders.")


def main():
    schedule.every(10).seconds.do(hydration_alert)
    schedule.every(20).seconds.do(posture_check)

    print("Break reminder is running. Press Ctrl+C to stop.")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReminder stopped. Take care of yourself!")


if __name__ == "__main__":
    main()
