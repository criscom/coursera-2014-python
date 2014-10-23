#Week 02

##Event driven programming

Event => Handler => executes code

for each event you write a handler

handler = function

* Input events
  * Button
  * Text box

* Keyboard events
  * Key down
  * Key up

* Mouse events 
  *  Click
  *  Drag

* Timer events

##Global and local variables 

>any var defined outside of a function =  global variable  
everything you define within a function is a local variable  
always use local variables unless you have a specific reason not to  

###Update a global variable in a function

```python
num = 4

def fun():
  global num
  num = 5```

  ###Simple Guy

  ####Seven step process
  #####Check list

  1. Globals (state)
  2. Helper functions
  3. Classes
  4. Define event handlers
  5. Create a frame
  6. Register event handlers
  7. Start frame & timers

  #####Example

  `import simplegui`

  1. Define global variable  (programm state)
  
  `counter = 0`

  2. Define helper functions

```python
def increment():
  global counter 
  counter = counter + 1```

  4. Define event handlers

  ```python
  def tick():
         increment()
         print counter

     def buttonpress():
         global counter
         counter = 0```

  5. Create a frame

  ```frame = simplegui.create_frame("Simple GUI Test", 100, 100)```

  6. Register event handlers

  ```timer = simplegui.create_timer(1000, tick)```
  ```frame.add_button("Click me!", buttonpress)```

  7. Start frame & timers

  ```frame.start()```
  ```timer.start()```


##Assignment for Week2
###Guess the number

>Player one chooses a number between 0 and 100
