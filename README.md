
Title: Pong Game Manual 
I. Game Manual
1.	Overview: Pong is a famous arcade game in which two players use paddles on opposing sides of the screen to knock a ball back and forth. The goal is to get the ball past the opponent's paddle and earn points.
2.	Controls: 
Player 1:
•	W: Move paddle up
•	S: Move paddle down
Player 2:	
•	Up arrow: Move paddle up
•	Down arrow: Move paddle down

Spacebar: Pause and unpause the game

Scoring: Each time a player gets the ball past their opponent's paddle, they score a point. The first player to reach the winning score of 5 points wins the game.
3.	Game over: When a player reaches the winning score, the game displays the winner and the game over message. The game then resets after a few seconds, and the players can start a new game.













II. Class Diagram:
+----------------+        +----------------+      +------------+
|    PongGame    |      |    Paddle      |      |    Ball    |
+----------------+         +----------------+      +------------+
| -screen_width  |<>----| -rect          |      | -rect      |
| -screen_height |      | -speed         |      | -speed     |
| -paddle_width  |      +----------------+      | -dx        |
| -paddle_height |      | +move_up()     |      | -dy        |
| -paddle_speed  |      | +move_down()   |      +------------+
| -ball_size     |      +----------------+      | +move()    |
| -ball_speed    |                                | +bounce_horizontal()
| -winning_score |                                | +bounce_vertical()
| -frame_rate    |                                +------------+
| -WHITE         |
| -BLACK         |
| -player1_score |
| -player2_score |
| -paused        |
| -screen        |
| -font          |
| -player1       |
| -player2       |
| -ball          |
| -clock         |
+----------------+
| +display_text()|
| +reset_ball()  |
| +play()        |
+----------------+

III. Original Creator's Contribution and Innovative Aspects:
The original Pong game concept is used in this Pong implementation. The code is a new implementation that makes use of the Pygame library and makes no reference to any previous implementations or the DroneInvasion project. 
• The usage of the Pygame library for a simpler and more efficient code structure is one of the game's distinctive features.
• A pause function using a spacebar that allows players to halt and continue the game. 
• An adjustable winning score and paddle speed for customizable gameplay.


IV. Work Distribution:
This project was completed by me.
