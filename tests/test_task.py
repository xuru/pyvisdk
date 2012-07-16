import unittest, types
from pyvisdk import Vim
from tests.common import get_options
from pyvisdk.facade.task import TaskManager

def nothing():
    pass

def random_string(n):
    import random
    import string
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(n))

TASKS = ['hello world',
         'I hate VMware',
         'This is a very long task name, a very very long name',
         'school sucks',
         'one more',
         'last one']

class Test_Task(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)
        cls.manager = TaskManager(cls.vim)
        cls.obj = cls.vim.getHostSystems()[0]
        cls.cleanUpStaleTasks()

    @classmethod
    def cleanUpStaleTasks(cls):
        for task in cls.manager._managed_object.recentTask:
            if task.info.state in ['running', 'queued']:
                task.SetTaskState('error', None, None)

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def test_task(self):
        with self.manager.task(self.obj, TASKS[0]):
            pass

    def test_task__error(self):
        with self.assertRaises(Exception):
            with self.manager.task(self.obj, TASKS[1]):
                raise Exception()

    def test_wrap(self):
        task = self.manager.task(self.obj, TASKS[2])
        func = task.wraps(nothing)
        func()

    def test_step(self):
        task = self.manager.task(self.obj, TASKS[3])
        task.step([nothing, nothing, nothing])

    def test_step_manually(self):
        with self.manager.task(self.obj, TASKS[4]) as task:
            task.update_progress(10)
            task.update_progress(20)
            task.update_progress(90)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHosts']
    unittest.main()

