from posix_message_queue_wrapper import PosixMessageQueueWrapper

input_coefficients = ','.join([2,5,3])

path_name = "faas_on_iot"


# Initialising Publisher
mq_pub = PosixMessageQueueWrapper("101", "compute_coefficients", path_name)
if not mq_pub.registerPublisher('localhost', 8000):
	print('Could not register Publisher')
	exit()

# Initialising Subscriber
mq_sub = PosixMessageQueueWrapper("101", "get_roots", path_name)
if not mq_sub.registerSubscriber('localhost', 8000):
	print('Could not register Subscriber')
	exit()


mq_pub.sendMessage(input_coefficients)
recvd_msg = mq_sub.recvMessage()
print("Message: ", recvd_msg)