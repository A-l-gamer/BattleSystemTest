# Introduction
This short project was my attempt to model and thus quickly experiment with the combat system for Heralds - a board game I'm working on.

Put symply, when a player attacks an other, both roll a number of custom six-sided dice (d6) equal to the number of forces involved in the battle. I was seeking to find which custom faces for the dice gave the expected outcomes.

The attacking and defending players rolled different dice, and each face had any combination of the following symbols:
- An explosion: Deals 1 damage to opponent forces
- A shield: Blocks 1 damage that would have been dealt to own forces
- A skull: Deals 1 damage to own foces

For each damage dealt, a force is removed.

# The model
To find how favourable attacking j tanks with my i, I wanted to produce a nxn matrix, where each entry represented my expected chance of victory for such battle. However, since most battles don't lead to a clear victory or defeat, I had to do this iteratively, where I looked at the probability of reaching each possible outcome, and how favourable that would be.
This was possible to do as no battle removed forces or left them unchanged; it was impossible for either player to end with more forces than when they attacked.

Key to the iteration, was defining the boundary quality of outcomes.
I did as follows:
If the attacker wiped out the defender and not itself: quality = 1.
If the attacker was wiped out and not the defender: quality = 0.
If both were wiped out, this wasn't as clear, but after some playtesting I reached the conclusion that quality = 0.25 was a good model. We call this variable alpha.

One can interpret the quality of an attack as the probability of eventually winning if they keep attacking until either side is defeated. This is imperfect as there's the possible case of elliminating both sides, whose quality of outcome is very case dependent.

# Outcome
The following is the outcome matrix with n = 9, a = 0.25, and the following dices:
attackDice = [[0,0], [0,0], [1,0], [1,0], [1,0], [2,1]]
defenceDice = [[0,0], [0,0], [-1,0], [-1,0], [0,1], [-1,1]]
<img width="802" height="512" alt="image" src="https://github.com/user-attachments/assets/676890d5-5083-4968-948c-4d5e98795e75" />
