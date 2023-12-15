#run_application(). A function that will run app.py and print the output if ran successfully, otherwise will return False.

#a function that will be able to run the run_application() 100 times, and store the results in a listimport subprocess

def run_application():
    try:
        result = subprocess.run(["python", "app.py"], check=True, text=True, capture_output=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"app.py failed with error: {e}")
        return False

def run_application_multiple_times():
    results = []
    for _ in range(100):
        result = run_application()
        results.append(result)
    return results
