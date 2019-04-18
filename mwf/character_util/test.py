from .player import Player, LV_UP_CONSTANT


p = Player()
print(p.exp)
print(p.lv)
p.add_exp(1)
print(p.exp, p.lv, p.req_exp_to_lv_up)
p.add_exp(LV_UP_CONSTANT)
print(p.exp, p.lv, p.req_exp_to_lv_up)
p.add_exp(LV_UP_CONSTANT * 100)
print(p.exp, p.lv, p.req_exp_to_lv_up)
print(p)
print(repr(p))