# btc_pong

**Goal**

Build a 2 player pong game where the two players bet a certain amount of Bitcoin (Sats) on who will win. The winner takes all the Sats.

**Details**
- Build a fun pong game and host it in AWS, or any other place. 
- Before the 2 players start playing each person needs to deposit a certain amount of Bitcoins, lets say 200 Sats, via lighting network.
- The page (game) will hold the Sats until one of the players achieves a score of  3 points. Then, the page (game) will send all the Sats to the winner
- After the game ends, the players abandon the page or play again

**Technical details**
- As of today the game is written in Python, but this can be changed if needed
- I think BTCPay Server could be used to manage the payment.

**Next steps**
- Improve game: Make it smoother and funny
- Build the web page ()
- Get the game running on the web page and accessible to any one
- Allow for 2 people to play against each other online
- Add payment capabilities: receive payments from the payers and pay to
  the winner. Via Lighting.

