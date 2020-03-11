#!/usr/bin/env python3

session.open(db='precoalvi_11')

domain = []
moves = session.env['account.move'].search(domain)
count = 0
print(len(moves))
for move in moves:
    move._compute_move_type()
    count += 1 
    print (count)

session.cr.commit()
exit()