from RequestClass import BusinessRequest, BusinessStep
from ResponseClass import BusinessResponse, BusinessHierarchicalStep
from business_mapper import MapToHierarchicalStep


def RecurrentFindAndMapToHierarchical(parent: BusinessHierarchicalStep, potential_children, max_duration_step_name = None, max_duration_step_duration = float('-inf')):
    children = FindAndMapToHierarchical(potential_children, parent.id)
    sorted_children = sorted(children, key=lambda x: x.duration, reverse= True)
    parent.children = sorted_children

    sum_of_durations_of_children = 0
    max_duration_step_duration_from_children = float('-inf')
    max_duration_step_name_from_children = ''

    for child in parent.children:
        parent, duration, max_duration_step_duration_from_children, max_duration_step_name_from_children = RecurrentFindAndMapToHierarchical(child, potential_children, max_duration_step_name, max_duration_step_duration)
        sum_of_durations_of_children += duration


    this_exact_duration = parent.duration - sum_of_durations_of_children

    if this_exact_duration > max_duration_step_duration_from_children:
        max_duration_step_duration = this_exact_duration
        max_duration_step_name = parent.name
    else:
        max_duration_step_duration = max_duration_step_duration_from_children
        max_duration_step_name = max_duration_step_name_from_children

    return parent, parent.duration, max_duration_step_duration, max_duration_step_name


def FindAndMapToHierarchical(potential_children, parent_id):
    step_children = []

    for potential_child in potential_children:
        if potential_child.parent_id == parent_id:
            step_children.append(MapToHierarchicalStep(potential_child))

    return step_children


def DisplayHierarchy(hierarchy, prefix = ""):
    print(prefix, hierarchy.id, hierarchy.name)
    for child in hierarchy.children:
        DisplayHierarchy(child, prefix + "---")



def DoBusinessLogic(req: BusinessRequest):
    root_step_id = None

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

    first_step = MapToHierarchicalStep(first_step)

    full_hierarchy, duration, max_duration_step_duration, max_duration_step_name = RecurrentFindAndMapToHierarchical(first_step, req.steps)

    full_hierarchy.duration = duration
    full_hierarchy.max_duration_step_duration = max_duration_step_duration
    full_hierarchy.max_duration_step_name = max_duration_step_name

    DisplayHierarchy(full_hierarchy)

    return full_hierarchy