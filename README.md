# Neural-Network-plays-Flappy-Bird

An implementation of flappy bird in python, that uses an AI that is beholden to a neuroevolution of augmenting topologies algorithm. Each generation a population of birds attempts to fly through pipes. Natural selection decides which birds will pass down their traits to their children. The project allows for configuration of the window, with varying results. This project used no external libraries, and made heavy use of statistics. 

<img width="455" height="558" alt="Screenshot 2026-02-21 164907" src="https://github.com/user-attachments/assets/c3ca67fc-ea6d-43df-a9b7-38062dc9c737" />



Each bird has a neural network brain with 3 distinct nodes.
Node 1 is the distance from the bird to the top pipe.
Node 2 is the horizontal distance to the next pipe
Node 3 is the distance from the bird to the bottom pipe. 

Node 1 uses a sigmoid function where if the output value calculated is greater than .73 the bird "flaps".

Natural selection occurs at the end of each generation where all birds die. 

<img width="417" height="551" alt="Screenshot 2026-02-21 165042" src="https://github.com/user-attachments/assets/08b1be03-826d-485b-a439-296ef911ad30" />


1. Speciation - Birds are grouped into a species based on the similarity of their neural network weights.
2. fitness calculation - Determined by the lifespan of the bird, or how many frames it survived on screen.
3. Culling - any species that has not improved in 8 generations is removed
4. Reproduction - The best bird of each generation has its traits passed down to a cloned child, while the rest of the offspring contain mutations from the parent.
5. Mutation - Each connection weight is mutated for the next generation. There is an 80% chance that each weight is nudged using gaussian noise.

This game requires pygame which must be installed.

pip install pygame.


Running the project

python main.py

<img width="428" height="574" alt="Screenshot 2026-02-21 164853" src="https://github.com/user-attachments/assets/f01290ac-42ea-446c-9d45-10f26e796574" />

