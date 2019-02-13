"""
	Curtis Fortenberry
	CS405
	HW1
	
	Checkers base: https://github.com/Saulius181/tk-python-checkers/blob/master/tk-checkers.py
	AI layout: https://github.com/microwerx/cs405605-aif/blob/master/experiments/tictactoe.py
"""
import random
import copy
import time
import tkinter as tk
import tkinter.font as tkfont

class Agent:
	# Base class for "Intelligent" Agents
	# Based off the tic tac toe example
	
	# ctor
	# Initialize from data
	def __init__(self, teamColor, environment):
		self.percepts = []
		self.teamColor = teamColor
		self.environment = Environment(environment.cutList, environment.moveList, environment.canvas, environment.player1Color, environment.player2Color)
		self.lastMove = []
		self.availableMoves = []
		self.nextMove = []
		self.selectCut = []
		self.selectMove = []
	
	# sense
	def sense(self):
		self.environment.getAvailableMoves(self, self.selectMove, self.selectCut)
		'''self.percepts.append(percepts)
		
		self.availableMoves = environment.getPossibleMoves()
		self.lastMove = environment.lastMove
		if self.lastMove[2] != 0:
			self.environment.put(self.lastMove[0], self.lastMove[1], self.lastMove[2]'''
	
	# think
	# Search for the answer
	def think(self):
		# What should we get for lunch today?
		''' This comment style allows the progam to compile '''
	
	# action
	# Do sometinng
	def action(self):
		'''return self.nextMove'''

class StochasticAgent(Agent):
	
	def __init__(self, teamColor, environment):
		super().__init__(teamColor, environment)
	
	def think(self):
		if self.selectCut:
			checker = random.choice(self.selectCut)
			move = random.choice(checker[2])[0]
			self.environment.movechecker(move[0], move[1], checker[0], checker[1])
			if "man" in self.environment.canvas.itemcget(self.environment.canvas.data["checker"][move[0]][move[1]][0], "tag"):
				self.environment.removechecker(move[0], move[1], move[2], checker[0], checker[1])
				if move[0] == 355:
					self.environment.canvas.itemconfig(self.environment.canvas.data["checker"][move[0]][move[1]][0], tag="king", dash=(5, 1, 2, 1), dashoff=3, width=5)
			elif "king" in self.environment.canvas.itemcget(self.environment.canvas.data["checker"][move[0]][move[1]][0], "tag"):
				self.environment.removechecker(move[0], move[1], move[2], checker[0], checker[1])
		elif self.selectMove:
			checker = random.choice(self.selectMove)
			move = random.choice(checker[2])[0]
			self.environment.movechecker(move[0], move[1], checker[0], checker[1])
			if "man" in self.environment.canvas.itemcget(self.environment.canvas.data["checker"][move[0]][move[1]][0], "tag"):
				if move[0] == 355:
					self.environment.canvas.itemconfig(self.environment.canvas.data["checker"][move[0]][move[1]][0], tag="king", dash=(5, 1, 2, 1), dashoff=3, width=5)
		else:
			return True
		self.selectCut = []
		self.selectMove = []
		self.environment.cutList = []
		self.environment.moveList = []
		

class BreadthFirstAgent(Agent):
	
	def __init__(self, teamColor, environment):
		super().__init__(teamColor, environment)
	
	def think(self):
		''''''
	
	def action(self):
		''''''

class DepthFirstAgent(Agent):
	
	def __init__(self, teamColor, environment):
		super().__init__(teamColor, environment)
	
	def think(self):
		''''''
	
	def action(self):
		''''''

class EvolutionaryAgent(Agent):
	
	def __init__(self, teamColor, environment):
		super().__init__(teamColor, environment)
	
	def think(self):
		''''''
	
	def action(self):
		''''''

class AlphaBetaAgent(Agent):
	
	def __init__(self, teamColor, environment):
		super().__init__(teamColor, environment)
	
	def think(self):
		bestMove = []
		alpha = -100
		alphai = 0
		beta = 100
		betai = 0
		i = 0
		hasWon = False
		
		# AlphaBeta
		# Do best move
		
		self.selectCut = []
		self.selectMove = []
		self.environment.cutList = []
		self.environment.moveList = []

class Environment:
	
	def __init__(self, cutList, moveList, canvas, player1Color, player2Color):
		self.cutList = cutList
		self.moveList = moveList
		self.canvas = canvas
		self.player1Color = player1Color
		self.player2Color = player2Color
		self.lastMove = []
		self.board = copy.copy(canvas)
	
	def getdir(self, dir):
		if dir == "topLeft":
			topDir = -1
			leftDir = -1
		elif dir == "topRight":
			topDir = -1
			leftDir = 1
		elif dir == "bottomLeft":
			topDir = 1
			leftDir = -1
		elif dir == "bottomRight":
			topDir = 1
			leftDir = 1
			
		return topDir, leftDir
	
	def testManCutList(self, top, left, dir, moveBool=True):
		topDir, leftDir = self.getdir(dir)
		
		moveList = []
		cutList = []
		
		if top+(topDir*50) in self.canvas.data["checker"]:
			if left+(leftDir*50) not in self.canvas.data["checker"][top+(topDir*50)]:
				if left+(leftDir*50) in self.canvas.data["board"][top+(topDir*50)]:
					if self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player1Color and dir in ("topLeft", "topRight") and moveBool:
						moveList.append( [top+(topDir*50), left+(leftDir*50), "move" ] )
					elif self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player2Color and dir in ("bottomLeft", "bottomRight") and moveBool:
						moveList.append( [top+(topDir*50), left+(leftDir*50), "move" ] )
			elif self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player1Color:
				if self.canvas.itemcget(self.canvas.data["checker"][top+(topDir*50)][left+(leftDir*50)][0], "fill") == self.player2Color:
					if top+(topDir*100) in self.canvas.data["checker"] and left+(leftDir*100) not in self.canvas.data["checker"][top+(topDir*100)] and left+(leftDir*100) in self.canvas.data["board"][top+(topDir*100)]:
						cutList.append( [top+(topDir*100), left+(leftDir*100), dir ] )		
			elif self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player2Color:
				if self.canvas.itemcget(self.canvas.data["checker"][top+(topDir*50)][left+(leftDir*50)][0], "fill") == self.player1Color:
					if top+(topDir*100) in self.canvas.data["checker"] and left+(leftDir*100) not in self.canvas.data["checker"][top+(topDir*100)] and left+(leftDir*100) in self.canvas.data["board"][top+(topDir*100)]:
						cutList.append( [top+(topDir*100), left+(leftDir*100), dir ] )
		
		return moveList, cutList
	
	def testKingCutList(self, top, left, dir, moveBool=True):
		topDir, leftDir = self.getdir(dir)
		
		moveList = []
		cutList = []
		
		count = 1
		self.cut = False
		
		while True:
			if top+(50*count*topDir) in self.canvas.data["checker"]:
				if left+(50*count*leftDir) not in self.canvas.data["checker"][top+(50*count*topDir)]:
					if left+(50*count*leftDir) in self.canvas.data["board"][top+(50*count*topDir)]:
						if not self.cut:
							if moveBool:
								moveList.append( [top+(50*count*topDir), left+(50*count*leftDir), "move" ] )
						else:
							cutList.append( [top+(50*count*topDir), left+(50*count*leftDir), dir ] )
				elif self.canvas.itemcget(self.canvas.data["checker"][top+(50*count*topDir)][left+(50*count*leftDir)][0], "fill") == self.player2Color and self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player1Color:
					if top+(50*count*topDir)+(topDir*50) in self.canvas.data["checker"] and left+(50*count*leftDir)+(leftDir*50) not in self.canvas.data["checker"][top+(50*count*topDir)+(topDir*50)] and left+(50*count*leftDir)+(leftDir*50) in self.canvas.data["board"][top+(50*count*topDir)+(topDir*50)]:
						self.cut = True
						cutList.append( [top+(50*count*topDir)+(topDir*50), left+(50*count*leftDir)+(leftDir*50), dir ] )
					else:
						break
				elif self.canvas.itemcget(self.canvas.data["checker"][top+(50*count*topDir)][left+(50*count*leftDir)][0], "fill") == self.player1Color and self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player2Color:
					if top+(50*count*topDir)+(topDir*50) in self.canvas.data["checker"] and left+(50*count*leftDir)+(leftDir*50) not in self.canvas.data["checker"][top+(50*count*topDir)+(topDir*50)] and left+(50*count*leftDir)+(leftDir*50) in self.canvas.data["board"][top+(50*count*topDir)+(topDir*50)]:
						self.cut = True
						cutList.append( [top+(50*count*topDir)+(topDir*50), left+(50*count*leftDir)+(leftDir*50), dir ] )
					else:
						break
				else:
					break
			else:
				break
						
			count+=1
			
		return moveList, cutList
		
	def movechecker(self, srcTop, srcLeft, destTop, destLeft):
		self.canvas.coords(self.canvas.data["checker"][destTop][destLeft][0], srcLeft, srcTop, srcLeft+50, srcTop+50)
		self.canvas.data["checker"][srcTop][srcLeft] = self.canvas.data["checker"][destTop][destLeft]
		self.canvas.data["checker"][destTop].pop(destLeft)
	
	def removechecker(self, srcTop, srcLeft, dir, destTop, destLeft):
		topDir, leftDir = self.getdir(dir)
		topDir *= -1
		leftDir *= -1
		
		for count in range(1, int(abs(((srcTop-5)-(destTop-5))/50))+1):
			if srcLeft+(50*count*leftDir) in self.canvas.data["checker"][srcTop+(50*count*topDir)]:
				self.canvas.delete(self.canvas.data["checker"][srcTop+(50*count*topDir)][srcLeft+(50*count*leftDir)][0])
				self.canvas.data["checker"][srcTop+(50*count*topDir)].pop(srcLeft+(50*count*leftDir))
	
	def getAvailableMoves(self, ply, selectMove, selectCut):
		for dTop, topRow in self.canvas.data["checker"].items():
			for dLeft, checker, in topRow.items():
				moveList = []
				cutList = []
				test = []
				
				if self.canvas.itemcget(checker[0], "fill") == ply.teamColor:
					if "man" in self.canvas.itemcget(checker[0], "tag"):
						test.append(self.testManCutList(dTop, dLeft, "topLeft"))
						test.append(self.testManCutList(dTop, dLeft, "topRight"))
						test.append(self.testManCutList(dTop, dLeft, "bottomLeft"))
						test.append(self.testManCutList(dTop, dLeft, "bottomRight"))
					elif "king" in self.canvas.itemcget(checker[0], "tag"):
						test.append(self.testKingCutList(dTop, dLeft, "topLeft"))
						test.append(self.testKingCutList(dTop, dLeft, "topRight"))
						test.append(self.testKingCutList(dTop, dLeft, "bottomLeft"))
						test.append(self.testKingCutList(dTop, dLeft, "bottomRight"))
				
				if test:
					for tuple in test:
						if tuple[0]:
							moveList.append(tuple[0])
						if tuple[1]:
							cutList.append(tuple[1])
					if moveList:
						selectMove.append([dTop, dLeft, moveList])
					if cutList:
						selectCut.append([dTop, dLeft, cutList])
	
	def reset(self):
		self.board = copy.copy(self.canvas)
	
	def put(self, srcTop, srcLeft, destTop, destLeft):
		self.board.coords(self.board.data["checker"][destTop][destLeft][0], srcLeft, srcTop, srcLeft+50, srcTop+50)
		self.board.data["checker"][srcTop][srcLeft] = self.board.data["checker"][destTop][destLeft]
		self.board.data["checker"][destTop].pop(destLeft)
	
	def getPossibleMovesMoves(self, ply, selectMove, selectCut):
		for dTop, topRow in self.board.data["checker"].items():
			for dLeft, checker, in topRow.items():
				moveList = []
				cutList = []
				test = []
				
				if self.board.itemcget(checker[0], "fill") == ply.teamColor:
					if "man" in self.board.itemcget(checker[0], "tag"):
						test.append(self.testManCutList(dTop, dLeft, "topLeft"))
						test.append(self.testManCutList(dTop, dLeft, "topRight"))
						test.append(self.testManCutList(dTop, dLeft, "bottomLeft"))
						test.append(self.testManCutList(dTop, dLeft, "bottomRight"))
					elif "king" in self.board.itemcget(checker[0], "tag"):
						test.append(self.testKingCutList(dTop, dLeft, "topLeft"))
						test.append(self.testKingCutList(dTop, dLeft, "topRight"))
						test.append(self.testKingCutList(dTop, dLeft, "bottomLeft"))
						test.append(self.testKingCutList(dTop, dLeft, "bottomRight"))
				
				if test:
					for tuple in test:
						if tuple[0]:
							moveList.append(tuple[0])
						if tuple[1]:
							cutList.append(tuple[1])
					if moveList:
						selectMove.append([dTop, dLeft, moveList])
					if cutList:
						selectCut.append([dTop, dLeft, cutList])

class Checkers:
	
	def __init__(self, root):
		self.root = root
		
		self.canvas = tk.Canvas(root, width=410, height=410)
		self.canvas.pack()
		
		self.top = 55
		self.left = 55
		
		self.player1Color = "light gray"
		self.player2Color = "red2"
		
		tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)
		
		self.controls = tk.Frame(root)
		self.controls.pack()
		self.startButton = tk.Button(self.controls, text="Start/Stop", command=self.startstopgame)
		self.startButton.pack(side=tk.LEFT)
		
		self.options = tk.Frame(root)
		self.options.pack()
		self.team1AgentType = tk.StringVar(value="Stochastic")
		self.team2AgentType = tk.StringVar(value="Stochastic")
		tk.Label(self.options, text="Team 1 Agent").grid(column=0, row=0)
		self.team1Type = tk.OptionMenu(self.options, self.team1AgentType, "Stochastic")
		tk.Label(self.options, text="Team 2 Agent").grid(column = 0, row = 1)
		self.team2Type = tk.OptionMenu(self.options, self.team2AgentType, "Stochastic")
		self.team1Type.grid(column = 1, row = 0)
		self.team2Type.grid(column = 1, row = 1)
		self.team1CountLabel = tk.Label(self.options, text="Wins")
		self.team1CountValue = tk.Label(self.options, text="0")
		self.team2CountLabel = tk.Label(self.options, text="Wins")
		self.team2CountValue = tk.Label(self.options, text="0")
		self.team1CountLabel.grid(row=0, column=3)
		self.team1CountValue.grid(row=0, column=4)
		self.team2CountLabel.grid(row=1, column=3)
		self.team2CountValue.grid(row=1, column=4)
		
		self.started = False
		self.init()
		self.gameloop()
	
	def newAgent(self, teamColor, type):
		if type == "Stochastic":
			return StochasticAgent(teamColor, self.environment)
	
	def init(self):
		self.gamecount = 0
		self.wincounts = [0, 0]
		self.simStartTime = time.time()
		
		self.reset()
	
	def reset(self):
		self.turn = "player1"
		self.moveCount = 0
		
		self.canvas.data = {}
		self.canvas.data["board"] = {}
		self.canvas.data["boardval"] = []
		self.canvas.data["checker"] = {}
		self.canvas.data["checkerval"] = []
		
		self.cutList = []
		self.moveList = []
		
		for row in range(8):
			self.canvas.data["board"][5+row*50] = {}
			for col in range(8):
				if row&1 ^ col&1:
					self.canvas.data["board"][5+row*50][5+col*50] = [self.canvas.create_rectangle( 5+col*50, 5+row*50, 5+col*50+50, 5+row*50+50, outline="black", fill="dark slate gray")]
				else:
					self.canvas.data["board"][5+row*50][5+col*50] = [self.canvas.create_rectangle( 5+col*50, 5+row*50, 5+col*50+50, 5+row*50+50, outline="black", fill="AntiqueWhite2")]
				self.canvas.data["boardval"].append([5+row*50, 5+col*50])
		
		for row in range(0, 3):
			self.canvas.data["checker"][5+row*50] = {}
			for col in range(-1, 7):
				if not row&1 ^ col&1:
					self.canvas.data["checker"][5+row*50][5+col*50+50] = [self.canvas.create_oval(5+col*50+50 , 5+row*50, 5+col*50+50+50 , 5+row*50+50, fill=self.player2Color, tag="man")]
					self.canvas.data["checkerval"].append([5+row*50, 5+col*50+50])
		
		self.canvas.data["checker"][5+3*50] = {}
		self.canvas.data["checker"][5+4*50] = {}
		
		for row in range(5, 8):
			self.canvas.data["checker"][5+row*50] = {}
			for col in range(-1, 7):
				if not row&1 ^ col&1:
					self.canvas.data["checker"][5+row*50][5+col*50+50] = [self.canvas.create_oval(5+col*50+50 , 5+row*50, 5+col*50+50+50 , 5+row*50+50, fill=self.player1Color, tag="man")]
					self.canvas.data["checkerval"].append([5+row*50, 5+col*50+50])
		
		self.runStartTime = time.time()
		
		self.environment = Environment(self.cutList, self.moveList, self.canvas, self.player1Color, self.player2Color)
		self.agent1 = self.newAgent(self.player1Color, self.team1AgentType.get())
		self.agent2 = self.newAgent(self.player2Color, self.team2AgentType.get())
	
	def startstopgame(self):
		if self.started:
			self.started = False
		else:
			self.started = True
			self.init()
	
	def man_cutList(self, top, left, dir, moveList, cutList, moveBool=True):
		topDir, leftDir = self.environment.getdir(dir)
		
		if top+(topDir*50) in self.canvas.data["checker"]:
			if left+(leftDir*50) not in self.canvas.data["checker"][top+(topDir*50)]:
				if left+(leftDir*50) in self.canvas.data["board"][top+(topDir*50)]:
					if self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player1Color and dir in ("topLeft", "topRight") and moveBool:
						moveList.append([top+(topDir*50), left+(leftDir*50), "move"])
					elif self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player2Color and dir in ("bottomLeft", "bottomRight") and moveBool:
						moveList.append([top+(topDir*50), left+(leftDir*50), "move"])
			elif self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player1Color:
				if self.canvas.itemcget(self.canvas.data["checker"][top+(topDir*50)][left+(leftDir*50)][0], "fill") == self.player2Color:
					if top+(topDir*100) in self.canvas.data["checker"] and left+(leftDir*100) not in self.canvas.data["checker"][top+(topDir*100)] and left+(leftDir*100) in self.canvas.data["board"][top+(topDir*100)]:
						cutList.append([top+(topDir*100), left+(leftDir*100), dir])		
			elif self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player2Color:
				if self.canvas.itemcget(self.canvas.data["checker"][top+(topDir*50)][left+(leftDir*50)][0], "fill") == self.player1Color:
					if top+(topDir*100) in self.canvas.data["checker"] and left+(leftDir*100) not in self.canvas.data["checker"][top+(topDir*100)] and left+(leftDir*100) in self.canvas.data["board"][top+(topDir*100)]:
						cutList.append([top+(topDir*100), left+(leftDir*100), dir])
	
	def king_cutList(self, top, left, dir, moveList, cutList, moveBool=True):
		topDir, leftDir = self.environment.getdir(dir)

		count = 1
		self.cut = False
		
		while True:
			if top+(50*count*topDir) in self.canvas.data["checker"]:
				if left+(50*count*leftDir) not in self.canvas.data["checker"][top+(50*count*topDir)]:
					if not self.cut:
						if moveBool:
							moveList.append([top+(50*count*topDir), left+(50*count*leftDir), "move"])
					else:
						cutList.append( [top+(50*count*topDir), left+(50*count*leftDir), dir ] )
				elif self.canvas.itemcget(self.canvas.data["checker"][top+(50*count*topDir)][left+(50*count*leftDir)][0], "fill") == self.player2Color and self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player1Color:
					if top+(50*count*topDir)+(topDir*50) in self.canvas.data["checker"] and left+(50*count*leftDir)+(leftDir*50) not in self.canvas.data["checker"][top+(50*count*topDir)+(topDir*50)] and left+(50*count*leftDir)+(leftDir*50) in self.canvas.data["board"][top+(50*count*topDir)+(topDir*50)]:
						self.cut = True
						cutList.append( [top+(50*count*topDir)+(topDir*50), left+(50*count*leftDir)+(leftDir*50), dir ] )
					else:
						break
				elif self.canvas.itemcget(self.canvas.data["checker"][top+(50*count*topDir)][left+(50*count*leftDir)][0], "fill") == self.player1Color and self.canvas.itemcget(self.canvas.data["checker"][top][left][0], "fill") == self.player2Color:
					if top+(50*count*topDir)+(topDir*50) in self.canvas.data["checker"] and left+(50*count*leftDir)+(leftDir*50) not in self.canvas.data["checker"][top+(50*count*topDir)+(topDir*50)] and left+(50*count*leftDir)+(leftDir*50) in self.canvas.data["board"][top+(50*count*topDir)+(topDir*50)]:
						self.cut = True
						cutList.append( [top+(50*count*topDir)+(topDir*50), left+(50*count*leftDir)+(leftDir*50), dir ] )
					else:
						break
				else:
					break
			else:
				break
						
			count+=1
	
	def run(self):
		if self.gamecount >= 20:
			self.simEndTime = time.time()
			print("Total simulation time: {}".format(self.simEndTime-self.simStartTime))
			self.startstopgame()
		
		hasWon = False
		
		if self.turn == "player1":
			self.agent1.sense()
			hasWon = self.agent1.think()
			self.moveCount = self.moveCount + 1
			if hasWon:
				self.wincounts[0] = self.wincounts[0] + 1
				self.gamecount = self.gamecount + 1
				self.runEndTime = time.time()
				print("Num of moves this during game {}, : {} over {}".format(self.gamecount, self.moveCount, self.runEndTime-self.runStartTime))
				self.reset()
			self.turn = "player2"
		elif self.turn == "player2":
			self.agent2.sense()
			hasWon = self.agent2.think()
			if hasWon:
				self.wincounts[1] = self.wincounts[1] + 1
				self.gamecount = self.gamecount + 1
				self.runEndTime = time.time()
				print("Num of moves this during game {}, : {} over {}".format(self.gamecount, self.moveCount, self.runEndTime-self.runStartTime))
				self.reset()
			self.turn = "player1"
	
	def update(self):
		if not self.started:
			return
		self.run()
	
	def draw(self):
		self.team1CountValue["text"] = self.wincounts[0]
		self.team2CountValue["text"] = self.wincounts[1]
	
	def gameloop(self):
		self.update()
		self.draw()
		if (self.started):
			self.root.after_idle(self.gameloop)
		else:
			self.root.after(100, self.gameloop)

if __name__ == "__main__":
	root = tk.Tk()
	root.title("Checkers i guess")
	root.resizable(0, 0)
	game = Checkers(root)
	root.mainloop()