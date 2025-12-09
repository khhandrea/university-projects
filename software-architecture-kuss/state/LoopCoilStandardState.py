from state import StateBase

class LoopCoilStandardState(StateBase):
    
    def action(self, loop_coil, detected):
        loop_coil._detected = detected

        if detected == True:
            return f"[{loop_coil.get_pos()}] 코일이 감지되었습니다."
        else:
            
            return f"[{loop_coil.get_pos()}] 코일 감지가 해제되었습니다."