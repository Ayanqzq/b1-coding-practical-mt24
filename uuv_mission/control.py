class PDController:
    def __init__(self, Kp: float, Kd: float) :
        self.Kp = Kp
        self.Kd = Kd
        self.prev_error = 0.0  # lasrt error for derivative term

    def compute(self,  observation: float, reference: float) -> float:
        e_t = reference - observation
        de = e_t - self.prev_error
        u_t = self.Kp * e_t + self.Kd * de
        self.prev_error = e_t  # update error for next time
        return u_t
