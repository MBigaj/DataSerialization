import messages_pb2
from ResponseClass import BusinessResponse, BusinessHierarchicalStep


def MapToProtobufResponse(b_res: BusinessResponse):
    res = messages_pb2.Response()

    res.max_duration_step_name = b_res.max_duration_step_name
    res.max_duration_step_duration = b_res.max_duration_step_duration

    hierarchical_step = MapHierarchicalStepToProtobuf(b_res.hierarchical_step)
    res.hierarchical_step.name = hierarchical_step.name
    res.hierarchical_step.duration = hierarchical_step.duration

    for child in hierarchical_step.children:
        res.hierarchical_step.children.append(child)

    return res


def MapHierarchicalStepToProtobuf(hierarchical_step: BusinessHierarchicalStep):
    dto_hierarch_step = messages_pb2.Response.HierarchicalStep()

    dto_hierarch_step.name = hierarchical_step.name
    dto_hierarch_step.duration = hierarchical_step.duration

    for child in hierarchical_step.children:
        dto_hierarch_step.children.append(MapHierarchicalStepToProtobuf(child))

    return dto_hierarch_step
