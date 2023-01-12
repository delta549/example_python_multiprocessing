from multiprocessing_example.example_multiprocess_class import ExampleMultiProcessClass
from multiprocessing import Queue
from time import sleep

if __name__ == "__main__":
    """
        The main loop for the module.
    """

    print("Starting main")

    # Create a report Queue
    report_queue: Queue = Queue()
    initial_integer: int  = 0
    

    # Instantiate the class.
    empc = ExampleMultiProcessClass(report_out_queue=report_queue, number=initial_integer)

    # Start the process.
    empc.start()

    # Start blocking loop to detected integer change.
    while True:
        print("getting number!")
        print(report_queue.get())
        sleep(3)

