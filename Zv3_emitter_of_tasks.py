"""
    This program is being used to develop code prior to using it in the normal file.
    
    This program sends a message to a queue on the RabbitMQ server after reading a csv file called tasks.csv.
    Will import the CsvReader class from the csv_reader.py module.
    Also imports socket to get the hostname of the computer running the program.
    Will import the time module to use the sleep function to simulate work.
    Pika imports are used to connect to the RabbitMQ server and send messages.
    Sys is used to get the command line arguments.
    Webbrowser is used to open the RabbitMQ Admin site.

    Screen shots in Readme.md

    Make tasks harder/longer-running by adding dots at the end of the message.

    Author: Julie Creech
    Date: February 9, 2023

"""

import pika
import sys
import webbrowser
import csv
import socket
import time

# Offer to open the RabbitMQ Admin website
def offer_rabbitmq_admin_site():
    """Offer to open the RabbitMQ Admin website"""
    show_offer = False
    #print()
    if show_offer == "True":
        ans = input("Would you like to monitor RabbitMQ queues? y or n ")
        print()
        webbrowser.open_new("http://localhost:15672/#/queues")
        print()

# Defines message sending function
def send_message(host: str, queue_name: str, message: str):
    """
    Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        host (str): the host name or IP address of the RabbitMQ server
        queue_name (str): the name of the queue
        message (str): the message to be sent to the queue
    """
    host = "localhost"
    port = 9999
    address_tuple = (host, port)

# create a socket family for IPv4
    socket_family = socket.AF_INET

# create a socket type for UDP 
    socket_type = socket.SOCK_DGRAM

# Use enumerated types to create a socket object
    sock = socket.socket(socket_family, socket_type)

# Read from file to get data
    input_file = open("tasks.csv", "r")

# Reverse Sort the file --pulling this out for now
   # reversed = sorted(input_file)

# Create a csv reader from input_file
    reader = csv.reader(input_file, delimiter=',')

# Read the first line of the file
    for row in reader:

#read a row from file
        input_file.read
        #fstring to print the row
        fstring_message = f"{row}"

        # send the message to the server
        message = fstring_message.encode()

        #use the socket to send the message to the server
        sock.sendto(message, address_tuple)
        # print a message to the console for the user
        print(f" [x] Sent {message}")
        # sleep for 5 second to simulate work
        time.sleep(5)

        
    try:
        # create a blocking connection to the RabbitMQ server
        conn = pika.BlockingConnection(pika.ConnectionParameters(host))
        # use the connection to create a communication channel
        ch = conn.channel()
        # use the channel to declare a durable queue
        # a durable queue will survive a RabbitMQ server restart
        # and help ensure messages are processed in order
        # messages will not be deleted until the consumer acknowledges
        ch.queue_declare(queue=queue_name, durable=True)
        # use the channel to publish a message to the queue
        # every message passes through an exchange
        ch.basic_publish(exchange="", routing_key=queue_name, body=message)
        # print a message to the console for the user
        print(f" [x] Sent {message}")
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)
    finally:
        # close the connection to the server
        conn.close()

# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":  
    # ask the user if they'd like to open the RabbitMQ Admin site
    offer_rabbitmq_admin_site()
    # get the message from the command line
    # if no arguments are provided, use the default message
    # use the join method to convert the list of arguments into a stringy
    # join by the space character inside the quotes
    message = " ".join(sys.argv[1:]) or "Hello World!"
    message = " ".join(sys.argv[1:]) or "{message}"
    # send the message to the queue
    send_message("localhost","task_queue3",message)