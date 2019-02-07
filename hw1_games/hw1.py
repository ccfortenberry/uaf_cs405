import random

class Agent:
	# Base class for "Intelligent" Agents
	# Based off the tic tac toe example
	
	# ctor
	def __init__(self, team, environment):
		self.percepts = []
		self.team = team
		self.environment = Environment(environment.width, environment.height)
		self.nextMove = (0, 0)
		self.availableMoves = []
		self.lastMove = (0, 0)
	
	def sense(self, percepts, environment):
		self.percepts.append(percepts)
		
		self.availableMoves = environment.getPossibleMoves()
		self.lastMove = environment.lastMove
		if self.lastMove[2] != 0:
			self.environment.put(self.lastMove[0], self.lastMove[1], self.lastMove[2])
	
	def think(self):
		# What should we get for lunch today?
		''' This comment style allows the progam to compile '''
	
	def action(self):
		return self.nextMove

class Environment:
	# Environment for the "Intelligent" Agent
	# Also based off of the tic tac toe example
	
	#ctor
	def __init__(self, width, height):
		self.board = [[0 for i in range(width)] for j in range(height)]
		self.width = width
		self.height = height
		self.lastMove = (0, 0)
		self.reset()
	
	def reset(self):
		for j in range(self.height):
			for i in range(self.width):
				self.board[j][i] = 0

	def resetRandom(self):
		turn = 0
		self.reset()
		x = [(i, j) for i in range(self.width)
			for j in range(self.height)]
		random.shuffle(x)
		count = 0
		for i, j in x:
			if turn == 0:
				self.board[j][i] = 1
			else:
				self.board[j][i] = 2
			turn = 1 - turn
			count = count + 1
			# print(self)
			# print("Turn: {}, Team 1: {}, Team 2: {}".format(
			# 	count, self.countPossibleWins(1), self.countPossibleWins(2)))
			# print(self.getPossibleMoves())

	def __str__(self):
		# The environment, but as a string
		s = ""
		for j in range(self.height):
			s = s + "[ "
			for i in range(self.width):
				s = s + str(format(self.board[j][i], "01d")) + " "
			s = s + "]"
			if j < self.height-1:
				s = s + "\n"
		return s

	def get(self, col, row):
		if row < 0 or row > self.height - 1:
			return 0
		if col < 0 or col > self.width - 1:
			return 0
		return self.board[row][col]

	def put(self, col, row, piece):
		if row < 0 or row > self.height - 1:
			return
		if col < 0 or col > self.width - 1:
			return
		self.lastMove = (col, row, piece)
		self.board[row][col] = piece

	def isPossibleWin(self, p1, p2, p3):
		if p1 == 0 and p2 == p3:
			return p2
		elif p2 == 0 and p1 == p3:
			return p1
		elif p3 == 0 and p1 == p2:
			return p1
		return 0

	def numAvailableMoves(self):
		count = 0
		for j in range(self.height):
			for i in range(self.width):
				if self.board[j][i] == 0:
					count = count + 1
		return count

	def countPossibleWins(self, team):
		count = 0

		for j in range(self.height):
			for i in range(self.width):
				p = self.board[j][i]
				h2 = self.get(i+1, j)
				h3 = self.get(i+2, j)
				v2 = self.get(i, j+1)
				v3 = self.get(i, j+2)
				d2 = self.get(i+1, j+1)
				d3 = self.get(i+2, j+2)
				o2 = self.get(i-1, j+1)
				o3 = self.get(i-2, j+2)

				t1 = self.isPossibleWin(p, h2, h3)
				t2 = self.isPossibleWin(p, v2, v3)
				t3 = self.isPossibleWin(p, d2, d3)
				t4 = self.isPossibleWin(p, o2, o3)

				if team > 0:
					# check if our team
					if t1 == team:
						count = count + 1
					elif t2 == team:
						count = count + 1
					elif t3 == team:
						count = count + 1
					elif t4 == team:
						count = count + 1
				else:
					# check if their team
					if t1 != 0 and t1 != -team:
						count = count + 1
					elif t2 != 0 and t2 != -team:
						count = count + 1
					elif t3 != 0 and t3 != -team:
						count = count + 1
					elif t4 != 0 and t4 != -team:
						count = count + 1

		return count

	def getPossibleMoves(self):
		x = []
		for j in range(self.height):
			for i in range(self.width):
				if self.board[j][i] == 0:
					x.append((i, j))
		return x

	def getWinner(self):
		'''checks to see if Tic Tac Toe has been won'''

		for j in range(self.height):
			for i in range(self.width):
				p = self.get(i, j)
				if p == 0:
					continue

				# check horizontal
				h2 = self.get(i+1, j)
				h3 = self.get(i+2, j)
				if p == h2 and h2 == h3:
					return p

				# check vertical
				v2 = self.get(i, j+1)
				v3 = self.get(i, j+2)
				if p == v2 and v2 == v3:
					return p

				# check diagonal
				d2 = self.get(i+1, j+1)
				d3 = self.get(i+2, j+2)
				if p == d2 and d2 == d3:
					return p

				# check reverse diagonal
				d2 = self.get(i-1, j+1)
				d3 = self.get(i-2, j+2)
				if p == d2 and d2 == d3:
					return p

		numMoves = self.numAvailableMoves()
		if numMoves == 0:
			return -1
		return 0

	def __len__(self):
		'''implements len(self)'''
		return self.width * self.height

print("Setup successful")