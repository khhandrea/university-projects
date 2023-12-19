from state import StateBase

class LoopCoilBrokenState(StateBase):
    
    def action(self, loop_coil, detected):
        return None