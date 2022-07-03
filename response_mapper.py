import messages_pb2
from ResponseClass import BusinessResponse, BusinessHierarchicalStep


def MapToProtobufResponse(b_res: BusinessResponse):
    dto_res = messages_pb2.Response()

    dto_res.max_duration_step_name = b_res.max_duration_step_name
    dto_res.max_duration_step_duration = b_res.max_duration_step_duration

    hierarchical_step = MapHierarchicalStepToProtobuf(b_res.hierarchical_step)
    dto_res.hierarchical_step.name = hierarchical_step.name
    dto_res.hierarchical_step.duration = hierarchical_step.duration

    for child in hierarchical_step.children:
        dto_res.hierarchical_step.children.append(child)

    return dto_res


def MapHierarchicalStepToProtobuf(hierarchical_step: BusinessHierarchicalStep):
    dto_hierarch_step = messages_pb2.Response.HierarchicalStep()

    dto_hierarch_step.name = hierarchical_step.name
    dto_hierarch_step.duration = hierarchical_step.duration

    for child in hierarchical_step.children:
        dto_hierarch_step.children.append(MapHierarchicalStepToProtobuf(child))

    return dto_hierarch_step
