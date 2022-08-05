# Space Invaders
A clone of famous space invaders game built using python turtle.
<div>
  <img src="./code_output.JPG" alt="Code Output">
</div>
  
<hr>
<h1> Program Flowchart</h1>
  <div>
    <img src="./Space Invaders Flowchart.png" alt="Program Flowchart">
  </div>
<hr>

# Guide to build this Project

<h3> Step 1: Deciding the Structure </h3>
<p>
  The first thing we do is breakdown the entire code into various subproblems. We tackle each of these problems using OOP paradigm. 
  We have the spacecraft object, alien ships object, then a collection of these alien ships objects, bullet object, a scoreboard object, and finally, an ui object.
</p>

<h3> Step 2: Initial Screen Setup and Our Spacecraft </h3>
<p>
  Using the <em> Screen </em> class of turtle, we create an object to create and control our screen. Use <em> mainloop </em> method to keep the screen on.
  Using this object's methods, we setup it's dimensions, title, and give it a background image. Remember that turtle only works with gif format images. <br>
  To setup our spacecraft, we create a separate python file, create a class, give the turtle the shape using a gif image using its <em> shape </em> method. 
  We have three gifs for it, which we assign randomly. Remember that this will work only if we have registered that gif using screen object in main.py using it's 
  <em> addshape </em> method. We use coordinate system of turtle's screen to place the spacecraft at bottom of screen. Use <em> screen </em> object's <em> tracer </em>
  and <em> update() </em> method to control animation. Turtle is only shown after its position and its shape is set. Then we define two methods of this turtle, which
  makes it move left and right using <em> backward </em> and <em> forward </em> methods of turtle.
</p>

<h3> Step 3: The Loop to Run the Game and Shooting some Bullets </h3>
<p>
  First of all, setup four screen listeners, left, right, up to shoot and p to pause the game. 
  Define a function that will reverse the value of a boolean variable everytime it is called. This is to maintain pause and resume functionality of game.
  To make our spacecraft shoot a bullet, we create another class in separate python file. Define a turtle with circular shape stretched vertically to make it look
  like a bullet. The spacecraft will have another attribute, a list of bullets. And a new method, <em> shoot </em>. 
  The shoot function creates a new object from <em> Bullet </em> class, make it go to coordinates of spacecraft, but a little upward and then append it to list of 
  bullets. <br>
  In the main.py, an infinite while loop is setup, delayed some milliseconds using <em> time </em> module of python. Inside it, if the game is not paused,
  then we keep updating the screen and make all the bullets in the list of bullets of spacecraft keep moving forward.
</p>

<h3> Step 4: Creating our <i>Alien Spacecrafts</i> </h3>
<p>
  Aliens are created similarly to spacecraft and bullets. We have to classes, <em> AlienShip </em>, which is an individual alien spacecraft, 
  a turtle given the shape of a gif image and has an attribute, quantity. <em> Aliens </em> which is the list of all those individual alien spacecrafts. 
  We define a method in <em> Aliens </em> class to create multiple alien ships and place them in a certain way on the screen, 
  and call this method inside <em> def __init__(self) </em>.
  Go back to main.py, create an object from <em> Aliens </em> class, then we can see our aliens. In the loop where we are making all our bullet move forward, 
  we nest another for loop iterating on all alien ships, see if the bullet got close enough, reduce the quantity of the alienship, which if fall to zero,
  then ship is first sent outside visible window dimensions, and then removed, the bullet is also removed in a similar way.
</p>

<h3> Step 5: Making Aliens move </h3>
<p>
  We use time module, to record seconds when program was started, as then seconds for every iteration, the moment the gap is 5 seconds between the two recorded time
  periods, we make the alien go down by decreasing their y coordinates. The we make the starting seconds equal to current seconds. We also make a condition,
  that if y coordinate of any alien ship is below a certain point, the the user has lost the game.
</p>

<h3> Step 6: The Scoreboard and UI </h3>
<p>
  Whenever we were recoding the alien ships being shot by our bullets, we increase the score. The scoreboard is another class, created in a separate python file
  where the class inherits the <em> Turtle class of turtle </em> module. The turtle is hidden, it's pen pulled up, and then we use <em>write</em> method to
  write some text on screen. Similarly we create UI class, which writes <em>Space Invaders</em> on screen and make them change colors every few milliseconds 
  whenever we pause the game. There also <em> sleep </em> method of <em> time </em> module is used. We also show texts when game is over. The text varies depending
  on whether the user won or lost.
</p>

<hr>
