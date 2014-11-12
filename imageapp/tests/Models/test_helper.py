

def obj_compare(obj1,obj2, excluded_keys):
        if isinstance(obj1, obj2.__class__):
            d1, d2 = obj1.__dict__, obj2.__dict__
            old, new = {}, {}
            for k,v in d1.items():
                if k in excluded_keys:
                    continue
                try:
                    if v != d2[k]:
                        old.update({k: v})
                        new.update({k: d2[k]})
                except KeyError:
                    old.update({k: v})
            return old==new
        return False
