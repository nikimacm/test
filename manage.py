def decode(message_file):
    pyramid = []
    
    with open(message_file, 'r') as file:
        for line in file:
            line = line.strip().split()
            pyramid.append(line[-1])
    
    decoded_message = ' '.join(pyramid)
    return decoded_message

# Example usage:
decoded_message = decode('/text/encoded_message_list.txt')
print(decoded_message.lower().strip())