# streaming-04-multiple-consumers

> Use RabbitMQ to distribute tasks to multiple workers

One process will create task messages. Multiple worker processes will share the work. 


## Before You Begin

1. Fork this starter repo into your GitHub.
1. Clone your repo down to your machine.
1. View / Command Palette - then Python: Select Interpreter
1. Select your conda environment. 

## Read

1. Read the [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
1. Read the code and comments in this repo.

## RabbitMQ Admin 

RabbitMQ comes with an admin panel. When you run the task emitter, reply y to open it. 

(Python makes it easy to open a web page - see the code to learn how.)

## Execute the Producer

1. Run emitter_of_tasks.py (say y to monitor RabbitMQ queues)

Explore the RabbitMQ website.

## Execute a Consumer / Worker

1. Run listening_worker.py

Will it terminate on its own? How do you know?  No it will not because the code indicates you must Ctrl+C to exit.

## Ready for Work

1. Use your emitter_of_tasks to produce more task messages.

## Start Another Listening Worker 

1. Use your listening_worker.py script to launch a second worker. 

Follow the tutorial. 
Add multiple tasks (e.g. First message, Second message, etc.)
How are tasks distributed? I opened two listeners and two producers. Round Robin was how the listeners received the packages no matter if it was sent from producer 1, 2 or 3 (including the VSCode terminal as well). 
Monitor the windows with at least two workers. 
Which worker gets which tasks? It is round robin, so they take turns.


## Reference

- [RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)


## Screenshot

See a running example with at least 3 concurrent process windows here:
The first screenshot shows the two producers and two listeners. The second screenshot shows how the producer was the VS Code terminal. It also participated in sending, and the listeners received them via a round robin method.
![Screenshot Creech Ex1_a](https://user-images.githubusercontent.com/89232631/217982154-b4f4f79f-f104-4e42-a047-91aacd85bfb8.jpg)
![Screenshot Creech Ex1_b](https://user-images.githubusercontent.com/89232631/217982228-a053ed8c-f84c-48d6-845f-93852c8f9804.jpg)
