from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class ModList:
    list_mods = []

    def __init__(self):
        stream = open("./mods.yml", "r")
        document = load(stream, Loader=Loader)
        print(document)
        for x in document["EnabledMods"]:
            try:
                modid = int(x)
                modname = document["EnabledMods"][x]
                print(type(modid))
                print(self.addMod(modid, modname))
            except ValueError:
                print("Valueerror in init")
        self.list_mods.sort(key=lambda mod: mod.name)
        pass
    
    def addMod(self, modid: int, modname: str):
        if modname == None or modname == "": return "No modname"
        checkValue = True
        if (self.list_mods.__len__() == 0): checkValue = True
        for i in range(self.list_mods.__len__()):
            cache: Mod = self.list_mods[i]
            if cache.name == modname and cache.modid == modid:
                checkValue = False
        if checkValue:
            mod: Mod = Mod(modname, modid)
            self.list_mods.append(mod)
            return ("400 OK")
        else: 
            return ("Duplikate Error")

    def removeMod(self, modid: int, modname: str = None):
        print(f"Trying to remove modid={modid}, modname={modname}")
        remove_indexes = []
        for i, mod in enumerate(self.list_mods):
            condition = (modname is None or modname == "" or mod.name == modname) and mod.modid == modid
            print(f"Checking index {i}: {mod.modid}, {mod.name} -> Match? {condition}")
            if condition:
                remove_indexes.append(i)
        print(f"Indexes to remove: {remove_indexes}")
        
        for i in reversed(remove_indexes):
            print(f"Removing index {i}")
            del self.list_mods[i]

    def getModList(self):
        cache: dict = {}
        for mod in self.list_mods:
            mod: Mod = mod
            cache[mod.modid] = mod.name
        return cache

class Mod:
    name: str
    modid: int

    def __init__(self, name: str, modid: int):
        self.name = name
        self.modid = modid