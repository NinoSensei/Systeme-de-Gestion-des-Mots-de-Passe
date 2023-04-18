import bcrypt
import random

# -*- coding: utf-8 -*-

pepper = ['~F=xK&C-Vv', 'eiA:?8xT>g', '0Kj;f$f#.c', 'B6sdC"W6(', 'Iv}$Q2^W8L', '{Nz)kp3q.#', 'NpW8"R6yjA', 'G>VH"2.6:s', 'K^nL3=zq3|', 'DdL1>9X$yK', 'n/[Vu]E~?x', '=T>2{zjK(', '@:^n%r8A9', 'V0mHp}b4t', '4t!Zk7VYp0', 'M?VjS8@9&g', 'O+n3H5d@uF',
          'Dg7...eY~k', '+jH0(Q8$<P', 't{u^7E4G4', '4!VZ!n<mY#', '#;]S~uS7Vb', 'q3o{5~[}5h', '1RZ,@w}Y"Q', '$fM"5G1R6U', '!6$#vN8xW', 'J,L6q`O3$5', 'BnS5R;@mB(', '5H6$xY9mF4', ')~h?6H3Jq<', 'r(~3rD1*F', 'H`+o9C@0}R', 'yL#0V7v}fD', 'O8z:n;=T~', '2v]t%j8!u']


def encrypt_password(password):
    password = bytes((password + random.choice(pepper)).encode("utf-8"))
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt), salt


def check_password(password, hashed):
    for _ in pepper:
        _pass = bytes((password + _).encode())
        if bcrypt.checkpw(_pass, hashed.encode()):
            return True
    return False
