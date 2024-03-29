#import gym
import Game
import random
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import median, mean
from collections import Counter
from tqdm import tqdm

LR = 1e-3
env = Game.Game()
env.reset()
goal_steps = 1000
score_requirement = -400.34*2#(turns-turns/2)
initial_games = 50000

def some_random_games_first():
    # Each of these is its own game.
    for episode in range(5):
        env.reset()
        # this is each frame, up to 200...but we wont make it that far.
        for t in range(200):
            # This will display the environment
            # Only display if you really want to see it.
            # Takes much longer to display it.
            env.render()
            
            # This will just create a sample action in any environment.
            # In this environment, the action can be 0 or 1, which is left or right
            action = env.action_space.sample()
            
            # this executes the environment with an action, 
            # and returns the observation of the environment, 
            # the reward, if the env is over, and other info.
            observation, reward, done, info = env.step(action)
            if done:
                break
                
#some_random_games_first()

def initial_population():
    # [OBS, MOVES]
    training_data = []
    # all scores:
    scores = []
    # just the scores that met our threshold:
    accepted_scores = []
    # iterate through however many games we want:
    for _ in tqdm(range(initial_games)):
        score = 0
        # moves specifically from this environment:
        game_memory = []
        # previous observation that we saw
        prev_observation = []
        # for each frame in 200
        for _ in range(goal_steps):
            # choose random action (0 or 1)
            action = [random.randrange(0,4),random.randrange(0,3),random.randrange(0,12),
                      random.randrange(0,11),random.randrange(0,3),random.randrange(0,2)]
            # do it!
            
            observation, reward, done, info = env.step(action)
            
            # notice that the observation is returned FROM the action
            # so we'll store the previous observation here, pairing
            # the prev observation to the action we'll take.
            if len(prev_observation) > 0 :
                game_memory.append([prev_observation, action])
            prev_observation = observation
            score+=reward
            if done: break
        # IF our score is higher than our threshold, we'd like to save
        # every move we made
        # NOTE the reinforcement methodology here. 
        # all we're doing is reinforcing the score, we're not trying 
        # to influence the machine in any way as to HOW that score is 
        # reached.
        if score >= score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                # convert to one-hot (this is the output layer for our neural network)
                output = [0]*35
                output[data[1][0]] = 1
                output[data[1][1]+3] = 1
                output[data[1][2]+6] = 1
                output[data[1][3]+18] = 1
                output[data[1][4]+29] = 1
                output[data[1][5]+32] = 1
                    
                # saving our training data
                training_data.append([data[0], output])
        # reset env to play again
        env.reset()
        # save overall scores
        scores.append(score)
    
    # just in case you wanted to reference later
    training_data_save = np.array(training_data)
    np.save('NAN.npy',training_data_save)
    
    # some stats here, to further illustrate the neural network magic!
    print('Average accepted score:',mean(accepted_scores))
    print('Median score for accepted scores:',median(accepted_scores))
    print(Counter(accepted_scores))
    
    return training_data

def initial_population_from_model(model):
    # [OBS, MOVES]
    training_data = []
    # all scores:
    scores = []
    # just the scores that met our threshold:
    accepted_scores = []
    # iterate through however many games we want:
    for _ in tqdm(range(initial_games)):
        observation = env.reset()
        score = 0
        # moves specifically from this environment:
        game_memory = []
        # previous observation that we saw
        prev_observation = observation
        # for each frame in 200
        for _ in range(goal_steps):
            # choose random action (0 or 1)
            obs = model.predict(observation.reshape(-1,len(observation),1))[0]
            
            action = [np.argmax(obs[0:4]),np.argmax(obs[4:7]),np.argmax(obs[7:19]),
                      np.argmax(obs[19:30]),np.argmax(obs[30:33]),np.argmax(obs[33:35])]
            # do it!
            
            observation, reward, done, info = env.step(action)
            
            # notice that the observation is returned FROM the action
            # so we'll store the previous observation here, pairing
            # the prev observation to the action we'll take.
            if len(prev_observation) > 0 :
                game_memory.append([prev_observation, action])
            prev_observation = observation
            score+=reward
            if done: break
        # IF our score is higher than our threshold, we'd like to save
        # every move we made
        # NOTE the reinforcement methodology here. 
        # all we're doing is reinforcing the score, we're not trying 
        # to influence the machine in any way as to HOW that score is 
        # reached.
        if score >= score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                # convert to one-hot (this is the output layer for our neural network)
                output = [0]*35
                output[data[1][0]] = 1
                output[data[1][1]+3] = 1
                output[data[1][2]+6] = 1
                output[data[1][3]+18] = 1
                output[data[1][4]+29] = 1
                output[data[1][5]+32] = 1
                    
                # saving our training data
                training_data.append([data[0], output])
        # reset env to play again
        
        # save overall scores
        scores.append(score)
    
    # just in case you wanted to reference later
    training_data_save = np.array(training_data)
    np.save('NAN.npy',training_data_save)
    
    # some stats here, to further illustrate the neural network magic!
    print('Average accepted score:',mean(accepted_scores))
    print('Median score for accepted scores:',median(accepted_scores))
    print(Counter(accepted_scores))
    
    return training_data



def train_model(training_data, model=False):

    X = np.array([i[0] for i in training_data]).reshape(-1,len(training_data[0][0]),1)
    y = [i[1] for i in training_data]

    if not model:
        model = neural_network_model(input_size = len(X[0]))
    
    model.fit({'input': X}, {'targets': y}, n_epoch=10, snapshot_step=500, show_metric=True, run_id='openai_learning')
    return model

def neural_network_model(input_size):

    network = input_data(shape=[None, input_size, 1], name='input')

    network = fully_connected(network, 512, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 1028, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 1028*2, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 1028, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 512, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 256, activation='relu')
    network = dropout(network, 0.8)
    network = fully_connected(network, 128, activation='relu')
    network = dropout(network, 0.8)
    network = fully_connected(network, 64, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 35, activation='relu')
    network = regression(network, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')
    model = tflearn.DNN(network, tensorboard_dir='log')

    return model




#training_data = np.load('saved.npy',allow_pickle=True)

training_data = initial_population()
model = train_model(training_data)

count = 0
while True:
    count +=1
    training_data = initial_population_from_model(model)
    input()
    model = train_model(training_data,model)
    if count == 5:
        c = int(input("countine?"))
        if c == 1:
            pass
        else:
            break



scores = []
choices = []
for each_game in range(10):
    score = 0
    game_memory = []
    prev_obs = []
    env.reset()
    for _ in range(goal_steps):

        if len(prev_obs)==0:
            action = [random.randrange(0,4),random.randrange(0,3),random.randrange(0,12),
                      random.randrange(0,11),random.randrange(0,3),random.randrange(0,2)]
        else:
            obs = model.predict(prev_obs.reshape(-1,len(prev_obs),1))[0]
            action = [np.argmax(obs[0:4]),np.argmax(obs[4:7]),np.argmax(obs[7:19]),
                      np.argmax(obs[19:30]),np.argmax(obs[30:33]),np.argmax(obs[33:35])]

        choices.append(action)
                
        new_observation, reward, done, info = env.step(action)
        prev_obs = new_observation
        game_memory.append([new_observation, action])
        score+=reward
        if done: break

    scores.append(score)

print('Average Score:',sum(scores)/len(scores))

print(score_requirement)

model.save("uy.model")


model.load("uy.model")
