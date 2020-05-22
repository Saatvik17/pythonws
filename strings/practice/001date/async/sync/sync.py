from timeit import default_timer
import requests

def load_data(delay):
    print(f"Starting {delay} second timer")
    text = requests.get(f"https://httpbin.org/delay/{delay}").text
    print(f"Completed {delay} second timer")
    return text 

def run_exe():
    start_time = default_timer()

    task_two = load_data(2)
    task_three = load_data(3)

    elapsed_time = default_timer() - start_time

    print(f"The program took {elapsed_time:.2} seconds")

def main():
    run_exe()

main()