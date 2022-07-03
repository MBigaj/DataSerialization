import messages_pb2
from RequestClass import BusinessRequest, BusinessStep


def MapToBusinessRequest(dto: messages_pb2.Request):
    steps = []
    for step in dto.steps:
        steps.append(MapToBusinessStep(step))

    if dto.HasField('step_id'):
        b_req = BusinessRequest(steps, dto.step_id)
    else:
        b_req = BusinessRequest(steps, None)
    return b_req


def MapToBusinessStep(dto: messages_pb2.Request.Step):
    if dto.HasField('parent_id'):
        b_step = BusinessStep(dto.id, dto.duration, dto.name, dto.parent_id)
    else:
        b_step = BusinessStep(dto.id, dto.duration, dto.name, None)
    return b_step