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
* (Use f, t, t, f to run Approximate Q Learning algo without queries and write weights to file)
* (Use t, f, f, t to run the algo. with feedback and load weights from previous run)

## Developed by
Abhiramon R. and Suraj Singh