# https://github.com/keanureano/cpu-scheduling
from matplotlib import pyplot as plt


def main():
    # Example processes:
    processes = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 8),
        Process("P4", 3, 6),
        Process("P5", 4, 7),
        Process("P6", 5, 2),
        Process("P7", 6, 4),
        Process("P8", 7, 6),
        Process("P9", 8, 5),
        Process("P10", 9, 3),
        Process("P11", 10, 7),
        Process("P12", 11, 4),
        Process("P13", 12, 6),
        Process("P14", 13, 2),
        Process("P15", 14, 8),
        Process("P16", 15, 5),
        Process("P17", 16, 9),
        Process("P18", 17, 3),
        Process("P19", 18, 6),
        Process("P20", 19, 4),
    ]

    # Get the user's choice of scheduling algorithm
    choice = get_user_choice()

    # Run the selected scheduling algorithm and obtain the schedule
    schedule_history = run_scheduler(processes.copy(), choice)

    # Display the selected schedule
    if schedule_history:
        plot_schedule(schedule_history, choice)


class Process:
    def __init__(self, name, arrival_time, burst_time):
        # Process constructor to initialize process attributes
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time


def fcfs(processes):
    # First-Come-First-Serve scheduling algorithm
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    history = []

    for process in processes:
        # Check if the process arrives after the current time
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        # Add process to history with the current time
        history.append((process.name, current_time))
        current_time += process.burst_time

    return history


def round_robin(processes, time_quantum):
    # Round-Robin scheduling algorithm
    queue = processes.copy()
    current_time = 0
    history = []

    while queue:
        # Get the next process from the front of the queue
        process = queue.pop(0)

        # Add process to history with the current time
        history.append((process.name, current_time))

        # Check if the process still has remaining burst time
        if process.remaining_time > time_quantum:
            current_time += time_quantum
            process.remaining_time -= time_quantum
            # Add the process back to the queue if it has remaining burst time
            queue.append(process)
        else:
            current_time += process.remaining_time
            process.remaining_time = 0

    return history


def get_user_choice():
    # Function to get the user's choice of scheduling algorithm
    options = {"1": "First Come First Serve", "2": "Round Robin"}
    print("Choose a scheduling algorithm:")
    print("1. First-Come-First-Serve (FCFS)")
    print("2. Round-Robin (RR)")
    selected_choice = options[input("Enter the number of your choice: ")]
    print(selected_choice)
    return selected_choice


def run_scheduler(processes, algorithm_choice):
    # Function to run the selected scheduling algorithm
    if algorithm_choice == "First Come First Serve":
        return fcfs(processes)
    elif algorithm_choice == "Round Robin":
        time_quantum = int(input("Enter the time quantum for Round-Robin: "))
        return round_robin(processes, time_quantum)
    else:
        print("Invalid choice. Please enter a valid number.")


def plot_schedule(schedule_history, schedule_title):
    # Extract time and process data for plotting
    times = [item[1] for item in schedule_history]
    processes = [item[0] for item in schedule_history]

    # Plot the schedule
    plt.step(times, processes, where="post", marker="o", color="b")

    # Add labels for each point on the plot
    for i, (process, time) in enumerate(schedule_history):
        plt.text(time, process, f"{process}", ha="left", va="bottom")

    plt.title(schedule_title)
    plt.xlabel("Time")
    plt.ylabel("Process")
    plt.show()


if __name__ == "__main__":
    main()
