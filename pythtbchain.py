from pythtb import tb_model

lat = [[1.0, 0.0], [0.0, 1.0]]
orb = [[0.0]]

chain = tb_model(2, 2, lat, orb)

chain.set_hop(-1.0, 0, 0, [1.0, 0])
chain.set_hop(-1, 0, 0, [0, 1])
