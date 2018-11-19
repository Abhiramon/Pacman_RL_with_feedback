# AI_Project
Reinforcement learning with human feedback implemented in Pacman environment

## About
This work is built upon the UC Berkley's Pacman environment (http://ai.berkeley.edu/home.html).
The program uses Approximate Q learning algorithm for reinforcement learning. Additional features are provided to incentivize Pacman to hunt and eat scared ghosts. Human feedback can also be provided in the form of weight adjustments for the features. With 36 trial runs, with and without feedback, we recorded an improvement of about 20 percent in score using the feedback mechanism.

## Setup
Requires Python2

## Usage instructions
* Move into src directory using "cd src"
* Normal game can be run using "python pacman.py"
* To run the Approximate Q Learning agent use: "python2 pacman.py -p ApproximateQAgent -a extractor=SimpleExtractorPellet -x 0 -n 4 -l mediumClassic" where 0 is for number of training runs and 4 is for total number of runs. This command can also be run using "bash run.sh"
* Option: Read from file - is for loading feature weights from previous run
* Option: Write to file - is for storing weights after runs to lead next time
* Option: Explore - To choose a random action with a probability (Required for learning).
* Option: Use queries - To give feedback after next 3 games
* (To run RL without feedback use: f, f, t, f )
* (To run RL with feedback use: f, f, t, t )

## Feedback mechanism
Feedback can be provided by adding/decreasing importance of following:
1. bias
2. run into scared ghosts 1 step away
3. run into non-scared ghosts 1 step away
4. eat food
5. distance to closest food
6. hunt scared ghost

To increase importance of a feature use *+*, to decrease importance use *-*.

For example:  
* 6 + (Increase importance of hunting scared ghost)
* 3 - (Increase importance of running from normal ghost)
* -1 -1 (End of feedback)

## Experiments with feedback
1. Use f, t, t, f to run with exploration, without feedback and write weights to file. (We used this for 3 episodes to allow agent to learn some basic rules)
2. Use t, f, f, t to load weights and use feedback without exploration. (We used this for 4 episodes to test feedback mechanism)
3. Use t, f, f, f to load same weights and run without feedback or exploration. (We ran this 4 times as well)

Comparision of performance in 2 and 3 will show the effect of using feedback.

The results of our experiments are documented in results.txt

## Developed by
Abhiramon R. and Suraj Singh