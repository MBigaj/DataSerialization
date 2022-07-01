import messages_pb2
from RequestClass import BusinessRequest, BusinessStep


def MapToBusinessRequest(dto: messages_pb2.Request):
    steps = []
    for step in dto.steps:
        steps.append(MapToBusinessStep(step))
    b_req = BusinessRequest(steps, dto.step_id)
    return b_req


def MapToBusinessStep(dto: messages_pb2.Request.Step):
    b_step = BusinessStep(dto.id, dto.duration, dto.name, dto.parent_id)
    return b_step