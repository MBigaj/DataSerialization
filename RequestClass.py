# Logic classes

class BusinessRequest():
    def __init__(self, steps, step_id = None):
        self.steps = steps
        self.step_id = step_id


class BusinessStep():
    def __init__(self, id, duration, name, parent_id = None):
        self.id = id
        self.parent_id = parent_id
        self.duration = duration
        self.name = name