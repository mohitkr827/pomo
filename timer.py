import time
from plyer import notification  

class PomodoroTimer:
    def __init__(self, work_minutes=25, break_minutes=5, rounds=4):
        self.work_minutes = work_minutes
        self.break_minutes = break_minutes
        self.rounds = rounds

    def countdown(self, minutes, message):
        seconds = minutes * 60
        while seconds:
            time.sleep(1)
            seconds -= 1
        notification.notify("Pomodoro Timer", message)

    def run(self):
        notification.notify("Pomo", "Pomodoro Timer Started! 🍅")
        for round in range(1, self.rounds + 1):
            self.countdown(self.work_minutes, f"Round {round}: Time's up! Take a break.")
            if round < self.rounds:
                self.countdown(self.break_minutes, "Break's over! Back to work.")
        notification.notify("Pomodoro Timer", "All rounds completed! Great job! 🎉", duration=10)