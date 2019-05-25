import random

WIDTH = 10  
HEIGHT = 10
board_u = []
board_c = []
board_vurus=[]

for x in range(HEIGHT):
  board_u.append(["O"] * 10)
for x in range(HEIGHT):
  board_c.append(["O"] * 10)

def print_board_us(board_u):
      print("-----USER BOARD-----")
      for row in board_u:
            print(" ".join(row),"")
            
            
def print_board_com(board_c):
      print("---COMPUTER BOARD---")
      for row in board_c:
            print(" ".join(row))


gemi_1 = [board_u[2][2],board_u[2][3],board_u[2][4]]
gemi_amiral = [board_u[1][7],board_u[2][7],board_u[3][7],board_u[4][7]]
gemi_ikilik = [board_u[9][4],board_u[9][5]]
gemi_birlik = board_u[6][7]



def giris_us():
      guess_row = int(input("Guess Row: "))
      guess_col = int(input("Guess Col: "))
      
      if board_u[guess_row][guess_col]=='O':
            board_u[guess_row][guess_col]="M"
      else:
            print("Cannot entry")
      print_board_us(board_u)
      print()
      return

def giris_com():
      guess_row_c = random.randint(0,len(board_c)-1)
      guess_col_c = random.randint(0,len(board_c)-1)
      if board_c[guess_row_c][guess_col_c]=='O':
            board_c[guess_row_c][guess_col_c]="G"
      else:
            print("Cannot entry")    
      print_board_com(board_c)
      print()
      return

def atis_control():
      guess_row = int(input("Guess Row: "))
      guess_col = int(input("Guess Col: "))
      if [guess_row][guess_col] not in board_vurus:
            board_vurus.append[guess_row][guess_col]
            board_u[guess_row][guess_col]="X"
            if gemi_amiral in board_u:
                  print("amiral vuruldu")                 
            
     

      #elif board_u[guess_row][guess_col] == board_u[2][2] or board_u[guess_row][guess_col] == board_u[2][3] or board_u[guess_row][guess_col] == board_u[2][4]:
       #     board_u[guess_row][guess_col]="X"

      else:
            board_u[guess_row][guess_col]="M"
            

      print_board_us(board_u)
      return

       
while True:
      #giris_us()
      #giris_com()
      atis_control()


      
  
