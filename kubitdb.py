import json

class Data:
    def __init__(self, dosyaismi=None):
        if dosyaismi is None:
            self.dosyaismi = "kubitdb.json"
        else:
            self.dosyaismi = dosyaismi
        
        try:
            open(self.dosyaismi, 'r', encoding="utf-8")
        except FileNotFoundError:
            with open(self.dosyaismi, "w", encoding="utf-8") as f:
                f.write('{}')

    def get(self, aranacak):
        try:
            with open(self.dosyaismi, "r") as dosya:
                veri = json.load(dosya)
                return veri.get(aranacak, None)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
        except Exception:
            return None

    def set(self, item, key):
        try:
            with open(self.dosyaismi, "r") as dosya:
                veri = json.load(dosya)
            veri[item] = key
            with open(self.dosyaismi, "w") as dosya:
                json.dump(veri, dosya, indent=4)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
        except Exception:
            return None

    def has(self, aranacak):
        try:
            with open(self.dosyaismi, "r") as dosya:
                veri = json.load(dosya)
                return aranacak in veri
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
        except Exception:
            return None

    def subtract(self, item, key):
        try:
            with open(self.dosyaismi, "r") as dosya:
                veri = json.load(dosya)
            tempdata = veri.get(item)
            if isinstance(tempdata, int):
                tempdata -= key
                veri[item] = tempdata
                with open(self.dosyaismi, "w") as dosya:
                    json.dump(veri, dosya, indent=4)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
        except Exception:
            return None

    def all(self):
        try:
            with open(self.dosyaismi, "r") as dosya:
                veri = json.load(dosya)
                return veri
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
        except Exception:
            return None

    def clear(self):
        with open(self.dosyaismi, "w", encoding="utf-8") as f:
            f.write('{}')

    def push(self, item, key):
        try:
            with open(self.dosyaismi, "r") as dosya:
                veri = json.load(dosya)
            if isinstance(veri.get(item), list):
                veri[item].append(key)
            else:
                veri[item] = [key]
            with open(self.dosyaismi, "w") as dosya:
                json.dump(veri, dosya, indent=4)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
        except Exception:
            return None

    def delete(self, item):
        try:
            with open(self.dosyaismi, "r") as dosya:
                veri = json.load(dosya)
            if item in veri:
                del veri[item]
            with open(self.dosyaismi, "w") as dosya:
                json.dump(veri, dosya, indent=4)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
        except Exception:
            return None
