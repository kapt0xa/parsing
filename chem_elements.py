chem_elements = \
[
    'H', 'He',

    'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',

    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',

    'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',

    'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',

    'Cs', 'Ba',
    'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
    'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'pb', 'Bi', 'Po', 'At', 'Rn',

    'Fr', 'Ra',
    'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No',
    'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'
]
element_groups = \
[
    's1',
    's2',
    'f1',
    'f2',
    'f3',
    'f4',
    'f5',
    'f6',
    'f7',
    'f8'
    'f9',
    'f10',
    'f11',
    'f12',
    'f13',
    'f14',
    'd1',
    'd2',
    'd3',
    'd4',
    'd5',
    'd6',
    'd7',
    'd8',
    'd9',
    'd10',
    'p1',
    'p2',
    'p3',
    'p4',
    'p5',
    'nbl',
]

chem_elements_indexes = {k: i + 1 for i, el in enumerate(chem_elements) for k in (el, el.lower())}
chem_elements_indexes['j'] = chem_elements_indexes['i']
chem_elements_indexes['J'] = chem_elements_indexes['I']
chem_elements_indexes['Ku'] = chem_elements_indexes['Rf'] # kurczatowij
chem_elements_indexes['ku'] = chem_elements_indexes['rf']

def build_link_map():
    table_template = \
'''
#                              #'
##                        ######'
##                        ######'
##              ################'
##              ################'
################################'
################################'
'''
    periodic_map = []
    period_map = []
    id = 1
    for char in table_template:
        if (char == '\n'):
            periodic_map.append(period_map)
            period_map = []
        elif(char == '#'):
            period_map.append(id)
            id += 1
        else: # (char == ' '):
            period_map.append(0)
    return periodic_map

periodic_map = build_link_map()

def build_periodic_table():
    f_group_begin = 2
    f_group_end = f_group_begin + 14
    f_period_begin = 5

    assembly = ''
    # main table without f-elements
    for period, period_data in enumerate(periodic_map):
        for group, index in enumerate(period_data):
            if(f_group_begin <= group < f_group_end):
                if(f_group_begin == group):
                    if(period <= f_period_begin):
                        assembly += '  '
                    else:
                        assembly += '| '
                continue
            if(index == 0):
                assembly += '    '
                assembly += '  '
            else:
                assembly += f'{index:>3}:'
                assembly += f'{chem_elements[index-1][:2]:<2}'
            assembly += ' '
        assembly += '\n'
    assembly += '\n'

    # f-elements
    for period, period_data in enumerate(periodic_map):
        if (period < f_period_begin):
            continue
        for group, index in enumerate(period_data):
            if not (f_group_begin <= group < f_group_end):
                continue
            if(index == 0):
                assembly += '    '
                assembly += '  '
            else:
                assembly += f'{index:>3}:'
                assembly += f'{chem_elements[index-1][:2]:<2}'
            assembly += ' '
        assembly += '\n'
    assembly += '\n'

    return assembly

print(build_periodic_table())