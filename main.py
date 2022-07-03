import messages_pb2
from request_mapper import MapToBusinessRequest
from BusinessLogicService import DoBusinessLogic
from data_generator import generate_data
from ResponseClass import BusinessResponse
from response_mapper import MapToProtobufResponse

# Function that generates a serialized message
generate_data()



def DataSerializer(req: messages_pb2.Request):
	b_req = MapToBusinessRequest(req)

	business_result = DoBusinessLogic(b_req)

	response = BusinessResponse(business_result, business_result.max_duration_step_name, business_result.max_duration_step_duration)

	protobuf_response = MapToProtobufResponse(response)

	# print(protobuf_response.__str__())

	return protobuf_response.SerializeToString()


def main():
	req = messages_pb2.Request()

	with(open('./messages_serialized', 'rb') as file):
		req.ParseFromString(file.read())

	serialized_response = DataSerializer(req)

	print(f'Response: {serialized_response.__str__()}')

	with(open('./response_serialized', 'wb') as file):
		file.write(serialized_response)



if __name__ == '__main__':
    main()
