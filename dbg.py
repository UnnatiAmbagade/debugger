import sys

class Dbg:
    def __init__(self):
        self.locals = {}

    def _breakpoint(self):
        frame = sys._getframe(1)  # Get the caller's stack frame
        self.locals = frame.f_locals.copy()

    def get_variables(self):
        return self.locals

dbg = Dbg()
sys.breakpointhook = dbg._breakpoint  # Override default breakpoint hook
