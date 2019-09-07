class Battleship:
    BOARD_DIM = 10
    COL_LABELS = [chr(ord('A')+i) for i in range(10)]
    def __init__(self,init_ships=[]):
        self.board = [self._decode(coord) for coord in init_ships]
        self.attack_board = []
    
    def _decode(self, coord):
        col = 'a' - coord[0]
        row = coord[1]
        return col + row * Battleship.BOARD_DIM

    @staticmethod
    def draw_board(board=[]):
        print('\n'*3,end='')
        print(f'{" "*3}| {" ".join(Battleship.COL_LABELS)} |')
        cap_row = f'{"-"*3}|{"-"*(Battleship.BOARD_DIM*2+1)}|{"-"*3}'
        basic_row = f'|{" "*(Battleship.BOARD_DIM*2+1)}|'
        print(cap_row)
        for x in range(1,11):
            spacing = ' ' if x<10 else ''
            print(f'{spacing}{x} {basic_row}')
        print(cap_row,end='\n\n')
        # print(f'{" "*3}|{" "*(Battleship.BOARD_DIM*2+1)}|')

Battleship().draw_board()