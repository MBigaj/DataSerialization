import messages_pb2
from request_mapper import MapToBusinessRequest

req = messages_pb2.Request()

# step1 = messages_pb2.Request.Step()
# step2 = messages_pb2.Request.Step()
# step3 = messages_pb2.Request.Step()
# step4 = messages_pb2.Request.Step()

# step1.id = 1
# step1.parent_id = 3
# step1. duration = 5
# step1.name = 'First'
#
# step2.id = 2
# step2.parent_id = 1
# step2. duration = 5
# step2.name = 'Second'
#
# step3.id = 3
# step3. duration = 10
# step3.name = 'Third'
#
# step4.id = 4
# step4.parent_id = 3
# step4. duration = 5
# step4.name = 'Fourth'
#
#
# req.steps.append(step1)
# req.steps.append(step2)
# req.steps.append(step3)
# req.steps.append(step4)
#
#
# with open("./messages_serialized", "wb") as f:
#     f.write(req.SerializeToString())

with(open('./messages_serialized', 'rb') as file):
	req.ParseFromString(file.read())


# Assigning proto Request to created BusinessClass
b_req = MapToBusinessRequest(req)

# print(b_req.steps)