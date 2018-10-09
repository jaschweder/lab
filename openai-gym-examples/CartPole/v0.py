#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gym
import os
import pickle
import numpy as np
import math
import random
import itertools

class Individual:
    env_name = ''
    values = []
    weight = 0
    def __init__(self, env_name, values):
        self.env_name = env_name
        self.values = values
        self.calc_weight()

    def calc_weight(self):
        env = gym.make(self.env_name)
        env.reset()
        weight = 0
        for action in self.values:
            weight += 1
            observation, reward, done, info = env.step(action)
            if done:
                break
        self.weight = weight

def env_file(env):
    return ".{}".format(env)

def generate_individuals(env_name):
    individuals = []
    for values in np.random.randint(2, size=(100, 1000)):
        i = Individual(env_name, values)
        individuals.append(i)
    return individuals

def load_individuals(env_name):
    file = env_file(env_name)
    if os.path.isfile(file):
        i = open(file, 'r')
        return pickle.load(i)
    return generate_individuals(env_name)

def save_individuals(env_name, individuals):
    file = env_file(env_name)
    o = open(file, 'wb')
    pickle.dump(individuals, o)

class GA:
    env_name = ''
    generation = 1
    individuals = []

    """
    Initialize the GA with number of individuals
    """
    def __init__(self, env_name, individuals):
        self.env_name = env_name
        self.individuals = individuals

    """
    Select best 3 individuals
    """
    def selection(self):
        self.individuals = sorted(self.individuals, key=lambda x: x.weight, reverse=True)[:3]

    """
    Cross information from individuals, generating new individuals, also generate a mutation in last position in values of each individuals
    """
    def cross(self):
        new = self.individuals[:]
        for i in self.individuals:
            for j in self.individuals:

                """
                Mutations, little changes in the genetic code to generate better unique individuals
                """
                values_i = i.values
                values_i[len(values_i) - 1] = random.randint(0, 1)
                values_i[len(values_i) - 2] = random.randint(0, 1)
                values_i[len(values_i) - 3] = random.randint(0, 1)
                new_values_i = np.reshape(values_i, (2, int(round(math.floor(len(values_i) / 2)))))

                values_j = j.values
                values_j[len(values_j) - 1] = random.randint(0, 1)
                values_j[len(values_j) - 2] = random.randint(0, 1)
                values_j[len(values_j) - 3] = random.randint(0, 1)
                new_values_j = np.reshape(values_j, (2, int(round(math.floor(len(values_j) / 2)))))

                """
                Cross genes from the individuals
                """
                new_individuals = []
                for ni in new_values_i:
                    for nj in new_values_j:
                        new_individuals.append(Individual(env_name, np.concatenate((ni, nj))))
                        new_individuals.append(Individual(env_name, np.concatenate((nj, ni))))
                        #for actions in itertools.permutations(values):
                        #    new_individuals.append(Individual(env_name, actions))

                new = np.concatenate((new, new_individuals))

        self.individuals = new

    """
    Check if condition was reached
    """
    def condition_hit(self):
        for i in self.individuals:
            if i.weight == 0:
                return True

        return False

    """
    Print 10 best results
    """
    def print_summary(self):
        individuals = sorted(self.individuals, key=lambda x: x.weight, reverse=True)[:10]
        print("-" * 98)
        print("Summary: ")
        print("-" * 98)
        idx = 0
        for i in individuals:
            idx += 1
            print("{:02d}: {:d}".format(idx, i.weight))

        print("-" * 98)
        print("Generation: {:d}".format(self.generation))
        print("-" * 98)
    """
    Run the GA with a minimum of :min_generations: for the solution
    """
    def run(self, min_generations=100):
        self.generation = 1
        while self.generation < min_generations:
            self.selection()
            self.cross()
            self.generation = self.generation + 1

if __name__ == "__main__":
    env_name = 'CartPole-v0'
    env = gym.make(env_name)
    individuals = load_individuals(env_name)
    ga = GA(env_name, individuals)
    ga.run(100)
    ga.print_summary()
    individuals = ga.individuals
    save_individuals(env_name, individuals)
