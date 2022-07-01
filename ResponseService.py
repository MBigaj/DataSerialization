from RequestClass import BusinessRequest, BusinessStep
from ResponseClass import BusinessResponse, BusinessHierarchicalStep
from business_mapper import MapToHierarchicalStep


def FindStepChildren(potential_children, parent_id):
    step_children = []

    for potential_child in potential_children:
        if potential_child.parent_id == parent_id:
            step_children.append(potential_child)

    return step_children



def DoBusinessLogic(req: BusinessRequest):
    if req.step_id != None:
        root_step_id = req.step_id
        for step in req.steps:
            if step.id == root_step_id:
                first_step = step
                break
    else:
        for step in req.steps:
            if step.parent_id == None: # Potential Root
                if root_step_id == None: # If the root is unknown
                    root_step_id = step.id
                    first_step = step
                else:
                    raise(' Cannot have 2 null parent_id elements! ')

    # first_step
    # root_step_id

    root_response_step = MapToHierarchicalStep(first_step)

    resp = BusinessResponse()

    step_children = FindStepChildren(req.steps, root_step_id)

    for child in step_children:
        step_children_2 = FindStepChildren(req.steps, child.parent_id)
