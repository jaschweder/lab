#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import math
import random

class Individual:
    values = []
    weight = math.inf

    def __init__(self, values):
        self.values = np.array(values)
        self.weight = abs(sum(values) - 2000)

class GA:
    generation = 1
    individuals = []

    """
    Initialize the GA with number of individuals
    """
    def __init__(self, individuals):
        self.individuals = individuals

    """
    Select best 3 individuals
    """
    def selection(self):
        self.individuals = sorted(self.individuals, key=lambda x: x.weight)[:3]

    """
    Cross information from individuals, generating new individuals, also generate a mutation in last position in values of each individuals
    """
    def cross(self):
        new = []
        for i in self.individuals:
            for j in self.individuals:

                """
                Mutations, little changes in the genetic code to generate better unique individuals
                """
                values_i = i.values
                values_i[len(values_i) - 1] = random.randint(1, 255)
                values_i[len(values_i) - 2] = random.randint(1, 255)
                values_i[len(values_i) - 3] = random.randint(1, 255)
                new_values_i = np.reshape(values_i, (2, math.floor(len(values_i) / 2)))

                values_j = j.values
                values_j[len(values_j) - 1] = random.randint(1, 255)
                values_j[len(values_j) - 2] = random.randint(1, 255)
                values_j[len(values_j) - 3] = random.randint(1, 255)
                new_values_j = np.reshape(values_j, (2, math.floor(len(values_j) / 2)))

                """
                Cross genes from the individuals
                """
                new_individuals = []
                for ni in new_values_i:
                    for nj in new_values_j:
                        new_individuals.append(Individual(np.concatenate((ni, nj))))

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
    Print 25 best results
    """
    def print_summary(self):
        individuals = sorted(self.individuals, key=lambda x: x.weight)[:25]
        print("-" * 98)
        print("Summary: ")
        print("-" * 98)
        idx = 0
        for i in individuals:
            idx += 1
            print("{:02d}: [{:s}] = {:4d} ({:3d})".format(idx, " ".join("{:3d}".format(x) for x in i.values), i.values.sum(), i.weight))

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
    individuals = [
        Individual([ 72, 147, 218, 203, 122, 142,  91, 197, 144,  67, 153,  24,   2, 196,  68,  13, 131,  51, 142, 246]),
        Individual([230,  46,  92,  66,  45,  77, 123,  97, 137,   0,   7,  16,  40, 120, 148,  93, 217,  88,  45, 164]),
        Individual([ 29, 245,   9,  92, 245,   2, 219, 139, 248, 143, 247, 178, 182, 235, 172, 156,  89,  43, 184, 172]),
        Individual([254, 162,  67,  60,  62, 131,  52, 232,  57,  31, 221, 181,  37, 186,  44,  93,  20, 208, 174,   6]),
        Individual([135, 100, 194, 103, 236, 141,  38, 149,  73, 165,  81, 155, 174, 214, 151, 192, 177, 135,  66, 130]),
        Individual([ 38, 162, 222, 150, 121,  70, 175, 150,  13, 122,  60,  77, 228, 73, 228, 206,  77, 191, 244,  97]),
        Individual([227,  77, 253, 191, 211,  85, 189,   6, 244,  45, 226,  20, 249, 115, 152,  62, 147, 235, 140, 196]),
        Individual([187, 200,   1,  82, 251,  78, 217, 254,  21, 209, 101,  47, 198, 104, 181, 210,  49,  27,  11, 168]),
        Individual([ 62, 123,  82, 206, 125, 120,  85, 172,  55,  57,  16, 112, 164, 43, 104, 148,  94,  14, 175,  39]),
        Individual([246,  35,  80,  94, 179, 180, 233,  19, 226,  99, 123, 131, 162, 79, 180, 216, 176,  68, 214, 191])
    ]

    ga = GA(individuals)
    ga.run()
    ga.print_summary()
