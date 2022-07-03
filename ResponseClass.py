# Logic classes

class BusinessResponse():
    def __init__(self, hierarchical_step, max_duration_step_name = None, max_duration_step_duration = None):
        self.hierarchical_step = hierarchical_step
        self.max_duration_step_name = max_duration_step_name
        self.max_duration_step_duration = max_duration_step_duration


class BusinessHierarchicalStep():
    def __init__(self, id, name, duration, children):
        self.id = id
        self.name = name
        self.duration = duration
        self.children = children