"""
H-E Selector™ — Reference Implementation (non-executable)
Copyright © 2025 Sébastien Favre-Lecca
Licensed under Apache 2.0
"""

def he_score(IG, C, R, E, beta1=0.33, beta2=0.33, beta3=0.34, gamma=0.1):
    """
    Compute illustrative H-E score according to Model E principles.
    J = β₁·IG + β₂·C + β₃·R − γ·E
    (Normalized values between 0 and 1)
    """
    return beta1*IG + beta2*C + beta3*R - gamma*E
