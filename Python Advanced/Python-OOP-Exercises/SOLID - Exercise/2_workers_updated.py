from abc import ABC, abstractmethod
import time


class Workable(ABC):
    @abstractmethod
    def work(self):
        ...


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        ...


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Workable):
    def work(self):
        print("I'm a robot. I'm working....")


class BaseManager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, Workable), f"`worker` must be of type {Workable}"

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, Eatable), f"`worker` must be of type {Eatable}"

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()

worker = Worker()
work_manager.set_worker(worker)
break_manager.set_worker(worker)
work_manager.manage()
break_manager.lunch_break()

super_worker = SuperWorker()
work_manager.set_worker(super_worker)
break_manager.set_worker(super_worker)
work_manager.manage()
break_manager.lunch_break()

robot = Robot()
work_manager.set_worker(robot)
work_manager.manage()

break_manager.set_worker(robot)