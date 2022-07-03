from RequestClass import BusinessStep
from ResponseClass import BusinessHierarchicalStep

def MapToHierarchicalStep(b_step :BusinessStep):
    return BusinessHierarchicalStep(b_step.id, b_step.name, b_step.duration, [])