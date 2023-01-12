from multiprocessing import Process, Queue
from time import sleep

class ExampleMultiProcessClass(Process):
    """
        Demonstration multiprocessing class.
    """

    def __init__(self, report_out_queue: Queue, number: int=0):
        super(ExampleMultiProcessClass, self).__init__()
        self.report_out_queue: Queue = report_out_queue
        self.number: int = number

    @staticmethod
    def example_method(number: int) -> int:
        """
            An example method just takes and integer and adds one.
        """
        return number + 1

    def run(self):
        """
            When run is called the default method is start within the class.

            Will simple take an initial integer.

            call the example method

            load that integer onto out queue.
        """
        print("Starting")
        while True:
            self.number: int = self.example_method(number=self.number)
            print("Putting number!")
            self.report_out_queue.put(self.number)
            sleep(1)
