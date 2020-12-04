import time
import asyncio, concurrent, threading

class DoThing:
    def __init__(self):
        self.something = True
        self.running = True

    def start_async(self):
        print("Starting async")
        #self.thread = threading.Thread(target=self.do_the_loop)
        #self.thread.start()
        pool = concurrent.futures.ThreadPoolExecutor()
        pool.submit(asyncio.run, self.do_the_loop())

    def shutdown(self):
        self.running = False
        print("Shutting down and waiting for thread to complete")
        #self.thread.join()
        concurrent.futures.ThreadPoolExecutor().shutdown()
        print("Thread complete")

    async def do_the_loop(self):
        while self.running:
            print("Running the loop")
            time.sleep(10)

class Parent:
    def __init__(self):
        print("Making the DoThing")
        self.thing = DoThing()
        print("Starting the async command")
        self.thing.start_async()

    def shutdown(self, return_code):
        self.thing.shutdown()
        print("Exiting program")
        exit(return_code)

    def go(self):
        for i in range(0,100000):
            if i % 10000 == 0:
                print("We're at " + str(i))
            counter = 0
            while counter < 10000:
                counter += 1
        self.shutdown(0)

p = Parent()
p.go()
