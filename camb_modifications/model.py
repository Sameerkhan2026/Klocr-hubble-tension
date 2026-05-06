# KLOCR modification for CAMB v1.5.3
# Add this to camb/model.py in CAMBparams class
# Sameer Khan, 2026

class KLOCRParams:
    """
    KLOCR phenomenological model for CAMB
    """
    def __init__(self):
        self.alpha = 1.0835  # Sound horizon scaling
        self.beta = 0.50     # Q(K) parameter
        self.use_klocr = False

    def c_local(self, z):
        """Effective local speed of light for KLOCR"""
        if not self.use_klocr:
            return 1.0
        K = (z + 1.0) / self.alpha
        Q = 1.0 + self.beta * (K - 1.0)
        return 1.0 / (K * Q)

# Instructions:
# 1. In CAMBparams.__init__, add: self.klocr = KLOCRParams()
# 2. In get_background function, multiply sound speed by self.klocr.c_local(z)
# 3. This scales the sound horizon: rs -> rs/alpha
