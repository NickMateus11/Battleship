class Battleship:
    BOARD_DIM = 10
    COL_LABELS = [chr(ord('A')+i) for i in range(10)]
    def __init__(self,init_ships=[]):
        self.ships = [self._decode(coord) for coord in init_ships]
        self.attack_board = []
    
    def _decode(self, coord):
        col = ord(coord[0].lower()) - ord('a')
        row = int(coord[1:])-1
        print(col,row)
        return col + (row * Battleship.BOARD_DIM)

    def draw_board(self):
        print('\n'*3,end='')
        print(f'{" "*3}| {" ".join(Battleship.COL_LABELS)} |',end='\t') # Self ships
        print(f'{" "*3}| {" ".join(Battleship.COL_LABELS)} |')          # Attacks
        cap_row = f'{"-"*3}|{"-"*(Battleship.BOARD_DIM*2+1)}|{"-"*3}'
        basic_row = f'|{" "*(Battleship.BOARD_DIM*2+1)}|'
        print(cap_row + '\t' + cap_row)
        for x in range(1,11):
            spacing = ' ' if x<10 else ''
            print(f'{spacing}{x} {self._inject_ships(basic_row, x)}',end='\t')
            print(f'{spacing}{x} {self._inject_attacks(basic_row, x)}')
        print(cap_row + '\t' + cap_row,end='\n\n')
        # print(f'{" "*3}|{" "*(Battleship.BOARD_DIM*2+1)}|')
    
    def _inject_ships(self, basic_row_text, row):
        for ship_seg_index in self.ships:
            if ship_seg_index//Battleship.BOARD_DIM == row-1:
                row_index = ship_seg_index%Battleship.BOARD_DIM*2+1
                basic_row_text = basic_row_text[0:row_index+1] + '@' + \
                     basic_row_text[row_index+2:] # TODO: enable different symbols for each ship
        return basic_row_text
    
    def _inject_attacks(self, basic_row_text, row):
        for ship_seg_index in self.ships:
            if ship_seg_index//Battleship.BOARD_DIM == row-1:
                row_index = ship_seg_index%Battleship.BOARD_DIM*2+1
                basic_row_text = basic_row_text[0:row_index+1] + chr(2155) + \
                    basic_row_text[row_index+2:] # TODO: enable different symbols for each ship
        return basic_row_text


Battleship(['a1','b2','d5','d6','d7','j1','j10','A10']).draw_board()