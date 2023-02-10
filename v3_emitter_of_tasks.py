"""
    This program sends a message to a queue on the RabbitMQ server after reading a csv file called tasks.csv.
    Will import the CsvReader class from the csv_reader.py module.
    Will import the time module to use the sleep function to simulate work.
    Pika imports are used to connect to the RabbitMQ server and send messages.
    Sys is used to get the command line arguments.
    Webbrowser is used to open the RabbitMQ Admin site.

    The code includes an option to open the RabbitMQ Admin site. 
    This code is set to false, but if you want to use it, change the value to True.

    The code is also set to slowly read and send the data from .csv to RabbitMQ.
    The code does not use sockets. 

    Screen shots in Readme.md

    Make tasks harder/longer-running by adding dots at the end of the message.

    Author: Julie Creech
    Date: February 9, 2023

"""

import pika
import sys
import webbrowser
import csv
import time



# Offer to open the RabbitMQ Admin website
#if show_offer is set to False, the code will not run, but if set to True, the code will run
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
def send_message(host: str, queue_name: str, message):
    """
    Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        host (str): the host name or IP address of the RabbitMQ server
        queue_name (str): the name of the queue
        message (str): the message to be sent to the queue
    """
  
        
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
        print(f" [x] Sent, {message}")
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
   #message = " ".join(sys.argv[1:]) or "Hello World!"
    #message = " ".join(sys.argv[1:]) or "{message}"
    # send the message to the queue
    #send_message("localhost","task_queue3",message)
    
    # assign the variable input_file_name to the name of the file to read
    input_file_name = "tasks.csv"

    # Open the file to read
    input_file = open(input_file_name, "r")

    # Create a csv reader object
    reader = csv.reader(input_file, delimiter=",")

    # header = next(reader)
    header_list = ["message"]

    # Get message from the file
    for row in reader:
        input_file.read
        fstring_message = f"{row}"
        message = fstring_message.encode()

        #Below converts list to a string. If the below is not done an error is thrown
        message = ",".join(row)
        # send the message to the queue
        send_message("localhost","task_queue3",message)
       
        # simulate work
        time.sleep(5)
        
    #close the file
    input_file.close()