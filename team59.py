import sys
import random
import time
import datetime

INF = float("inf")

class Team59:
  	# The team's entire code to be written under this class
  	def __init__(self):
  		self.timestart = 0.00
  		self.maxTime = 8
  		self.terminate = False
		pass

  	def heuristic(self,board):

		heu = 0

		blockmap = ( 0 , 3 , 9 , 27, 100 )
		boardmap = ( 0 , 3 , 9 , 27, 100 )

		blockh = [[ 0 for i in range(4)] for j in range(4)]


		for i in range(4):
			for j in range(4):


				#along rows
				for u in range(4*i, 4*i+4):
					ocount = 0
				  	xcount = 0
				  	for v in range(4*j, 4*j+4):
				  		if board.board_status[u][v] == 'o':
				  			ocount+= 1
				  		elif board.board_status[u][v] == 'x':
				  			xcount+= 1
				  	if xcount > 0 and ocount == 0:
						blockh[i][j] += blockmap[xcount]
					elif xcount == 0 and ocount > 0 :
						blockh[i][j] -= blockmap[ocount]


				#along colomns
				for u in range(4*j, 4*j + 4):
				  	ocount = 0
				  	xcount = 0
				  	for v in range(4*i , 4*i + 4):
				  		if board.board_status[v][u] == 'o':
				  			ocount+= 1
				  		elif board.board_status[v][u] == 'x':
							xcount+= 1
				  	if xcount > 0 and ocount == 0:
						blockh[i][j] += blockmap[xcount]
					elif xcount == 0 and ocount > 0 :
						blockh[i][j] -= blockmap[ocount]


				#along diamond1
				xcount = 0
				ocount = 0
				if board.board_status[4*i+1][4*j+0]=='o':
					ocount+=1
				elif board.board_status[4*i+1][4*j+0]=='x':
					xcount+=1
				if board.board_status[4*i+0][4*j+1]=='o':
					ocount+=1
				elif board.board_status[4*i+0][4*j+1]=='x':
					xcount+=1
				if board.board_status[4*i+2][4*j+1]=='o':
					ocount+=1
				elif board.board_status[4*i+2][4*j+1]=='x':
					xcount+=1
				if board.board_status[4*i+1][4*j+2]=='o':
					ocount+=1
				elif board.board_status[4*i+1][4*j+2]=='x':
					xcount+=1

				if xcount > 0 and ocount == 0:
					blockh[i][j] += blockmap[xcount]
				elif xcount == 0 and ocount > 0:
					blockh[i][j] -=blockmap[ocount]

				#along diamond2
				xcount = 0
				ocount = 0
				if board.board_status[4*i+1][4*j+1]=='o':
					ocount+=1
				elif board.board_status[4*i+1][4*j+1]=='x':
					xcount+=1
				if board.board_status[4*i+0][4*j+2]=='o':
					ocount+=1
				elif board.board_status[4*i+0][4*j+2]=='x':
					xcount+=1
				if board.board_status[4*i+2][4*j+2]=='o':
					ocount+=1
				elif board.board_status[4*i+2][4*j+2]=='x':
					xcount+=1
				if board.board_status[4*i+1][4*j+3]=='o':
					ocount+=1
				elif board.board_status[4*i+1][4*j+3]=='x':
					xcount+=1

				if xcount > 0 and ocount == 0:
					blockh[i][j] += blockmap[xcount]
				elif xcount == 0 and ocount > 0:
					blockh[i][j] -=blockmap[ocount]

				#along diamond3
				xcount = 0
				ocount = 0
				if board.board_status[4*i+2][4*j+0]=='o':
					ocount+=1
				elif board.board_status[4*i+2][4*j+0]=='x':
					xcount+=1
				if board.board_status[4*i+1][4*j+1]=='o':
					ocount+=1
				elif board.board_status[4*i+1][4*j+1]=='x':
					xcount+=1
				if board.board_status[4*i+3][4*j+1]=='o':
					ocount+=1
				elif board.board_status[4*i+3][4*j+1]=='x':
					xcount+=1
				if board.board_status[4*i+2][4*j+2]=='o':
					ocount+=1
				elif board.board_status[4*i+2][4*j+2]=='x':
					xcount+=1

				if xcount > 0 and ocount == 0:
					blockh[i][j] += blockmap[xcount]
				elif xcount == 0 and ocount > 0:
					blockh[i][j] -=blockmap[ocount]

				#along diamond4
				xcount = 0
				ocount = 0
				if board.board_status[4*i+2][4*j+1]=='o':
					ocount+=1
				elif board.board_status[4*i+2][4*j+1]=='x':
					xcount+=1
				if board.board_status[4*i+1][4*j+2]=='o':
					ocount+=1
				elif board.board_status[4*i+1][4*j+2]=='x':
					xcount+=1
				if board.board_status[4*i+3][4*j+2]=='o':
					ocount+=1
				elif board.board_status[4*i+3][4*j+2]=='x':
					xcount+=1
				if board.board_status[4*i+2][4*j+3]=='o':
					ocount+=1
				elif board.board_status[4*i+2][4*j+3]=='x':
					xcount+=1

				if xcount > 0 and ocount == 0:
					blockh[i][j] += blockmap[xcount]
				elif xcount == 0 and ocount > 0:
					blockh[i][j] -=blockmap[ocount]



		#find xmax , omax
		#along rows
		for u in range(4):
			ocount = 0
		  	xcount = 0
		  	for v in range(4):
		  		if board.block_status[u][v] == 'o':
		  			ocount+= 1
		  		elif board.block_status[u][v] == 'x':
		  			xcount+= 1
		  	if not(xcount > 0 and ocount  > 0):
				if xcount == 0 and ocount > 0 :
					heu -= boardmap[ocount]
				elif xcount > 0 and ocount == 0:
					heu += boardmap[xcount]
		  


		#along colomns
		for u in range(4):
		  	ocount = 0
		  	xcount = 0
		  	for v in range(4):
		  		if board.block_status[v][u] == 'o':
		  			ocount+= 1
		  		elif board.block_status[v][u] == 'x':
		  			xcount+= 1
		  	if not(xcount > 0 and ocount  > 0):

				if xcount == 0 and ocount > 0 :
					heu -= boardmap[ocount]
				elif xcount > 0 and ocount == 0:
					heu += boardmap[xcount]
		  	

		#along diamond1
		xcount = 0
		ocount = 0
		if board.block_status[1][0] == 'o':
			ocount += 1
		elif board.block_status[1][0] == 'x':
			xcount += 1
		if board.block_status[0][1] == 'o':
			ocount += 1
		elif board.block_status[0][1] == 'x':
			xcount += 1
		if board.block_status[2][1] == 'o':
			ocount += 1
		elif board.block_status[2][1] == 'x':
			xcount += 1
		if board.block_status[1][2] == 'o':
			ocount += 1
		elif board.block_status[1][2] == 'x':
			xcount += 1

		if not(xcount > 0 and ocount > 0):

			if xcount == 0 and ocount > 0 :
				heu -= boardmap[ocount]
			elif xcount > 0 and ocount == 0:
				heu += boardmap[xcount]
			

		#along diamond2
		xcount = 0
		ocount = 0
		if board.block_status[1][1] == 'o':
			ocount += 1
		elif board.block_status[1][1] == 'x':
			xcount += 1
		if board.block_status[0][2] == 'o':
			ocount += 1
		elif board.block_status[0][2] == 'x':
			xcount += 1
		if board.block_status[2][2] == 'o':
			ocount += 1
		elif board.block_status[2][2] == 'x':
			xcount += 1
		if board.block_status[1][3] == 'o':
			ocount += 1
		elif board.block_status[1][3] == 'x':
			xcount += 1

		if not(xcount > 0 and ocount > 0):

			if xcount == 0 and ocount > 0 :
				heu -= boardmap[ocount]
			elif xcount > 0 and ocount == 0:
				heu += boardmap[xcount]
			

		#along diamond3
		xcount = 0
		ocount = 0
		if board.block_status[2][0] == 'o':
			ocount += 1
		elif board.block_status[2][0] == 'x':
			xcount += 1
		if board.block_status[1][1] == 'o':
			ocount += 1
		elif board.block_status[1][1] == 'x':
			xcount += 1
		if board.block_status[3][1] == 'o':
			ocount += 1
		elif board.block_status[3][1] == 'x':
			xcount += 1
		if board.block_status[2][2] == 'o':
			ocount += 1
		elif board.block_status[2][2] == 'x':
			xcount += 1

		if not(xcount > 0 and ocount > 0):

			if xcount == 0 and ocount > 0 :
				heu -= boardmap[ocount]
			elif xcount > 0 and ocount == 0:
				heu += boardmap[xcount]
			

		#along diamond4
		xcount = 0
		ocount = 0
		if board.block_status[2][1] == 'o':
			ocount += 1
		elif board.block_status[2][1] == 'x':
			xcount += 1
		if board.block_status[1][2] == 'o':
			ocount += 1
		elif board.block_status[1][2] == 'x':
			xcount += 1
		if board.block_status[3][2] == 'o':
			ocount += 1
		elif board.block_status[3][2] == 'x':
			xcount += 1
		if board.block_status[2][3] == 'o':
			ocount += 1
		elif board.block_status[2][3] == 'x':
			xcount += 1

		if not(xcount > 0 and ocount > 0):

			if xcount == 0 and ocount > 0 :
				heu -= boardmap[ocount]
			elif xcount > 0 and ocount == 0:
				heu += boardmap[xcount]
			

		for u in range(4):
			for v in range(4):
				if board.block_status[u][v]=='-' :
					if (u==0 or u==3) and (v==0 or v==3) :
						heu += 2*blockh[u][v]
					elif ((u==0 or u==3) and (v==1 or v==2)) or ((u==1 or u==2) and (v==0 or v==3)):
						heu += 3*blockh[u][v]
					else:
						heu += 4*blockh[u][v]		


		return heu


  	def minimax(self, board, old_move, present_d, depth, flag, alpha, beta):
  		status = board.find_terminal_state()
  		if time.time()-self.timestart >= self.maxTime-1:
  			self.terminate = True
  			return self.heuristic(board)

  		if (status[1] == 'WON') or (status[1] == 'DRAW') or (present_d == depth):

  			return self.heuristic(board)

  		if flag=='x':
  			opp = 'o'
  			best = -INF
			cells = board.find_valid_move_cells(old_move)
			if len(cells) == 0:
				return self.heuristic(board)
			if len(cells) > 16 and depth - present_d>=3:
				present_d += 1
			elif self.is_freemove(board,old_move,flag) and len(cells)>16:
				present_d += 1
			for cell in cells:
				board.board_status[cell[0]][cell[1]] = flag
				best = max(best,self.minimax(board,(cell[0],cell[1]),present_d+1,depth,opp,alpha,beta))
				board.board_status[cell[0]][cell[1]] = '-'
				alpha = max(alpha, best)
				if (beta <= alpha):
				  	break

			return best
		elif flag=='o':
			opp = 'x'
			best = INF
			cells = board.find_valid_move_cells(old_move)
			if len(cells) == 0:
				return self.heuristic(board)
			if len(cells) > 16 and depth - present_d>=3:
				present_d += 1
			elif self.is_freemove(board,old_move,flag)and len(cells)>16:
				present_d += 1
			for cell in cells:
				board.board_status[cell[0]][cell[1]] = flag
				best = min(best,self.minimax(board,(cell[0],cell[1]),present_d+1,depth,opp,alpha,beta))
				board.board_status[cell[0]][cell[1]] = '-'
				beta = min(beta, best)
				if (beta <= alpha):
					break
			return best

  	def move(self, board, old_move, flag):
  		self.timestart = time.time()
  		self.terminate = False
		cells = board.find_valid_move_cells(old_move)  	#Found all the possible steps and need to choose one from them

		if (flag=='x'):
		  	bestval = -INF
		  	opp='o'
		elif (flag=='o'):
		  	bestval = INF
		  	opp='x'  
		bestrow = -1
		bestcol = -1
		depth = 4
		pcount = self.noofpossible_empty_cells(board,old_move,flag)
		depth = self.set_depth(pcount,len(cells))
		for cell in cells:
			if (time.time() - self.timestart) >= (self.maxTime-0.25):
				self.terminate = True
				break
			if self.terminate:
				break
			board.board_status[cell[0]][cell[1]] = flag
			old_move = (cell[0],cell[1])
			moveval = self.minimax(board, old_move, 1, depth, opp, -INF, INF)
			board.board_status[cell[0]][cell[1]] = '-'
			if flag=='x':  	# maximizer
				if moveval>bestval:
					bestval = moveval
					bestrow = cell[0]
					bestcol = cell[1]
			elif flag=='o': # minimizer
				if moveval<bestval:
					bestval = moveval
					bestrow = cell[0]
					bestcol = cell[1]
		return (bestrow,bestcol)

	def noofpossible_empty_cells(self,board,old_move,flag):
		pcount = 0
		for u in range(4):
			for v in range(4):
				if board.block_status[u][v] == '-':
					for a in range(4):
						for b in range(4):
							if board.board_status[4*u+a][4*v+b] == '-':
								pcount += 1
		return pcount

	def set_depth(self,pcount,kcell):
		if kcell>=16:
			return 3
		elif pcount<64 and pcount>0:
			return 4
		elif pcount >=64:
			return 3

	def is_freemove(self,board,old_move,flag):
		if (board.block_status[old_move[0]/4][old_move[1]/4]!='-'):
			return 1
		else:
			return 0

